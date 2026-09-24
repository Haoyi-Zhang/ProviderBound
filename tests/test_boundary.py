from pathlib import Path
from copy import deepcopy
import ast, json, random, sys, unittest
from itertools import permutations
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from producer import infer, normalize, InputError
from checker import verify, Rejected, read_model
ROOT=Path(__file__).resolve().parents[1]

def G(owners,rows,edges=()):
    return {'kind':'graph','owners':owners,'before':[list(e) for e in edges],
            'rows':[{'key':f'r{i}','present':p,'good':g} for i,(p,g) in enumerate(rows)]}

class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.forced=G(['developer','lib:A'],[([0,1],[0,1]),([0,1],[0])])
        self.ambiguous=G(['developer','lib:A'],[([0,1],[0,1])])
    def reject(self,raw,cert):
        with self.assertRaises((Rejected,ValueError,TypeError,KeyError)):
            verify(raw,cert)
    def test_nonlocal_unique(self):
        out=verify(self.forced,infer(self.forced))
        self.assertEqual(out['regions'][0]['owners'],['developer'])
    def test_ambiguity_not_inconsistency(self):
        cert=infer(self.ambiguous); out=verify(self.ambiguous,cert)
        self.assertEqual(out['regions'][0]['class'],'ambiguous')
        self.assertGreaterEqual(len(cert['orders']),2)
    def test_all_equal_payload_orders_are_valid(self):
        x=G(['lib:A']*3,[([0,1,2],[0,1,2])]); c=infer(x)
        self.assertEqual(verify(x,c)['regions'][0]['owners'],['lib:A'])
    def test_delete_negative_obligation(self):
        c=infer(self.forced); c['regions'][0]['excluded']=[]; self.reject(self.forced,c)
    def test_forged_trap_without_reasons(self):
        c=infer(self.forced); c['obstructions'][c['regions'][0]['excluded'][0]['obstruction']]['reasons']=[]; self.reject(self.forced,c)
    def test_empty_trap(self):
        c=infer(self.forced); t=c['obstructions'][c['regions'][0]['excluded'][0]['obstruction']]; t['nodes']=[]; t['reasons']=[]; self.reject(self.forced,c)
    def test_invented_precedence_reason(self):
        c=infer(self.forced); t=c['obstructions'][c['regions'][0]['excluded'][0]['obstruction']]; t['reasons'][0]={'node':t['nodes'][0],'kind':'before','pred':t['nodes'][0]}; self.reject(self.forced,c)
    def test_wrong_forced_edge(self):
        c=infer(self.forced); t=c['obstructions'][c['regions'][0]['excluded'][0]['obstruction']]
        for r in t['reasons']:
            if r['kind']=='forced': r['pred']=r['node']; break
        self.reject(self.forced,c)
    def test_false_row_blocker(self):
        c=infer(self.forced); t=c['obstructions'][c['regions'][0]['excluded'][0]['obstruction']]
        for r in t['reasons']:
            if r['kind']=='row': r['row']=0; break
        self.reject(self.forced,c)
    def test_unused_obstruction_rejected(self):
        c=infer(self.forced); c['obstructions'].append(deepcopy(c['obstructions'][0])); self.reject(self.forced,c)
    def test_obstruction_index_out_of_range(self):
        c=infer(self.forced); c['regions'][0]['excluded'][0]['obstruction']=99; self.reject(self.forced,c)
    def test_obstruction_index_boolean(self):
        c=infer(self.forced); c['regions'][0]['excluded'][0]['obstruction']=False; self.reject(self.forced,c)
    def test_same_trap_not_reusable_for_different_force(self):
        x=G(['developer','lib:A','lib:B'],[([0,1,2],[0,1,2]),([0,1,2],[0])])
        c=infer(x); blocks=c['regions'][0]['excluded']; self.assertEqual(len(blocks),2)
        blocks[1]['obstruction']=blocks[0]['obstruction']; self.reject(x,c)
    def test_shared_obligation_round_trip(self):
        x=G(['developer','lib:A'],[([0,1],[0,1])]*30+[([0,1],[0])]); c=infer(x)
        self.assertEqual(len(c['obstructions']),1)
        self.assertEqual(verify(x,json.loads(json.dumps(c)))['regions'][0]['owners'],['developer'])
    def test_wrong_order(self):
        c=infer(self.forced); c['orders'][0]=[1,0]; self.reject(self.forced,c)
    def test_repeated_provider_order(self):
        c=infer(self.forced); c['orders'][0]=[0,0]; self.reject(self.forced,c)
    def test_bool_is_not_index(self):
        c=infer(self.forced); c['orders'][0]=[False,1]; self.reject(self.forced,c)
    def test_wrong_owner(self):
        c=infer(self.forced); c['regions'][0]['owners']=['lib:invented']; self.reject(self.forced,c)
    def test_wrong_category(self):
        c=infer(self.forced); c['regions'][0]['class']='ambiguous'; self.reject(self.forced,c)
    def test_duplicate_region_omission(self):
        c=infer(self.forced); c['regions'].pop(); self.reject(self.forced,c)
    def test_witness_for_wrong_owner(self):
        c=infer(self.ambiguous)
        c['regions'][0]['support'][1][1]=c['regions'][0]['support'][0][1]
        self.reject(self.ambiguous,c)
    def test_empty_witness_bank(self):
        c=infer(self.forced); c['orders']=[]; self.reject(self.forced,c)
    def test_cannot_certify_all_orders_from_one_witness(self):
        c=infer(self.ambiguous); c['regions'][0]={'owners':['developer'],'class':'developer','support':[['developer',0]],'excluded':[]}
        self.reject(self.ambiguous,c)
    def test_false_inconsistency(self):
        self.reject(self.ambiguous,{'status':'inconsistent','obstruction':{'kind':'missing','row':0}})
    def test_missing_candidate_is_inconsistent(self):
        x=G(['developer'],[([],[])])
        self.assertEqual(verify(x,infer(x))['status'],'inconsistent')
    def test_self_cycle(self):
        x=G(['developer'],[([0],[0])],[(0,0)])
        self.assertEqual(verify(x,infer(x))['status'],'inconsistent')
    def test_owner_projection_is_not_provider_projection(self):
        x=G(['lib:A','lib:A','developer'],[([0,1],[0,1])])
        self.assertEqual(verify(x,infer(x))['regions'][0]['class'],'library')
    def test_or_is_not_and(self):
        x=G(['developer','lib:A','lib:B'],[([0,1,2],[0,1,2]),([0,1,2],[0,1])])
        self.assertEqual(verify(x,infer(x))['regions'][0]['owners'],['developer','lib:A'])
    def test_observation_weakening_widens(self):
        strong=verify(self.forced,infer(self.forced))['regions'][0]['owners']
        weak=verify(self.ambiguous,infer(self.ambiguous))['regions'][0]['owners']
        self.assertTrue(set(strong)<set(weak))
    def test_missing_inventory_is_not_detectable_in_general(self):
        # An omitted equal-byte provider changes the premise, not the checker result.
        reduced=G(['developer'],[([0],[0])])
        self.assertEqual(verify(reduced,infer(reduced))['regions'][0]['owners'],['developer'])
        self.assertEqual(verify(self.ambiguous,infer(self.ambiguous))['regions'][0]['class'],'ambiguous')
    def test_renaming_invariance(self):
        x=deepcopy(self.forced); x['owners']=list(reversed(x['owners']))
        for row in x['rows']:
            row['present']=[1-p for p in row['present']]; row['good']=[1-p for p in row['good']]
        self.assertEqual(verify(self.forced,infer(self.forced)),verify(x,infer(x)))
    def test_total_order_collapses_or_rejects(self):
        # A complete inventory need not include a complete order. Once order
        # evidence is complete, remaining owner ambiguity must disappear.
        x=G(['developer','lib:A','lib:B'],[([0,1,2],[0,1,2]),([1,2],[1,2])],[(0,1),(1,2)])
        out=verify(x,infer(x))
        self.assertEqual([r['owners'] for r in out['regions']],[['developer'],['lib:A']])
        x['rows'][0]['good']=[1,2]
        self.assertEqual(verify(x,infer(x))['status'],'inconsistent')
    def test_every_stored_input(self):
        for record in json.loads((ROOT/'inputs/index.json').read_text()):
            x=json.loads((ROOT/record['path']).read_text())
            if record['admission']=='rejected':
                with self.assertRaises((InputError,ValueError,TypeError,KeyError)): normalize(x)
                with self.assertRaises((Rejected,ValueError,TypeError,KeyError)): read_model(x)
            else:
                self.assertEqual(normalize(x),read_model(x))
                verify(x,infer(x))
    def test_no_checker_inference_import(self):
        tree=ast.parse((ROOT/'src/checker.py').read_text())
        modules=[]
        for node in ast.walk(tree):
            if isinstance(node,ast.Import): modules.extend(a.name for a in node.names)
            if isinstance(node,ast.ImportFrom): modules.append(node.module or '')
        self.assertFalse(any('producer' in name or 'oracle' in name for name in modules))
    def test_unsupported_input_is_not_ambiguous(self):
        x=G(['developer'],[([0],[0])]); x['rows'][0]['good']=[1]
        with self.assertRaises(InputError): infer(x)
        with self.assertRaises(Rejected): read_model(x)
    def test_json_duplicates_and_file_bounds(self):
        from producer import _object
        from checker import no_duplicates
        for f in (_object,no_duplicates):
            with self.assertRaises(ValueError): f([('x',1),('x',2)])
        # Exercise the actual file path at and above a reduced limit. Small
        # limits test the boundary without allocating an oversized input.
        from tempfile import TemporaryDirectory
        from unittest.mock import patch
        import producer, checker
        with TemporaryDirectory() as folder:
            path=Path(folder)/'input.json'
            with patch.object(producer,'MAX_INPUT_BYTES',2), patch.object(checker,'MAX_FILE_BYTES',2):
                path.write_bytes(b'{}')
                self.assertEqual(producer.load(path),{})
                self.assertEqual(checker.load(path),{})
                path.write_bytes(b'{} ')
                with self.assertRaises(InputError): producer.load(path)
                with self.assertRaises(Rejected): checker.load(path)

    def test_concrete_archive_adapters_and_safety(self):
        from tempfile import TemporaryDirectory
        from zipfile import ZipFile
        from archive_producer import lower_archives, ArchiveInputError
        from archive_checker import interpret_archives, ArchiveRejected
        with TemporaryDirectory() as folder:
            folder=Path(folder); a=folder/'a.jar'; b=folder/'b.jar'; out=folder/'out.zip'
            with ZipFile(a,'w') as z:
                z.writestr('same.bin',b'x'); z.writestr('probe.bin',b'a')
                z.writestr('META-INF/MANIFEST.MF',b'ignored-a')
            with ZipFile(b,'w') as z:
                z.writestr('same.bin',b'x'); z.writestr('probe.bin',b'b')
                z.writestr('META-INF/MANIFEST.MF',b'ignored-b')
            with ZipFile(out,'w') as z:
                z.writestr('same.bin',b'x'); z.writestr('probe.bin',b'a')
            specs=[('a','developer',a),('b','lib:B',b)]
            graph=lower_archives(specs,out)
            graph2=interpret_archives([{'id':i,'owner':o,'path':str(q)} for i,o,q in specs],out)
            self.assertEqual(graph,graph2)
            answer=verify(graph2,infer(graph))
            self.assertEqual({x['key']:x['owners'] for x in answer['regions']},
                             {'probe.bin':['developer'],'same.bin':['developer']})
            bad=folder/'bad.zip'
            with ZipFile(bad,'w') as z: z.writestr('../escape',b'x')
            with self.assertRaises(ArchiveInputError): lower_archives([('x','developer',bad)],bad)
            with self.assertRaises(ArchiveRejected):
                interpret_archives([{'id':'x','owner':'developer','path':str(bad)}],bad)

    def test_seeded_larger_models_against_literal_orders(self):
        """Differentially check producer/checker on deterministic 4--7-provider cases.

        This complements the exhaustive n<=3 oracle.  It does not claim exhaustive
        coverage for larger n; it protects the implementation against size-specific
        mistakes while retaining a literal, independently written order oracle.
        """
        rng=random.Random(0xC0FFEE)
        labels=['developer','lib:A','lib:B','lib:C']
        for n in range(4,8):
            universe=list(range(n))
            all_orders=list(permutations(universe))
            for case in range(32):
                owners=[rng.choice(labels) for _ in universe]
                edges=[]
                for a in universe:
                    for b in universe:
                        if rng.random() < (0.035 if a == b else 0.12):
                            edges.append((a,b))
                rows=[]
                for _ in range(rng.randrange(0,6)):
                    if rng.random() < 0.05:
                        present=[]
                    else:
                        present=[p for p in universe if rng.random() < 0.5]
                        if not present:
                            present=[rng.randrange(n)]
                    good=[p for p in present if rng.random() < 0.55]
                    rows.append((present,good))
                raw=G(owners,rows,edges)
                feasible=[]
                for order in all_orders:
                    rank={p:i for i,p in enumerate(order)}
                    if any(rank[a] >= rank[b] for a,b in edges):
                        continue
                    winners=[]
                    valid=True
                    for present,good in rows:
                        if not present:
                            valid=False; break
                        winner=min(present,key=rank.get)
                        if winner not in good:
                            valid=False; break
                        winners.append(winner)
                    if valid:
                        feasible.append(winners)
                answer=verify(raw,json.loads(json.dumps(infer(raw))))
                with self.subTest(n=n,case=case):
                    if not feasible:
                        self.assertEqual(answer['status'],'inconsistent')
                    else:
                        self.assertEqual(answer['status'],'classified')
                        expected=[]
                        for r in range(len(rows)):
                            expected.append(sorted({owners[winners[r]] for winners in feasible}))
                        self.assertEqual([row['owners'] for row in answer['regions']],expected)

    def test_concrete_archive_output_union_rejected(self):
        from tempfile import TemporaryDirectory
        from zipfile import ZipFile
        from archive_producer import lower_archives, ArchiveInputError
        from archive_checker import interpret_archives, ArchiveRejected
        with TemporaryDirectory() as folder:
            folder=Path(folder); provider=folder/'p.jar'; output=folder/'o.zip'
            with ZipFile(provider,'w') as z: z.writestr('x',b'x')
            with ZipFile(output,'w') as z: z.writestr('y',b'y')
            with self.assertRaises(ArchiveInputError): lower_archives([('p','developer',provider)],output)
            with self.assertRaises(ArchiveRejected):
                interpret_archives([{'id':'p','owner':'developer','path':str(provider)}],output)

if __name__=='__main__': unittest.main()

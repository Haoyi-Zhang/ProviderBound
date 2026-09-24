# Input-hardening audit

Presence is a static navigation aid, not proof that every path is hardened. Runtime adversarial tests remain authoritative.

| Concern | Source/test evidence present |
|---|---|
| unknown fields | yes |
| duplicate json keys | yes |
| schema version | yes |
| path traversal | yes |
| absolute paths | yes |
| backslashes | yes |
| nul | yes |
| noncanonical hex | yes |
| malformed order | yes |
| unsupported transform | yes |

## Raw JSON-load sites

| Source | Strict hook visible on call line | Code |
|---|---|---|
| `src/producer.py:31` | yes | `return json.loads(data.decode('utf-8'), object_pairs_hook=_object)` |
| `src/checker.py:31` | yes | `return json.loads(data.decode('utf-8'), object_pairs_hook=no_duplicates)` |
| `tests/test_boundary.py:121` | no / wrapper inspection required | `for record in json.loads((ROOT/'inputs/index.json').read_text()):` |
| `tests/test_boundary.py:122` | no / wrapper inspection required | `x=json.loads((ROOT/record['path']).read_text())` |
| `scripts/audit_release.py:20` | yes | `json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=strict_pairs,parse_constant=parse_constant)` |
| `scripts/audit_claims.py:64` | no / wrapper inspection required | `try: obj=json.loads(p.read_text(encoding='utf-8'))` |
| `scripts/build_data_dictionary.py:26` | no / wrapper inspection required | `try:o=json.loads(p.read_text(encoding='utf-8'))` |
| `scripts/campaign.py:11` | no / wrapper inspection required | `index=json.loads((ROOT/'inputs/index.json').read_text()); records=[]` |
| `scripts/campaign.py:14` | no / wrapper inspection required | `raw=json.loads((ROOT/item['path']).read_text()); t=time.process_time()` |

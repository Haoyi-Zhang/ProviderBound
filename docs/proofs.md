# Mathematical argument for first-winner inventories

These are ordinary mathematical proofs, not mechanically checked general
proofs. Executable finite validation is reported separately. The feasibility
construction is a specialization of the established Horn-rule representation of
antimatroids by Yoshikawa, Hirai, and Makino (Journal of Mathematical Psychology
77, 2017, 82–93, DOI 10.1016/j.jmp.2016.09.002), particularly the tight-path
membership algorithm in Section 3.1 of the accessible author manuscript.

## Definitions

Let V be a nonempty finite provider set and let owner: V → L map providers to
owner labels. The distinguished label `developer` is one owner; every other
nonempty label denotes a named library. K ⊆ V×V is a declared precedence
relation, not assumed acyclic. Each region r has a provider set P_r ⊆ V and an
observationally compatible set G_r ⊆ P_r. Put B_r = P_r \ G_r.

An inventory lowers to this graph as follows. Independently within each
provider, apply the single longest matching declared directory-prefix rule to
an original name, at most once. Payload bytes do not change. Rules have distinct
source prefixes; source names and transformed names are unique within a
provider. The output name set must equal the union of the transformed input
name sets. P_r consists of providers of that output name; G_r consists of those
whose transformed entry has exactly the observed payload bytes. This lowering
is intentionally not a semantics for Java/DEX bytecode rewriting.

For a permutation π of V, let first_π(P) be the earliest element of nonempty P.
A world is a permutation that respects K and has first_π(P_r) ∈ G_r for every
region. Let Ω be the set of all such worlds. A region with P_r empty makes Ω
empty. For Ω nonempty, its exact owner set is

    O_r = {owner(first_π(P_r)) : π ∈ Ω}.

A singleton `developer` is developer classification; a singleton other label is
library classification; at least two labels is ambiguity. There is no owner
classification when Ω is empty. In particular, universal quantification over an
empty world set is never used to manufacture a unique owner.

## Lemma 1: disjunctive predecessor characterization

For nonempty P_r, a permutation obeys the observation for r exactly when every
b ∈ B_r has at least one g ∈ G_r earlier than b.

Proof. If the first provider is a good g, it is earlier than every bad provider.
Conversely, if the earliest provider were bad b, the required earlier good
provider would also lie in P_r, contradicting earliestness. If G_r is empty and
P_r nonempty, the right-hand condition fails for each bad provider, as does the
left-hand condition. This proves the boundary case as well. ∎

This is an existential predecessor condition, not a demand that all good
providers precede every bad provider. For G={a,b} and B={c}, the order a,c,b is
valid. Replacing OR with AND loses a genuine world.

## Lemma 2: eligibility of the next provider

After selecting a prefix with selected set S, an unselected provider v may be
appended while satisfying every newly incurred obligation exactly when (i) each
K-predecessor of v belongs to S and (ii) for every r with v ∈ B_r, G_r ∩ S is
nonempty. Both conditions are monotone in S.

Proof. Appending v makes precisely its incoming precedence requirements and
its bad-provider requirements newly relevant. Earlier obligations remain true;
none is destroyed by adding an element. A missing predecessor violates its
edge; a bad provider with no earlier good violates Lemma 1. Conversely, the two
conditions supply all newly necessary earlier elements. ∎

An eligible prefix need not be extendible in an inconsistent instance. The
algorithm does not assume extendibility as an unproved invariant.

## Theorem 1: greedy feasibility and completeness

First return inconsistency if any P_r is empty. For the remaining case,
where every P_r is nonempty, repeatedly append any eligible provider.
If all providers are selected, the
result is a world. If the process stops at a proper set S, no world exists.

Proof. An empty-provider row makes Ω empty by definition. In the remaining
nonempty-row case, each appended provider satisfies Lemma 2; thus the complete order
satisfies all precedence edges and, by Lemma 1, all observations. For the other
direction, suppose the process is stuck and a world π exists. Choose the first
provider v in π not in S. All providers earlier than v in π belong to S,
regardless of their order in the constructed prefix. Every K-predecessor of v
is earlier in π and is therefore in S. For every row in which v is bad,
Lemma 1 supplies an earlier good provider in π, also in S. Thus v is eligible,
contradicting that the process is stuck. This proof also covers cycles in K:
none can admit a total order, and the algorithm cannot finish them. ∎

Relation to known theory. Introduce the Horn-style rules (G_r,b) for each
b ∈ B_r and ({a},b) for each edge (a,b) ∈ K. A set accepts (A,q) when q's
presence implies the presence of some element of A. Eligible prefixes are the
accessible sets of this rule family. Theorem 1 instantiates the tight-path
argument; it is not a new general antimatroid theorem. Keeping a good set once
per row avoids physically duplicating it for every bad provider.

## Theorem 2: self-blocking sets certify infeasibility

A trap is a nonempty U ⊆ V together with one reason for each v ∈ U. A reason
is either (a) a required edge (u,v) with u ∈ U, or (b) a row r with v ∈ B_r
and G_r ⊆ U. Every valid trap implies that no world exists. Whenever greedy
feasibility gets stuck without an empty-provider row, its residual set admits
a trap.

Proof of soundness. Suppose π were a world and let v be its first member of U.
An edge reason requires an earlier u ∈ U, a contradiction. A row reason
requires, by Lemma 1, an earlier g ∈ G_r ⊆ U, also a contradiction. The argument
uses every member of U having a reason; a partially explained set is not a
certificate.

Proof of completeness. Let U=V\S be the residual at a stuck state. By
ineligibility, every v ∈ U either has an unselected predecessor u ∈ U, or is
bad in a row with no good selected. In the latter case G_r ⊆ U. Choose one such
reason per v. ∎

An empty-provider row has a separate direct infeasibility certificate. No
subset-minimality or minimum-cardinality claim is made about the emitted trap.
Those are different optimization obligations.

## Lemma 3: counterfactual winner query

For p ∈ G_r, add edges F(r,p)={(p,q): q ∈ P_r and q≠p} to K. The augmented
instance has a world exactly when some original world has p first at r.

Proof. In any augmented world p precedes all other candidates for r and thus
wins r. The world still satisfies every original obligation. Conversely, an
original world in which p wins already respects every edge in F(r,p), so it is
also a world of the augmented instance. ∎

For two rows with identical P sets and the same p, these added edge sets are
identical. Thus a force query may be reused between those rows in the same
unchanged input instance. Equality of output bytes alone or equality of owner
labels does not suffice for this reuse.

## Theorem 3: certificate soundness

For a claimed owner set S_r at every region, the classification certificate must
contain at least one full valid world overall; a supporting valid world for
each label in S_r whose winner has that label; and a valid augmented-instance
infeasibility certificate for every p ∈ G_r with owner(p) ∉ S_r. Then S_r=O_r
for every region.

Proof. Supporting worlds show S_r ⊆ O_r and establish nonemptiness of Ω. If
some label outside S_r occurred in a world, its winning provider would belong
to G_r by observation validity. Its counterfactual obligation would have a
world by Lemma 3, contradicting its trap or missing-provider certificate by
Theorem 2. Thus O_r ⊆ S_r. The three categories follow from equality and the
specified distinguished developer label. ∎

This proves an ownership projection, not an exact projection of providers. Two
providers with the same owner need not both be supported. Likewise, checking
two full orders with different owner labels demonstrates ambiguity but does
not prove that these are the only possible owners; exclusions establish that
stronger statement.

## Theorem 4: relative completeness of the certificate protocol

For every finite admitted graph instance, either an inconsistency certificate
exists, or a classification certificate exists for the exact nonempty owner
projection. The producer's search scheme constructs one of these certificates.

Proof. If Ω is empty, the greedy test either finds an empty-provider row or
returns a trap by Theorems 1–2. Otherwise it returns one world. For each row and
each still unsupported owner, test the good providers of that owner with
Lemma 3. A successful query adds a witness for that owner. If no query succeeds,
Theorem 2 supplies an obstruction for each of its good providers. All finite
queries terminate, and their collected supports and exclusions satisfy
Theorem 3. Owner labels already supported need no further provider tests. ∎

This theorem does not assert that all bounded instances fit the producer's
serialization budget or complete within a fixed wall time. Mathematical
existence, finite algorithm termination, and measured engineering closure are
separate propositions. Python itself has not been formally verified.

## Proposition 1: invariance and observation refinement

A bijection on providers, with consistent rewriting of K, P, G and the owner
map, induces a bijection between worlds and preserves each named region's
owner set. Region reordering likewise only reorders the answer. More generally,
any two inputs that have corresponding worlds and identical owner-winner
projections have identical classifications; this is semantic equivalence, not
a discovered efficient canonicalization algorithm.

Proof. Apply the bijection pointwise to a world and its inverse for the reverse
map. Precedence and earliest membership are preserved. The mapped owner labels
are the same by hypothesis. ∎

With V, owner and all P fixed, adding precedence constraints or shrinking some
G can only remove worlds. If the refined world set is nonempty, its owner sets
are subsets of the originals. If it becomes empty, the result is inconsistent,
not a singleton classification. Removing a provider is not an instance of this
information-refinement proposition: it changes the input universe.

## Corollary: complete order evidence removes ambiguity

If K has a unique total-order extension, Ω contains either that permutation
alone or no permutation. In the former case every region has exactly one owner;
in the latter the observations are inconsistent. This follows because Ω is a
subset of the total-order extensions of K. In particular a complete chain
fixes the order. Inventory completeness is not execution-trace completeness:
the positive examples rely on partially observed ordering. A practical study
must justify that information boundary rather than treating order uncertainty
as an inevitable property of a fully recorded build.

## Proposition 2: missing equal-byte inputs are not observationally detectable

No procedure receiving only an alleged inventory, its output bytes, and a
certificate over that inventory can in general certify the inventory's actual
completeness.

Proof by indistinguishable histories. In history H1, the real build contains
only developer provider a with entry r=x. In H2, it also contains library
provider b with the same entry r=x and uses order b,a. Both deliver output r=x.
Present the same alleged inventory {a} and the same valid certificate for a in
both histories. All received bytes and labels are identical. The procedure must
make the same decision, although H2 omitted a real input and the real first
provider is b. Thus no decision on these observations alone can establish the
completeness property. A trusted or independently evidenced build inventory
would be an additional premise, not a consequence of the certificate. ∎

## Concrete boundary counterexamples

* Equal payloads from developer a and library b, with no other facts, admit
  a,b and b,a. This is ambiguity in a satisfiable model, not an unsatisfiable
  dependency core.
* Two rows with P={a,b}, respectively G={a} and G={b}, admit no single global
  order. Labelling each locally and calling their disagreement ambiguity loses
  the consistency requirement.
* A target with G=P={a,b}, plus a probe with P={a,b}, G={a}, forces a at both
  rows. Local target bytes alone cannot obtain the singleton owner result.
* Mutual calls between classes do not imply common provenance. The model does
  not quotient an ordinary call-graph SCC into one owner.
* A path-only rename of a class entry leaves names embedded in its class-file
  contents unchanged. The implemented language rejects this operation rather
  than representing it as genuine JVM or DEX relocation.

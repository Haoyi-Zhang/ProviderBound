# Input, certificate, and replay contract

## Graph form

A graph is an object with `kind: "graph"`, `owners`, `before`, and `rows`.
`owners` is a nonempty list of nonempty strings. Providers are zero-based list
indices. `before` is a list of distinct two-index edges. A row has exactly
`key`, `present`, and `good`; row keys are unique nonempty strings, candidate
lists contain distinct valid integer indices, and good is a subset of present.
Boolean JSON values are not integer indices. Extra top-level graph fields are
ignored; row and certificate fields are checked exactly. Graph form treats the
candidate relations as supplied premises, not independently extracted facts.

The structural caps are 300 providers, 20,000 rows, and 250,000 incidences,
where an incidence is a precedence edge or a provider membership in a row.
Good memberships are a subset of present memberships. These are admission
caps, not a theorem that every admitted instance meets a given runtime budget.

## Inventory form

An inventory instead has `kind: "inventory"`, `providers`, `before`, and
`observed`. Each provider has a unique nonempty `id`, its `owner`, a list of at
most 32 `relocations`, and named `entries`. Each entry has `name` and a hex
`payload`. Observed entries have the same name/payload representation. Precedence
still uses provider indices, not string identifiers.

Each rule is a pair of directory-prefix strings ending in `/`; the old prefix
is nonempty and unique within that provider. Among rules matching the original
name, apply the longest once. Do not feed the transformed name through another
rule. Input names and transformed names are unique within one provider. The
observed name set must equal the union of all transformed names. A mismatch is
an unsupported/incomplete representation, not a theorem-certified ambiguity.
Any `.class` or `.dex` entry in a provider with relocation rules is rejected.

The producer and checker independently reconstruct P and G from this form. The
inventory still does not prove which artifacts the actual build consumed.

## Classified certificate

The exact top-level fields are `status`, `orders`, `obstructions`, and `regions`.
Status is `classified`. Every item of `orders` is a full provider permutation
respecting the base precedence and every observed row. There is at least one
order. `obstructions` is a shared list of trap objects. Each region contains:

- `owners`: nonempty sorted unique owner labels;
- `class`: `developer`, `library`, or `ambiguous`;
- `support`: exactly one `[owner, order_index]` pair for each claimed owner;
- `excluded`: exactly one `{provider, obstruction}` object for every good
  provider of an owner not claimed, with an index into the obstruction bank.

A trap has `kind: "trap"`, nonempty distinct `nodes`, and exactly one reason
for each node. An edge reason has `node`, `kind: "before"` or `"forced"`, and
`pred`. The checker validates the actual base or current counterfactual edge.
A row reason has `node`, `kind: "row"`, and `row`; the node must be bad in
that row and every good provider must lie in the trap. No trap-bank entry may
be unused. Reference indices must be ordinary integers in range.

Caching is allowed only for the same trap index, forced provider, and identical
candidate set of the queried row in the same immutable model. A reference to a
previously valid trap does not authorize a different force obligation.

## Inconsistent certificate

Its exact fields are `status: "inconsistent"` and `obstruction`. A base trap
is valid here without counterfactual edges. Alternatively, a direct object
`{kind: "missing", row: i}` proves that row i has no providers. This can arise
in graph form. The inventory form rejects union mismatches before lowering.

## Cost and trust

For input incidence count I and W stored witness orders, straightforward witness
replay scans O(W I) incidences. Trap reasoning also charges the good-set
membership tests it actually performs. The checker uses structural memoization
for repeated forced edge sets. Compact JSON references do not make all semantic
validation O(I + serialized certificate length): witness/input products and
candidate-set canonicalization must still be charged. No linear-time compact
checker theorem is claimed.

The producer rejects input files over 32 MiB and final compact certificates over
64 MiB. The checker rejects a file over 64 MiB. Both reject duplicate JSON keys. File reads stop after their byte limit plus one
byte, so oversized files are rejected without reading the whole file. This is
a read bound, not a general parser-memory or wall-time theorem.
The library interfaces are for finite in-memory objects; the file budget is
exercised separately by the scale experiment. Neither component is a hardened
network service or an APK parser.

# Fixed study protocol and evidence boundaries

## Research question and falsifiers

For a closed archive inventory governed by one global first-winner provider
order, can a producer emit a certificate that lets a separate checker recover
the exact possible owner set for every observed region?  The retained evidence
must distinguish classified inputs, inconsistent inputs, and unsupported inputs.

The central claim is falsified by any of the following: a mismatch with literal
permutation semantics in the exhaustive oracle; an accepted mutated certificate
with a false witness or obstruction; a disagreement with an external builder on
which provider wins; a disagreement between certificate owners and all concrete
orders in a two-provider public pair; a changed result after a semantics-
preserving identifier rename; or acceptance of a transformation excluded by the
language.

## Frozen semantics

Providers have caller-declared owner labels and finite path-to-byte maps.  A
world is a total provider order extending declared precedence.  At every output
path, the first provider containing that path wins.  Observed output bytes retain
only worlds whose winner carries those bytes.  Owner classification is the
projection of all feasible winning providers through the declared owner map.
Empty world sets are inconsistency, not ambiguity.

The only normalization beyond exact archive reading is simultaneous path-only
relocation under deterministic longest-directory-prefix matching.  Payloads are
opaque.  Bytecode relocation, DEX transformation, Android resource/manifest
merging, and target collisions within one provider are rejected.

## Exact finite oracle

For one, two, and three providers, every provider has one of three row states:
absent, present with output-equal bytes, or present with different bytes.  The
all-absent row is covered by a boundary fixture.  The oracle uses zero, one, or
two rows, every subset of the `n(n-1)` off-diagonal precedence edges (including
cyclic relations), every provider permutation, and two owner maps: one
provider-distinct map with provider zero declared developer, and an all-shared
library map.

The structural population is

```
sum(n=1..3) 2^(n(n-1)) * [1 + (3^n-1) + (3^n-1)^2]
= 7 + 292 + 44,992
= 45,291.
```

Applying the two owner maps yields 90,582 labelled models.  Literal permutation
enumeration is the oracle.  It checks producer status, feasible worlds, winning
providers, and projected owner sets.  This is exhaustive only for the stated
finite family, not for arbitrary provider counts or transformation languages.

## Fixed generated and boundary campaign

Before execution, eight generated families were fixed at 2, 3, 5, 8, and 16
providers.  They cover identical payloads, observation chains, shared owners,
precedence chains, disjunctive roots, observation cycles, path-only relocation,
and missing payloads.  Twenty named boundary fixtures in `inputs/index.json`
exercise malformed, inconsistent, unsupported, and edge-case inputs.  No random
seed, training/test split, learned parameter, performance target, or outcome-
based selection is used.

The 60-case campaign is semantic and branch coverage.  It is not substituted for
the public builds and is not used to estimate a population prevalence.

## Public collision corpus and external exact oracle

The public corpus is frozen under `inputs/public/` and contains 43 unmodified
JAR providers distributed in Debian packages plus the Apache Ant 1.10.15 and
Ant-launcher builder JARs.  Package/version/file-size metadata are in
`providers.csv`; verbatim Debian copyright records are retained under
`licenses/`.

Selection is deterministic and outcome-blind after freezing the 43 providers:
read every archive; ignore `META-INF/MANIFEST.MF` for build interpretation;
enumerate all `43 choose 2 = 903` unordered provider pairs; and retain every pair
sharing at least one non-`META-INF` path.  The independent verifier must
recompute exactly 40 pairs: 30 equal-only, nine different-only, and one mixed.

For each retained pair, Apache Ant materializes two archives: left-then-right and
right-then-left.  The generated build file uses two explicit `zipfileset`s,
`duplicate="preserve"`, and `filesonly="true"`.  These two builds enumerate all
total orders of a two-provider world.  Thus the external oracle is exact for
each pair rather than a sample of possible orders.

Four comparisons must agree:

1. direct first-winner prediction from the ordered provider maps;
2. actual Ant output contents;
3. the archive producer/checker pair; and
4. literal owner sets obtained from the two concrete orders.

The corpus is intentionally collision-bearing and dominated by modular Apache
Batik archives.  It validates first-winner archive semantics; it is not a random
sample of Android apps, Java projects, or Maven Central.

## Reference methods

`catalogue_tiebreak` and `inventory_size_proxy` are transparent forced-singleton
probes.  `dependency` returns all providers containing a path.  `local_bytes`
returns all providers whose bytes match the output.  `certified` is the exact
global result.  `trusted_trace` reports the winner in one concrete build order.

Rates are computed only on collision-region observations.  Exactness compares a
method's owner set with the two-order external oracle.  Conservativeness asks
whether the method contains the oracle set.  Hidden-winner coverage counts
whether both winners are retained when reversing a build changes provenance.
These methods are information probes, not replicas of published library
identification systems.

## Additional probes

Three deterministic scale recipes exercise repeated and distributed obligations:

1. 300 providers, 20,000 repeated 12-way equal-byte rows, 240,000 incidences;
2. the same scale with 11 observed pairwise probes forcing one order; and
3. 300 providers, 900 three-way rows, and 2,700 incidences distributed across
   the provider universe.

They record production, serialization, file-read, and replay behavior.  They are
not a worst-case complexity proof and do not establish a universal runtime
ceiling.

Two owned Java builds compile one shared equal-byte class and one distinguishing
probe class in two providers.  A minimal first-winner ZIP assembler changes only
provider order.  This verifies the cross-region mechanism on owned compiled
bytecode without claiming Maven Shade, Gradle, Android, device, or deployment
execution.

## Resource and reliability controls

Reproduction uses no more than four workers, no GPU, no model API, no private
data, no network acquisition, no device, and no external compute.  Every stage
has a timeout.  The runner records stage exit status and wall time. POSIX runs additionally
record child CPU and a child-process peak-RSS high-water mark; these OS counters
are unavailable and recorded as null in the fresh Windows run.  Timing values are descriptive single
runs; correctness claims depend on discrete equality checks, not speed.

All claimed experimental inputs are bundled.  The public-input verifier
recomputes metadata, all 903 pair comparisons, the retained collision table, and
license-record coverage before any build.  Producer/checker separation is
source- and test-checked, but both are ordinary Python programs and no
mechanized refinement proof connects them to the paper proof.

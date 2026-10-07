# Proof-Carrying Library Boundary

This standalone repository implements and evaluates an independently replayable
certificate protocol for **first-winner archive composition**.  The input is a
closed finite inventory of providers, exact path-to-byte maps, caller-declared
owner labels, optional precedence facts, and observed output bytes.  One global
provider order selects the first provider of every duplicate path.  The result
for each output region is the exact set of owner labels possible in any feasible
order: developer, a named library, or an irreducibly ambiguous set.  An empty
world set is reported as input inconsistency, and unsupported transformations
are rejected rather than coerced into a classification.

The feasibility routine is a specialization of established Horn-rule /
antimatroid membership algorithms; this repository does not claim that greedy
algorithm as new.  Its contribution is the frozen build-language semantics,
exact owner projection, explicit positive and counterfactual certificates, a
separate replay checker, and an end-to-end study that connects the semantics to
real Apache Ant archive builds.

## Evidence at a glance

| Evidence | Result |
|---|---:|
| Exact finite oracle | 45,291 structural / 90,582 owner-labelled models; 0 mismatches |
| Regression and mutation tests | 47 passed in the complete current Linux run |
| Public provider archives | 43 licensed JARs, plus 2 Ant builder JARs |
| Exhaustive public collision pairs | 40 of all 903 unordered pairs |
| Concrete public builds | 80 Ant builds: both orders for every collision pair |
| Public region observations | 165,630 total; 8,156 collision-region observations |
| External-oracle/checker disagreement | 0 |
| Hidden source flips with identical output maps | 3,471 regions across 30 reversed pairs |
| Local equal-byte ambiguities resolved globally | 100 |
| Generated/boundary campaign | 60 cases: 43 classified, 15 inconsistent, 2 rejected |
| Largest fixed probe | 300 providers and 20,000 regions; disk replay passed |

The public pair study is exact for its two-provider worlds: building `A,B` and
`B,A` enumerates every total provider order.  It is a frozen collision-bearing
sample of Debian-distributed Java archives, not a representative sample of
Android applications or Maven Central. `results/current/` contains the complete
Linux 6.17 / CPython 3.12.14 / Temurin 21.0.12.1 campaign: eight successful
stages in 72.17 wall seconds, including all 80 Ant builds and both owned Java
builds. Its public stage took 58.43 seconds; all three scale certificates
replayed. Earlier Linux records and `results/local/` Windows finite results
retain their original measurements. The paper tables read only current results.

## Reproduce everything

The finite-only campaign requires Python 3.10 or newer and its standard
library and runs on Windows or Linux. The complete external-builder campaign
additionally requires a JDK that can execute bundled Apache Ant 1.10.15 and
provide `javac` with `--release 8` support.  No network access, pip package, GPU,
model API, private cache, paper directory, or external service is required.

From the repository root:

```sh
python scripts/reproduce.py --output reproduced --java
```

The command performs, in order:

1. deterministic fixture regeneration into the fresh output and comparison with all 61 retained structured input files;
2. independent public-input and collision-pair verification;
3. all unit, negative, separation, and metamorphic tests;
4. exhaustive tiny-model oracle comparison;
5. the fixed 60-case generated/boundary campaign;
6. all 80 concrete Ant public builds and their independent replay checks;
7. the three fixed representation/scale probes; and
8. the two benign owned Java builds.

Each stage has a timeout and the driver has a 1,650-second overall deadline.
The destination must be absent or empty. Progress and failed-stage logs are
retained; `reproduction_summary.json` has status `complete` only after every
requested stage exits successfully.  The public stage uses at most four workers; all other stages are
sequential.

For the portable finite-only campaign (no Ant or JVM execution):

```sh
python -B scripts/reproduce.py --output fresh-finite --skip-public
```

The passive public-input census still reads the bundled archives and notices;
it does not execute their classes. Windows RSS and child CPU counters are
unavailable and recorded as null. See `ENVIRONMENT.md` for current versus
retained measurements. `scripts/reproduce_release.py` is a compatibility entry
point for this same campaign with release-manifest integrity verification. The older exploratory
107-JAR analyses are not part of the current 43-provider study.

`.github/workflows/scientific-checks.yml` runs the complete fresh Ant/JVM
campaign on Ubuntu/Python 3.12 within 30 minutes and uploads raw results and
logs even on failure. Preparing this workflow is not evidence of a CI run.

Useful focused commands are:

```sh
python scripts/verify_public_inputs.py
python scripts/public_corpus.py --output reproduced/public --workers 4
python -m unittest discover -s tests -p 'test_*.py' -v
python tests/oracle.py reproduced
python -B -m unittest discover -s tests -p 'test_present_provider_tuple.py' -v
```

The eight file-free provider-tuple regressions include a test-local literal-order
reference over the 90,582 labelled tiny models, strict admission and exclusion
mutations, exact force-query counts, and lazy per-row tuple preparation.
They check correctness, not runtime. The full-run measurements above remain
retained campaign evidence; they are not a fresh run of the expanded suite.

## Repository map

- `src/producer.py` normalizes the inventory and emits exact certificates.
- `src/checker.py` independently reconstructs constraints and replays them; it
  does not import producer inference code.
- `src/archive_producer.py` and `src/archive_checker.py` are separate archive
  adapters for real JAR/ZIP inputs.
- `tests/oracle.py` compares certificates with exhaustive literal permutation
  enumeration for the frozen up-to-three-provider space; `tests/test_boundary.py`
  also includes 128 fixed-seed four-to-seven-provider differential cases.
- `tests/test_present_provider_tuple.py` is a self-contained finite regression
  for the unchanged force keys and once-per-row canonical candidate tuple.
- `inputs/public/` contains the frozen public JAR corpus, pair inventory, and
  verbatim Debian copyright records.
- `scripts/public_corpus.py` materializes both Ant orders and checks builder,
  adapter, certificate, and exact-two-order agreement.
- `results/public/` retains the public summary, case table, builder log, and
  representative graphs/certificates.
- `docs/proofs.md`, `docs/protocol.md`, and `docs/study-protocol.md` state the
  semantics, arguments, certificate obligations, and fixed evaluation design.
- `docs/literature-calibration.csv` and `.md` record the 12 + 5 + 5 paper
  calibration used to position the work; `docs/reference-audit.csv` and `.md`
  record the final targeted metadata corrections.
- `claim_evidence_ledger.csv` maps every material paper claim to proofs, code,
  tests, raw results, and manuscript locations.

## What the checker establishes

For an admitted input, acceptance establishes that every reported owner is
realized by a feasible provider order and that every excluded provider/owner is
blocked by a replayable counterfactual obstruction.  Relative completeness is
with respect to the supplied closed inventory, exact observations, precedence
facts, and the frozen first-winner language.  The checker also validates its
input bounds, normalized graph, order witnesses, bytes, blocking reasons, and
owner projection.

The protocol does **not** prove that an alleged inventory is complete in the
real world.  An omitted provider carrying identical bytes is observationally
indistinguishable without authenticated acquisition evidence.  A trusted
complete provider order collapses the problem to deterministic replay and
therefore removes ownership ambiguity (or exposes inconsistent observations).

## Scope boundary

Supported transformations are simultaneous path-only relocations of opaque
entries under deterministic longest-directory-prefix rules.  Relocation or
rewriting of `.class` or `.dex` entries, within-provider target collisions,
Android resource and manifest merging, AAR variant selection, D8/R8 rewriting,
native libraries, generated code, dynamic loading/downloads, obfuscation,
reflection semantics, legal ownership, and malware attribution are outside the
implemented language.  Inputs requiring them are rejected or must be handled by
a separately proved front end.

The public study validates the exact archive-composition fragment implemented by
Apache Ant's Zip task with `duplicate="preserve"`, `filesonly="true"`, and two
explicit `zipfileset`s.  It is not presented as a complete Gradle or Android APK
build front end.

## Reference methods

The experiment includes transparent information probes, not reimplementations
of published library detectors:

- `catalogue_tiebreak`: choose one provider by a fixed catalogue order;
- `inventory_size_proxy`: choose the archive with more entries as a singleton proxy (left wins ties);
- `dependency`: return all declared providers of a path;
- `local_bytes`: return all providers with bytes equal to the output;
- `certified`: exact global owner set under the frozen semantics; and
- `trusted_trace`: singleton owner from one concrete build order.

The singleton probes are intentionally non-conservative and expose the cost of
forcing an answer.  `dependency` and `local_bytes` are conservative but may be
strictly wider than the exact global answer.  No rate in this repository is a
performance claim about LibScout, LibRadar, AndroLibZoo, or another published
tool.

## Reliability, disclosure, and licensing

All scientific inputs needed for the reported runs are retained.  Result tables
are generated from JSON/CSV evidence, and the paper build fails when required
measurements are absent.  Passing commands demonstrate execution on the
retained inputs; the ordinary mathematical proof remains distinct from finite
testing and there is no mechanized proof of the Python implementation.


Original repository material is under `LICENSE` (MIT).  The embedded public JARs
retain their own upstream terms; `licenses/NOTICE.txt`, `inputs/public/providers.csv`,
and `inputs/public/licenses/` identify and preserve those records.  The MIT
license does not relicense third-party binaries.

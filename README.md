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
| Regression and mutation tests | 74 passed in a separate Windows run; 47 in the retained Linux campaign |
| Public provider archives | 43 licensed JARs, plus 2 Ant builder JARs |
| Exhaustive public collision pairs | 40 of all 903 unordered pairs |
| Concrete public builds | 80 Ant builds: both orders for every collision pair |
| Public region observations | 165,630 total; 8,156 collision-region observations |
| External-oracle/checker disagreement | 0 |
| Hidden source flips with identical output maps | 3,471 regions across 30 reversed pairs |
| Local equal-byte ambiguities resolved globally | 100 with per-JAR labels; 0 with Debian-package labels |
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
retain their original measurements. Paper tables distinguish the retained
campaign from the separate Windows tests and owner-granularity replay.

## Reproduce everything

The finite-only campaign requires Python 3.10 or newer and its standard
library and runs on Windows or Linux. The complete external-builder campaign
additionally requires a JDK that can execute bundled Apache Ant 1.10.15 and
provide `javac` with `--release 8` support.  No network access, pip package, GPU,
model API, private cache, paper directory, or external service is required.

From the repository root:

```sh
python -B scripts/reproduce.py --output ../verification-full --java
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
python -B scripts/reproduce.py --output ../verification-finite --skip-public
```

The passive public-input census still reads the bundled archives and notices;
it does not execute their classes. Windows RSS and child CPU counters are
unavailable and recorded as null. See `ENVIRONMENT.md` for current versus
retained measurements. `scripts/reproduce_release.py` is a compatibility entry
point for this same campaign with release-manifest integrity verification.
Both examples keep their fresh results outside the artifact, so they do not
alter the retained release-manifest inventory.

For read-only result checks, run `python -B scripts/final_release_gate.py`.
It binds the finite-oracle, fixture, public-build, scale and owner-label counts
to their named JSON fields and CSV rows, independently recomputes the bundled
collision-pair census, and checks manifest membership and Python syntax. It
also checks the retained direct-comparison counts against every output/schema
row and the current 80-build census, together with the diagnostic producer and
input-catalogue bindings. Changed producers or labels require new diagnostic
evidence; they cannot inherit the recorded comparisons or zero scope changes.
The earlier diagnostic's execution receipt and test counts remain unchanged. It
prints its report without changing the artifact. These checks reuse recorded
executions; they do not run a new Ant or JVM experiment.

`.github/workflows/scientific-checks.yml` runs the complete fresh Ant/JVM
campaign on Ubuntu/Python 3.12 within 30 minutes and uploads raw results and
logs even on failure.

Useful focused commands are:

```sh
python scripts/verify_public_inputs.py
python scripts/public_corpus.py --output reproduced/public --workers 4
python -m unittest discover -s tests -p 'test_*.py' -v
python tests/oracle.py reproduced
python -B -m unittest discover -s tests -p 'test_present_provider_tuple.py' -v
python -B scripts/analyze_owner_granularity.py
```

The eight file-free provider-tuple regressions include a test-local literal-order
reference over the 90,582 labelled tiny models, strict admission and exclusion
mutations, exact force-query counts, and lazy per-row tuple preparation.
They check correctness, not runtime. The retained 74-test suite passes in the separate
Windows/Python 3.12.14 run recorded in `results/unit-tests.json` and
`results/unit-tests.txt`; the retained Linux campaign ran 47 tests and remains
the source of the full-campaign measurements above.

The archive-metadata tests validate original decoded ZIP member names before
directory or manifest filtering. They use in-memory metadata, not constructed
malformed archives. The concrete adapters reject parser-altered names, including
NUL truncation. JSON inventory names are symbolic nonempty strings and do not
carry the stricter archive-path admission guarantee; see `docs/protocol.md`.

`scripts/analyze_owner_granularity.py` reconstructs both first-winner content
maps from retained bytes without executing Ant or provider classes. It compares
local bytes and certified answers under the same information and the same label
map, checking archive-label counts against all 80 retained case records.
`results/owner-granularity.json` records 100 extra resolutions for per-JAR
labels, but zero for the recorded Debian binary-package grouping: both methods
are exact on all 8,156 collision observations with mean package-set size one.
The 100 provider-level narrowings remain. No public provider is labelled
developer, so the developer-inclusion policy changes on zero regions. This is
not a downstream analyzer, vulnerability, suppression, or call-graph experiment.

## Current bounded diagnostics

OpenAI Codex assisted manuscript revision, implementation and test development,
and checking of the ordinary arguments. Reported measurements come from the
executed artifact workflows.

Run the current offline model/receipt checks into a fresh directory:

```sh
python -B scripts/reproduce_diagnostics.py --output results/fresh-diagnostics
```

`results/diagnostics/current/` records the current execution:
110 of 111 discovered tests run and pass. The explicitly excluded retained test
writes a traversal-name ZIP; it is not executed or counted as a pass by this
benign-fixture path. The other tests include the unchanged 90,582-model finite
family, owned ordinary ZIP readback, metadata-only NUL admission controls, and
four new interface/receipt/decision controls and one Java-entry portability
control that reaches the missing-JDK error without running Java. No generated
population is added. Six command-capture and optimization-guard controls also
test raw diagnostic preservation, nonzero compiler/builder exits and exact
numeric probe decoding.

The diagnostic includes thirteen original result-binding controls that reject missing named sources, unrelated
numeric reports, changed summary fields, inconsistent census rows, duplicate
keys or columns, Boolean count substitutions and nonfinite numbers. Two
manifest controls reject duplicate membership and invalid relative paths.
Eight additional auditor tests cover the direct-comparison records,
their row membership, receipt, source bindings and label census. The complete
21-method auditor suite is included in the current 110-test execution. Earlier
diagnostic receipts retain their own original execution counts and logs.

The owner diagnostic admits exactly two complete provider maps and two labels,
rejecting a third rather than omitting it. Zero-collision rates and means are
undefined (`null`), not a division error or an exactness score. It records
actual developer-inclusion counts for local, certified and direct two-order
methods. Both label schemes have 8,156 direct--certificate owner and decision
matches and zero developer inclusions for all three methods. The package map
removes the 100 per-JAR owner narrowings, not the provider-level exclusions.
These are conditional calculations under supplied labels, not label validation.

The current record contains all 160 per-output/schema count observations, the
40-pair input census, 36 unchanged retained-metric checks, selected test IDs,
raw logs, source/input bindings and the Windows/Python environment. It records
**zero new Ant builds**, zero provider-code execution and zero extraction.
The earlier `results/current/`, `results/unit-tests.*` and
`results/owner-granularity.json` stay separate and unchanged. The manuscript
table generator consumes the new diagnostic receipt without relabelling those
historical executions as current-code validation.

The separate current native replay in `results/native-replay/` executes all 80
Ant builds and both owned Java assemblies. All 165,630 regional observations
agree with the native two-order oracle, and the owned probe returns 11 and 22.
The same frozen input corpus is used; these are not extra independent projects.

The public study's optional `--prebuilt-output-dir` mode checks supplied ZIP
contents but records `execution_mode: prebuilt-output-replay`,
`actual_ant_builds: 0`, `builder: null` and
`ant_first_winner_mismatches: null`. `output_first_winner_mismatches` reports the
content check separately. Its orchestration is covered by a mock receipt test;
that test's forty slots are not forty actual public builds. The owned two-ZIP
readback test exercises serialized certificates independently. Native execution
is represented by the separate current replay, not by the mock.

The owned Java entry now uses the common optional OS-counter interface instead
of importing POSIX-only `resource` unconditionally. A platform without those
counters can reach explicit JDK admission. If a native run is performed there,
unavailable child CPU/RSS and aggregate CPU are null, while measured parent
CPU remains separate. The native replay used an isolated Temurin JDK
21.0.12.1. Compiler and builder streams are retained as raw bytes; display-only
decoding does not determine build success or change the numeric probe contract.
Standalone Java and diagnostic commands reject optimized Python before output
creation because their scientific checks require active assertions.

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

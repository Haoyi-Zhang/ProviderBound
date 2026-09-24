# Literature calibration: 12 same-venue + 5 influential + 5 adjacent papers

This matrix calibrates the manuscript’s contribution, evidence standard, and narrative structure. It is a qualitative reading matrix, not a systematic review, venue-median estimate, or award claim. For each paper, the review covered the full available article or author manuscript at least across the abstract, introduction, method/design, evaluation or central argument, threats/limitations where present, and conclusion. Bibliographic claims are tied to the manuscript bibliography; papers are not redistributed.

## Coverage

- **12 same-venue TOSEM articles:** Android/static-analysis, binary-similarity, repair, program-analysis, repository-mining, and supply-chain examples.
- **5 foundational or demonstrably influential papers:** proof-carrying code, verified compilation, FlowDroid, build-system semantics, and in-toto.
- **5 adjacent papers:** AndroLibZoo and four strong Android third-party-library detection/versioning systems.

## Cross-paper patterns used in the manuscript

1. **Concrete failure before abstraction.** Strong papers first establish a real analysis or engineering failure, then introduce the general mechanism. The manuscript therefore opens with byte-identical outputs whose hidden winners differ and a mixed pair where one path constrains ownership elsewhere.
2. **Assumptions as part of the contribution.** Build and Android papers make semantic coverage explicit. The manuscript freezes the first-winner language and rejects unsupported transforms instead of implying full Gradle/Android coverage.
3. **Separate theorem, implementation, and external validity.** Formal papers distinguish semantic guarantees from mechanization; systems papers distinguish implementation tests from workload evidence. The manuscript reports ordinary proofs, exhaustive tiny-model checking, mutation tests, and external Ant agreement as different evidence classes.
4. **Strongest related systems are not straw baselines.** The library-detection papers use structural and transformation-resilient evidence. The two singleton rules in the experiment are therefore described only as transparent information probes, not as replicas of published detectors.
5. **Evaluation needs a real semantic bridge.** Android/TOSEM studies connect mechanisms to real artifacts. The 80 Ant builds provide that bridge for duplicate-path archive semantics while the paper explicitly withholds full-Android claims.
6. **Artifacts support claims but do not replace them.** Main guarantees and limitations stay in the article; the repository supplies replayable code, inputs, certificates, and raw results.

## Per-paper matrix


### Same-venue TOSEM articles

| Key | Year | Paper | Problem and principle | Evidence/narrative lesson |
|---|---:|---|---|---|
| `libam` | 2024 | LibAM: An Area Matching Framework for Detecting Third-Party Libraries in Binaries | Detect reused library areas when whole-library and package boundaries are unreliable. Build function-level area representations and align anchors rather than relying on names alone. | Use a concrete running notion of region, compare to strongest practical systems, keep exact-byte scope explicit. |
| `incompatibleapi` | 2024 | Automatically Detecting Incompatible Android APIs | Android API behavior and availability differ across versions and devices. Combine static analysis and compatibility specifications to identify incompatible uses. | Separate language assumptions from empirical claims and report unsupported Android features directly. |
| `tamingreflection` | 2021 | Taming Reflection: An Essential Step Toward Whole-program Analysis of Android Apps | Reflective calls hide targets from Android whole-program static analysis. Resolve targets through constant propagation and instrument equivalent direct calls for downstream analyzers. | State excluded mechanisms once, explain why they can invalidate inventory completeness. |
| `hiddenops` | 2023 | Demystifying Hidden Sensitive Operations in Android Apps | Sensitive behavior can be hidden behind framework and atypical invocation mechanisms. Model hidden operations and reveal them to security analysis. | Do not overclaim downstream security benefit from a boundary certificate alone. |
| `reunify` | 2025 | Demystifying React Native Android Apps for Static Analysis | Cross-language React Native structure fragments code and call information. Recover and unify native/JavaScript components for analysis. | Frame the current archive language as a reusable kernel, not an end-to-end Android solution. |
| `archer` | 2026 | Resolving Conditional Implicit Calls to Improve Static and Dynamic Analysis in Android Apps | Android framework callbacks and conditional implicit calls are missed by conventional call graphs. Resolve implicit calls with conditions and integrate them into analyses. | Use contemporary closest work to bound claims and motivate authenticated build evidence. |
| `arcturus` | 2024 | ARCTURUS: Full Coverage Binary Similarity Analysis with Reachability-guided Emulation | Binary similarity misses behavior when static coverage is incomplete. Guide emulation with reachability to improve representation coverage. | Keep reference methods honest and avoid presenting local byte equality as a detector benchmark. |
| `beyondtests` | 2021 | Beyond Tests: Program Analysis as a Generalisation of Testing | Testing samples executions while analysis can summarize larger behavior sets. Relate testing and program analysis through a common conceptual framework. | Lead from a concrete ambiguity to the general principle before implementation details. |
| `seads` | 2021 | SEADS: Scalable and Cost-effective Dynamic Dependence Analysis of Distributed Systems via Reinforcement Learning | Dynamic dependence tracking in distributed systems is costly. Use adaptive selection to reduce observation cost while retaining useful dependence information. | Report resource behavior as measured evidence, not as a universal complexity claim. |
| `reliablefix` | 2023 | Reliable Fix Patterns Inferred from Static Checkers for Automated Program Repair | Static checker findings can seed repair but naive pattern mining is unreliable. Infer and validate fix patterns grounded in checker evidence. | Make producer/checker trust separation central and include adversarial mutations. |
| `seal` | 2023 | SEAL: Integrating Program Analysis and Repository Mining | Static analysis and repository history offer complementary evidence but are often isolated. Integrate code semantics with mined evolution information. | Separate upstream candidate evidence, build evidence, certificate, and downstream policy. |
| `supplychainresearch` | 2025 | Research Directions in Software Supply Chain Security | Software supply-chain risks span dependencies, builds, provenance, and governance. Organize open research directions across the supply chain. | State what the certificate can consume from provenance systems and what it cannot authenticate itself. |

### Foundational / influential papers

| Key | Year | Paper | Problem and principle | Evidence/narrative lesson |
|---|---:|---|---|---|
| `pcc` | 1997 | Proof-Carrying Code | A code consumer should validate safety without trusting the producer. The producer supplies a proof; a small checker validates it against a policy. | Make checker obligations explicit and smaller than producer search. |
| `compcert` | 2009 | Formal Verification of a Realistic Compiler | Optimizing compilers are too complex to trust solely through testing. Mechanize a semantics-preservation proof for a realistic compiler. | Distinguish ordinary theorem proof, finite oracle, and implementation assurance. |
| `flowdroid` | 2014 | FlowDroid: Precise Context, Flow, Field, Object-sensitive and Lifecycle-aware Taint Analysis for Android Apps | Android lifecycle and callbacks frustrate precise taint analysis. Model lifecycle semantics with a precise interprocedural data-flow analysis. | Do not transfer JAR-fragment evidence to complete Android analysis. |
| `buildsystems` | 2018 | Build Systems à la Carte | Build systems mix dependency discovery, scheduling, and rebuilding semantics. Factor build systems into reusable abstractions and explicit choices. | Define worlds and builder semantics before discussing algorithms. |
| `intoto` | 2019 | in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes | Consumers lack end-to-end evidence about software supply-chain steps. Record and verify signed link metadata for authorized steps and materials/products. | Treat inventory authenticity as an upstream premise, not something inferred from output bytes. |

### Adjacent venue papers

| Key | Year | Paper | Problem and principle | Evidence/narrative lesson |
|---|---:|---|---|---|
| `androlibzoo` | 2024 | AndroLibZoo: A Reliable Dataset of Libraries Based on Software Dependency Analysis | Android analyzers need a reliable evolving library catalogue. Mine declared software dependencies and refine identifiers into a reusable dataset. | Explain the trust-boundary change without mischaracterizing catalogue methods. |
| `libscout` | 2016 | Reliable Third-Party Library Detection in Android and its Security Applications | Package names and hashes fail under common Android transformations. Build structural profiles from original SDKs to identify libraries and versions. | Position certification after candidate discovery; do not call a name lookup “LibScout-like”. |
| `libd` | 2017 | LibD: Scalable and Precise Third-Party Library Detection in Android Markets | Market-scale library detection needs both scalability and precision. Use feature-based clustering/matching suitable for large Android corpora. | Keep scale-probe claims descriptive and separate from market-scale applicability. |
| `libid` | 2019 | LibID: Reliable Identification of Obfuscated Third-Party Android Libraries | Obfuscation and library customization defeat naive identifiers. Combine resilient signatures and matching to identify library identity/version. | Reject unsupported transforms instead of silently inheriting detector equivalence. |
| `atvhunter` | 2021 | ATVHunter: Reliable Version Detection of Third-Party Libraries for Vulnerability Identification in Android Applications | Vulnerability analysis needs exact third-party library version identification. Use multi-stage structural matching to identify versions despite transformations. | Avoid claiming legal/security attribution from first-winner provenance alone. |

The machine-readable CSV beside this file records all requested dimensions: motivating problem, general principle, proof/performance argument, practical connection, evaluation breadth, artifact strength, narrative sequence, and the lesson applied to this project.

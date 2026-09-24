# Claim-language audit

Blocking rules are deliberately narrow. Sensitive contexts require human reading and are not automatic errors.

Blocking hits: **0**


## Scope-sensitive contexts

| Source | Text |
|---|---|
| `main.tex:18` | \title{Proof-Carrying Provider Attribution under First-Winner Archive Merging} |
| `main.tex:28` | \newcommand{\first}{\operatorname{first}} |
| `main.tex:36` | We study that provenance question for a closed, finite first-winner language: |
| `main.tex:44` | Ordinary proofs establish soundness and relative completeness within the |
| `main.tex:50` | have zero mismatches against this complete two-order oracle.  Thirty reversed |
| `main.tex:54` | 100 equal-byte observations beyond local byte matching.  The guarantees remain |
| `main.tex:55` | conditional on a complete supplied inventory and the declared merge semantics; |
| `main.tex:56` | they do not cover arbitrary Gradle/Android transformations or infer omitted |
| `main.tex:58` | \par\noindent Throughout, an owner is a caller-supplied label over build-input providers; it is neither inferred authorship nor legal ownership. Our empirical claims concern JAR/ZIP first-winner archive merging, not Android resource merging, variant selection, D8/R8, or dynamic loading. |
| `sections/01-introduction.tex:4` | Static analyses of Android applications routinely distinguish application code |
| `sections/01-introduction.tex:11` | of Android static analysis and third-party-library research likewise identify |
| `sections/01-introduction.tex:27` | A downstream analyzer, however, may need a different guarantee: given a |
| `sections/01-introduction.tex:32` | If the build operation retains the first occurrence under one global provider |
| `sections/01-introduction.tex:56` | proposes an ownership set for every output region.  A separately implemented |
| `sections/01-introduction.tex:69` | first provider in that order that contains a name wins, and the observation |
| `sections/01-introduction.tex:73` | inventory itself is complete.  These restrictions are not descriptive claims |
| `sections/01-introduction.tex:74` | about Android or Gradle; they are the boundary within which the answer can be |
| `sections/01-introduction.tex:81` | ownership semantics and a complete replay protocol for each region.  Positive |
| `sections/01-introduction.tex:96` | first-winner builder, does the independent lowering and certificate checker |
| `sections/01-introduction.tex:107` | substituting one for another.  First, ordinary mathematical arguments prove the |
| `sections/01-introduction.tex:109` | soundness, and relative completeness.  Second, literal enumeration covers |
| `sections/01-introduction.tex:118` | providers, those two builds enumerate the complete order space for that case. |
| `sections/01-introduction.tex:124` | the complete output content map unchanged while changing the hidden provider |
| `sections/01-introduction.tex:132` | Android APKs, AAR transformation pipelines, obfuscated applications, or the |
| `sections/01-introduction.tex:133` | completeness of a global library catalogue. |
| `sections/01-introduction.tex:141` | ordered first-winner assembly and |
| `sections/01-introduction.tex:145` | completeness arguments and an independently written replay checker. |
| `sections/01-introduction.tex:155` | The paper does not claim a new library detector, a complete Android build |
| `sections/02-question.tex:8` | Figure~\ref{fig:coupled}. A first-winner assembler can produce this observation |
| `sections/02-question.tex:17` | that both providers contribute to each output entry. Only the first provider at |
| `sections/02-question.tex:34` | to one library. None of those possibilities licenses a legal-ownership claim. |
| `sections/02-question.tex:42` | Their local observations can remain unchanged while the actual first provider |
| `sections/02-question.tex:57` | bytes are provided, but some provider ordering is not. If the actual complete |
| `sections/02-question.tex:61` | Another tempting shortcut is to infer common ownership from an ordinary |
| `sections/02-question.tex:74` | coupled first-winner selection from finite inventories. |
| `sections/02-question.tex:87` | The first is \emph{admission}: can the supplied archives and transformations be |
| `sections/02-question.tex:89` | one order reproduce all observed bytes?  The third is \emph{ownership}: among |
| `sections/02-question.tex:92` | strange form of inconsistency, and an inconsistent graph has no ownership set |
| `sections/02-question.tex:99` | cycle, or mutually incompatible first-winner requirements is admitted but |
| `sections/02-question.tex:107` | model.  Neither is supplied.  Treating the first enumerated order as more likely |
| `sections/02-question.tex:128` | first in a catalogue. |
| `sections/02-question.tex:133` | shrinks.  The certificate for developer ownership contains an $a,b$ world and |
| `sections/02-question.tex:137` | If a second probe requires $b$ before $a$ while the first requires $a$ before |
| `sections/02-question.tex:164` | At the other extreme, shipping every feasible order would be complete but can |
| `sections/03-model.tex:1` | \section{Frozen Inventories and Ownership Worlds} |
| `sections/03-model.tex:87` | \subsection{A completeness premise cannot be certified from itself} |
| `sections/03-model.tex:100` | omits a real input and has a different first provider. A procedure acting on |
| `sections/03-model.tex:102` | cannot certify actual completeness in general. |
| `sections/03-model.tex:105` | The result does not prevent completeness from being established by additional |
| `sections/03-model.tex:108` | premises. The ownership checker cannot manufacture that record from identical |
| `sections/03-model.tex:130` | A higher-assurance deployment could retain complete payloads or use an |
| `sections/03-model.tex:141` | Many provider permutations induce the same first winner at every region.  Let |
| `sections/03-model.tex:154` | respected, and every row's first present provider is good.  A compressed |
| `sections/03-model.tex:170` | histories of this kind.  If their first providers differ at a shared name, the |
| `sections/03-model.tex:194` | precedence edges, revealing a trusted complete order, or replacing an unknown |
| `sections/03-model.tex:221` | be worse than a smaller honest model.  An extension is scientifically complete |
| `sections/04-certificates.tex:11` | If the first candidate is good, it is earlier than every bad candidate. |
| `sections/04-certificates.tex:12` | Conversely, if the first candidate were bad, the stated condition would supply |
| `sections/04-certificates.tex:21` | the disjunction by activating the row when its first good provider is selected. |
| `sections/04-certificates.tex:44` | requirements by Equation~\eqref{eq:eligibility}. A complete order therefore |
| `sections/04-certificates.tex:47` | $\pi$ exists. Choose the first provider $v$ of $\pi$ that is not in $S$. |
| `sections/04-certificates.tex:71` | provider first activates a row, the blocked counts of its bad providers are |
| `sections/04-certificates.tex:76` | reported as a linear bound for the full ownership producer. |
| `sections/04-certificates.tex:81` | have a first member in any valid order. |
| `sections/04-certificates.tex:96` | For soundness, suppose a world existed and choose its first member $v$ of |
| `sections/04-certificates.tex:99` | all such good providers lie in $U$, again a contradiction. For completeness, |
| `sections/04-certificates.tex:106` | The proof depends on complete reason coverage. A set with a reason for only |
| `sections/04-certificates.tex:107` | one of several nodes does not show that its first node is blocked. It also |
| `sections/04-certificates.tex:131` | an original world has $p$ as its first provider at $r$. |
| `sections/04-certificates.tex:153` | \subsection{Sound and relatively complete owner answers} |
| `sections/04-certificates.tex:156` | order whose first provider at $r$ has that label. For every compatible provider |
| `sections/04-certificates.tex:183` | Relative completeness here is a property of the finite language and the |
| `sections/04-certificates.tex:184` | certificate protocol. It does not assert complete Android modeling, complete |
| `sections/04-certificates.tex:185` | inventories in reality, or a universal wall-time guarantee. Nor is it a |
| `sections/04-certificates.tex:194` | a bijection between worlds, and corresponding first providers retain their |
| `sections/04-certificates.tex:210` | \emph{available} when two conditions hold.  First, every declared predecessor |
| `sections/04-certificates.tex:215` | The second condition follows directly from first-winner semantics.  If $p$ is |
| `sections/04-certificates.tex:220` | $p$: if it becomes the first present provider, it satisfies the row. |
| `sections/04-certificates.tex:230` | completeness.  Accessibility of the associated Horn-rule system ensures that |
| `sections/04-certificates.tex:233` | set but lists a different available provider first.  Moving the chosen |
| `sections/04-certificates.tex:235` | bad first winner: all its predecessors and all rows that need an earlier good |
| `sections/04-certificates.tex:287` | complete candidate set.  The key is sufficient because $F(r,p)$ depends only |
| `sections/04-certificates.tex:304` | \subsection{A complete certificate for the running example} |
| `sections/04-certificates.tex:323` | correspond exactly to unique ownership, ambiguity, and inconsistency. |
| `sections/04-certificates.tex:331` | A trusted complete provider order $\tau$ leaves at most one candidate world: it |
| `sections/04-certificates.tex:333` | Thus complete-order evidence eliminates ownership ambiguity in this language. |
| `sections/04-certificates.tex:334` | It does not guarantee consistency or inventory completeness.  This corollary |
| `sections/04-certificates.tex:341` | exact-byte reference performs the first removal independently per row; the |
| `sections/05-implementation.tex:37` | one. Certificate fields are checked explicitly, including complete regional |
| `sections/05-implementation.tex:57` | query by the forced provider and complete candidate set, and interns repeated |
| `sections/05-implementation.tex:59` | when the obstruction reference, forced provider and complete candidate set |
| `sections/05-implementation.tex:73` | patterns to expose this distinction. It does not infer a compression guarantee |
| `sections/05-implementation.tex:129` | whose complete content map is compared with predictions for both concrete |
| `sections/05-implementation.tex:151` | complete complement of excluded good providers.  It also derives the displayed |
| `sections/05-implementation.tex:178` | Every command writes results into a caller-selected destination.  A stage first |
| `sections/05-implementation.tex:202` | cell is questioned, while the complete command verifies that no hidden working |
| `sections/06-method.tex:5` | an Android-app accuracy claim.  The central empirical obligation is to test |
| `sections/06-method.tex:7` | same first-winner operation, including cases where local bytes are |
| `sections/06-method.tex:22` | \item[H2: external first-winner fidelity.] For every selected two-provider |
| `sections/06-method.tex:24` | the content map predicted by first-winner semantics, both independently |
| `sections/06-method.tex:28` | occurring public pair for which reversing provider order preserves the complete |
| `sections/06-method.tex:60` | permutation, filters by precedence, evaluates first-winner output bytes, and |
| `sections/06-method.tex:138` | JARs are launched in a child JVM.  The complete output archives are then read |
| `sections/06-method.tex:146` | total orders.  Building both orders therefore enumerates the complete world |
| `sections/06-method.tex:166` | \item \textbf{Catalogue tie-break} always chooses the first catalogue entry. |
| `sections/06-method.tex:177` | \item \textbf{Trusted trace} returns the actual first provider for a concrete |
| `sections/06-method.tex:191` | Additional metrics count complete output maps that remain identical after |
| `sections/07-results.tex:51` | \subsection{RQ2: agreement with an external first-winner builder} |
| `sections/07-results.tex:64` | with first-winner prediction.  The producer-side and checker-side archive |
| `sections/07-results.tex:79` | whole Android toolchain.  Ant is neither Gradle's complete dependency resolver |
| `sections/07-results.tex:80` | nor the Android Gradle Plugin's transform pipeline.  No APK signing, resource |
| `sections/07-results.tex:84` | first-winner ZIP/JAR merge on the retained corpus. |
| `sections/07-results.tex:92` | complete output content map.  Nevertheless, the first provider changes.  Over |
| `sections/07-results.tex:102` | the component family; none can reconstruct the historical first provider from |
| `sections/07-results.tex:120` | For the build whose output contains the first archive's policy bytes, the |
| `sections/07-results.tex:121` | second-before-first order is globally impossible; the reverse holds for the |
| `sections/07-results.tex:123` | the same first provider. |
| `sections/07-results.tex:129` | single owner allowed by the complete output.  The example is natural in the |
| `sections/07-results.tex:208` | fixed provider is first in one build and second in the other.  This arithmetic |
| `sections/07-results.tex:217` | plausible pipeline, but end-to-end Android accuracy remains future work. |
| `sections/07-results.tex:222` | with a median of \CertMedianKiB{} KiB.  In the retained measurement run, the public stage completed in 27.95 |
| `sections/07-results.tex:226` | current host completed in roughly 46--50 seconds.  Both figures are descriptive, |
| `sections/07-results.tex:229` | Certificate size reflects the deliberate choice to retain complete witness |
| `sections/07-results.tex:245` | are not estimates of Android prevalence. |
| `sections/07-results.tex:280` | with the concrete two-order oracle.  This supports the first-winner archive |
| `sections/07-results.tex:281` | fragment, not complete Android builds. |
| `sections/07-results.tex:291` | \CertMedianKiB{} KiB, and all bounded scale probes replay.  Complete orders and |
| `sections/08-discussion.tex:9` | \subsection{Library identification and Android analysis boundaries} |
| `sections/08-discussion.tex:11` | Android library research has progressively strengthened the evidence used to |
| `sections/08-discussion.tex:23` | Binary software-composition analysis extends the problem beyond Android |
| `sections/08-discussion.tex:32` | question: which candidates can be first winners under one explicit assembly |
| `sections/08-discussion.tex:39` | infrastructure used by many Android studies \cite{androzoo}.  Both illustrate |
| `sections/08-discussion.tex:45` | The boundary also affects general Android analysis.  FlowDroid and IccTA model |
| `sections/08-discussion.tex:75` | from Android external validity. |
| `sections/08-discussion.tex:90` | scheduling abstractions \cite{buildsystems}.  Our first-winner model is much |
| `sections/08-discussion.tex:95` | A future Gradle or Android extension should add those semantics explicitly |
| `sections/08-discussion.tex:96` | rather than interpreting the current theorem as a generic build guarantee. |
| `sections/08-discussion.tex:110` | how outputs depend on inputs \cite{provenance}.  First-winner ownership is a |
| `sections/08-discussion.tex:131` | Android data-flow results \cite{dcert}.  The present object differs in both |
| `sections/08-discussion.tex:134` | completeness therefore requires a counterfactual obstruction for every excluded |
| `sections/08-discussion.tex:150` | semantics are correct and complete, the accepted certificate equals the owner |
| `sections/08-discussion.tex:151` | projection of every feasible first-winner order.  The mathematical proof gives |
| `sections/08-discussion.tex:156` | identical-output pairs show that output bytes cannot reveal a hidden first |
| `sections/08-discussion.tex:173` | Exact owner projection in the frozen language & Soundness and relative-completeness arguments; exact small oracle; accepted certificates & Correct language definition, checker/runtime, complete supplied facts \\ |
| `sections/08-discussion.tex:174` | External first-winner conformance & 80 Apache Ant builds; two independent archive adapters; complete two-order oracle & Ant fragment only, not Gradle, AAR, DEX, resource merging, or rewriting \\ |
| `sections/08-discussion.tex:176` | Nonlocal precision & Mixed public pair with 100 equal-byte observations resolved by one differing path & Frequency and magnitude are not estimated for Android applications \\ |
| `sections/08-discussion.tex:177` | Offline reproducibility & Retained inputs, licenses, scripts, raw summaries, and clean-extraction rerun & No authentication of historical origins or guarantee for future toolchains \\ |
| `sections/08-discussion.tex:191` | builder experiment, and offline package can be complete while live venue rules, |
| `sections/08-discussion.tex:196` | The results do not establish the prevalence of these phenomena in Android apps. |
| `sections/08-discussion.tex:209` | first-winner provenance under one build operation.  Calling the result |
| `sections/08-discussion.tex:249` | The model excludes Android resource merging, manifest mergers, DEX and R8/D8 |
| `sections/08-discussion.tex:254` | JAR/ZIP first-winner fragment, not an APK ownership oracle. |
| `sections/08-discussion.tex:261` | complete consumed input sequence. |
| `sections/08-discussion.tex:290` | analysis as four explicit stages.  First, an existing library detector or |
| `sections/08-discussion.tex:304` | first label in a serialized set has no semantic justification. |
| `sections/08-discussion.tex:308` | policy used to turn set-valued ownership into analysis scope.  When a finding is |
| `sections/08-discussion.tex:318` | change ownership elsewhere.  Safe incremental validation must track the rows |
| `sections/08-discussion.tex:320` | recheck the complete graph.  The current artifact performs complete replay and |
| `sections/08-discussion.tex:332` | consumed provider list, complete order, and output digest.  With a trusted |
| `sections/08-discussion.tex:333` | complete order, the inference collapses to deterministic replay, but the |
| `sections/08-discussion.tex:354` | but inventory completeness, label provenance, or trace authenticity lacks |
| `sections/08-discussion.tex:369` | complete order.  Each level changes the interpretation of the same finite |
| `sections/08-discussion.tex:376` | affirmative answers: (1) is the provider inventory believed complete for the |
| `sections/08-discussion.tex:379` | does one global first-provider order govern duplicate paths; and (5) are owner |
| `sections/09-conclusion.tex:4` | For finite first-winner assembly, library-boundary provenance is an exact |
| `sections/09-conclusion.tex:8` | inconsistency, ambiguity, and unique ownership as distinct machine-checkable |
| `sections/09-conclusion.tex:15` | changes behind identical complete content maps and show one global-order |
| `sections/09-conclusion.tex:18` | These guarantees are a proof boundary, not a universal Android build model. |
| `sections/09-conclusion.tex:19` | Candidate detection, inventory completeness, owner-label validity, and |
| `sections/09-conclusion.tex:20` | transformations outside path-only first-winner assembly remain external |

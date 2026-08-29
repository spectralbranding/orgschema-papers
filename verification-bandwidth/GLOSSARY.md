<!-- GENERATED FILE - do not hand-edit. This glossary is a rendered projection of the corpus ontology graph, regenerated on each release. -->

## Glossary

_Terms used by **2026bn** (Verification Bandwidth Under Correlated Evaluators: What an Effective-Sample-Size Statistic Measures in an Acceptance Cascade). Defined terms this paper introduces, refines, or imports from the corpus ontology._

*Terms introduced by this paper*

- **accountable-signatory residual**
  - The share of a specification's stated acceptance conditions whose satisfaction a receiving executor's panel cannot independently establish, and which some identified party must therefore underwrite by assurance rather than by test. It is the complement of the transferable share, it grows as the ratio of specified conditions to effective verification rank grows, and it is what remains of a signature once verification is treated as a capacity with a measurable ceiling rather than as an attestation.
  - _not_: sign-off; the human in the loop
  - first use: What Does Not Transfer
- **detection bracket**
  - The interval between the detection probability of the unanimous rule and that of the disjunctive rule, within which every aggregation rule that neither flags what no member flagged nor clears what every member flagged must lie, for every deviation distribution. Its WIDTH is the probability that the panel disagrees, so it narrows as evaluator errors become correlated and is exactly zero when they are perfectly correlated. Where the bracket has closed, the choice of aggregation rule cannot change what the panel detects.
  - _not_: aggregation envelope
  - first use: The Bracket
- **engineered evaluator diversity**
  - The deliberate spreading of a panel's inspection directions, as opposed to enlarging the panel and letting diversity arrive by sampling. The distinction is forced by a ceiling: independently and uniformly oriented evaluators saturate near the square root of the state-space dimension rather than at their own number, so beyond a modest size additional evaluators recruited without regard to what they inspect add nominal capacity and no effective capacity.
  - _not_: evaluator diversity; panel heterogeneity
  - first use: The Dimensional Ceiling
- **error-vector design effect**
  - The design effect, and the effective sample size derived from it, computed on evaluators' binary ERROR indicators against gold labels rather than on their raw judgements. Computing it on errors rather than on codes is what separates shared signal -- items really do differ -- from shared error, which is the dependence that costs a panel its independence. The quantity is borrowed from survey sampling by way of the evaluation-panel literature; what is established here is what it measures.
  - _not_: effective number of judges; effective votes
  - first use: What the Statistic Already Is
- **evaluator blind spot**
  - The set of deviations one evaluator cannot detect: the kernel of its projection in the exact case, and the region below its detection threshold in general. Blind spots compose differently under different aggregation rules, and that difference is the whole content of the detection bracket -- the disjunctive rule's blind spot is the intersection of the members' blind spots and is a subspace, while the unanimous rule's is their union and in general is not.
  - first use: The Model
- **folded dichotomization**
  - The closed-form map carrying the geometric correlation between two evaluators' inspection directions to the correlation of their binary error indicators, under a two-sided detection rule that flags on absolute magnitude. It is the classical dichotomization of a bivariate normal with the two tails folded together, and it is even in its argument, strictly increasing, fixed at both endpoints, and strictly below the identity. That last property is what makes the statistic computed on errors a bound rather than an estimate.
  - first use: From Geometry to Error
- **inspection subspace**
  - The subspace of the organizational state space that one evaluator can read: the range of that evaluator's projection. An evaluator flags a deviation only when the component of it lying in this subspace exceeds a threshold, so the subspace, not the evaluator's diligence, fixes what that evaluator is capable of detecting at all. Naming it separately from the accepted subspace is what keeps the two readings of a projection apart.
  - _not_: invariant subspace; what the evaluator checks
  - first use: The Model

*Imported terms refined by this paper*

- **Verification Bandwidth** (write: `verification bandwidth`)
  - _refined here_: the multi-evaluator case, where the maximum number of independent specification conditions an organization can evaluate per cycle is the effective RANK of its panel's family of inspection directions -- and is therefore bounded above by the design effect computed on that panel's error vectors, without inverting anything or assuming a distribution
  - The maximum number of independent specification conditions an organization can evaluate per verification cycle, which bounds the projection rank it can sustain at steady state.

*Imported terms (defined elsewhere)*

- **Cascade Consistency Condition** (write: `cascade consistency condition`)
  - The requirement that range($P_k$) is not contained in kernel($P_{k+1}$) for all $k$, ensuring each cascade level contributes independent information so the cascade remains full-rank.
  - _defined by 2026ae_
- **Executor Invariance** (write: `executor-invariant`)
  - The property that a specification level defines what must be achieved independently of who or what achieves it, drawing the boundary between contract levels (L0-L2) and implementation levels (L3-L5).
  - _defined by 2026i_
- **Organizational Metamerism** (write: `organizational metamerism`)
  - An observer-relative condition in which two structurally distinct organizational configurations executing the same process map to identical value outputs for a specific evaluator.
  - _defined by org-as-metadata_
- **Projection Cascade** (write: `projection cascade`)
  - A six-tier sequence of rank-reducing linear projection operators linking owner intent, business model, governance, architecture, routines, and positions, in which each junction carries a rank deficiency that bounds downstream information loss.
  - _defined by 2026m_
- **Rank-1 Audit** (write: `rank-1 audit`)
  - Conventional audit modeled as a degenerate rank-1 projection onto a single compliance axis, discarding by construction all information orthogonal to that axis.
  - _defined by 2026ae_
- **Six-Level TDD Cascade** (write: `six-level TDD cascade`)
  - The core OST artifact: a six-level specification cascade (L0 experience contracts through L5 sourcing) where each level functions as the acceptance test for the level below it.
  - _defined by 2026i_
- **Spectral Projection Operator** (write: `spectral projection operator`)
  - An idempotent ($P^2=P$), self-adjoint ($P^*=P$) linear map onto an invariant subspace whose rank determines how many independent dimensions of organizational performance the verification process can discriminate.
  - _defined by 2026ae_
- **Verification as Operator** (write: `verification as operator`)
  - The formalization of organizational verification as a spectral projection operator P that maps organizational states onto invariant subspaces defined by acceptance criteria.
  - _defined by 2026ae_

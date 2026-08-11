# Verification Bandwidth Under Correlated Evaluators: What an Effective-Sample-Size Statistic Measures in an Acceptance Cascade

Dmitry Zharnikov

ORCID: 0009-0000-6893-9231

DOI: [10.5281/zenodo.21891435](https://doi.org/10.5281/zenodo.21891435)

Working Paper v1.0.0 – August 2026

---

## Abstract

Organizational verification is representable as an orthogonal projection whose rank bounds what an organization detects about itself, but that formalization assumes one evaluator per acceptance test and supplies no procedure for estimating the projection. This paper establishes what a panel buys. Every aggregation rule that neither flags what no member flagged nor clears what every member flagged has a detection probability lying between the unanimous and the disjunctive rule, and the width of that bracket is the probability the panel disagrees, which vanishes as evaluator errors become correlated. Above a correlation level, therefore, no aggregation rule recovers detection the evaluator set does not collectively possess, however well designed. For evaluators whose inspection directions carry a geometric correlation, a closed-form folded dichotomization maps that geometry to the correlation of their errors and lies strictly below the identity, so the effective-sample-size statistic already used to audit evaluator panels is an upper bound on the rank of the acceptance projection. The statistic is borrowed and cited; what is new is that it measures a rank. Two consequences follow: randomly constituted panels saturate near the square root of the state-space dimension, and the independently verifiable share of a transferred specification is capped accordingly.

**Keywords**: verification, effective sample size, design effect, evaluator panels, correlated errors, acceptance testing, organizational design, projection rank.

---

Organizations check themselves through acceptance tests, and an acceptance test reads some of what it is given and discards the rest. Represented formally, the test is an orthogonal projection, and the rank of that projection is the number of independent things the organization is capable of noticing about its own state — so a low-rank test guarantees that deviations lying outside what it reads stay invisible however diligently it is applied [@zharnikov-2026-verification-as-operator-why-acceptance; @zharnikov-2026m-projection-cascade-why]. That account is stated for a single authoritative evaluator per cascade level. It says so in print, names multi-evaluator regimes as an extension requiring separate treatment, states that it provides no procedure for estimating the projections empirically, and flags formal comparison with an adjacent bounded-verification framework as warranting dedicated treatment [@zharnikov-2026-verification-as-operator-why-acceptance; @kovalenko-2026-bounded-compositional-verification]. This paper closes the first two of those gaps and, in doing so, changes what a familiar statistic is understood to measure.

The reason the single-evaluator restriction is not cosmetic is that the obvious extension has two readings that point in opposite directions. On one, adding evaluators with different views shrinks what is jointly accepted, because a configuration must now satisfy all of them; the parent text takes this reading and observes that cascade rank under disagreement may fall below any single evaluator's. On the other, adding evaluators with different views raises the number of dimensions someone is checking, so rank should rise. Both readings are defensible and they cannot both describe the same quantity. The resolution is that they are not two descriptions of one thing but two aggregation rules, and the interesting object is what lies between them.

Four literatures already own pieces of this, and the paper concedes all four before claiming anything. That the gain from combining predictors is limited by the correlation among them is the classical content of the error–ambiguity decomposition and of the ensemble-diversity literature built on it [@krogh-1994-neural-network-ensembles-cross-validation; @kuncheva-2003-measures-diversity-classifier-ensembles; @dietterich-2000-ensemble-methods-machine-learning; @brown-2005-diversity-creation-methods-survey; @kuncheva-2014-combining-pattern-classifiers], with the voting-theoretic form long established for correlated jurors [@austen-smith-1996-information-aggregation-condorcet-jury; @csaszar-2013-organizational-decision-making]. That dichotomizing a continuous variable attenuates its correlation is textbook, with the tetrachoric coefficient as its classical parent [@pearson-1900-mathematical-contributions-correlation-characters; @divgi-1979-calculation-tetrachoric-correlation]. That a family of unit vectors in a bounded-dimensional space cannot all be near-orthogonal is a first-order coherence bound from frame theory [@welch-1974-lower-bounds-maximum-cross-correlation]. And the contemporary question of whether diversity helps or hurts an aggregation pipeline is already occupied: diversity can beat ability given an effective aggregation mechanism, which that result does not specify [@hong-2004-groups-diverse-problem-solvers], and the mechanism has since been supplied as selector quality, with a closed-form crossover between the two regimes [@maryanskyy-2026-when-agents-disagree]. **This paper claims the bound, not the phenomenon.** What is offered is a statement about what *any* aggregation mechanism can deliver, not a new account of when diversity pays.

Two contributions follow. The first is an identification. The effective-sample-size statistic already used to audit evaluator panels — the survey-sampling design effect [@kish-1965-survey-sampling; @kalton-2001-leslie-kish-impact], computed on evaluators' binary error indicators — bounds the rank of an acceptance projection from above, and identifies it exactly given two further quantities. That claim is licensed by two results rather than led by them: a bracket theorem placing every admissible aggregation rule between the unanimous and disjunctive extremes, and a closed-form map from the geometry of what evaluators inspect to the correlation of their errors, which is strictly attenuating. **The statistic itself is not this paper's.** A published nine-judge evaluation panel already computes it, and its reported effective sample sizes are the design-effect formula evaluated at its own reported error correlations, to three decimals in every condition it reports [@kohli-2026-nine-judges-two-effective-votes]. It is cited, not claimed. What is new is that a quantity computed to audit a panel bounds a quantity defined to characterize an organization's capacity to detect its own deviations. The second contribution is an executor-invariance ceiling, and it is what the identification buys: because the rank is bounded, the share of a specification's acceptance conditions a receiving executor can independently verify is bounded too, and the residual is what an accountable signatory rather than a document underwrites. **The practical consequence is a ceiling that can be computed rather than asserted** — an organization can now ask how many independent things its panel is capable of checking, and get a number.

**One disambiguation is owed immediately, because the paper's central word is borrowed from a field that means something else by it.** Verification *bandwidth* here is an effective **rank** — a count of independent directions a family of evaluators can check — and not a channel capacity. No mutual-information quantity is estimated, no coding theorem is invoked, and nothing in what follows should be read as a statement about the rate at which information can be conveyed through the verification process [@cover-2006-elements-information-theory]. Whether the effective rank additionally bounds a capacity, rather than merely resembling one, is an open question that belongs in a separate note. A second disambiguation, of the parent's projection notation, is the first substantive thing the model section does, because a reader carrying the other orientation will find every proposition below inverted.

## Related Work

### *The four conceded literatures, and where each stops.*

The ensemble literature establishes that combining predictors buys less as their errors correlate, and it does so with the sharpest available identity: the ensemble's error is the average member error minus the ambiguity, so diversity is the term being purchased [@krogh-1994-neural-network-ensembles-cross-validation]. The subsequent programme catalogues diversity measures and their relationship to accuracy [@kuncheva-2003-measures-diversity-classifier-ensembles; @brown-2005-diversity-creation-methods-survey; @kuncheva-2014-combining-pattern-classifiers], and the same constraint appears in the voting literature as the observation that correlated jurors can underperform individuals [@austen-smith-1996-information-aggregation-condorcet-jury] and in organization theory as the information-aggregation view of the firm's decision structures [@csaszar-2013-organizational-decision-making]. What none of them does is identify the correlation-corrected count with the rank of a projection representing what an organization can detect about itself.

The dichotomization literature establishes that thresholding a continuous variable attenuates correlation, and supplies the closed-form machinery this paper's map is assembled from — the tetrachoric coefficient and its computation [@pearson-1900-mathematical-contributions-correlation-characters; @divgi-1979-calculation-tetrachoric-correlation], and the reduction formula for the derivative of the bivariate normal integral on which the monotonicity proof rests [@plackett-1954-reduction-formula-normal-multivariate]. The only element that is not already there is the *folded* form arising from a two-sided detection rule, which flags on absolute magnitude and therefore cannot see the sign of an inspection direction. The frame-theoretic literature supplies the coherence bound behind the dimensional ceiling [@welch-1974-lower-bounds-maximum-cross-correlation], and the bracket for monotone Boolean functions is elementary [@crama-2011-boolean-functions-theory-algorithms; @genest-zidek-1986-combining-probability-distributions]. Both are conceded as such rather than presented as results.

### *What the sweep did not find.*

A search across the projection, ensemble-diversity, dichotomization, frame-coherence, collective-intelligence and evaluator-panel literatures returned no prior work formalizing organizational verification as a projection family over multiple correlated evaluators. The nearest hits are role-based modelling of multi-agent systems, which is a different sense of verification; cascaded verification layers in agent pipelines, which is engineering rather than measurement; and the evaluator-panel literature itself, which is empirical and does not connect to specification cascades. Each candidate record was confirmed at composition level — author string, year, venue, volume, issue and pages against a publisher's or library's own record — rather than confirmed merely to exist.

The same sweep returns a second negative that is worth stating separately. The effective-sample-size correction is applied to sampled clusters in survey statistics [@kish-1965-survey-sampling], to correlated tests in multiple-comparison work, and to evaluator panels in the machine-evaluation literature [@kohli-2026-nine-judges-two-effective-votes]. Its identification with the rank of a verification projection appears in none of them. This is a negative over a searched space and not a proof of absence, and it is falsified by any prior work identifying an effective-sample-size statistic with the rank of an acceptance or audit projection.

**The positioning against the diversity result is the one that decides the paper's claim.** Diversity can outperform ability *given* an effective aggregation mechanism, and the mechanism is left unspecified [@hong-2004-groups-diverse-problem-solvers]; selector quality has since been supplied as that mechanism, together with a crossover threshold separating the regime where diversity helps from the regime where it hurts [@maryanskyy-2026-when-agents-disagree]. Neither bounds what an aggregation mechanism can deliver. The bracket and its collapse do exactly that, for all mechanisms at once, which is why the claim here is the bound rather than the phenomenon.

## The Model

### *An orientation the parent leaves ambiguous, and which must be fixed first.*

The parent text uses its projection notation in two incompatible orientations. In its formal statement of the projection identity, the projection's range is the *accepted* subspace, the acceptance condition is membership in it, and the deviation is the residual — so a deviation off the range is a failure and therefore something the test catches. In its central proposition, that proposition's proof, and its published simulation, the projection is *what the audit reads*, its range is the compliance axis, and the residual is what is discarded: variation the audit never sees. On that reading a deviation off the range is invisible rather than caught. The residual cannot be both the detected failure and the discarded information.

**This paper adopts the second orientation throughout.** Three things recommend it: it is the reading under which the parent's own proposition, residual arithmetic and simulation are all consistent; it is the reading under which the rank-1 audit critique has its meaning; and it is the only one under which the parent's multi-evaluator remark is true. Under it, the remark that the effective accepted subspace becomes an intersection, with cascade rank under disagreement potentially lower than any single evaluator's, is exactly the unanimity regime of the bracket below. **The parent's own term for that subspace is not reused below**, precisely so that the two senses stay apart: what an evaluator can read is its inspection subspace, and nothing here is called invariant. **Fixing this is a contribution of the companion rather than a criticism of the parent, and it appears here rather than in an appendix because a reader carrying the first orientation finds every proposition below inverted.** The orientation is not relaxable: it is a convention, and the alternative convention inverts the results rather than weakening them.

### *Evaluators, panels, and the rule that combines them.*

Let $O$ be the organizational state space, a real inner product space with $\dim O = n$. An **evaluator** is a pair $e = (P_e, \tau_e)$: an orthogonal projection $P_e$ onto its **inspection subspace** $C_e = \operatorname{range}(P_e)$, and a threshold $\tau_e \ge 0$. Evaluator $e$ **flags** a deviation $\delta \in O$ if and only if $\lVert P_e \delta \rVert > \tau_e$. In the rank-one case $C_e = \operatorname{span}\{v_e\}$ for a unit vector $v_e$, and the rule reads $|\langle v_e, \delta \rangle| > \tau_e$: an audit sees only the component of a deviation lying in what it inspects. Write $D_e = \{\delta : \lVert P_e\delta\rVert > \tau_e\}$ for the **detection region** and $B_e = O \setminus D_e$ for the **evaluator blind spot**, which at $\tau_e = 0$ is exactly $\ker P_e$. Thresholds are indexed by evaluator rather than shared, because instruments in a heterogeneous panel do not have a common detection floor and the abstention behaviour that follows from that is itself a studied object [@zharnikov-2026ay-substrate-floor].

A **panel** is a finite family $\{e_1, \dots, e_k\}$ together with a **rule** $f : \{0,1\}^k \to \{0,1\}$ carrying the vector of member verdicts to a panel verdict. Write $s(\delta)$ for the vector of member indicators and $D_f = \{\delta : f(s(\delta)) = 1\}$. The rule is **non-degenerate** when $f(0,\dots,0) = 0$ and $f(1,\dots,1) = 1$: the panel neither flags what no member flagged nor clears what every member flagged.

**That condition is a scope statement, not a technicality, and it excludes real rules.** A chair's veto, a regulator's override, and any "one reviewer may wave this through" escalation all violate it, and the bracket below genuinely fails for them. The exclusion is named here rather than deferred to a limitations paragraph, because panels with override authority are organizationally common and a reader entitled to apply the result needs to know at the point of statement that they are outside it.

### *Effective rank, and the quantity it is not.*

For rank-one evaluators write $\bar\rho = \binom{k}{2}^{-1}\sum_{e<f} |\langle v_e, v_f \rangle|$ for the mean absolute geometric correlation of the inspection directions, and

$$n_{\text{eff}} = \frac{k}{1 + (k-1)\bar\rho}$$

for the effective rank. This is the estimand: the parent's verification bandwidth, "the maximum number of independent specification conditions the organization can evaluate in a given verification cycle." The functional form is the survey-sampling design effect [@kish-1965-survey-sampling; @kalton-2001-leslie-kish-impact], and the whole of what follows turns on the relationship between this geometric quantity and the same formula evaluated on a panel's observed errors.

**The disambiguation from the introduction is repeated here in the notation, because this is where a reader would otherwise supply the wrong construct.** $n_{\text{eff}}$ counts independent *directions of inspection*. It is not a channel capacity, does not have units of information, and no result below bounds a mutual-information quantity [@cover-2006-elements-information-theory]. A second collision is verbal rather than conceptual and is disposed of in a sentence when it arises: at the methodological venues where this argument belongs, "invariance" ordinarily means *measurement* invariance — whether an instrument functions equivalently across populations [@putnick-2016-measurement-invariance-conventions] — whereas executor-invariance below is a property of an acceptance criterion under a change of the party performing the work. The two are unrelated.

## The Bracket

### *Every admissible rule lies between two.*

**Proposition 1.** For every non-degenerate rule $f$,

$$\bigcap_e D_e \;\subseteq\; D_f \;\subseteq\; \bigcup_e D_e,$$

and hence $\mu(D_{\text{AND}}) \le \mu(D_f) \le \mu(D_{\text{OR}})$ for every deviation distribution $\mu$. Equivalently, on blind spots,

$$B_{\text{OR}} = \bigcap_e B_e \;\subseteq\; B_f \;\subseteq\; \bigcup_e B_e = B_{\text{AND}},$$

and in the limit $\tau_e \to 0$, $B_{\text{OR}} = \bigcap_e \ker P_e = \big(\sum_e C_e\big)^{\perp}$ while $B_{\text{AND}} = \bigcup_e \ker P_e$.

*Proof.* If $\delta \in \bigcap_e D_e$ then $s(\delta) = (1,\dots,1)$ and $f(s) = 1$ by non-degeneracy; if $\delta \notin \bigcup_e D_e$ then $s(\delta) = (0,\dots,0)$ and $f(s) = 0$. Both inclusions follow, and monotonicity of measure gives the probability statement. Complementation gives the blind-spot form. For the limit, $\lVert P_e \delta \rVert > 0$ if and only if $\delta \notin \ker P_e$, and $\bigcap_e C_e^{\perp} = (\sum_e C_e)^{\perp}$. $\square$

**Monotonicity of the rule is not required — only the two boundary values are.** The proposition is elementary and is conceded as such [@crama-2011-boolean-functions-theory-algorithms]; the classical treatment of combining several opinions into one is likewise long-standing [@genest-zidek-1986-combining-probability-distributions]. Its content is not the inequality.

*Falsification*: Proposition 1 is falsified by a cascade whose panel flags a deviation no member flagged, or clears one every member flagged. Such rules exist, they are the override class excluded above, and their existence marks the boundary of the proposition rather than refuting it.

### *The asymmetry of the two ends is the whole content.*

$B_{\text{OR}}$ is a *subspace*, of dimension $n - \dim \sum_e C_e$, and it **shrinks** as evaluators diversify. $B_{\text{AND}}$ is a *union of subspaces*, in general not a subspace at all, and it **grows** as evaluators diversify. The two aggregation rules therefore move in opposite directions with diversity, and each of the two readings in the introduction is correct about its own end. The parent's multi-evaluator remark describes the unanimity end; the bandwidth intuition describes the disjunctive end; the contradiction the parent leaves implicit is a type error rather than a conflict.

Simulation confirms the direction and the magnitude. On a nine-evaluator panel in ten dimensions with a common threshold, as the imposed geometric correlation rises across its range, disjunctive detection **falls** by $.539$ while unanimous detection **rises** by $.301$, and a single evaluator's rate stays flat at about $.370$ throughout — which establishes that the panel effects are not artifacts of individual sensitivity. Every randomly generated aggregation rule falls inside the interval the two extremes define; at zero correlation the rules span $[.005, .864]$ inside a bracket of $[.005, .917]$. Full conditions and the rule-generation procedure are in the appendix.

**One consequence deserves naming because the corpus has a construct for it already.** A blind spot is the set of configurations one evaluator cannot tell apart, which is an organizational-metamerism set relative to that evaluator [@zharnikov-2026-organizational-metamerism-when-distinct-configurations]. The panel case is therefore a metamerism set indexed by an aggregation rule, and the asymmetry above says that the two rules generate metamerism sets of different kinds — one a subspace, one a union of subspaces — from the same evaluators.

## The Bracket Closes

### *The width is the probability that the panel disagrees.*

Write $W = \mu(D_{\text{OR}}) - \mu(D_{\text{AND}})$ for the **bracket width**, let $A_e$ be the indicator that evaluator $e$ flags, and write $p_e = \mu(D_e)$ and $P_{1e} = \Pr[A_1 = A_e = 1]$.

**Proposition 2.** (i) $W$ is the probability that the panel disagrees — that at least one member flags and at least one does not. (ii) Without further assumptions, $W \le \sum_{e \ge 2}(p_1 + p_e - 2P_{1e})$. (iii) If all $p_e = p$ and $\phi_{1e}$ is the phi coefficient between members $1$ and $e$, then $W \le 2(k-1)\,p(1-p)\,(1 - \bar\phi_1)$ with $\bar\phi_1 = (k-1)^{-1}\sum_{e \ge 2}\phi_{1e}$. (iv) At $\bar\phi = 1$ with common marginals, $W = 0$ exactly.

*Proof.* (i) $D_{\text{OR}} \setminus D_{\text{AND}}$ is precisely the disagreement event. (ii) All members agree if and only if $A_e = A_1$ for every $e \ge 2$, so the disagreement event is $\bigcup_{e \ge 2}\{A_e \ne A_1\}$; a union bound gives $W \le \sum_{e\ge2}\Pr[A_e \ne A_1]$, and $\Pr[A_e \ne A_1] = p_1 + p_e - 2P_{1e}$ identically. (iii) Under common marginals $P_{1e} = p^2 + \phi_{1e}p(1-p)$, so $\Pr[A_e \ne A_1] = 2p(1-p)(1 - \phi_{1e})$; summing gives the bound. (iv) A phi coefficient of $1$ between binary variables with equal marginals forces $A_e = A_1$ almost surely, so the two extreme regions coincide. $\square$

**Form (ii) is assumption-free, and that is why it is retained below alongside an exact expression that is not.** It needs no exchangeability, no common marginals and no distributional assumption, which matters because real panels are none of those things.

*Falsification*: Proposition 2 is falsified by a panel whose measured error correlation is high and whose choice of aggregation rule nonetheless changes detection by more than the bracket permits.

### *An exact form under a single-factor panel, and its attribution.*

The union bound is loose, and stopping there would leave a limit statement dressed as a bound. Under the model the estimator already assumes there is an exact expression. Take an **equiangular** panel, $v_e = \sqrt{\rho}\,u + \sqrt{1-\rho}\,w_e$ with $u, w_1, \dots, w_k$ orthonormal, which is feasible whenever $k + 1 \le n$ and makes every pairwise inner product exactly $\rho$ and every $v_e$ exactly a unit vector. For isotropic Gaussian deviations $\delta \sim N(0, \sigma^2 I)$ the inspected components are $X_e = \sqrt{\rho}\,G_0 + \sqrt{1-\rho}\,G_e$ with $G_0, G_1, \dots, G_k$ independent and identically distributed $N(0,\sigma^2)$ exactly, because the defining vectors are orthonormal.

**Proposition 2, part (v).** Conditional on the common factor $G_0 = z$, the $k$ detection indicators are independent with common flag probability

$$p(z) = 1 - \Phi\!\left(\frac{t - \sqrt{\rho}\,z}{\sqrt{1-\rho}}\right) + \Phi\!\left(\frac{-t - \sqrt{\rho}\,z}{\sqrt{1-\rho}}\right), \qquad t = \tau/\sigma,$$

and hence, exactly,

$$\mu(D_{\text{AND}}) = E_Z\big[p(Z)^k\big], \qquad \mu(D_{\text{OR}}) = 1 - E_Z\big[(1 - p(Z))^k\big], \qquad W = 1 - E_Z\big[p(Z)^k + (1 - p(Z))^k\big].$$

*Proof.* Orthonormality of $\{u, w_e\}$ makes the $G$'s independent Gaussians; conditioning on $G_0$ leaves the $X_e$ independent, and functions of independent variables are independent. The three expressions are then the probability that all $k$ Bernoulli$(p(Z))$ draws are one, that none is, and the complement of their sum. $\square$

**This reduction is classical and is attributed rather than claimed.** Collapsing an equicorrelated multivariate normal probability to a one-dimensional integral via a common latent variate is due to Dunnett and Sobel [-@dunnett-1955-approximations-probability-integral], framed on orthant probabilities specifically by Stuart [-@stuart-1958-equally-correlated-variates], extended to general single-factor structures by Curnow and Dunnett [-@curnow-1962-numerical-evaluation-multivariate-normal] and surveyed by Gupta [-@gupta-1963-probability-integrals-multivariate-normal]; the modern computational treatment is standard [@genz-2009-computation-multivariate-normal-t]. The closest precedent for the use made of it here is the psychometric one: Gaussian quadrature over $n$ conditionally independent binary indicators given a shared latent variable [@bock-1970-fitting-response-model-dichotomously] is this panel, forty-six years early, in another field. **The only claim entered here is that the bracket width happens to be exactly computable because the model is single-factor.**

**Table 1: Exact Bracket Width Against Its Union Bound, $k = 9$, $t = .30$.**

| $\rho$ | $\phi_{\text{err}}$ | $W$ exact | Union bound | Bound / exact | Bound informative |
|---|---|---|---|---|---|
| .000 | .000 | .911 | 2.883 | 3.16 | no |
| .500 | .044 | .850 | 2.756 | 3.24 | no |
| .700 | .112 | .763 | 2.561 | 3.36 | no |
| .900 | .323 | .569 | 1.952 | 3.43 | no |
| .950 | .480 | .462 | 1.500 | 3.25 | no |
| .990 | .761 | .226 | .689 | 3.04 | **yes** |
| .999 | .924 | .072 | .218 | 3.04 | **yes** |

*Notes*: $\phi_{\text{err}}$ is the induced correlation of the binary error indicators, not the geometric correlation $\rho$. The exact column is dense fixed-grid quadrature of the expression above, agreeing with direct Monte Carlo on the equiangular panel to within $.0021$ at 400,000 deviations per cell; a generic shared-factor construction with unequal pairwise angles tracks it to within $.031$. The union bound exceeds $1$, and so says nothing at all, until the error correlation approaches $.88$. **The looseness factor is between 3.04 and 3.43 across the entire range**, which is worth stating because it makes the union bound a stable rescaling of the truth rather than a bound that degrades where it is needed.

### *What the collapse answers.*

Every admissible rule lies inside the bracket, and the bracket closes as errors correlate, independently of which rule is chosen. **Above a correlation level, therefore, no aggregation mechanism can be *effective* however well designed — not because aggregation is poorly engineered, but because every rule satisfying non-degeneracy is trapped in a bracket that has already closed.** *Effective* is used here in the sense the diversity literature gives it, and the distinction matters: the claim is not that a highly correlated panel detects little, since at perfect correlation every rule detects at the common member rate, which may be high. The claim is that **no rule recovers detection the evaluator set does not collectively possess** — that the choice of aggregation mechanism stops being a lever, not that the panel stops working.

That is the answer, in the negative and for all mechanisms at once, to the question the classical diversity result leaves open [@hong-2004-groups-diverse-problem-solvers]. Where the contemporary treatment locates a crossover *within* a mechanism by improving the selector [@maryanskyy-2026-when-agents-disagree], the statement here bounds what any selector can reach. It also rules out a natural objection: that a better-designed aggregation rule would recover the detection a correlated panel appears to lose. It would not, and the empirical counterpart is already on the record — established aggregation methods close at most 11% of the gap to the best single judge even given oracle access to gold labels [@kohli-2026-nine-judges-two-effective-votes].

**A caution the tables do not carry.** Bracket width *grows* with panel size at fixed correlation and *collapses* with correlation at fixed panel size. Both directions are what the asymmetry of the two ends predicts, and neither is the paper's claim on its own; the claim is about the second at realistic values of the first.

## From Geometry to Error

### *The reduction that makes the map tractable.*

The bracket is stated in the geometry of what evaluators inspect. Every quantity an analyst can actually measure on a panel is stated in the correlation of what evaluators get wrong. The link between them is not an analogy.

Evaluator $e$ inspects the unit direction $v_e$ and flags $\delta$ when $|\langle v_e, \delta\rangle| > \tau_e$. A deviation is present by construction, so a non-flag *is* an error, and the binary error indicator is $E_e = \mathbb 1[|\langle v_e, \delta\rangle| \le \tau_e]$ — exactly the vector on which an evaluator-panel study computes its correlations against gold labels. Take $\delta \sim N(0, \sigma^2 I_n)$. Then $(\langle v_e, \delta\rangle, \langle v_f, \delta\rangle)$ is bivariate normal with correlation **exactly** $\rho = \langle v_e, v_f \rangle$. The geometric correlation *is* the correlation of the inspected components, and the question collapses to a classical one: what does a symmetric two-sided dichotomization at $\pm\tau$ do to a bivariate normal correlation?

**Proposition 3.** Write $t_e = \tau_e/\sigma$ and $q_e = 2\Phi(t_e) - 1$ for the marginal error rate. Then the induced correlation of the error indicators is the **folded dichotomization**

$$\phi(\rho) = \frac{P_{11}(\rho) - q_e q_f}{\sqrt{q_e(1-q_e)\,q_f(1-q_f)}}, \qquad P_{11}(\rho) = 2\Phi_2(t_e, t_f; \rho) + 2\Phi_2(t_e, t_f; -\rho) - 2\Phi(t_e) - 2\Phi(t_f) + 1,$$

which is even in $\rho$, strictly increasing on $(0,1)$, fixes both endpoints, and satisfies $\phi(\rho) < \rho$ strictly.

*Proof.* $P_{11}$ follows by inclusion–exclusion on the bivariate normal integral with the reflection identities. For the sign, Plackett's identity $\partial_\rho \Phi_2(h,k;\rho) = \varphi_2(h,k;\rho)$ [@plackett-1954-reduction-formula-normal-multivariate] gives $\partial_\rho P_{11} = 2\varphi_2(t_e,t_f;\rho) - 2\varphi_2(t_e,t_f;-\rho)$, and $\varphi_2(h,k;\rho) > \varphi_2(h,k;-\rho)$ if and only if $\rho hk > 0$, which is strictly positive for $t_e, t_f > 0$. At equal thresholds this reduces to $\big(e^{-t^2/(1+\rho)} - e^{-t^2/(1-\rho)}\big)\big/\big(\pi\sqrt{1-\rho^2}\big)$. Evenness is immediate from the form of $P_{11}$. $\square$

**Evenness is not an incidental property.** A rule that flags on absolute magnitude cannot see the sign of an inspection direction, so the induced correlation depends on $|\rho|$ — which is why the mean *absolute* inner product is the right definition of $\bar\rho$ rather than a convenience.

*Falsification*: Proposition 3 is falsified by a threshold pair and correlation at which the map is non-monotone or exceeds the identity.

### *The map's properties, checked rather than asserted.*

The derivative is strictly positive on a dense grid, with a minimum of $+3.7 \times 10^{-8}$ over a $40 \times 60$ grid at equal thresholds and $+2.8\times10^{-63}$ under heterogeneous thresholds, and the analytic and numerical derivatives agree to $1.3 \times 10^{-10}$. **Heterogeneous thresholds are the robustness check that matters most here**, because a panel of non-identical instruments does not share a detection floor, and the monotonicity proof and its numerical confirmation both hold when the thresholds differ. The map vanishes at the origin to first order and is therefore quadratic there, with analytic and numerical coefficients agreeing to $2.8 \times 10^{-4}$ relative. Attenuation holds throughout: the maximum of $\phi - \rho$ is $-.0099$ at equal thresholds and $-.0484$ under heterogeneous ones over dense grids. The quadrature underlying the map agrees with its closed form to $2.1\times10^{-14}$ and with a 2,000,000-draw Monte Carlo to $4.7\times10^{-4}$.

**The map reproduces a panel, which is a stronger statement than any pairwise property.** Simulating a full nine-evaluator panel under the map's own model, measuring the error correlation on binary miss indicators exactly as an evaluator-panel study would, and comparing against the map applied pairwise and averaged gives a maximum residual of $.0008$ across the full correlation range and two state-space dimensions.

**Table 2: Panel Recovery Under Gaussian Deviations, $k = 9$, 400,000 Deviations per Row.**

| $n$ | $\rho$ | $\bar\phi_{\text{geom}}$ | $\phi_{\text{err}}$ measured | Map of mean | Mean of map | Residual |
|---|---|---|---|---|---|---|
| 10 | .00 | .271 | .0610 | .0391 | .0618 | $-.0008$ |
| 10 | .20 | .314 | .0834 | .0530 | .0828 | $+.0006$ |
| 10 | .50 | .610 | .2476 | .2227 | .2471 | $+.0006$ |
| 10 | .90 | .902 | .6050 | .6003 | .6049 | $+.0001$ |
| 40 | .00 | .119 | .0107 | .0073 | .0111 | $-.0005$ |
| 40 | .20 | .227 | .0355 | .0271 | .0359 | $-.0004$ |
| 40 | .50 | .539 | .1750 | .1680 | .1750 | $-.0000$ |
| 40 | .90 | .904 | .6058 | .6039 | .6058 | $+.0001$ |

*Notes*: "Map of mean" applies the map to the mean geometric correlation; "mean of map" applies it to each pairwise absolute inner product and then averages. Residual is measured minus mean of map. **The ordering of those two columns is a procedural rule, not a presentational choice.** The map is convex at low correlation, so Jensen's inequality bites and applying it to the mean understates the mean induced correlation — by up to $.0298$ in this table, which at $\rho = 0$ and $n = 10$ is a 37% understatement. **Map pairwise, then average; never the reverse.**

An independent cross-check is worth more than either property list. The induced error correlation can be computed from the bivariate normal integral with reflection identities, or by conditioning on the common factor as in the exact bracket expression. Two derivations, two implementations, neither resting on the other, agree to $2.5 \times 10^{-14}$ across a grid of thresholds and correlations.

### *Shared item difficulty is a second channel, and it is real.*

The most serious rival explanation for the low effective independence observed in evaluator panels is that some items are simply hard for everyone — shared *difficulty* rather than shared inspection geometry. **The rival names a real channel and is not dismissed.** If deviations carry a random common magnitude $R$, so that items differ in difficulty, then conditioning on $R$ leaves the model intact with a common random threshold $T = \tau/R$, and the law of total covariance splits the induced correlation exactly:

$$\phi = \underbrace{\frac{E_T\big[\operatorname{Cov}(E_e, E_f \mid T)\big]}{q(1-q)}}_{\text{geometric}} \;+\; \underbrace{\frac{\operatorname{Var}_T\big(q(T)\big)}{q(1-q)}}_{\text{difficulty}}.$$

So $\phi(\rho = 0) = \operatorname{Var}_T(q(T))/(q(1-q)) > 0$: **geometrically orthogonal evaluators still show correlated errors, purely because items share difficulty.** This is verified to machine precision against direct computation at four difficulty spreads, giving $\phi(0) = $ .000, .0073, .0444 and .1512 at lognormal spreads of .00, .10, .25 and .50. Pinning the deviation magnitude instead switches the channel off and over-corrects through the sphere constraint, placing the measured error correlation up to $.056$ *below* the map at low correlation and decaying with dimension. **The difficulty term must therefore be netted out before the map is inverted, or the recovered geometric correlation is biased upward** — which makes the resulting bandwidth estimate too pessimistic rather than too optimistic, the safe direction, but still wrong. The rival is handled by decomposition rather than by denial, and the decomposition is exact.

**One figure in circulation must not be reused as this correction.** A published panel reports a shared-item-difficulty component of 6.8%, but as recorded that is a share of the *Condorcet gap* rather than a decomposition of the error correlation [@kohli-2026-nine-judges-two-effective-votes]. Establishing what it decomposes is prior to reusing it, and it is not reused here.

## What the Statistic Already Is

### *A published panel's effective sample sizes are the design-effect formula.*

A nine-judge evaluation panel drawn from seven model families and run on 1,000 items reports effective sample sizes of 2.18, 2.35, 2.48 and 1.99 across four benchmarks; mean pairwise error correlations of .391, .354 and .328; an independence ratio of 24.2%; Condorcet gaps of 22.0, 14.0 and 7.6 percentage points; that established aggregation closes at most 11% of that gap even with oracle labels; that using one judge per model family *reduces* the effective sample size to 1.93; and that chain-of-thought prompting *raises* error correlation to .456 [@kohli-2026-nine-judges-two-effective-votes]. Its gold labels come from the benchmarks it runs on. It is a preprint and has not been peer reviewed, and is cited as such; every use made of it here is either a re-derivation from its own reported figures, which is internally checkable, or an illustration explicitly labelled as directional.

**Those reported effective sample sizes are the design-effect formula evaluated at that study's own reported error correlations.**

**Table 3: Reported Effective Sample Sizes Against the Design-Effect Formula at the Reported Error Correlation.**

| Condition | $k$ | Reported $\bar\phi$ | Formula | Reported $n_{\text{eff}}$ | Difference |
|---|---|---|---|---|---|
| MNLI | 9 | .391 | 2.180 | 2.18 | $+.000$ |
| SNLI | 9 | .354 | 2.349 | 2.35 | $-.001$ |
| AlphaNLI | 9 | .328 | 2.483 | 2.48 | $+.003$ |
| MNLI (chain-of-thought) | 9 | .456 | 1.936 | 1.94 | $-.004$ |

*Notes*: The formula column is $k/(1 + (k-1)\bar\phi)$ evaluated at the reported correlation, to three decimals, with no fitting and no free parameter. The reported independence ratio of 24.2% is $2.18/9 = .242$, which is the effective sample size over the panel size exactly. This is arithmetic on published summary statistics rather than inference, and it is falsified only by a reading of that study establishing that its figures come from a different estimator that happens to agree to three decimals four times over.

**The general point outlived the check that produced it: a number reproducible from a source's own reported figures is a claim that source is making, whether or not it names the formula.**

### *The same expression is already familiar, read in two other directions.*

**A reader who works with rater panels has met $k/(1 + (k-1)\bar\rho)$ before, and the resemblance is an exact identity rather than an analogy.** Write $\mathrm{ICC}(1)$ for the reliability of a single rater and $\mathrm{ICC}(k)$ for that of their average. The prophecy formula, stated independently and in consecutive articles of one 1910 issue [@spearman-1910-correlation-calculated-faulty-data; @brown-1910-experimental-results-correlation-mental-abilities] and since absorbed into the intraclass-correlation family [@shrout-1979-intraclass-correlations-assessing-rater; @mcgraw-1996-forming-inferences-intraclass-correlation], gives $\mathrm{ICC}(k) = k\bar\rho/(1 + (k-1)\bar\rho)$. Dividing,

$$\frac{\mathrm{ICC}(k)}{\mathrm{ICC}(1)} = \frac{k}{1 + (k-1)\bar\rho} = n_{\text{eff}}.$$

**The effective sample size is the step-up ratio: the factor by which averaging $k$ raters multiplies reliability.** Psychometrics reads the expression as what a composite gains, survey sampling reads the same expression as what clustering costs [@kish-1965-survey-sampling], and this paper reads it a third way, as a count of independent directions. The three are one formula with three referents.

**Conceding the identity is what makes this paper's difference visible, and the difference is the criterion.** The reliability tradition computes its coefficient on raters' *ratings*, and the standing applied guidance is largely built for the case where no criterion exists [@lebreton-2008-answers-twenty-questions-interrater]. The quantity here is computed on *errors against gold labels*, and the two are not monotone transformations of each other, because two raters can agree while both being wrong. That is the same separation of shared signal from shared error argued above, aimed at the tradition that will otherwise supply the wrong reading — and it is why the gold-label condition is a scope condition rather than an inconvenience.

**One further concession is owed before it is demanded.** The mean absolute inner product is not itself an intraclass correlation, and the design-effect form is a *one-parameter summary* of the frame operator's spectrum: two panels with the same mean correlation and different eigenvalue structure receive the same value and need not have the same rank. Table A1 shows the gap, reporting an eigenvalue-based effective rank of 3.76 against a design-effect value of 3.14 on the same uncorrelated panel, converging as correlation rises. The eigenvalue quantity is the estimand; the design-effect form is what a panel with gold labels can actually compute, and the discrepancy between them is a second reason — beyond attenuation — that the computed figure should be read as a bound rather than as a measurement.

### *What is borrowed, and what is not.*

**The estimator is not this paper's and is not claimed.** Computing a design effect on evaluators' binary *error* indicators rather than on their raw judgements — which is what separates shared signal, since items really do differ, from shared error, which is the dependence that costs a panel its independence — is already published practice, for the same stated reason. What remains is a smaller claim about the estimator and a larger claim about what it means.

What is new is the identification: that this quantity estimates a *projection rank*; the closed-form map that establishes the link; the upper-bound theorem that follows from the map's attenuation; and the two organizational ceilings that follow from the bound. A quantity computed to audit a panel turns out to bound a quantity defined to characterize an organization's capacity to detect its own deviations. Since the corpus stated the premise before this paper existed — that generation is becoming cheap while verification stays expensive, so verification is the binding constraint [@zharnikov-2026ao-spec-based-research-post-ai] — a measurable ceiling on verification capacity is the quantity that premise was missing.

## The Identification

### *The bound, which needs no inversion.*

**Proposition 4.** The effective-sample-size statistic computed on evaluators' error vectors is an upper bound on the rank of the acceptance projection:

$$n_{\text{eff}}^{\text{rank}} = \frac{k}{1 + (k-1)\bar\rho} \;\le\; \frac{k}{1 + (k-1)\bar\phi} = n_{\text{eff}}^{\text{vote}},$$

and is exactly invertible to it given the panel's marginal error rate and a shared-difficulty correction.

*Proof.* The design effect is decreasing in its argument, and by Proposition 3 the map lies strictly below the identity, so $\bar\phi < \bar\rho$ and the ordering follows. $\square$

**This is the result that survives the most.** It requires only that the map be increasing and lie below the identity. It does not require inverting the map, knowing the marginal error rate, or trusting the Gaussian model for a point estimate — and the Gaussian assumption is precisely the one most likely to fail in practice, since organizations plausibly fail in preferred directions rather than isotropically. The direction of the inequality is also the safe one. A published finding that nine judges supply an effective sample size near two does not need correcting before it can be quoted; correcting it makes the finding **more** pessimistic, not less. Every pessimistic claim this paper makes about correlated evaluator panels is therefore conservative as stated.

*Falsification*: Proposition 4 is falsified by a panel whose geometric effective rank, measured directly from its inspection directions, exceeds the value computed from its error vectors.

### *Inversion, and the condition that decides whether it is available at all.*

The point inversion requires two things the bound does not. It requires the panel's marginal error rate, without which the map cannot be inverted; and it requires the shared-difficulty term to be netted out first, without which the recovered geometric correlation is biased upward.

**It also requires gold labels, and that condition decides where the quantity can be estimated at all.** The correlation is computed on error vectors, so it needs to be known what the right answer was. Correlating raw codes instead measures dependence but conflates shared signal with shared error — the exact confound the construct exists to break. Where the only adjudicated sample is conditioned on disagreement, or adjudicated by the same hand that authored the instrument, the estimate is not available, and the honest report says so rather than substituting a naive agreement rate.

**The labels must also be good, not merely present, and this is the assumption on which the bound's direction rests.** What counts as ground truth in machine-evaluated settings is itself contested, and treating a convenient label as truth is a documented failure mode [@lebovitz-levina-lifshitz-2021-ai-ground-truth]; the rater-error tradition exists precisely because labels sometimes have to be estimated rather than known [@dawid-1979-maximum-likelihood-observer-error]. Label error therefore has to be classified by its relation to the panel's. Label error *independent* of the panel's error attenuates the measured correlation toward zero, which inflates the computed effective sample size and so leaves every claim here conservative. Label error *correlated with the panel's* — a gold standard that fails in the same directions the panel fails in, which is the realistic hazard when labels and evaluators share a lineage — attenuates it too, and that is the single direction in which the upper bound can fail. **The condition Proposition 4 needs is not an errorless gold standard but one that does not fail where the panel fails**, and a study using the estimator owes an argument for it rather than an assurance. Since this section proposes a new reading of a measure, it should be held to the standard for questionable measurement practice from the outset rather than after the fact [@flake-2020-measurement-schmeasurement-questionable]; the rater-error tradition offers the corresponding latent-class treatment when labels must themselves be estimated [@dawid-1979-maximum-likelihood-observer-error].

**Table 4: Bracket Width Surviving at a Published Panel's Error Correlations, $k = 9$, as a Percentage of the Zero-Correlation Width.**

| Condition | $\phi$ | $q = .10$ | $q = .25$ | $q = .50$ |
|---|---|---|---|---|
| MNLI | .391 | 42.5% | 58.8% | 76.1% |
| SNLI | .354 | 45.2% | 61.6% | 79.4% |
| AlphaNLI | .328 | 47.2% | 63.6% | 81.6% |
| MNLI (chain-of-thought) | .456 | 38.4% | 53.9% | 69.6% |

*Notes*: **This table is model-dependent and directional, and is not a measurement.** The inversion needs the panel's marginal error rate $q$, which the published record does not carry, so $q$ is bracketed rather than fixed, and no difficulty correction is applied. Read as stated, between roughly a quarter and three fifths of the zero-correlation bracket width has already been lost at these correlations — not "most of it" and not none. The union bound of Proposition 2 says nothing whatever in this range, since it exceeds $1$ until the error correlation approaches $.88$; the exact form is what makes the range reportable.

**Nothing here is a prediction of an observed effective sample size.** The design-effect value at a reported error correlation is that formula evaluated at that correlation, which is a calibration check on the model's arithmetic rather than a theoretical derivation of the number. A simulated panel reproducing a value near 2.2 at a matched correlation shows that the simulation is set up correctly and shows nothing more.

## The Dimensional Ceiling

### *The exact ceiling, from a coherence bound.*

**Proposition 5.** For rank-one evaluators with unit inspection directions $v_1, \dots, v_k$ in a state space of dimension $n$, $n_{\text{eff}} \le \min(k, n)$.

*Proof.* $n_{\text{eff}} \le k$ is immediate from $\bar\rho \ge 0$. For the other bound let $G = \sum_e v_e v_e^{\top}$, positive semidefinite with $\operatorname{tr} G = k$ and $\operatorname{rank} G \le n$. Cauchy–Schwarz on its eigenvalues gives $\operatorname{tr}(G^2) \ge (\operatorname{tr} G)^2/\operatorname{rank}(G) \ge k^2/n$, while $\operatorname{tr}(G^2) = k + \sum_{e \ne f}\langle v_e, v_f\rangle^2$. Hence $\sum_{e \ne f}\langle v_e, v_f \rangle^2 \ge k(k-n)/n$, so the mean over ordered off-diagonal pairs obeys $\overline{\rho^2} \ge (k-n)/(n(k-1))$; since $|\rho| \ge \rho^2$ on the unit interval, $\bar\rho \ge (k-n)/(n(k-1))$ and therefore $n_{\text{eff}} \le k/(1 + (k-n)/n) = n$. For $k < n$ this intermediate bound is vacuous and $n_{\text{eff}} \le k$ covers the case. $\square$

This is the first-order coherence bound from frame theory, and it is conceded as such [@welch-1974-lower-bounds-maximum-cross-correlation]. It is also not tight — equality would require every pairwise correlation to be exactly zero or one — which is why the operative statement is the next one.

### *The typical ceiling, which is the one that binds.*

**Proposition 6.** If inspection directions are drawn independently and uniformly on the unit sphere, then as $k \to \infty$,

$$n_{\text{eff}} \;\longrightarrow\; \frac{1}{E\lvert\langle u, v\rangle\rvert} = \frac{\sqrt{\pi}\,\Gamma\!\big(\tfrac{n+1}{2}\big)}{\Gamma\!\big(\tfrac{n}{2}\big)} \;\sim\; \sqrt{\tfrac{\pi n}{2}} \approx 1.25\sqrt{n}.$$

*Proof.* $\bar\rho \to E|\langle u, v\rangle|$ almost surely as $k \to \infty$, so $n_{\text{eff}} \to 1/E|\langle u,v\rangle|$. Writing the density of one coordinate of a uniform point on the sphere as $c_n(1-x^2)^{(n-3)/2}$ and integrating gives $E|\langle u,v\rangle| = \Gamma(n/2)\big/\big(\sqrt{\pi}\,\Gamma(\tfrac{n+1}{2})\big)$, with the stated asymptotic. $\square$

*Falsification*: Propositions 5 and 6 are falsified by a panel whose independently measured effective rank exceeds the dimensionality of its state space, or by a large randomly constituted panel whose measured effective rank materially exceeds $\sqrt{\pi n/2}$.

**Table 5: Both Ceilings. Worst Case Over 30 Configurations per Row, and the Typical Case Under Uniform Directions.**

| $n$ | $k$ | $n_{\text{eff}}$ max | $\min(k,n)$ | | $n$ | Exact limit | $\sqrt{\pi n/2}$ | $n_{\text{eff}}$ at $k = 200$ |
|---|---|---|---|---|---|---|---|---|
| 10 | 5 | 4.58 | 5 | | 4 | 2.356 | 2.507 | 2.352 |
| 10 | 9 | 5.01 | 9 | | 10 | 3.866 | 3.963 | 3.803 |
| 10 | 40 | 8.06 | 10 | | 25 | 6.204 | 6.267 | 6.034 |
| 10 | 200 | 8.19 | 10 | | 48 | **8.638** | 8.683 | **8.236** |
| 4 | 50 | 3.69 | 4 | | 100 | 12.502 | 12.533 | 11.761 |
| 25 | 200 | 15.64 | 25 | | | | | |

*Notes*: The left block searches random, near-orthogonal and clustered configurations for the largest effective rank achievable and confirms the exact bound is never violated and never approached. The right block is the typical case. Read the $n = 48$ row: on the 48-dimensional specification space of a six-level cascade over eight dimensions, a randomly constituted panel saturates below **nine** effective acceptance predicates at a panel size of 200.

### *Diversity must be engineered, not sampled.*

The two bounds say that hiring more reviewers buys nominal capacity and, past a modest size, no effective capacity. **What a panel needs is engineered evaluator diversity — inspection directions deliberately spread — rather than the diversity that arrives by sampling when the panel is enlarged.** The corpus already bounds what can be *specified* by a high-dimensional geometric argument [@zharnikov-2026-specification-impossibility-organizational-design-high]; the pair of results here bounds what can be *verified* by one, and the two bounds are independent.

**The two bounds compound with the attenuation result, in the unhelpful direction.** Near orthogonality, induced error correlation is second-order small in geometric correlation, so a panel's measured effective sample size looks considerably healthier than its geometry warrants. The geometry caps bandwidth and the measurement flatters it. How much better an engineered panel can do, up to the hard ceiling, is the design question this paper raises and does not answer.

## What Does Not Transfer

### *The transferable share of a specification.*

A design theory of specification cascades requires that acceptance be a function of the contract set alone, so that an executor swap changes how contracts are met and never which contracts must be met, and makes a responsibility centre forkable by sharing that test suite [@zharnikov-2026-organizational-schema-theory-test-driven]. The classical statement of what travels with a specification is the visible-information and hidden-information split of modular design [@baldwin-2000-design-rules-power], and the corpus's own taxonomy of what transfers across an organizational boundary sets out the tiers at which such claims are made [@zharnikov-2026-dual-hierarchies-organizational-transferability-six]. The result below bounds all of them.

**Proposition 7** (a dimension count, not a deeper theorem; its work is interpretive)**.** Let a contract specify $r$ independent acceptance conditions, and let the receiving executor verify with a panel of effective rank $n_{\text{eff}}$. The share of the contract that executor can independently verify is at most

$$\sigma \;\le\; \frac{\min(n_{\text{eff}}, r)}{r},$$

with $n_{\text{eff}}$ bounded by Propositions 5 and 6, and bounded in turn by Proposition 4 whenever it is estimated from error vectors. The residual $1 - \sigma$ is the share of the *stated* contract whose satisfaction the receiving panel cannot establish.

*Proof.* The panel's detection capability spans at most $n_{\text{eff}}$ independent directions, and $r$ conditions cannot be independently checked by a family spanning fewer than $r$ independent directions, so at most $\min(n_{\text{eff}}, r)$ are checkable. $\square$

**This is a dimension count, and is presented as one.** It has no mathematical content beyond the ceiling above; its work is interpretive, and it earns its place by converting an asserted design property into a measurable one.

**Table 6: Transferable Share of a Specification Under a Correlated Receiving Panel.**

| $r$ | $k$ | $\bar\phi$ | $n_{\text{eff}}$ | Transferable | Signatory residual |
|---|---|---|---|---|---|
| 6 | 3 | .35 | 1.76 | 29.4% | 70.6% |
| 6 | 9 | .39 | 2.18 | 36.4% | 63.6% |
| 16 | 9 | .39 | 2.18 | 13.7% | 86.3% |
| 16 | 40 | .39 | 2.47 | 15.4% | 84.6% |
| 48 | 200 | .25 | 3.94 | 8.2% | 91.8% |

*Notes*: Rows are illustrative combinations of contract size and panel configuration, not measurements. The effective-rank column is the design effect at the stated correlation, which by Proposition 4 is an upper bound, so each transferable share is an upper bound and each residual a lower bound. **The rows are also computed under rank-one inspection**, which is the assumption least true of organizational reviewers, since a real reviewer checks several things at once. Higher-rank inspection raises the effective rank and therefore the transferable share, so the residual column should be read as a lower bound in that direction too — the table's use is to show how fast the share falls as specified conditions outrun verification capacity, not to price a particular contract.

**The organizational payload is a distinction between two things a specification is usually assumed to carry together.** Executor-invariance of the acceptance criteria *as stated* does not confer executor-invariance of their *verification*. A specification transfers its contract; it does not transfer the capacity to check it. Forkability therefore has a measurable ceiling — what forks is the test suite, what does not fork is the bandwidth needed to enforce it — and the gap is exactly the accountable-signatory residual. That residual is not a governance preference but a structural requirement, which is the management-theory form of the automation–augmentation paradox: augmentation is where the work cannot be handed over rather than where handing it over is culturally resisted [@raisch-2021-artificial-intelligence-management]. It is also what makes the audit-society diagnosis more than a critique of ritual [@power-1997-audit-society-rituals; @power-2021-modelling-microfoundations-audit]: a signature is what remains once verification is treated as a capacity with a ceiling, and machine-readable claims that a receiving party can check are the operational form of the share that does transfer [@zharnikov-2026t-paper-as-specification].

### *This is not tacitness, and the difference is testable.*

The standard explanation for the limit on what transfers with a written specification is tacitness: some knowledge cannot be written down, so it stays with the people [@polanyi-1966-the-tacit-dimension]. **The mechanism derived here is not tacitness, and the rival is not refuted but given a competitor that makes a different prediction.** Tacit domains have many dimensions along which performance can deviate and no correspondingly engineered spread of inspection directions, so the transferable share is small by the dimensional ceiling *even when everything relevant is written down*. The two accounts diverge on an intervention: engineering the receiving panel's inspection directions should raise the transferable share without making anything less tacit. This sharpens rather than contradicts the boundary condition the design theory already records, that its executor-invariant boundary weakens in high-tacit domains [@zharnikov-2026-organizational-schema-theory-test-driven].

### *This is not measurement invariance either.*

At the methodological venues where this argument belongs, "invariance" ordinarily denotes measurement invariance — whether an instrument functions equivalently across groups, tested by a well-established sequence of nested model comparisons [@putnick-2016-measurement-invariance-conventions]. Executor-invariance is a property of an acceptance criterion under a change of the party performing the work, not of a measurement model under a change of population. **The collision is verbal, it is disposed of in this sentence, and no result above depends on the psychometric construct.**

## Demonstration and Its Limits

### *What the published panel demonstrates, and what it does not.*

The evaluator-panel study is used as an existence demonstration, not as a test. It establishes that a panel with nominal size nine can carry an effective size near two, that the effective size is the design effect at the observed error correlation, and that established aggregation recovers very little of the resulting gap. It does not establish that the same holds for organizational acceptance panels, and it does not confirm the geometric account, since the arithmetic runs entirely on error indicators and never observes an inspection direction.

**Its regime is the scope condition on every empirical claim here.** The evidence is machine evaluators on classification and pairwise preference. Machine annotators matching or exceeding crowd workers is what makes such panels worth studying at all [@gilardi-2023-chatgpt-outperforms-crowd], the scope of that substitution is already carefully drawn [@ziems-2024-can-large-language-models], and the validity of treating a language model as a measurement instrument has its own literature [@li-2024-frontiers-determining-validity]; instrument self-inconsistency across repeated runs [@haldar-2025-rating-roulette-selfinconsistency] and the question of whether machine annotators are statistically distinguishable from human ones [@he-2025-can-we-hide-machines-crowd] both bear directly on what a panel's error vector contains. Human annotator panels are reported to reach roughly double the effective independence of model panels, which is a difference in degree that the theory accommodates and the evidence does not establish. Organizational acceptance tests are neither classification nor pairwise preference, so the transfer of the empirical claim to them is argued rather than demonstrated.

### *A corpus instrument that cannot supply the estimate, and why saying so matters.*

The corpus contains a blinded multi-model content-coding instrument with 406 coded cells over 30 cases, three heterogeneous pinned models, a Fleiss $\kappa$ of $.838$ [@fleiss-1971-measuring-nominal-scale], a 2.7% flag rate, and adjudicated values for its 11 flagged cells only [@zharnikov-2026bh-multi-llm-coding-instrument]. It is the obvious demonstration corpus and it cannot serve as one.

**The reason is the gold-label condition, and the paper's own claim is what forbids the shortcut.** The adjudicated sample is conditioned on disagreement and was adjudicated by the same hand that authored the instrument, so it does not supply gold labels in the sense the estimator requires. The naive portability figure — one minus the flag rate, or 97.3% — therefore overstates transferable verification by exactly the correlated-error term this paper is about. Quoting it would be the error the paper exists to identify. **Reporting a quantity as unavailable is the correct output here, not a gap in the design.**

The clean route is a contrast study whose human double-coding arm supplies gold labels over the full item set, from coders who have never seen the adjudication record; without that condition the estimate is circular. Two quantities are pre-specified for it by the results above: the panel's marginal error rate, without which the map cannot be inverted, and a shared-difficulty correction, without which the recovered correlation is biased upward.

## Scope and Limitations

### *What the model does not contain.*

**There is no false-alarm arm.** A deviation is present by construction, so an error means a miss. A real acceptance cascade has both error types and they need not share a correlation structure. This is stated as a scope condition rather than discovered in review, and the extension is named rather than attempted.

**Each evaluator inspects a one-dimensional subspace.** The bracket and the collapse do not depend on this, but the dimensional ceiling's exact constant does, and the map from geometric to error correlation is derived for it. The bound should generalize with the trace of the frame operator replaced by the summed ranks, but the corresponding definition of mean correlation has not been worked out, so higher-rank inspection subspaces are flagged as an extension and not claimed.

**Anisotropic deviation distributions are untested, and this is the most likely place for the clean result to degrade.** Organizations plausibly fail in preferred directions rather than isotropically. The attenuation result and therefore the bound survive on far weaker terms than the Gaussian model — they need only that the map be increasing and lie below the identity — but the point inversion from a measured error correlation back to a geometric one becomes model-dependent, and it is the inversion that is at risk.

**The executor-invariance ceiling has no mathematical content beyond the dimensional ceiling.** Its work is interpretive and it is presented as a dimension count, so that the reader is not invited to read it as a deeper theorem.

### *What the evidence does not reach.*

**The empirical spine is a re-analysis of one preprint's published summary statistics plus simulation.** No new evaluator panel was run, and the corpus instrument available for demonstration has adjudicated values only for cells conditioned on disagreement. The scope is stated here and in the introduction rather than defended late: this paper supplies an identification and its properties, with a published panel as an existence demonstration and a contrast study as the route to more.

**The evidence base is machine evaluators on classification and pairwise preference**, and the transfer to human acceptance panels in organizations is argued rather than demonstrated. The theory is stated for any threshold evaluator and does not depend on the regime; the empirical claim is scoped to the regime the evidence covers.

**Evaluation of this work is single-author.** That is recorded as an accepted cost rather than an oversight. Every computational claim above is reproducible from seeded scripts, which is the substitute available.

## What the Identification Changes

### *For reading a panel.*

An organization that has assembled an evaluator panel and wants to know what it bought has, on the account given here, three separate questions rather than one. The first is how many independent directions the panel spans, which is what the effective-sample-size statistic bounds, and which is not answered by counting the evaluators. The second is whether the aggregation rule is a lever at all, which is answered by where the panel sits in the correlation range: where the bracket has closed, redesigning the rule is effort spent on a quantity that no longer varies. The third is whether the panel can be improved by enlargement, and the dimensional ceiling answers no beyond a modest size — a randomly constituted panel on a 48-dimensional space saturates below nine effective predicates however many evaluators are hired, so the available lever is the spread of inspection directions and not the headcount.

**None of these questions could be asked of the statistic before, because the statistic was a diagnostic of a panel rather than a measurement of a capacity.** That is the whole of what the identification changes: the same number, computed the same way, now answers a question about the organization instead of a question about the raters.

### *For reading a signature.*

The executor-invariance ceiling says that a specification transfers its contract and not the capacity to check it, and that the gap is not a governance preference. A receiving unit that cannot span the directions a contract specifies has a residual it must underwrite by assurance rather than by test, and the size of that residual is computable from quantities the receiving unit can measure. **A signature is therefore what remains of verification once verification is treated as a capacity with a ceiling** — which is a narrower and more defensible claim than either the view that accountability is ceremonial or the view that a sufficiently complete specification makes it unnecessary.

The claim is bounded in the way the rest of the paper is bounded. It is derived under rank-one inspection, it is demonstrated on machine evaluators, and the estimator that makes it measurable needs gold labels that do not fail where the panel fails. What the paper establishes is that the question is well posed and that the quantity answering it is already being computed, in another field, for another purpose.

## Companion Computation Scripts

Every numerical value in this paper is reproduced by one of six scripts published with it. All six fix the seed 20260811 at file top and exit nonzero if any internal check fails, so a silent numerical regression cannot pass. **Reproduction requires no network access, no provider key and no data download**, because the paper collected no data: every figure is either arithmetic on another study's published summary statistics or a seeded simulation of a stated model. A single command at the paper directory's root runs the whole pipeline in dependency order, captures each script's stdout to `output/logs/`, and writes the tables and figures:

```
git clone https://github.com/spectralbranding/orgschema-papers
cd orgschema-papers/verification-bandwidth
./reproduce.sh
```

Each script and what it reproduces, by full path:

| Script | Reproduces |
|---|---|
| [`code/reported_neff_check.py`](https://github.com/spectralbranding/orgschema-papers/blob/main/verification-bandwidth/code/reported_neff_check.py) | Table 3. Deterministic; no randomness at all. The standing guard against the paper ever claiming the estimator it cites |
| [`code/phi_mapping.py`](https://github.com/spectralbranding/orgschema-papers/blob/main/verification-bandwidth/code/phi_mapping.py) | Table 2 and both figures, at 400,000 deviations per row with a 2,000,000-draw Monte Carlo cross-check |
| [`code/p2_exact.py`](https://github.com/spectralbranding/orgschema-papers/blob/main/verification-bandwidth/code/p2_exact.py) | Tables 1 and 4, by dense fixed-grid quadrature checked against 400,000-deviation Monte Carlo per cell |
| [`code/formal_model_checks.py`](https://github.com/spectralbranding/orgschema-papers/blob/main/verification-bandwidth/code/formal_model_checks.py) | The random-rule checks on Proposition 1, the correlation sweep behind Proposition 2, and the worst-case block of Table 5 over 30 configurations per row |
| [`code/threat1_kill_test.py`](https://github.com/spectralbranding/orgschema-papers/blob/main/verification-bandwidth/code/threat1_kill_test.py) | Table A1, at 200,000 deviations per condition |
| [`code/emit_paper_tables.py`](https://github.com/spectralbranding/orgschema-papers/blob/main/verification-bandwidth/code/emit_paper_tables.py) | A CSV projection of the deterministic tables, so this paper can be diffed against its own derivations mechanically rather than read against them |

*Notes*: Each script is also runnable alone; the per-script run commands are in [`code/README.md`](https://github.com/spectralbranding/orgschema-papers/blob/main/verification-bandwidth/code/README.md). Tables 2 and A1 and the worst-case block of Table 5 are seeded Monte Carlo and are deliberately not re-derived by the CSV emitter, since a second implementation of a seeded simulation is the drift this discipline exists to prevent; their record is the captured stdout in `output/logs/`. Running the pipeline reproduces every cited figure within the reported Monte Carlo error.

**One numerical choice is stated because it affects reproduction.** The one-dimensional integrals behind Tables 1 and 4 are evaluated on a dense fixed grid over $\pm 12\sigma$ rather than by Gauss–Hermite quadrature, which is unstable at the node counts this integrand wants; the Monte Carlo comparison reported above is what certifies the grid.

## Data and Code Availability

### *What is published.*

**No new data were collected, and the paper is reproducible without any.** Every empirical figure attributed to a published panel is quoted from that panel's own published summary statistics [@kohli-2026-nine-judges-two-effective-votes], and every derived figure is regenerated by the scripts above from source.

Published with this record, in the paper's public repository at [github.com/spectralbranding/orgschema-papers/tree/main/verification-bandwidth](https://github.com/spectralbranding/orgschema-papers/tree/main/verification-bandwidth): the six computation scripts with their seeds and internal checks, under [`code/`](https://github.com/spectralbranding/orgschema-papers/tree/main/verification-bandwidth/code) with its own [`README.md`](https://github.com/spectralbranding/orgschema-papers/blob/main/verification-bandwidth/code/README.md) mapping each script to the tables it produces; the [`reproduce.sh`](https://github.com/spectralbranding/orgschema-papers/blob/main/verification-bandwidth/reproduce.sh) orchestrator; the proposition and dependency graph behind the argument as [`SPINE.yaml`](https://github.com/spectralbranding/orgschema-papers/blob/main/verification-bandwidth/SPINE.yaml); the [`ONTOLOGY.yaml`](https://github.com/spectralbranding/orgschema-papers/blob/main/verification-bandwidth/ONTOLOGY.yaml) module defining the terms this paper introduces and the one it narrows; the machine-readable claim bundle [`paper.yaml`](https://github.com/spectralbranding/orgschema-papers/blob/main/verification-bandwidth/paper.yaml); and the generated [`output/`](https://github.com/spectralbranding/orgschema-papers/tree/main/verification-bandwidth/output) split into `tables/`, `figures/` and `logs/`, the last holding the captured stdout of every script in the published run.

**Nothing is withheld.** There is no dataset to redact, no third-party text to avoid redistributing, and no provider credential in the pipeline.

### *Identifiers.*

Concept DOI: [10.5281/zenodo.21891435](https://doi.org/10.5281/zenodo.21891435), which resolves to the most recent version and is the identifier to cite unless a specific version is intended. This record is version v1.0.0, whose version DOI is [10.5281/zenodo.21891436](https://doi.org/10.5281/zenodo.21891436). The derived results — the emitted tables, the run logs and the figures — are additionally archived as a dataset at [10.57967/hf/9953](https://doi.org/10.57967/hf/9953), whose card documents what each file holds and, explicitly, that the record is an audit trail rather than observational evidence. That dataset is a convenience for auditing rather than a dependency: the repository above regenerates every one of its files from source.

## Acknowledgments

AI assistants (Claude Opus 5, Gemini 3.1 Pro, Grok 4.3) were used for initial literature search, for software development — implementing and running the companion computation scripts that reproduce the paper's reported numerical and simulation results — and for editorial refinement; all theoretical claims, propositions, and interpretations are the author's sole responsibility.

The bounded-verification framework whose formal comparison the parent paper flagged as warranting dedicated treatment [@kovalenko-2026-bounded-compositional-verification] is engaged here through its published record only.

## CRediT contributions

Conceptualization, methodology, formal analysis, investigation, writing — original draft, writing — review and editing, visualization: Dmitry Zharnikov.

## References

::: {#refs}
:::

## Appendix A: The Bracket Simulation

The simulation behind *The Bracket* generates $k = 9$ evaluators in $n = 10$ dimensions with a shared-factor geometric correlation and a common threshold $\tau = .30$, draws 200,000 unit-norm deviations per row, and records detection rates for the disjunctive rule, the majority rule, the unanimous rule, and a single evaluator as a control.

**Table A1: Detection Rates by Aggregation Rule Across the Correlation Range.**

| $\rho$ | $\bar\rho$ realized | $n_{\text{eff}}$ (eigenvalue) | $n_{\text{eff}}$ (design effect) | Disjunctive | Majority | Unanimous | Single | Bracket |
|---|---|---|---|---|---|---|---|---|
| .000 | .234 | 3.76 | 3.14 | .983 | .197 | .000 | .370 | .983 |
| .200 | .302 | 2.72 | 2.63 | .979 | .222 | .000 | .370 | .979 |
| .391 | .390 | 2.12 | 2.19 | .968 | .248 | .003 | .371 | .965 |
| .500 | .478 | 1.83 | 1.87 | .966 | .249 | .010 | .370 | .956 |
| .700 | .718 | 1.33 | 1.33 | .879 | .307 | .058 | .371 | .821 |
| .900 | .903 | 1.09 | 1.09 | .652 | .347 | .158 | .370 | .494 |
| .990 | .991 | 1.01 | 1.01 | .445 | .368 | .301 | .370 | .144 |

*Notes*: The realized correlation column is **geometric**, not the error correlation of Table 2. "Single" is one evaluator's detection rate, flat at about $.370$ across every condition, which is the control establishing that the panel effects are not artifacts of individual sensitivity; "bracket" is the disjunctive rate minus the unanimous rate. Disjunctive detection falls by $.539$ across the range while unanimous detection rises by $.301$ — the decisive observation, since the two have opposite signs — and the majority rule lies strictly inside the bracket at every row. The bracket collapses from $.983$ to $.144$. The two effective-rank estimators, one from the eigenvalues of the frame operator and one from the design effect, agree to within $.63$ at worst and converge as correlation rises. **This simulation draws unit-norm deviations, which pins deviation magnitude and therefore removes the shared-item-difficulty channel**, placing its measured error correlation up to $.056$ below the map at low correlation; under the Gaussian model of Table 2 the same residual falls below $.001$, which identifies the mechanism as a property of the radial distribution rather than of the map.

Pointwise checks on Proposition 1 cover all $2^5$ input vectors for 400 randomly generated rules, drawn from weighted-threshold and general monotone families, and the inclusion holds in every case. In detection probability at correlations of $.00$, $.40$ and $.80$, over 60 random rules per condition, every rule's rate falls inside the bracket its panel defines.

# Pilot frame + feasibility findings (dossier-build stage)

Recorded 2026-07-29 during construction of the 10 separated sub-dossier pairs
(`pilot_dossiers/`) from SEC EDGAR primary filings. These are the build-time
verification findings the pilot pre-registration anticipated (`PILOT_PREREGISTRATION.md`
§2: "residual deal-value/type verification still happens at dossier-build") plus the
new frame-quality findings that extend `DRAW_QUALITY_FINDING.md`. They are inputs to the
go/no-go report and, above all, to the sampling-frame redesign for the full N≈300 draw.
None of these bears on the reliability/pipeline validation the coding step measures (the
dossiers built are all real, separated, and citation-grade); they bear on whether the
*sampling frame* is fit to scale.

## 1. Carve-out stratum: form-type classification is unreliable (2 of 3 drawn "carve-outs" are not carve-outs)

The pilot drew 3 carve-outs by classifying on filing form-type (Form 10 / 10-12B). Two
of the three are not carve-outs of a product/asset from a shared-services parent:

- **P01 Bank First National Corp (accession 0001571049-18-000511)** — NOT a carve-out.
  The drawn Form 10-12B/A is a bank holding company's voluntary Section 12(b)
  registration of its OWN common stock to uplist from OTC Pink ("BFNC") to Nasdaq. There
  is no parent distributing/divesting the registrant, no spin-off/split-off, and no
  transition-services / separation / tax-matters agreement (confirmed by text search of
  the stripped information statement). The struct dossier records the transaction as it
  is (an uplisting registration with no product/shared-services separation); a coder will
  correctly read no structural gap. Kept in the pilot as a codeable "no-separation" case.
- **P02 John Bean Technologies Corp (drawn accession 0001433660-18-000012)** — the drawn
  filing is a MIS-DRAW: it is Amendment No. 6 to JBT's 2008 Form 10 whose entire
  substance is a First Amendment to the shareholder Rights Agreement (a poison-pill
  expiration acceleration), documenting no separation. The registrant DOES have a genuine
  parent carve-out — the 2008 spin-off of JBT from FMC Technologies — so the struct
  dossier was built from the real 2008 information statement (EX-99.1 to Amendment No. 5,
  accession 0001193125-08-150024) and the outcome dossier from the ~FY2012 10-K
  (0001437749-13-002494, ~4.5yr post-spin). NOTE: this substitution moves the deal era
  (2008) OUTSIDE the pilot frame's era band; it was a build-time recovery, not a blind
  draw, so it is sound for the reliability read (κ) but must NOT be treated as a blind
  case-control selection. Only P03 (Adient/Johnson Controls) is a genuine carve-out drawn
  cleanly at the intended accession.

**Implication for the full draw:** do NOT select carve-outs by form-type alone. Form 10 /
10-12B is used for uplistings, rights-plan amendments, and many registrations besides
spin-offs. The full-draw frame needs a positive spin-off/divestiture signal — e.g. an
Item 2.01 disposition completion 8-K on the PARENT, a distribution-ratio + former-parent
disclosure in the information statement, or a curated spin-off list (SDC/Refinitiv) —
plus a build-time confirmation gate before a deal enters the sample.

## 2. Control stratum: two failure modes for the outcome pass

- **Going-private controls have no public 3–5yr outcome record.** P07 VeriFone (taken
  private by a Francisco Partners-led group, 2018) and P09 Gramercy Property Trust
  (taken private by Blackstone, 2018) both filed Form 15 and deregistered; neither has a
  public audited 10-K in the outcome window. Their outcome dossiers are necessarily
  press-only, with financial trajectory flagged `[UNVERIFIED]`. 2 of 5 controls in the
  pilot hit this. **Implication:** the full-draw control frame should prefer whole-company
  acquisitions whose ACQUIRER continues public reporting (so the combined-entity outcome
  is audited), or explicitly budget for press-only outcome coding on going-private exits.
- **A "matched going-concern control" can itself be structurally gap-prone.** P08 Wabtec
  is matched to P03 Adient on SIC×size×era, but the Wabtec/GE-Transportation deal is a
  modified Reverse Morris Trust — GE carved its Transportation business out (product +
  operations transferred; GE-level IP/software/shared services retained by GE, bridged by
  a TSA). Structurally that is a carve-out with a product↔shared-substrate gap, not a
  whole-company going-concern combination where product+process+organization move
  together. **Implication:** match controls on being a genuine WHOLE-COMPANY going-concern
  acquisition (product+process+organization transfer together), not merely on SIC×size×
  era; screen out RMT/carve-out-into-acquirer structures from the control pool.

## 3. Construct-fit contrast within the roll-up stratum (a GOOD signal, reportable)

The two roll-ups differ on exactly the structural axis the constructs target, which is
useful: **P04 Griffin/Peakstone** consolidated the portfolios AND internalized the
advisory/asset-/property-management (a concurrent Self-Administration Transaction moving
the operating substrate in-house) — process/organization consolidated coherently
alongside the product, so a coder should read little/no structural gap. **P05
Colony/BrightSpire** consolidated three portfolios but stayed EXTERNALLY managed by a
sponsor affiliate (no internalization) — operating processes/management did not
consolidate onto the platform alongside the assets, a candidate structural gap. This is
the intended within-stratum variation and is a good sign the constructs discriminate.

## 4. Carry-forward (already recorded, restated for the full-draw frame)

- **Size-gate skew** (`DRAW_QUALITY_FINDING.md`, PROGRAM_PLAN STATE): the ≥$1bn
  Assets/Revenues gate favours asset-heavy financials; the roll-up qualifying pool
  collapsed to 8 and both drawn roll-ups are REITs. Consider operating-company /
  cascade-relevant SIC scoping or a deal-value size measure for N≈300.

## Net read for the go/no-go report

The dossier-build + separation + porosity + coding PIPELINE works end-to-end on real
primary filings (feasibility PASS on the mechanics). The SAMPLING FRAME, however, is not
yet fit to scale: form-type carve-out classification is unreliable (§1), and the control
pool needs a whole-company + acquirer-still-reporting screen (§2). These are frame-design
fixes for the full draw, surfaced exactly because the pilot ran first.

# Audit pass 4: verification of the revision

Date: 2026-11-22
Manuscript: `fuchs-bc-treespecies-fire`, HEAD `511985c` (W2.4 risk metric wording)
Code of record: `fresh-fuchs-ws4`, rotation artifact and scripts at the current checkout; fire API at
`9918fb17`, handoff summaries at `474dca6e`
Scope: the current `main.tex` and all `text/*.tex`; `review/AUDIT-03-ANTAGONISTIC.md`;
`review/AUDIT-03-RESPONSE.md`; the code artifacts named by the paper; the current claims register.
Method: verify every M1–M12 and S1–S10 against the manuscript, not against the response file;
recompute the composition and fire table arithmetic; trace every new number to an artifact.
No manuscript file was edited.

## Verdict

**Not submittable now.** The revision fixes the most serious conceptual error of the previous draft:
the CVaR-of-NPV claim and the leader min-CVaR equation are gone, the RQs are answerable, the methods
now describe a two-layer scenario analysis, and the fire table is materially better. That is real
progress.

But the revision replaces the old risk error with a new one. The abstract, the contribution list, the
discussion, and the conclusion all say that downside risk **is measured / is reported** as
volume-at-risk on paired draws. There is no volume-at-risk results subsection, and the claims
register still marks the metric **pending** (`notes/claims-register.md:99`). The paper is therefore
claiming a result it does not contain. Separately, the composition table still has the infeasible
6% row (53.3 M m3/period against a 51.9 M m3/period sustained level), and the rotation artifact does
not contain the aspen-maximisation rotation (101.7 years) or the “44% older than 100 years” claim
that the manuscript and register attribute to it.

If the ensemble lands and a risk subsection with numbers is added, and the 6% row, the rotation
artifact, the register, the supplement, and the cover letter are fixed, the paper could be
submittable. If the ensemble never lands, the risk claim and the fourth contribution must be removed;
the paper can still stand as a composition–production case study with a fire-calibration and
coupling demonstration, but the abstract, title, discussion, and conclusion must say so.

## Severity table

| ID | Severity | Finding | Main location |
| --- | --- | --- | --- |
| V1 | **Must fix** | The paper claims a volume-at-risk result on paired draws, but no risk subsection or numbers exist, and the register says `pending`. The abstract uses “is measured”, the contribution says “a paired volume-at-risk comparison”, the discussion says “reports”, and the conclusion says “is reported”. | `text/0_abstract.tex:22-23`; `text/1_introduction.tex:79-80`; `text/4_discussion.tex:89-91`; `text/5_conclusion.tex:8`; `notes/claims-register.md:99` |
| V2 | **Must fix** | The composition table still lists 6% at 53.3 M m3/period while the caption and text say a six percent share is feasible at the sustained level (51.9 M m3/period). The row is arithmetically 3.20/0.06, but it is not a feasible level under the flat-flow cap. | `text/3_results.tex:131-132,136-138,144` |
| V3 | **Must fix** | The 101.7-year aspen-maximisation rotation and the “44% of managed area older than 100 years” claim are not in `rotation.json`; the register cites that file for both. The artifact contains only the baseline rotation and the 92-year median age. | `text/3_results.tex:210`; `text/4_discussion.tex:29-30,67-68`; `text/99_online_supplement.tex:124-125`; `notes/claims-register.md:79-80`; `experiments/tsa24-evenflow/rotation.json:1-8` |
| V4 | **Must fix** | The methods still say “we never report an absolute fire size as a result”, while the abstract and Table 5 report absolute fire sizes and say the regime “reproduces” the median, p90, and share above 500. The p90 is at the lower edge of a 349–1,051 interval, not a reproduction of the 490 point estimate. | `text/2_methods.tex:127-128`; `text/0_abstract.tex:19-21`; `text/3_results.tex:159-166`; `text/4_discussion.tex:79-83` |
| V5 | **Must fix** | The methods say “every headline result is reported with a sensitivity across … the fire-weather initialisation”, but the fire-weather initialisation is not varied; the paper uses one 2023 season. The risk metric also omits its 20% tail probability and the constant 59.99 CAD/m3 margin used by the code. | `text/2_methods.tex:83-87,158-163`; `experiments/p4-risk/run_ensemble.py:41,87-104,315-322` |
| V6 | **Must fix** | The register still cites `tsa24-thlb.md` and `tsa24-yield-reconciliation.md`, which do not exist in `fresh-fuchs-ws4/notes/reference/`. It still lacks rows for 1,037.9 M m3, 680/435 ha per ignition, 25%, 2.5%, 8.35/7.35, the 10,000 even-flow weight, and the full historical fire table. The response claims several of these rows were added; they are absent. | `notes/claims-register.md:18-24,40-43,49,56-57,71,79-80,99`; `text/3_results.tex:24,30,41,196-198`; `text/4_discussion.tex:31-33` |
| V7 | **Must fix** | The supplement still says the deciduous price sensitivity runs from 35 to 61.74 CAD/m3, while the main text and Table 3 use 35 to 40 and the register records −26 to +26 across 35–40. The 61.74 row was removed from the main text but not from the supplement. | `text/99_online_supplement.tex:90-91`; `text/3_results.tex:83-86,100-101`; `notes/claims-register.md:61` |
| V8 | **Must fix** | The flow-rule attribution remains causal: “the shortfall is the cost of the flow rule”, “the difference is the cost”, “the gap is the cost”. The paper shows the land base matches and the maximum MAI is above the cut, but it does not run a declining-profile counterfactual. The previous M6 asked for “consistent with”; only the growth-curve part was softened. | `text/0_abstract.tex:12-13`; `text/3_results.tex:33-34`; `text/4_discussion.tex:28-35`; `text/5_conclusion.tex:13-14` |
| V9 | **Must fix** | “The discount rate dominates every other lever” remains in the results, although a 10% composition share removes 38% of volume and is comparable to the 46% NPV effect of moving the discount rate from 3% to 5%. The discussion still says diversification “costs a third of the harvest”, which is true only for the 10% case (23% at 8%, 38% at 10%, 59% at 15%). | `text/3_results.tex:78`; `text/4_discussion.tex:51-54` |
| V10 | **Must fix** | The cover letter is stale: it still uses the old title (“a two-level policy model”), says a regional policy “sets … species targets”, reports 0.3% rather than 0.32%, says “three contributions” rather than four, and claims the flow-rule attribution. The response says S10 is fixed; it is not. | `submission/cover-letter.md:14-15,17-19,22-23,29-34,41-43` |
| SH1 | Should fix | “With the composition weight at 200, twice the level weight” is not supported by the composition artifact, which names weight 200 but does not document a level weight of 100. The 500-fold increase over the 200 run is supported. | `text/3_results.tex:118-120`; `experiments/tsa24-composition/README.md:20-26` |
| SH2 | Should fix | The sentence “173 m3/ha … about three quarters of the area-weighted maximum mean annual increment of 2.31 m3/ha/yr” compares a stock (m3/ha) to a flow (m3/ha/yr). The intended comparison is 173/(2.31 × 102.2) = 0.734, i.e. 73% of the volume the maximum MAI accumulates over a 102-year rotation. | `text/3_results.tex:216-220` |
| SH3 | Should fix | The P3.3 report still says the maximum “sits inside” the historical interval and that the regime “reproduces … the maximum”, while the manuscript and register correctly say the maximum interval is one-sided and not used. The source record is stale relative to the paper. | `notes/reports/p3-3-distribution-comparison.md:28,32-33,50-51`; `text/3_results.tex:164-166`; `notes/claims-register.md:97` |
| SH4 | Should fix | The supplement’s composition table says the aspen-maximisation share is 6.20%, while `summary.json` records 6.18%. The main text’s “6.2” is fine; the supplement’s two-decimal value is not. | `text/99_online_supplement.tex:108`; `experiments/tsa24-composition/summary.json:21` |
| SH5 | Should fix | The declarations assert WS4 is “released under the Apache License 2.0”, but the project repository has no `LICENSE` file and its README says “Choose and add a license before the first public release.” The composition run script and composition species-period tables are still absent, yet the supplement says the analysis code produces every number. | `text/6_declarations.tex:9,16-18`; `text/99_online_supplement.tex:129-132`; `fresh-fuchs-ws4/README.md:47` |
| SH6 | Should fix | The nine limitations do not mention that NPV excludes road construction, administration, taxes, and risk premia; the reported “net present value” is an operating margin, not a profit. The short composition searches are mentioned in the composition subsection but not in the formal limitations list. | `text/4_discussion.tex:107-142`; `text/2_methods.tex:150-155` |
| SH7 | Should fix | “Our result qualifies that finding rather than contradicting it” still implies the paper tested the European finding. The paper establishes a supply precondition; it does not test whether diversification buffers severe events. | `text/4_discussion.tex:95-103` |
| SH8 | Should fix | S1 is still open: one figure and five tables, no two-level diagram, composition figure, or fire ECDF. The discussion is 1,539 words against a 900-word plan target; the abstract is 294 words against 250; the supplement is still inside the main PDF; the acknowledgements file is empty but included. | `planning/paper-plan.md:51-70`; `main.tex:47`; `text/9_acknowledgements.tex` |
| C1 | Consider | The title still says “under forest fire risks” and the keywords still say “fire risk”, although the paper does not estimate a fire-risk effect; it compares a calibrated fire-size distribution and couples one run. If the volume-at-risk result does not land, change “fire risk” to “fire scenario”. | `main.tex:23`; `text/0_abstract.tex:30-31` |
| C2 | Consider | The 2017 Prince George rationale is now cited, but its URL does not print in the bibliography, so a reader cannot reach the source of the 8.35/7.35 values from the reference list. Add a note or use a `@misc` entry that prints the URL. | `references.bib:181-188`; `main.bbl:15-21` |
| C3 | Consider | The rotation mean is area-weighted, but the median and p10–p90 are unweighted (`rotation.py` uses `np.median`/`np.quantile` on intervals). The manuscript does not say this. Either weight the quantiles or state that they are unweighted. | `scripts/rotation.py:77-83`; `text/3_results.tex:207-208` |
| C4 | Consider | “The two searches behind the ceiling” is imprecise: the ceiling comes from the aspen-maximisation run, not the two composition-weight searches. The two weight runs support the supply-limit interpretation. | `text/4_discussion.tex:58-61` |
| C5 | Consider | “The scenario sits inside the historical spread” compares 680/435 ha per ignition to a historical mean of 512.9 ha, not a spread or interval. Say “the grown area is above the historical mean and the applied area below it”, or give a historical interval. Also say “ending standing volume” rather than “ending volume”. | `text/3_results.tex:196-198` |

---

## 1. Per-item verification of AUDIT-03

Legend: **Fixed** = the specific defect is gone and the replacement is supported; **Partly** = the old
defect is gone but a related defect remains; **Not fixed** = the old defect is still present.

| Item | Status | Evidence and current location |
| --- | --- | --- |
| M1 CVaR/NPV-at-risk unsupported | **Partly** | CVaR of NPV is gone from the abstract, methods, discussion, conclusion, and keywords. The abstract now says “volume-at-risk on paired draws” (`text/0_abstract.tex:22-23`), the methods defines the metric (`text/2_methods.tex:83-87`), and the conclusion says “risk is reported as volume-at-risk” (`text/5_conclusion.tex:8`). But there is no volume-at-risk result, and the register says `pending` (`notes/claims-register.md:99`). The old metric error is fixed; the replacement is unsupported. |
| M2 No policy comparison under fire | **Partly** | The RQs are now answerable: level (`text/1_introduction.tex:59-60`), share and volume cost (61-62), rotation (63), fire distribution and coupling (64-65). The paper says the single run is not a policy comparison (`text/4_discussion.tex:88-89`; `text/3_results.tex:154-155`). But the fourth contribution still claims “a paired volume-at-risk comparison of two schedules” (`text/1_introduction.tex:79-80`), and the results say the fire scenario is not used to rank composition scenarios. The paired comparison is not delivered. |
| M3 Composition 6%, weights, level | **Partly** | Weights 200 and 100,000 and the 5.16 level are now stated (`text/3_results.tex:118-121`); the constant-supply assumption and the absolute target are disclosed (127-128; caption 136-138); the short searches are disclosed (`text/4_discussion.tex:62-63`). But the 6% row is still 53.3 (`text/3_results.tex:144`) while the caption says “A six percent share is feasible at the sustained level” (138) and the text says the same (131-132). “Twice the level weight” is unsupported (118). The row is the main remaining defect. |
| M4 Fire table/abstract overclaim | **Partly** | Table 5 is fixed: n = 3,450, simulated values not bootstrapped, shares above 100 and 1,000 added, maximum marked one-sided and not used (`text/3_results.tex:168-190`). But the abstract still says the regime “reproduces” the median, p90, and share above 500 (19-21); the results say “the central distribution is therefore reproduced” (159-166); the discussion says “reproduces” (79-83). The p90 is 361.5 against 490.17, at the lower edge of 349.13–1,051.26. The methods still says “never report an absolute fire size as a result” (127-128), contradicted by the abstract and table. |
| M5 Methods describe a model not run | **Mostly fixed** | The leader min-CVaR equation is deleted; the enterprise equation is deleted; the one-sided goal program and the even-flow term are described (`text/2_methods.tex:54-81`). “Highest even flow” is replaced by “six searches converged to a plateau; not a proven maximum” (97-104; `text/3_results.tex:16-20`). Remaining: “every headline result … fire-weather initialisation” is false (158-163); the risk metric is defined but not reported (83-87; 141-142). |
| M6 Yield bridge not a validation | **Partly** | The upper-bound check is stated in the results and discussion (`text/3_results.tex:28-34`; `text/4_discussion.tex:24-26,37-39`); 0.32% is stated (methods 19; results 26; discussion 23); the median age is 92 years, sourced to `rotation.json` (discussion 29); the 8.35/7.35 profile is cited to the 2017 rationale (31-33). But the abstract, results, discussion, and conclusion still say the shortfall “is the cost” of the flow rule (abstract 12-13; results 33-34; discussion 28-35; conclusion 13-14), with no declining-profile counterfactual. The 44% older than 100 years is unsourced (30). |
| M7 Missing register rows/dead paths | **Mostly not fixed** | Rotation now has `scripts/rotation.py` and `rotation.json`; the baseline 53,071/102.2/100/60-160/92 match (`experiments/tsa24-evenflow/rotation.json`; `text/3_results.tex:204-210`). But 101.7 and 44% are not in `rotation.json` (register 79-80); `tsa24-thlb.md` and `tsa24-yield-reconciliation.md` still do not exist (register 18-24); rows for 1,037.9, 680/435, 25%, 2.5%, 8.35/7.35, 10,000, and the full historical fire table are still missing. The response’s claim that rows were added for total volume, per-ignition areas, and the transition profile is false. |
| M8 Limitations seven vs five | **Mostly fixed** | Nine limitations now (`text/4_discussion.tex:107-142`), including the missing fire-risk policy result (121-123), volume-only risk metric (125-127), clearcut (134-135), leading species (137-138), in-sample calibration and one weather season (140-142), mixed vintages (129-132). Remaining: road construction/administration/taxes/risk premia are not listed; the short composition searches are in the composition subsection (62-63), not the formal list. |
| M9 Data/code availability overclaims | **Partly** | The API commit `9918fb17` and handoff `474dca6e` are now cited (`text/2_methods.tex:135-136`; `text/6_declarations.tex:9`); S1/S2 distinguish the benchmark target from the model schedule (`text/99_online_supplement.tex:8-11,53-54`). Remaining: the calibration is “archived … on acceptance” with no DOI (declarations 10-14); the composition script and composition species-period tables are still absent (declarations 16-18; supplement 129-132); the Apache 2.0 claim is unverified (`fresh-fuchs-ws4/README.md:47`). |
| M10 Gap not established | **Mostly fixed** | Fuel-treatment and bilevel fuel-treatment references are added and the gap claim is narrowed (`text/1_introduction.tex:31-44`; `references.bib:151-179`). Remaining: the paragraph covers fuel treatment, not stochastic harvest scheduling; the sentence “we do not review them exhaustively” is honest but invites a referee to ask for the stochastic-scheduling literature. |
| M11 Title/author/date/keywords/abstract | **Mostly fixed** | Title has a scoped subtitle; “working title” and author-order notes are gone; date is fixed; keywords no longer say CVaR (`main.tex:23-30`; `text/0_abstract.tex:30-31`). Remaining: the abstract still overclaims “reproduces” and “volume-at-risk is measured”; the funding TODO is still in the declarations (`text/6_declarations.tex:30`). |
| M12 BC policy setting | **Fixed** | The introduction states the AAC is a maximum, that silviculture is constrained by prescriptions and stocking standards, and that the composition aspiration is hypothetical (`text/1_introduction.tex:3-11`); the methods repeats it (`text/2_methods.tex:56-63`); the 2017 rationale is cited (`text/2_methods.tex:17-19`; `references.bib:181-188`). |
| S1 Figures | **Not fixed** | Still one map and five tables; no two-level diagram, composition figure, or fire ECDF. The response says a figure pass remains. |
| S2 Discussion length | **Partly** | The duplicate European paragraph is gone; the discussion is 1,539 words, down from 1,705, but still 1.7× the 900-word plan target. The results are 1,659 words. |
| S3 Fire table | **Fixed** | n = 3,450, not bootstrapped, shares above 100 and 1,000 added, maximum one-sided (`text/3_results.tex:168-190`). The P3.3 report is stale on the maximum (SH3). |
| S4 Units | **Fixed** | Composition table labels “M m3/period” and “M m3/yr” (`text/3_results.tex:142`); supplement S4 does the same (103-108); the text labels both. |
| S5 Price mapping | **Fixed** | Methods now prices subalpine fir on the Hem-Bal series (`text/2_methods.tex:146-150`), matching `scripts/valuation.py:18-26`. |
| S6 No composition NPV | **Fixed** | The old “economically favourable mixtures” RQs are gone; the paper asks what composition costs in volume (`text/1_introduction.tex:38-40`; `text/3_results.tex:152-155`). |
| S7 Stale reference notes | **Partly** | The main text no longer uses the benchmark fixture; the supplement still says the deciduous sensitivity runs to 61.74 (`text/99_online_supplement.tex:90-91`), contradicting the main text and register. The code notes still carry the old fixture. |
| S8 Validation wording | **Fixed** | Results now say the validator checks manifest and schema invariants, not the inventory against its source (`text/3_results.tex:6-12`). |
| S9 Fire limits | **Fixed** | In-sample, 24 ignitions, one 2023 season, current fuels, clearcut, five dropped blocks are in methods and limitations (`text/2_methods.tex:132-142`; `text/4_discussion.tex:140-142`). |
| S10 Cover letter | **Not fixed** | The cover letter still has the old title, “two-level policy model”, “a regional policy sets … species targets”, 0.3%, three contributions, and the flow-rule attribution (`submission/cover-letter.md:14-15,17-19,22-23,29-34,41-43`). The response says it is aligned; it is not. |

---

## 2. Issues introduced or left by the rewrite

### 2.1 The volume-at-risk claim is an unsupported result, not a method statement (V1)

This is the central new defect. The paper uses the present tense in four places:

- Abstract: “Downside risk **is measured** as volume-at-risk on paired draws”
  (`text/0_abstract.tex:22-23`).
- Contribution: “a **paired volume-at-risk comparison** of two schedules”
  (`text/1_introduction.tex:79-80`).
- Discussion: “The paired ensemble **reports** volume-at-risk for two schedules on common draws”
  (`text/4_discussion.tex:89-91`).
- Conclusion: “risk **is reported** as volume-at-risk on paired draws” (`text/5_conclusion.tex:8`).

There is no risk subsection in the results. The results end with rotation
(`text/3_results.tex:202-220`), and the fire subsection explicitly says the scenario “is not used to
rank composition scenarios” (`text/3_results.tex:154-155`). The register says
`Volume-at-risk by policy | paired ensemble running … | pending` (`notes/claims-register.md:99`).
The code has a metric definition (`experiments/p4-risk/run_ensemble.py:41,87-104,315-322`), but
`experiments/p4-risk/` contains no `ensemble.json`.

So the current wording is **an unsupported result claim**, not a promise and not a method statement.
The methods paragraph is a method statement; the abstract, contribution, discussion, and conclusion
are result claims. The paper cannot have it both ways.

If the ensemble lands, add a results subsection with: number of draws, the two schedules, the 20%
lower-tail CVaR of ending standing volume, the value conversion at 59.99 CAD/m3, and the paired
difference. If it never lands, remove the risk claim from the abstract, contribution, discussion, and
conclusion; either keep the metric definition as a future-work paragraph or delete it. The paper can
still be submittable as a composition/fire-calibration paper, but the fourth contribution and the
abstract’s risk sentence must go.

### 2.2 The composition table’s 6% row is still infeasible (V2)

The table:

- 6% → 53.3 M m3/period, 5.33 M m3/yr (`text/3_results.tex:144`).
- Caption: “The total level is the level at which the share is reached. A six percent share is
  feasible at the sustained level.” (136-138).
- Text: “A six percent share is feasible at the sustained level, because the ceiling is about
  6.2 percent.” (131-132).

The arithmetic 3.20/0.06 = 53.3 is correct as an arithmetic identity, but 53.3 exceeds the 51.9
M m3/period plateau. At the sustained 51.9 level, a 6% share needs 3.114 M m3/period of aspen, which
is below the 3.20 ceiling, so a 6% target is feasible — but the level at which it is reached is
51.9, not 53.3. The table’s 6% row is above the flow cap and is not a feasible point. The caption and
the row contradict each other.

Fix: either

- replace the 6% row with “6.2 (aspen max, no level target) | 51.8 | 5.18” and put the 6% feasibility
  in the text; or
- keep a 6% row but write “51.9 (flow-limited) | 5.19” and add a note that the arithmetic 53.3 is
  above the cap; or
- start the table at 8% and state the 6% feasibility separately, with the 51.9 cap.

The current “level at which the share is reached” framing makes the problem worse, because it invites
the reader to treat 53.3 as a feasible level. The paper’s own README has the same inconsistency
(`experiments/tsa24-composition/README.md:41-49`), so the manuscript inherited it.

### 2.3 The rotation artifact does not support the rotation result (V3)

`rotation.json` contains only:

```
intervals 53071, mean_years 102.1539, median_years 100, p10 60, p90 160,
median_managed_age_years 92
```

(`experiments/tsa24-evenflow/rotation.json:1-8`).

The manuscript claims:

- “Under the aspen-maximisation schedule the mean is 101.7 years”
  (`text/3_results.tex:210`; discussion 67-68).
- “44% of the managed area is older than a century” (`text/4_discussion.tex:29-30`; supplement
  124-125).
- The register cites `rotation.json` for both 101.7 and 44% (`notes/claims-register.md:79-80`).

Neither value is in the artifact, and `scripts/rotation.py` does not compute the 44% share. The
44% is a new number introduced by the rewrite; it has no artifact. The 101.7 is a carry-over from the
previous draft; the new artifact was supposed to fix it but only covers the baseline.

Fix: add an `aspen_max` block to `rotation.json` (and a `share_older_than_100` field to the script),
or remove the 101.7 and 44% claims. If the 101.7 is kept, the artifact must show the schedule and the
summary. If the 44% is kept, the script must compute it.

There is also a wording problem independent of the artifact. The results say “the rotation is
essentially invariant to the composition target” (`text/3_results.tex:214`), and the discussion says
“Diversification does not require a different age at harvest” (`text/4_discussion.tex:67-69`). Both
are based on one alternative schedule, the aspen-maximisation run, which has no level target and is
an upper bound on aspen supply, not a composition target at the sustained level. The honest claim is
“between the baseline and the aspen-maximisation schedules, the area-weighted rotation changes by
0.5 years.” Do not generalize to “the composition target.”

### 2.4 The fire wording still overclaims and still contradicts the methods (V4)

The table is fixed, but the prose is not:

- Abstract: “reproduces the historical median, 90th percentile, and share above 500”
  (`text/0_abstract.tex:19-21`).
- Results: “The central distribution is therefore reproduced” (`text/3_results.tex:163`).
- Discussion: “reproduces the historical median, the 90th percentile, and the share above 500”
  (`text/4_discussion.tex:79-83`).

The p90 is 361.5 ha against a point estimate of 490.17 and a 5th–95th interval of 349.13–1,051.26.
It is inside the interval, but 26% below the point estimate and only 3.5% above the lower bound. The
source report’s table verdict for p90 is “consistent”
(`notes/reports/p3-3-distribution-comparison.md:22`), even though its reading paragraph also uses
“reproduced” (line 32). “Reproduces” is stronger than the table’s own verdict; “consistent with, at
the lower edge” is the honest wording. The same applies to the share above 500 (8.3 against
7.6–12.5).

The methods also still says “we never report an absolute fire size as a result”
(`text/2_methods.tex:127-128`), while the abstract and Table 5 report absolute sizes. The intended
distinction is calibration comparison vs prediction. Rewrite: “We report absolute fire sizes only in
the calibration comparison, never as predictions of future fire.” That resolves the contradiction
without weakening the discipline.

The maximum is now handled correctly: the table says “one-sided”, the text says it is reported for
completeness and not used as a target (`text/3_results.tex:164-166,187`). Good. But the P3.3 report
still says the maximum “sits inside” the interval and the regime “reproduces … the maximum”
(`notes/reports/p3-3-distribution-comparison.md:28,32-33,50-51`). Update the report so the record
matches the paper.

### 2.5 The methods’ sensitivity sentence is false (V5)

“Because several constants are ranges rather than points, every headline result is reported with a
sensitivity across the documented range: the deciduous price, the haul distance, the discount rate,
and the fire-weather initialisation” (`text/2_methods.tex:158-163`).

The results vary only the first three (`text/3_results.tex:72-105`). The fire-weather
initialisation is not varied; the paper uses one 2023 season
(`text/2_methods.tex:138-139`). The fire-weather initialisation is not a constant, and it is not a
headline-result sensitivity. Rewrite: “The economic constants are varied across their documented
ranges: the deciduous price, the haul distance, and the discount rate. The fire-weather
initialisation is a scenario choice; we do not vary it, and we state that as a limitation.”

Also, the risk metric definition (`text/2_methods.tex:83-87`) does not state the 20% tail probability
or the 59.99 CAD/m3 margin that the code uses (`run_ensemble.py:41,315`). The register does
(`notes/claims-register.md:99`). Add both, or the metric is underspecified. If the paper reports a
value, say whether it is the CVaR volume × 59.99 or the worst volume × 59.99; the code’s
`worst_value_cad` is the minimum, not the CVaR (`run_ensemble.py:314-316`).

### 2.6 The register is still not a register (V6)

The response says M7 added rows for “total harvested volume, … per-ignition areas, … and the
transition profile.” They are not there. I searched the register:

- No 1,037.9 M m3 row. The manuscript reports it at `text/3_results.tex:41`.
- No 680/435 ha per ignition row. The manuscript reports them at `text/3_results.tex:196-198`.
- No 25% row. The manuscript reports it at `text/3_results.tex:24`.
- No 2.5% row. The manuscript reports it at `text/3_results.tex:30`.
- No 8.35/7.35 row. The manuscript reports them at `text/4_discussion.tex:31-33`.
- No 10,000 even-flow weight row. The supplement reports it at `text/99_online_supplement.tex:53`.
- No full historical fire table rows: p95 1,918.88/1,415.35–2,955.33, share above 100 26.2/22.7–29.6,
  share above 500 10.0/7.6–12.5, share above 1,000 7.9/5.8–10.2, median interval 20.85–30.16 are
  all reported at `text/3_results.tex:180-187` but absent from the register.
- `tsa24-thlb.md` and `tsa24-yield-reconciliation.md` are still named
  (`notes/claims-register.md:18-24`) and still absent from `fresh-fuchs-ws4/notes/reference/`.
- The 44% and 101.7 rows cite `rotation.json`, which does not contain either (V3).

The register also still carries the benchmark-fixture rows marked “superseded” or “provenance
unverified” (40-43, 49, 56-57). They are not in the manuscript; they should be removed or moved to
an archive section. A register with dead rows and `provenance unverified` entries is not a register
that supports “no row, no shipment.”

### 2.7 The supplement contradicts the main text on the deciduous price (V7)

Main text: “between 35 and 40 CAD per cubic metre the net present value moves by 26 million”
(`text/3_results.tex:83-86`); Table 3 has 35 and 40 only (`text/3_results.tex:100-101`); register
says −26 to +26 across 35–40 (`notes/claims-register.md:61`).

Supplement: “The sensitivity analysis varies the deciduous price over 35 to 61.74 CAD/m3”
(`text/99_online_supplement.tex:90-91`).

The 61.74 value was removed from the main text and register but survives in the supplement. Either
restore the 61.74 source and the row, or change the supplement to 35–40. The current supplement
contradicts the paper’s own table.

### 2.8 The flow-rule attribution is still causal (V8)

The paper has good evidence that the gap is not the land base (0.32%) and not the growth potential
(7.07 upper bound). It does not run a declining-profile counterfactual. Yet:

- Abstract: “The shortfall is the cost of the flow rule, not the land base”
  (`text/0_abstract.tex:12-13`).
- Results: “The difference between that bound and the realized level is the cost of holding a
  constant profile” (`text/3_results.tex:33-34`).
- Discussion: “the difference is the cost of the rule we imposed” (`text/4_discussion.tex:34-35`).
- Conclusion: “the gap is the cost of a flat harvest profile” (`text/5_conclusion.tex:13-14`).

The 92-year median age and the 44% older than 100 (if sourced) support the mechanism, but they do not
prove the counterfactual. The previous M6 asked for “consistent with” and a declining-profile run.
Only the growth-curve part was softened. Rewrite the four sentences to “consistent with the cost of
the flat-flow rule” or run a declining-profile schedule at the same land base and report the
difference. The abstract should also say “an upper bound of 7.07”, not “the curves imply 7.07” as if
it were a sustainable yield.

### 2.9 “Dominates every other lever” and “a third” are still overgeneralized (V9)

Results: “The discount rate dominates every other lever” (`text/3_results.tex:78`). The composition
lever is not in Table 3, and a 10% share removes 38% of volume; if margins are constant, that is
roughly a 38% NPV effect, comparable to the 46% NPV effect of moving the discount rate from 3% to
5% (`4,010/8,779 = 0.457`). The discount rate dominates the *economic constants*, not every lever.
Rewrite: “Among the economic constants, the discount rate dominates.”

Discussion: “A policy analyst who looks at the schedule will find that it costs a third of the
harvest” (`text/4_discussion.tex:51-54`). The table gives 23% at 8%, 38% at 10%, 59% at 15%, and
about zero at 6.2%. “A third” is only the 10% case. Rewrite with the actual points, or say “a ten
percent share costs about 38 percent; an eight percent share about 23 percent.”

### 2.10 The cover letter is stale (V10)

The cover letter still says:

- Title: “Tree-species diversification under forest fire risks: a two-level policy model for the
  Prince George Timber Supply Area” (`submission/cover-letter.md:14-15`). The manuscript title is
  “composition–production trade-offs and a calibrated fire scenario…”.
- “when a regional policy sets the harvest level and species targets” (17-19). The manuscript now
  says the composition aspiration is hypothetical and BC does not set a landscape target.
- “within 0.3 percent” (22-23). The manuscript says 0.32.
- “It makes three contributions” (19). The manuscript says fourfold.
- “show that it comes from the flat harvest-profile rule” (41-43). The manuscript says “consistent
  with” only in the upper-bound paragraph; the abstract still says “is the cost.”
- “The economic side is equally sharp: the discount rate dominates every market and biological
  parameter…” (32-34). The results says “every other lever” (also overbroad).

S10 is not fixed. A cover letter that describes a different paper is a submission-package defect.

### 2.11 Smaller numerical and presentation defects

- **173 vs 2.31 (SH2).** `text/3_results.tex:216-220` compares 173 m3/ha with 2.31 m3/ha/yr and calls
  it “about three quarters.” The correct comparison is 173/(2.31 × 102.2) = 0.734, i.e. 73% of the
  volume the maximum MAI accumulates over a 102-year rotation (236 m3/ha). The sentence is
  dimensionally wrong as written.
- **6.20 vs 6.18 (SH4).** `text/99_online_supplement.tex:108` says 6.20; `summary.json:21` says 6.18.
  The main text’s 6.2 is fine; the supplement’s two-decimal value is not.
- **“Twice the level weight” (SH1).** `text/3_results.tex:118` says weight 200 is “twice the level
  weight”; the composition README names weight 200 but does not document a level weight of 100. The
  “500-fold increase over that run” is correct. Delete “twice the level weight” unless the run
  configuration documents it.
- **“The two searches behind the ceiling” (C4).** `text/4_discussion.tex:58-61` says the two
  composition-weight searches are “behind the ceiling.” The ceiling is from the aspen-maximisation
  run; the two weight runs support the supply-limit interpretation. Reword.
- **“Sits inside the historical spread” (C5).** `text/3_results.tex:196-198` compares 680/435 ha per
  ignition to a historical mean of 512.9 ha, not a spread. Either give a historical interval or say
  “the grown area is above the historical mean and the applied area below it.” Also say “ending
  standing volume” at line 196.
- **Rotation quantiles (C3).** `scripts/rotation.py:77-83` uses `np.median` and `np.quantile`, which
  are unweighted, while the mean is area-weighted. The manuscript says “area-weighted mean rotation”
  and then “median 100, p10–p90 60–160” without saying the quantiles are unweighted. Either weight
  them or state it.

---

## 3. Focused checks requested

### 3.1 Composition table arithmetic and wording

- 6%: 3.20/0.06 = 53.33; table 53.3; mean 5.33. Arithmetic correct, feasible level wrong (V2).
- 8%: 3.20/0.08 = 40.0; mean 4.00. Correct.
- 10%: 3.20/0.10 = 32.0; mean 3.20. Correct.
- 15%: 3.20/0.15 = 21.33; table 21.3; mean 2.13. Correct.
- The constant-supply assumption is now stated in the text and caption
  (`text/3_results.tex:127-128,136-138`). Good.
- The absolute target is now disclosed (`text/3_results.tex:115-118`). Good.
- The weights are 200 and 100,000; the 500-fold increase is over the 200 run. Correct, except
  “twice the level weight” (SH1).
- The 100,000 run’s level is 5.16, stated. Good.
- The caption’s “A six percent share is feasible at the sustained level” is true only if the table’s
  6% row is 51.9, not 53.3. The row and caption contradict. Must fix.

### 3.2 Fire table and abstract

- Statistics claimed inside the historical interval: median (23.8 vs 20.85–30.16), p90 (361.5 vs
  349.13–1,051.26), share above 500 (8.3 vs 7.6–12.5). All inside, but p90 and share above 500 are
  at the lower edge. The abstract and results say “reproduces”; “consistent with, at the lower edge”
  is more accurate (V4).
- Statistics below the interval: p95 (1,100.9 vs 1,415.35–2,955.33), share above 1,000 (5.5 vs
  5.8–10.2), share above 5,000 (1.8 vs 1.9–4.4). The text says “at or just below the lower edge.”
  Accurate.
- Maximum: table says “one-sided”; text says reported for completeness, not a target. Correct.
  The P3.3 report is stale (SH3).
- n and bootstrapping: table caption states 3,450 fires and not bootstrapped. Correct.
- The methods’ “never report an absolute fire size as a result” contradicts the absolute values in
  the abstract/table (V4). Fix the sentence.

### 3.3 Risk claim

- Current wording is an unsupported result claim, not a promise or method statement (V1).
- The register says `pending` (`notes/claims-register.md:99`).
- The code’s metric is a 20% lower-tail CVaR of ending standing volume, valued at a constant
  59.99 CAD/m3 (`run_ensemble.py:41,87-104,315-322`). The manuscript does not state 20% or 59.99.
- If the ensemble never lands: remove the risk claim from the abstract, contribution, discussion, and
  conclusion; remove the fourth contribution; keep the composition/fire-calibration results. The
  paper can still be honest and publishable, but the risk promise must go.

### 3.4 Methods against code

- Goal-program description: fixed (`text/2_methods.tex:54-81`). No absolute-deviation equation; one-
  sided penalties and even-flow term described.
- Flat-level plateau: fixed (`text/2_methods.tex:97-104`; `text/3_results.tex:16-20`).
- Fire scenario limits: mostly fixed (`text/2_methods.tex:132-142`; `text/4_discussion.tex:140-142`).
  Missing the “coverage is by tile, not cell” sentence, but “not a Monte Carlo of the estate” covers
  the main point.
- Price mapping: fixed (`text/2_methods.tex:146-150`; `valuation.py:18-26`).
- API commit: fixed (`text/2_methods.tex:135-136`; `text/6_declarations.tex:9`).
- Remaining: risk metric underspecified (V5); “every headline result … fire-weather initialisation”
  false (V5); stumpage “grades 1 and 2” condition not implemented (code applies 0.50 to all
  deciduous); “net present value” is an operating margin (SH6).

### 3.5 RQs and contribution

- RQ1–RQ4 are all answered in the results: level (`text/3_results.tex:14-36`), composition (113-155),
  rotation (202-220), fire distribution and coupling (157-200). Good.
- The contribution’s fourth item adds a “paired volume-at-risk comparison of two schedules”
  (`text/1_introduction.tex:79-80`) that no RQ asks for and no result reports. The contribution list
  does not match the delivered content. Remove the paired comparison or add a fifth RQ and a results
  subsection.
- The results say the fire scenario “is not used to rank composition scenarios”
  (`text/3_results.tex:154-155`), while the contribution and discussion say a paired comparison of
  two schedules exists. These cannot both be true. Decide which paper this is.

### 3.6 Claims register

- `Volume-at-risk by policy … pending` (`notes/claims-register.md:99`) is the honest status and the
  strongest evidence that V1 is a real defect.
- Dead paths: `tsa24-thlb.md`, `tsa24-yield-reconciliation.md` (`notes/claims-register.md:18-24`).
- False artifact citations: 101.7 and 44% to `rotation.json` (79-80; artifact lacks both).
- Missing rows: 1,037.9, 680/435, 25%, 2.5%, 8.35/7.35, 10,000, full historical fire table.
- Stale rows: benchmark fixture rows 40-43, 49, 56-57.
- The register line 71 says “6 percent is feasible at the sustained level”; the table’s 6% row is
  53.3. The row is a claim, not a number, but it inherits V2.

---

## 4. Is it submittable now?

**No.** The paper is much closer than the previous version: the CVaR-of-NPV error is gone, the RQs
are answerable, the methods mostly match the code, the fire table is fixed, and the limitations are
nine instead of five. But it still claims a volume-at-risk result that is not in the paper, and its
composition table still contains an infeasible 6% row. Those are not copy-edits; they are
claim-and-evidence failures.

Conditions for a submittable version:

1. **The ensemble lands and a risk subsection is added**, with draws, schedules, the 20% tail, the
   59.99 CAD/m3 conversion, and the paired difference; or the risk claim is removed from the
   abstract, contribution, discussion, and conclusion, and the paper is reframed as a
   composition/fire-calibration case study.
2. **The composition table’s 6% row is fixed** (51.9 flow-limited or the 6.18 aspen-max point), and
   the caption no longer says a 53.3 level is feasible at 51.9.
3. **The rotation artifact contains 101.7 and 44%**, or those claims are removed.
4. **The register is cleaned**: dead paths removed, 101.7/44% resolved, missing rows added, benchmark
   rows archived.
5. **The supplement’s 61.74 sentence is fixed** to 35–40, or the 61.74 source is restored.
6. **The fire wording is fixed**: “consistent with, at the lower edge” instead of “reproduces”; the
   “never report an absolute fire size” sentence rewritten.
7. **The flow-rule and discount-rate overclaims are softened**: “consistent with” and “among the
   economic constants”; “a third” replaced with the 8/10/15 points.
8. **The cover letter is rewritten** to the current title, “two-layer scenario analysis”, 0.32%,
   four contributions, and no flow-rule assertion.
9. **The funding TODO and author decisions are resolved.**

If items 1 and 2 are not fixed, the paper should not be sent out. If they are fixed, the remaining
items are a normal revision pass, not a rejection.

## 5. Rewrite order

1. Decide the risk claim: land the ensemble and write the results subsection, or remove the claim and
   the fourth contribution. (V1)
2. Fix the composition table’s 6% row and caption. (V2)
3. Extend `rotation.json` with the aspen-max rotation and the 44% share, or remove those claims. (V3)
4. Fix the fire wording and the absolute-size sentence. (V4)
5. Fix the methods’ sensitivity sentence and specify the risk metric’s 20% tail and 59.99 margin. (V5)
6. Clean the register: dead paths, missing rows, stale benchmark rows. (V6)
7. Fix the supplement’s 61.74 sentence and the 6.20/6.18 value. (V7, SH4)
8. Soften the flow-rule attribution in abstract/results/discussion/conclusion. (V8)
9. Fix the discount-rate and “a third” overgeneralizations. (V9)
10. Rewrite the cover letter. (V10)
11. Fix the smaller numerical/presentation items: 173/2.31, “twice the level weight”, P3.3 report,
    license/composition code, road-cost limitation, figures, length, empty acknowledgements. (SH1–SH8,
    C1–C5)
12. Re-run this verification.

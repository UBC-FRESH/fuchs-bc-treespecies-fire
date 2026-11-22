# Audit pass 5: final verification

Date: 2026-11-22
Manuscript: `fuchs-bc-treespecies-fire`, HEAD `0c47093` (W2.5 remove unsupported risk claims and fix
the revision audit findings)
Code of record: `fresh-fuchs-ws4`, rotation artifacts at `2e79fed`; fire API at `9918fb17`, handoff
summaries at `474dca6e`
Scope: current `main.tex` and all `text/*.tex`; `review/AUDIT-04-REVISION.md`;
`review/AUDIT-04-RESPONSE.md`; the code artifacts named by the paper; the current claims register and
cover letter.
Method: verify V1–V10 against the manuscript, not the response; check the composition table
arithmetic; check the fire claims against the table and the P3.3 report; check the flow-rule caveat
against the categorical sentences; check the register and cover letter. No manuscript file was
edited.

## Verdict

**Still has must-fix items, but they are a short text/record pass — no new modelling.** The revision
fixes the big problems from AUDIT-04: the volume-at-risk claim is gone, the 6% row is removed, the
rotation artifacts now contain 44.1% and 101.7, the fire table and abstract are precise about the
p90 lower edge, the flow-rule attribution is explicitly an interpretation, and the cover letter is
current. The paper is close.

What remains are five concrete issues, none requiring new analysis:

1. The results still say 173 m3/ha is “about three quarters of the … maximum mean annual increment of
   2.31 m3/ha/yr” — a stock compared to a flow. The intended ratio is 173/(2.31 × 102.2) = 0.734,
   i.e. 73% of the 236 m3/ha accumulated over a rotation.
2. Three sentences still assert the flow-rule attribution categorically (“is the cost”, “is a
   flow-rule cost”) after the paper says it is an interpretation.
3. The register still cites two missing notes for the land-base and yield numbers, and the 10,000
   even-flow weight row cites a README that does not contain 10,000. The share-above-100 row cites
   the wrong note, and the simulated 100/1,000 rows are missing.
4. The data-availability statement says the composition code and species-period tables are in the
   repository; they are not.
5. The reported “net present value” excludes road construction, administration, taxes, and risk
   premia, and the limitations do not say so.

These are “fix before submission” items, not “reject” items. After them, the paper is submittable
with minor edits (figures, 6.20 vs 6.18, “twice the level weight”, “rotation invariant”, “reproduces”
p90, “sits inside the historical spread”, “ending volume”, and the funding/author housekeeping).

## Severity table

| ID | Severity | Finding | Main location |
| --- | --- | --- | --- |
| F1 | **Must fix** | 173 m3/ha is compared to 2.31 m3/ha/yr and called “about three quarters.” A stock is compared to a flow; the intended ratio is 173/(2.31 × 102.2) = 0.734, i.e. 73% of the 236 m3/ha accumulated over a 102-year rotation. | `text/3_results.tex:217-221` |
| F2 | **Must fix** | The paper says the flow-rule attribution is an interpretation, then asserts it categorically in three places: “the difference is the cost”, “the difference is the cost of the rule we imposed”, “the gap … is a flow-rule cost.” | `text/3_results.tex:33-34`; `text/4_discussion.tex:36-37,157-158` |
| F3 | **Must fix** | The register still cites `tsa24-thlb.md` and `tsa24-yield-reconciliation.md`, which do not exist in `fresh-fuchs-ws4/notes/reference/`. The 10,000 even-flow weight row cites `experiments/tsa24-evenflow/README.md`, which does not contain 10,000. The share-above-100 row cites `fire-tail-uncertainty.md`, which has the count but not the 26.2%/22.7–29.6 interval; the P3.3 report has it. Simulated share above 100 (23.6) and 1,000 (5.5) are in the table but not the register. | `notes/claims-register.md:18-24,30,98,103`; `experiments/tsa24-evenflow/README.md:12-27`; `notes/reference/fire-tail-uncertainty.md:24-35` |
| F4 | **Must fix** | The data-availability statement says “the analysis code, the derived species-period tables, the composition runs, and the summary files are held in the project repository.” `experiments/tsa24-composition/` contains README.md, summary.json, and rotation-aspen-max.json only — no run script and no species-period tables. | `text/6_declarations.tex:16-18`; `text/99_online_supplement.tex:129-132`; `experiments/tsa24-composition/` |
| F5 | **Must fix** | “Net present value” is computed from log revenue less harvest, haul, silviculture, and stumpage only. Road construction, administration, taxes, and risk premia are excluded, and the limitations do not say so. The number is an operating margin, not a full NPV. | `text/2_methods.tex:145-155`; `text/4_discussion.tex:109-144` |
| S1 | Should fix | “With the composition weight at 200, twice the level weight” is not documented. The composition README names weight 200 but no level weight; the 500-fold increase over the 200 run is supported. | `text/3_results.tex:118-120`; `experiments/tsa24-composition/README.md:20-26` |
| S2 | Should fix | “The rotation is essentially invariant to the composition target” and “evidence that the implied rotation is invariant to composition” generalize from one alternative schedule, the aspen-maximisation run (no level target), not a composition target at the sustained level. Say “between the baseline and aspen-maximisation schedules.” | `text/3_results.tex:213-215`; `text/4_discussion.tex:69-73`; `text/1_introduction.tex:78`; `submission/cover-letter.md:32-34` |
| S3 | Should fix | The abstract and results say the p90 is at the lower edge, but the methods and discussion still say the regime “reproduces” the p90 inside the interval, and the results then says “the central distribution is therefore reproduced.” Align the wording: “consistent with, at the lower edge.” | `text/2_methods.tex:130-132`; `text/3_results.tex:160-163`; `text/4_discussion.tex:81-83`; `text/5_conclusion.tex:18` |
| S4 | Should fix | The supplement’s composition table says the aspen-maximisation share is 6.20%; `summary.json` records 6.18%. The main text’s 6.2 is fine; the supplement’s two-decimal value is overprecise. | `text/99_online_supplement.tex:107`; `experiments/tsa24-composition/summary.json:21` |
| S5 | Should fix | “Against a historical mean of 512.9 hectare; the scenario sits inside the historical spread” compares 680/435 ha per ignition to a mean, not a spread. Say “the grown area is above the historical mean and the applied area below it”, or give an interval. Also say “ending standing volume” rather than “ending volume.” | `text/3_results.tex:196-198` |
| S6 | Should fix | The methods says deciduous stumpage is 0.50 CAD/m3 “for deciduous timber in grades 1 and 2”; the code applies 0.50 to all deciduous volume. Say “the grade 1–2 rate applied to all deciduous volume.” | `text/2_methods.tex:153-154`; `scripts/valuation.py:138-153` |
| S7 | Should fix | “Our result qualifies that finding rather than contradicting it” still implies the paper tested the European finding. The paper establishes a supply precondition; it does not test whether diversification buffers severe events. | `text/4_discussion.tex:95-105` |
| S8 | Should fix | Figures 2–4 are still missing; the discussion is 1,539 words against the 900-word plan target; the abstract is 294 against 250; the supplement is inside the main PDF; the acknowledgements file is empty but included; the 2017 rationale URL does not print; unused bib entries remain; rotation quantiles are unweighted. | `planning/paper-plan.md:51-70`; `main.tex:47`; `text/9_acknowledgements.tex`; `main.bbl:15-21` |
| S9 | Should fix | The declarations assert WS4 is “released under the Apache License 2.0”; the project repository has no `LICENSE` file and its README says “Choose and add a license before the first public release.” Verify the upstream WS4 license or remove the claim. | `text/6_declarations.tex:9`; `fresh-fuchs-ws4/README.md:47` |
| S10 | Should fix | The funding TODO and author decisions (order, journal) remain. They are not visible in the PDF, but they are pre-submission housekeeping. | `text/6_declarations.tex:30`; `submission/cover-letter.md:3-8` |
| C1 | Consider | The title still says “under forest fire risks” and the keywords still say “fire risk”, although the paper explicitly does not report a policy risk ranking. “Fire scenario” would match the delivered content. | `main.tex:23`; `text/0_abstract.tex:30-31` |
| C2 | Consider | The P3.3 report still says the maximum “sits inside” the historical interval and the regime “reproduces … the maximum,” while the manuscript correctly says the maximum interval is one-sided and not used. Update the source record. | `notes/reports/p3-3-distribution-comparison.md:28,32-33,50-51`; `text/3_results.tex:164-166`; `notes/claims-register.md:106` |
| C3 | Consider | The 2017 Prince George rationale is cited, but its URL does not print in the bibliography; a reader cannot reach the source of the 8.35/7.35 values from the reference list. Add a note or use a `@misc` entry that prints the URL. | `references.bib:181-188`; `main.bbl:15-21` |
| C4 | Consider | The rotation mean is area-weighted, but the median and p10–p90 are unweighted (`rotation.py` uses `np.median`/`np.quantile` on intervals). State that, or weight the quantiles. | `scripts/rotation.py:77-83`; `text/3_results.tex:207-208` |

---

## 1. Per-item verification of AUDIT-04 (V1–V10)

| Item | Status | Evidence and current location |
| --- | --- | --- |
| V1 Volume-at-risk claimed without a result | **Fixed** | No volume-at-risk result is claimed. Abstract: “The fire process is a scenario; the paper does not report a policy risk ranking” (`text/0_abstract.tex:23`). Intro: no policy risk ranking; composition not varied in the fire run (`text/1_introduction.tex:52-54`); “A policy risk ranking is not claimed” (81). Methods: scope statement (`text/2_methods.tex:83-86`); paired ensemble “not reported here” (141). Discussion: “No policy risk ranking is reported; volume-at-risk … and NPV-at-risk are natural extensions” (`text/4_discussion.tex:91-93`). Conclusion: fire “used as a scenario” (`text/5_conclusion.tex:8`). Register: the policy risk ranking is marked not reported and not claimed (`notes/claims-register.md:109`). |
| V2 Infeasible 6% row | **Fixed** | The 6% row is removed; the text says 6% needs 3.11 M m3/period, below the 3.20 ceiling, so it is feasible at the sustained level and not a binding row (`text/3_results.tex:131-133`). Table 4 reports 8, 10, 15% with “Maximum total level” (`text/3_results.tex:137-148`). Arithmetic: 8% → 3.20/0.08 = 40.0; 10% → 32.0; 15% → 21.3. The 6% arithmetic 0.06 × 51.9 = 3.114, rounded to 3.11, below 3.20. Caption says 6% is feasible and not shown (137-139). |
| V3 Rotation artifact incomplete | **Fixed** | `rotation.json` now has `mean_years 102.1539` and `share_over_100_years 0.441077`; `rotation-aspen-max.json` has `mean_years 101.7187` and `share_over_100_years 0.441077` (`experiments/tsa24-evenflow/rotation.json`; `experiments/tsa24-composition/rotation-aspen-max.json`). Results cite both (`text/3_results.tex:204-211`); discussion cites the 92/44% to `rotation.json` (`text/4_discussion.tex:29-31`); supplement S5 cites both (`text/99_online_supplement.tex:119-125`); register cites both (`notes/claims-register.md:84-86`). |
| V4 Fire wording contradicts methods and overclaims p90 | **Mostly fixed** | Methods no longer says “never report an absolute fire size as a result”; it now says absolute values are reported beside the interval but not interpreted as predictions (`text/2_methods.tex:126-128`). Abstract is precise: median and share above 500 inside, p90 at lower edge, p95 and tails below (`text/0_abstract.tex:20-22`). Results says the same (160-162). Residual: results then says “the central distribution is therefore reproduced” (163); methods says “reproduces … the 90th percentile … inside” (130-132); discussion says “reproduces … the 90th percentile … inside” (81-83); conclusion says “reproduces the central historical distribution” (18). The p90 is at the lower edge of 349.13–1,051.26. This is a wording alignment issue (S3), not a data error. |
| V5 False sensitivity sentence; risk metric underspecified | **Fixed** | Methods now limits sensitivity to the three economic constants and says the fire scenario uses one weather season and is not a sensitivity axis (`text/2_methods.tex:159-162`). The risk-metric paragraph is replaced by a scope statement; no volume-at-risk/NPV-at-risk metric is defined or reported (`text/2_methods.tex:83-86`). |
| V6 Register paths and missing rows | **Partly fixed** | Rows were added for total volume (`notes/claims-register.md:27`), 25% (28), 2.5% (29), even-flow weight/penalties (30-31), 8.35/7.35 (32), per-ignition areas (108), and the full historical fire table (98-100). But: `tsa24-thlb.md` and `tsa24-yield-reconciliation.md` are still cited (18-24) and still absent from `fresh-fuchs-ws4/notes/reference/`; the 10,000 weight row cites `experiments/tsa24-evenflow/README.md` (30), which does not contain 10,000; the share-above-100 row cites `fire-tail-uncertainty.md` (98), which has the count but not the 26.2/22.7–29.6 interval; simulated share above 100 (23.6) and 1,000 (5.5) are in Table 5 but not the register (103 covers only 500 and 5,000); stale benchmark rows remain (47-49, 55, 62-63). |
| V7 Supplement price range | **Fixed** | Supplement now says “the documented 35 to 40 CAD/m3 range” (`text/99_online_supplement.tex:90-91`), matching the main text (`text/3_results.tex:83-86`) and register (`notes/claims-register.md:67`). |
| V8 Flow-rule and discount overclaims | **Partly fixed** | The caveat is added: abstract 12-14 (“The attribution is an interpretation; a declining-profile counterfactual is not run”), intro 74-75, discussion 31-32. The discount sentence is qualified: “Among the economic constants, the discount rate dominates” (`text/3_results.tex:78`); “a ten percent share costs about 38%” (`text/4_discussion.tex:55-56`). But three categorical sentences remain: results 33-34 (“The difference … is the cost”), discussion 36-37 (“the difference is the cost of the rule we imposed”), discussion 157-158 (“the gap … is a flow-rule cost”). These contradict the “interpretation” caveat (F2). |
| V9 “Dominates every other lever” / “a third” | **Fixed** | Results 78 now says “Among the economic constants…”; discussion 55-56 says “a ten percent share costs about 38 percent.” The “a third” overgeneralization is gone. The residual “flow-rule cost” is F2, not V9. |
| V10 Cover letter stale | **Fixed** | Current title (`submission/cover-letter.md:14-16`); four contributions (19); 0.32% (22); 5.4–6.2 and 38% (27-30); fire claims with p90 lower edge (36-39); no policy risk ranking and no NPV-at-risk (39-40); flow-rule attribution as interpretation (23-25). |

---

## 2. New findings / residual issues

### 2.1 The 173 m3/ha sentence is dimensionally wrong (F1)

`text/3_results.tex:217-221`:

> “At a 102-year rotation over 3.06 M ha, about 30,000 ha are harvested each year; at 5.19 M m3/yr
> that is 173 m3/ha, a merchantable volume that is about three quarters of the area-weighted maximum
> mean annual increment of 2.31 m3/ha/yr.”

173 m3/ha is a stock; 2.31 m3/ha/yr is a flow. The ratio 173/2.31 = 74.9, which is not “three
quarters.” The intended comparison is:

- 2.31 m3/ha/yr × 102.2 years = 236 m3/ha;
- 173/236 = 0.734, i.e. 73%.

Rewrite: “At a 102-year rotation over 3.06 M ha, about 30,000 ha are harvested each year; at
5.19 M m3/yr that is 173 m3/ha, about 73% of the 236 m3/ha that the maximum MAI of
2.31 m3/ha/yr would accumulate over a 102-year rotation.”

This is a one-line fix, but it is a quantitative error in the results and would be caught by a
referee.

### 2.2 The flow-rule attribution is still categorical in three places (F2)

The paper now says the attribution is an interpretation:

- Abstract 12-14: “The attribution is an interpretation; a declining-profile counterfactual is not
  run.”
- Intro 74-75: “as an interpretation rather than a tested counterfactual.”
- Discussion 31-32: “a declining-profile counterfactual is not run, so the attribution is an
  interpretation.”

Then:

- Results 32-34: “The difference between that bound and the realized level **is the cost** of holding
  a constant profile…”
- Discussion 36-37: “and the difference **is the cost** of the rule we imposed.”
- Discussion 157-158: “The gap between the model's sustained level and the official cut **is a
  flow-rule cost**…”

A referee will see the caveat and the categorical sentence in the same paragraph and ask which is
the claim. Rewrite the three sentences to “is consistent with the cost” or “we interpret the
difference as the cost.” The conclusion (“we attribute the gap to a flat harvest profile”) is fine;
“attribute” is a claim about interpretation, not a proof.

### 2.3 The register still has dead paths and two wrong artifact citations (F3)

The response says “External notes are prefixed `fresh-fuchs-ws4:`.” The prefix does not create the
files. `fresh-fuchs-ws4/notes/reference/` contains only:

```
economics-constants.md
economics-sensitivity.md
fire-tail-uncertainty.md
issue-tree-manifest.md
tsa24-estate.md
```

`tsa24-thlb.md` and `tsa24-yield-reconciliation.md` are cited at `notes/claims-register.md:18-24`
and do not exist. Those rows carry the central land-base numbers (5,899,680; 3,060,473; 2,839,207;
−9,828; −0.32%) and the central yield numbers (2.309; 7.07). The supplement S1 gives the area table
and the 2017 rationale gives the published THLB, but the 3,060,473 derivation and the 2.309 MAI
derivation are not in the repository. The paper's own rule is “Every number cites an artifact”
(`AGENTS.md:18-19`). Create the two notes with the derivations, or change the rows to the actual
artifact (the compiled dataset plus the `IFM(managed)` rule for the area; the compiled curves plus
the area-weighting for the MAI).

The 10,000 row (`notes/claims-register.md:30`) cites
`experiments/tsa24-evenflow/README.md`, which contains the six-seed table and the penalties 1.3–2.7 /
515 but **not** 10,000. The supplement says “weight 10,000”
(`text/99_online_supplement.tex:53`). Either commit the run configuration that contains the weight,
or remove the 10,000 claim from the supplement. A row that cites a file not containing the number is
not a citation.

The share-above-100 row (`notes/claims-register.md:98`) cites
`notes/reference/fire-tail-uncertainty.md`; that note has the count (113 fires above 100 ha) but not
the percentage 26.2% or the interval 22.7–29.6. The P3.3 report has both
(`notes/reports/p3-3-distribution-comparison.md:24`). Change the artifact to P3.3.

The table also reports simulated share above 100 (23.6%) and 1,000 (5.5%)
(`text/3_results.tex:183,185`), but the register’s simulated row covers only 500 and 5,000
(`notes/claims-register.md:103`). Add the two values or remove them from the table.

The stale benchmark rows (`notes/claims-register.md:47-49,55,62-63`) are marked superseded or
`provenance unverified`; they are not in the manuscript. Remove them or move them to an archive
section. This is register hygiene, not a manuscript blocker.

### 2.4 The composition code and species-period tables are still absent (F4)

`text/6_declarations.tex:16-18` says:

> “The schedules, the derived species-period tables, the sensitivity runs, and the analysis code that
> produce every number in this paper are held in the project repository…”

`text/99_online_supplement.tex:129-132` says the same for “the analysis code, the derived
species-period tables, the composition runs, and the summary files.”

`experiments/tsa24-composition/` contains:

```
README.md
summary.json
rotation-aspen-max.json
```

There is no composition run script and no species-period table for the composition runs. The
rotation script exists (`scripts/rotation.py`); the valuation (`scripts/valuation.py`) and fire
(`experiments/p3-fire/run_scenario.py`) scripts exist. The composition runs (5.69%, 5.94%, 3.20)
are not reproducible from the summary alone. Add the script and the species-period tables, or
soften the claim to “the summary files and the rotation artifacts are held in the repository; the
composition run configuration is available from the authors.” A false data-availability claim is a
submission-package defect.

### 2.5 The NPV excludes road construction and other costs (F5)

The methods lists log revenue less harvest, haul, silviculture, and stumpage
(`text/2_methods.tex:145-155`). It does not mention road construction, administration, taxes, or
risk premia. The limitations list nine items and do not mention them either
(`text/4_discussion.tex:109-144`). The reported 8,779 M CAD is an operating margin, not a full
forest-gate NPV. A forest-economics referee will ask for the exclusions, especially road
construction, which is a major BC cost and is explicitly unsourced in the code notes
(`notes/reference/economics-constants.md:121-124`). Add one sentence to the methods and one to the
limitations: “The NPV is an operating margin: it excludes road construction, administration, taxes,
and risk premia.” This is a text fix, not a new analysis.

### 2.6 Minor residuals (S1–S10)

- **“Twice the level weight” (S1).** `text/3_results.tex:118` says weight 200 is “twice the level
  weight.” The composition README names weight 200 but does not document a level weight of 100. The
  “500-fold increase over that run” is correct. Delete “twice the level weight” or document the level
  weight.
- **“Rotation invariant” (S2).** The evidence is baseline vs aspen-maximisation, not a composition
  target at the sustained level. Rewrite “the rotation is essentially invariant to the composition
  target” (`text/3_results.tex:213-215`), “evidence that the implied rotation is invariant to
  composition” (`text/1_introduction.tex:78`), and “Diversification does not require a different age
  at harvest” (`text/4_discussion.tex:69-73`) as “between the baseline and aspen-maximisation
  schedules.” The cover letter repeats the broad claim (`submission/cover-letter.md:32-34`).
- **“Reproduces” p90 (S3).** The abstract and results say p90 at lower edge; methods/discussion say
  “reproduces … inside”; results line 163 says “central distribution is therefore reproduced.” Align
  to “consistent with, at the lower edge.”
- **6.20 vs 6.18 (S4).** `text/99_online_supplement.tex:107` says 6.20%; `summary.json:21` says 6.18%.
  Use 6.18 or 6.2.
- **“Sits inside the historical spread” (S5).** `text/3_results.tex:196-198` compares 680/435 ha per
  ignition to a historical mean of 512.9 ha. A mean is not a spread. Say “the grown area is above the
  historical mean and the applied area below it,” or give a historical interval. Also “ending
  standing volume.”
- **Stumpage grades (S6).** `text/2_methods.tex:153-154` says 0.50 “for deciduous timber in grades 1
  and 2”; `scripts/valuation.py:151-153` applies 0.50 to all deciduous. Say “the grade 1–2 rate
  applied to all deciduous volume.”
- **“Qualifies” the European finding (S7).** `text/4_discussion.tex:98` says “Our result qualifies
  that finding rather than contradicting it.” The paper establishes a supply precondition; it does
  not test the European finding. Rewrite: “We do not test that finding; we establish a precondition
  that any such test on this estate must confront.”
- **Presentation (S8).** Figures 2–4 remain missing; the discussion is 1,539 words against the
  900-word plan target; the abstract is 294 against 250; the supplement is inside the main PDF; the
  acknowledgements file is empty but included; the 2017 rationale URL does not print; unused bib
  entries remain; rotation quantiles are unweighted. These are polish, not blockers.
- **License (S9).** The declarations assert WS4 is Apache 2.0; the project repo README says “Choose
  and add a license before the first public release.” Verify the upstream WS4 license or remove the
  claim.
- **Funding TODO (S10).** `text/6_declarations.tex:30` still has a `% TODO` comment. It is not in the
  PDF, but it is a pre-submission housekeeping item, along with author order and journal choice.

### 2.7 Consider

- **Title/keyword “fire risk” (C1).** The paper does not report a policy risk ranking. The title’s
  “under forest fire risks” and the keyword “fire risk” are broader than the delivered content; the
  subtitle “a calibrated fire scenario” is closer. A referee might not object, but “fire scenario”
  would be more precise.
- **P3.3 report stale on the maximum (C2).** The report still says the maximum “sits inside” and the
  regime “reproduces … the maximum” (`notes/reports/p3-3-distribution-comparison.md:28,32-33,50-51`),
  while the manuscript correctly says the maximum interval is one-sided and not used. Update the
  source record so the paper and its citation agree.
- **2017 rationale URL (C3).** The `@techreport` entry has a URL, but `main.bbl:15-21` does not print
  it. Add a `note` or use `@misc` so a reader can reach the 8.35/7.35 source.
- **Rotation quantiles (C4).** The mean is area-weighted, but the median and p10–p90 are unweighted.
  State it or weight them.

---

## 3. What is now clean

- The volume-at-risk/NPV-at-risk claim is gone. The paper consistently says it does not report a
  policy risk ranking (`text/0_abstract.tex:23`; `text/1_introduction.tex:52-54,81`;
  `text/2_methods.tex:83-86,141`; `text/4_discussion.tex:91-93`; `text/5_conclusion.tex:8`;
  `notes/claims-register.md:109`).
- The 6% composition row is removed; 3.11 < 3.20 is stated; Table 4 reports 8/10/15 under “Maximum
  total level” (`text/3_results.tex:131-148`).
- The rotation artifacts now contain 102.15/101.72 and 44.1%; the paper, supplement, and register
  cite both (`rotation.json`; `rotation-aspen-max.json`; `text/3_results.tex:204-211`;
  `text/99_online_supplement.tex:119-125`; `notes/claims-register.md:84-86`).
- The fire table has n = 3,450, not bootstrapped, shares above 100/500/1,000/5,000, and the maximum
  marked one-sided (`text/3_results.tex:168-190`). The abstract is precise about the p90 lower edge
  (`text/0_abstract.tex:20-22`).
- The flow-rule interpretation caveat is in the abstract, intro, and discussion
  (`text/0_abstract.tex:12-14`; `text/1_introduction.tex:74-75`; `text/4_discussion.tex:31-32`).
- The cover letter is current: title, four contributions, 0.32%, 5.4–6.2, 38%, no policy risk
  ranking, flow-rule interpretation (`submission/cover-letter.md:14-40`).
- No undefined references; 0 overfull boxes; 25 pages. Only three underfull hbox warnings
  (`main.log:613,619,626`).

## 4. Submittability

**Still has must-fix items, but they are a short text/record pass — no new analysis.** The remaining
must-fix list is:

1. Fix the 173 m3/ha sentence (F1).
2. Replace the three categorical flow-rule sentences with “consistent with” or “we interpret as”
   (F2).
3. Fix the register’s dead paths, the 10,000-weight citation, the share-above-100 artifact, and the
   missing simulated 100/1,000 rows (F3).
4. Add the composition script/species-period tables, or soften the data-availability claim (F4).
5. Add the NPV-exclusion sentence to the methods and limitations (F5).

After those, the paper is submittable with minor edits. The should-fix list (S1–S10) is polish and
consistency: “twice the level weight,” “rotation invariant,” “reproduces” p90, 6.20 vs 6.18, “sits
inside the spread,” stumpage grades, “qualifies,” figures/length, license, funding. None of these
requires new modelling; they are a copy-edit and repository-hygiene pass.

The paper is not “submittable now” because F1 and F2 are text errors that a quantitative referee
would catch, and F3/F4 are evidence-trail defects under the paper’s own rule. But it is no longer a
“reject” or “major revision” case. The core claims — the estate validation, the composition
frontier, the rotation result, the fire calibration and coupling — are now consistent and supported.

## 5. Fix order

1. Fix the 173 m3/ha sentence (F1).
2. Replace the three categorical flow-rule sentences (F2).
3. Fix the register rows: create the missing notes or change the paths; correct the 10,000 citation;
   correct the share-above-100 citation; add simulated 100/1,000 rows (F3).
4. Add the composition script/species-period tables or soften the data-availability claim (F4).
5. Add the NPV-exclusion sentence (F5).
6. Fix the should-fix wording: “twice the level weight,” “rotation invariant,” “reproduces” p90,
   6.20 vs 6.18, “sits inside the spread,” stumpage grades, “qualifies” (S1–S7).
7. Produce figures 2–4, separate the supplement if the journal requires it, remove the empty
   acknowledgements include, print the 2017 URL, clean unused bib entries (S8, C2–C4).
8. Verify the Apache 2.0 claim, resolve the funding/author/journal decisions (S9–S10).
9. Re-run this verification.

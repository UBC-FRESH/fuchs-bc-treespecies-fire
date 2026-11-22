# Audit pass 6: final verification

Date: 2026-11-22
Manuscript: `fuchs-bc-treespecies-fire`, HEAD `7b6bfa3` (W2.6 fix the third audit findings)
Code of record: `fresh-fuchs-ws4`, `notes/reference/tsa24-thlb.md` and
`notes/reference/tsa24-yield-reconciliation.md` restored; rotation artifacts at `2e79fed`; fire API
at `9918fb17`, handoff summaries at `474dca6e`; paired ensemble now committed at
`experiments/p4-risk/ensemble.json`
Scope: current `main.tex` and all `text/*.tex`; `review/AUDIT-05-FINAL.md`;
`review/AUDIT-05-RESPONSE.md`; the claims register, cover letter, and the artifacts the paper cites.
Method: verify F1–F5 and S1–S4 against the manuscript, not the response; check the composition table
arithmetic; check the fire claims; check the register’s paths with `ls`; check the declarations
against `experiments/`. No manuscript file was edited.

## Verdict

**Submittable with minor edits. No blockers.** The revision fixes the substantive problems from
AUDIT-05: the 173 m3/ha sentence is now 73% of 236 m3/ha; the 6% row is gone and 3.11 < 3.20 is
stated; the rotation artifacts contain 102.15/101.72 and 44.1%; the fire table and abstract are
precise about the p90 lower edge and the one-sided maximum; the declarations and supplement now say
the composition run directories are on the work host; and the NPV exclusions are stated. The land-base
and yield notes are back in `fresh-fuchs-ws4/notes/reference/`, so the register’s two dead paths are
fixed. The cover letter is current.

What remains is a short SHOULD-FIX list (one categorical sentence in the results, one unsupported
“twice the level weight,” the intro/discussion rotation generalisation, a data-availability sentence
that still overclaims the baseline schedule and sensitivity runs, and one register row whose target
file is not on the branch) plus POLISH. None of these requires new modelling, and none is a
reproduction failure for the paper’s main results.

## Severity table

| ID | Severity | Finding | Main location |
| --- | --- | --- | --- |
| B0 | **Blocker** | None. The paper’s main claims are supported by committed artifacts; no claim depends on a missing analysis. | — |
| SH1 | SHOULD-FIX | The results still says “The difference … **is the cost** of holding a constant profile,” after the abstract/introduction/discussion say the attribution is an interpretation. Two of the three categorical sentences were changed; this one was not. | `text/3_results.tex:32-34`; contrast `text/0_abstract.tex:12-14`; `text/1_introduction.tex:74-75`; `text/4_discussion.tex:31-32,36-37,158` |
| SH2 | SHOULD-FIX | The introduction still says “evidence that the implied rotation is invariant to composition,” and the discussion still says “Diversification does not require a different age at harvest.” The results and cover letter were narrowed to “between the baseline and aspen-maximisation schedules”; the intro and discussion rotation subsection were not. | `text/1_introduction.tex:78`; `text/4_discussion.tex:69-73`; contrast `text/3_results.tex:213-215`; `submission/cover-letter.md:32-34` |
| SH3 | SHOULD-FIX | The declarations say “the baseline schedule … and the sensitivity runs are held in the project repository.” The baseline block-level schedule is not in `fresh-fuchs-ws4` (only `species_periods.csv`, `summary.json`, `rotation.json`); the model-schedule sensitivity runs are not a committed artifact (the `economics-sensitivity.md` note is the old 70 M fixture). The composition run directories are correctly caveated as work-host. | `text/6_declarations.tex:16-19`; `text/99_online_supplement.tex:129-132`; `experiments/tsa24-evenflow/`; `notes/reference/economics-sensitivity.md:5-17` |
| SH4 | SHOULD-FIX | The register’s 10,000 weight row cites “benchmark target `evenflow_tsa24.yaml` (`min_weight: 10000`).” No `evenflow_tsa24.yaml` exists on this branch (the WS4 source reports reference it under `config/ws4/targets/`, but the file is not committed). The row is marked `verified` against a file a reader cannot open. | `notes/claims-register.md:30`; `find . -name 'evenflow_tsa24.yaml'` returns nothing |
| SH5 | SHOULD-FIX | The paired ensemble has finished (`experiments/p4-risk/ensemble.json`, 5 draws, 6 ignitions) with a negative result: burned area varies 650–1,609 ha across draws, ending volume varies only in the third decimal of a percent. The manuscript still calls a paired ensemble a “natural extension” and “not reported here” (`text/2_methods.tex:141`; `text/4_discussion.tex:91-93`). The no-ranking claim is consistent, but the analysis is no longer future work. | `text/2_methods.tex:141`; `text/4_discussion.tex:91-93`; `experiments/p4-risk/ensemble.json` |
| P1 | POLISH | The results still says “With the composition weight at 200, **twice the level weight**.” The response says the level weight is 100; no committed run configuration documents it. The “500-fold increase over that run” is supported. | `text/3_results.tex:118-120`; `experiments/tsa24-composition/README.md:20-26` |
| P2 | POLISH | Methods and results say p90 at the lower edge, but the discussion still says “reproduces … the 90th percentile … inside,” and the results still says “the central distribution is therefore reproduced.” Align to “consistent with, at the lower edge.” | `text/4_discussion.tex:81-83`; `text/3_results.tex:163`; contrast `text/2_methods.tex:130-132`; `text/0_abstract.tex:20-22` |
| P3 | POLISH | The supplement’s composition table is now 6.18% (fixed). The only remaining stale number is the register’s benchmark-fixture rows (70 M m3, 151,518, 83,465, 12,248) marked superseded; they are not in the manuscript. | `notes/claims-register.md:47-49,55,62-63`; `text/99_online_supplement.tex:107` |
| P4 | POLISH | The P3.3 report still says the maximum “sits inside” the interval and the regime “reproduces … the maximum,” while the manuscript correctly says the maximum interval is one-sided and not used. Update the source record. | `notes/reports/p3-3-distribution-comparison.md:28,32-33,50-51`; `text/3_results.tex:164-166` |
| P5 | POLISH | The 2017 rationale URL does not print in `main.bbl`; the 8.35/7.35 values are cited but the reader cannot reach the source from the reference list. Add a `note` or use `@misc`. | `references.bib:181-188`; `main.bbl:15-21` |
| P6 | POLISH | Figures 2–4 are still missing; the discussion is 1,539 words against the 900-word plan target; the abstract is 294 against 250; the supplement is inside the main PDF; the acknowledgements file is empty but included. | `planning/paper-plan.md:51-70`; `main.tex:47`; `text/9_acknowledgements.tex` |
| P7 | POLISH | “Against a historical mean of 512.9 hectare; the scenario sits inside the historical spread” compares 680/435 ha per ignition to a mean, not a spread. Say “the grown area is above the historical mean and the applied area below it,” or give an interval. Also “ending standing volume” for 1,015.9. | `text/3_results.tex:196-198` |
| P8 | POLISH | The methods says 0.50 CAD/m3 “for deciduous timber in grades 1 and 2”; the code applies 0.50 to all deciduous volume. Say “the grade 1–2 rate applied to all deciduous volume.” | `text/2_methods.tex:153-154`; `scripts/valuation.py:151-153` |
| P9 | POLISH | “Our result qualifies that finding rather than contradicting it” still implies the paper tested the European finding. The paper establishes a supply precondition; it does not test whether diversification buffers severe events. | `text/4_discussion.tex:98` |
| P10 | POLISH | The title still says “under forest fire risks” and the keyword still says “fire risk”, although the paper explicitly does not report a policy risk ranking. “Fire scenario” would match the delivered content. | `main.tex:23`; `text/0_abstract.tex:30-31` |
| P11 | POLISH | The rotation mean is area-weighted, but the median and p10–p90 are unweighted. State it or weight them. | `scripts/rotation.py:77-83`; `text/3_results.tex:207-208` |
| P12 | POLISH | “The two searches behind the ceiling” is imprecise: the ceiling comes from the aspen-maximisation run, not the two composition-weight searches. | `text/4_discussion.tex:58-63` |
| P13 | POLISH | The restored `tsa24-yield-reconciliation.md` says “The curves carry the productivity the official determination assumes,” which is stronger than the manuscript’s “upper-bound consistency check, not a validation.” Align the note’s prose. | `notes/reference/tsa24-yield-reconciliation.md`; `text/3_results.tex:28-34` |
| P14 | POLISH | The declarations still assert WS4 is “released under the Apache License 2.0”; the project repository has no `LICENSE` file and its README says “Choose and add a license before the first public release.” Verify the upstream WS4 license or remove the claim. | `text/6_declarations.tex:9`; `fresh-fuchs-ws4/README.md:47` |
| P15 | POLISH | Funding TODO and author decisions (order, journal) remain. Not visible in the PDF, but pre-submission housekeeping. | `text/6_declarations.tex:30`; `submission/cover-letter.md:3-8` |

---

## 1. Per-item verification of AUDIT-05

### F1 — 173 m3/ha dimensional error

**Fixed.** `text/3_results.tex:219-221` now says:

> “173 m3/ha, a merchantable volume that is about 73 percent of the 236 m3/ha that the area-weighted
> maximum mean annual increment accumulates over a 102-year rotation.”

The arithmetic is right: 2.31 × 102.2 = 236.1 m3/ha; 173/236.1 = 0.733. The stock/flow error is
gone.

### F2 — Categorical flow-rule attribution

**Partly fixed.** Two of the three categorical sentences were changed:

- Discussion 36-37: “we interpret the difference as the cost of the rule we imposed.” Fixed.
- Discussion 157-158: “We interpret the gap … as a flow-rule cost.” Fixed.
- Results 32-34: “The difference between that bound and the realized level **is the cost** of holding
  a constant profile…” **Still categorical.** The abstract, introduction, and discussion all say the
  attribution is an interpretation; the results should say “we interpret the difference as the cost”
  or “the difference is consistent with the cost.” This is a one-line SHOULD-FIX, not a blocker.

### F3 — Dead register paths and wrong citations

**Mostly fixed.** The two restored notes exist:

```
fresh-fuchs-ws4/notes/reference/tsa24-thlb.md
fresh-fuchs-ws4/notes/reference/tsa24-yield-reconciliation.md
```

The register rows now point to them (`notes/claims-register.md:18-24`). The share-above-100 row now
points to P3.3 (`:98`), and the simulated shares row covers 100/500/1,000/5,000 (`:103`). The
remaining defect is the 10,000 weight row (`:30`), which cites `evenflow_tsa24.yaml`; no such file
exists on this branch. The stale benchmark-fixture rows (`:47-49,55,62-63`) remain, marked
superseded; they are register hygiene, not a manuscript defect.

### F4 — Composition code and tables absent

**Mostly fixed.** The declarations and supplement now say:

> “The baseline schedule, the derived species-period table, the composition summaries, the fire
> scenario record, the valuation and rotation code, and the sensitivity runs are held in the project
> repository. The composition run directories remain on the work host and are described in their
> summary.” (`text/6_declarations.tex:16-19`; `text/99_online_supplement.tex:129-132`)

The composition run directories are correctly caveated. Two items in that list are still not in the
repository:

- The baseline **block-level schedule** is not in `fresh-fuchs-ws4`; `experiments/tsa24-evenflow/`
  contains `species_periods.csv`, `summary.json`, `rotation.json`, and `README.md`, but no
  `schedule.csv`.
- The **model-schedule sensitivity runs** are not a committed artifact; the only sensitivity note,
  `notes/reference/economics-sensitivity.md`, is the old 70 M fixture (12,248 base, −250 haul,
  6,786 at 5%). The paper’s sensitivity values are reproducible from `scripts/valuation.py` and
  `species_periods.csv`, but the declaration says “runs.”

Fix: say “the derived species-period table, the composition summaries, the fire scenario record, and
the valuation and rotation code are in the repository; the baseline schedule and composition run
directories are on the work host and described in the summaries; the sensitivity values are
reproducible from the valuation code.” That matches the archive.

### F5 — NPV exclusions

**Fixed.** Methods now says: “The net present value is an operating margin: it excludes road
construction, administration, taxes, and risk premia”
(`text/2_methods.tex:154-155`). The limitation repeats it (`text/4_discussion.tex:134-135`).

### S1 — “Twice the level weight”

**Not fixed.** `text/3_results.tex:118` still says “With the composition weight at 200, twice the
level weight.” The response says the level weight is 100; no committed run configuration documents
it. The “500-fold increase over that run” is supported (`experiments/tsa24-composition/README.md:24-26`).
Either document the level weight or delete “twice the level weight.” This is POLISH, not a blocker:
the weight 200 is named and the 100,000 run is described.

### S2 — Rotation-invariance overgeneralisation

**Partly fixed.** Results 213-215 now says “between the baseline and aspen-maximisation schedules,”
and the cover letter says “between the two schedules.” But the introduction still says “evidence that
the implied rotation is invariant to composition” (`text/1_introduction.tex:78`), and the discussion
rotation subsection still says “Diversification does not require a different age at harvest”
(`text/4_discussion.tex:69-73`). The implications section does say “Between the two schedules”
(`:155`). Fix the intro and the rotation subsection to the same wording. SHOULD-FIX, one line each,
not a blocker: the aspen-max is the most diversified schedule, so the extreme comparison supports the
claim, but the wording should not generalise beyond the two schedules.

### S3 — p90 “reproduces” vs “lower edge”

**Partly fixed.** Methods 130-132 now says “places the median and the share above 500 inside the
interval and the 90th percentile at its lower edge.” The abstract is precise (`:20-22`). But the
results still says “the central distribution is therefore reproduced” (`:163`), and the discussion
still says “reproduces the historical median, the 90th percentile, and the share above 500 inside”
(`:81-83`). The p90 is inside the interval but at the lower edge; “consistent with, at the lower
edge” is the honest wording. This is POLISH, not a blocker: the table and abstract are transparent.

### S4 — Supplement 6.20 vs 6.18

**Fixed.** `text/99_online_supplement.tex:107` now says 6.18 percent; `summary.json:21` says 6.18.
Good.

---

## 2. New findings

### 2.1 The paired ensemble is finished, but the paper still calls it a “natural extension” (SH5)

`experiments/p4-risk/ensemble.json` now exists: 5 draws, 6 ignitions, horizon 200, two schedules
(`baseline`, `aspen-max`). The summary’s within-schedule volume variation is in the third decimal of
a percent; mean burned area is about 1,092 ha, with draw-level burned area varying 650–1,609 ha. The
task states this is the negative result that justifies reporting no policy risk ranking.

The manuscript says:

- Methods: “A paired ensemble across draws is the natural extension; it is not reported here.”
  (`text/2_methods.tex:141`)
- Discussion: “No policy risk ranking is reported; volume-at-risk across paired draws and
  net-present-value-at-risk are natural extensions…” (`text/4_discussion.tex:91-93`)

The no-ranking claim is consistent with the negative result. But the analysis is no longer future
work. Add one sentence in methods or discussion:

> “A paired ensemble of 5 draws and two schedules found burned area varying 650–1,609 ha across draws
> but ending volume varying only in the third decimal of a percent; we therefore do not report a
> volume-at-risk ranking.”

Or, if the authors prefer not to report the ensemble, change “natural extension” to “we do not report
a paired ensemble here.” Calling a completed null analysis a future extension is stale. This is
SHOULD-FIX, not a blocker: the paper’s claim is conservative and does not overstate a result.

### 2.2 The declarations still overclaim the baseline schedule and sensitivity runs (SH3)

The baseline block-level schedule is not in `fresh-fuchs-ws4`; the species-period table and summary
are. The sensitivity note is the old 70 M fixture; the model-schedule sensitivity values are
reproducible from `valuation.py` but are not a committed run. The composition run directories are
correctly caveated. Fix the sentence to match the archive. SHOULD-FIX, not a blocker: the derived
tables and code support the paper’s numbers, and the correction is one sentence.

### 2.3 The 10,000 weight row cites a file not on the branch (SH4)

`notes/claims-register.md:30` cites “benchmark target `evenflow_tsa24.yaml` (`min_weight: 10000`).”
`find . -name 'evenflow_tsa24.yaml'` returns nothing in this checkout. The WS4 source reports refer to
`config/ws4/targets/evenflow_tsa24.yaml` in the FEMIC instance, not in this repository. Either cite
the actual benchmark artifact (with a path that exists) or remove the 10,000 from the supplement.
SHOULD-FIX, not a blocker: the paper’s results do not depend on the exact even-flow weight, and the
six-seed plateau/penalties are documented.

### 2.4 What is now clean

- F1 fixed; F5 fixed; S4 fixed.
- The composition table has no 6% row; 3.11 < 3.20 is stated; 8/10/15 are under “Maximum total
  level” (`text/3_results.tex:131-148`).
- Rotation artifacts contain 102.15/101.72 and 44.1%; the paper, supplement, and register cite both
  (`rotation.json`; `rotation-aspen-max.json`; `text/3_results.tex:204-211`;
  `text/99_online_supplement.tex:119-125`; `notes/claims-register.md:84-86`).
- Fire table has n = 3,450, not bootstrapped, shares above 100/500/1,000/5,000, maximum one-sided
  (`text/3_results.tex:168-190`).
- The volume-at-risk/NPV-at-risk claim is gone; the paper consistently says no policy risk ranking
  (`text/0_abstract.tex:23`; `text/1_introduction.tex:52-54,81`; `text/2_methods.tex:83-86,141`;
  `text/4_discussion.tex:91-93`; `text/5_conclusion.tex:8`; `notes/claims-register.md:109`).
- The land-base and yield notes exist in `fresh-fuchs-ws4/notes/reference/`; the register’s rows
  point to them.
- No undefined references, 0 overfull boxes, 25 pages; only underfull warnings.
- Cover letter current: title, four contributions, 0.32%, 5.4–6.2, 38%, no policy risk ranking,
  flow-rule interpretation.

## 3. Is it submittable?

**Yes — submittable with minor edits. No blockers.**

The paper’s main claims are now supported: the estate validation, the sustained level, the
composition–production trade-off, the rotation result, the fire distribution comparison, and the
coupling demonstration. The remaining issues are accuracy/consistency edits, not new analysis:

1. Change the results’ “is the cost” to “we interpret the difference as the cost” (SH1).
2. Narrow the intro and discussion rotation sentence to “between the baseline and aspen-maximisation
   schedules” (SH2).
3. Make the declarations’ archive sentence match the repository: baseline schedule and composition
   run directories on the work host; sensitivity values reproducible from `valuation.py` (SH3).
4. Fix the 10,000 row’s citation or remove 10,000 from the supplement (SH4).
5. Optionally add the negative paired-ensemble sentence (SH5).

Then POLISH: “twice the level weight,” “reproduced” p90, stale benchmark rows, P3.3 maximum, 2017
URL, figures/length, “sits inside the spread,” stumpage grades, “qualifies,” title/keyword, rotation
quantiles, “two searches behind the ceiling,” yield-note prose, license, funding.

None of these is a blocker. The paper is ready for a final copy-edit and submission package.

## 4. Fix order

1. Results 32-34: “we interpret the difference as the cost” (SH1).
2. Intro 78 and discussion 69-73: “between the baseline and aspen-maximisation schedules” (SH2).
3. Declarations/supplement: archive sentence matches the work host and the derived artifacts (SH3).
4. Register 30: cite an existing benchmark artifact or remove 10,000 from the supplement (SH4).
5. Add the negative paired-ensemble sentence or drop “natural extension” (SH5).
6. POLISH pass: P1–P15.
7. Rebuild and check 0 errors/0 undefined/0 overfull.

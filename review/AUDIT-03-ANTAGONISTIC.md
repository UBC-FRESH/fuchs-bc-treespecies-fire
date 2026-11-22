# Audit pass 3: antagonistic referee report

Date: 2026-11-22
Manuscript: `fuchs-bc-treespecies-fire`, HEAD `a48669f` (W1.3 fire comparison and estate coupling)
Code of record: `fresh-fuchs-ws4`, HEAD `9af7c07` (P4 risk phase active); fire API/artifacts at
`9918fb17` and `474dca6e`
Scope: the whole manuscript, the plan and claims register, and the code artifacts that are supposed
to produce every number.
Method: read every text file, recompute the non-fire numbers from the named artifacts, trace the fire
numbers to `notes/reports/p3-3-distribution-comparison.md` and `experiments/p3-fire/scenario-estate-01.json`,
and read the code that defines the risk metric. No manuscript file was edited.

## Verdict

**Reject in present form.** This is not a fabrication problem: most of the arithmetic checks out, the
estate validation is careful, and the paper is honest in several places about what it does not do.
The problem is that the paper's headline is not the paper. It promises a two-level policy model, a
process fire coupled to policy alternatives, and CVaR of NPV. What exists is a well-documented
case study of a sustained-yield plateau, a composition–production arithmetic trade-off, a single
24-ignition fire-coupling demonstration, and a volume-at-risk ensemble that has not been run and
could not produce a species-resolved NPV-at-risk even if it were.

The authors' own claims register says `CVaR by policy | to compute`
(`notes/claims-register.md:105`). The code says the risk metric is "ending standing volume, valued at
the mean net margin" (`experiments/p4-risk/run_ensemble.py:322`) and the process evaluation exposes
ending volume and biomass, not species-resolved harvest
(`notes/reports/p3-closeout.md:44-47`; `notes/reports/p164-8-handoff-review.md:116-119`). A paper
whose abstract says "risk is measured as the conditional value at risk of net present value"
(`text/0_abstract.tex:8-9`) cannot ship while its own register says the metric is uncomputed.

A substantially reframed paper — around the composition–production trade-off and the fire-coupling
demonstration — could be reconsidered. The present framing cannot.

## Severity table

| ID | Severity | Dimension | Finding | Main location |
| --- | --- | --- | --- | --- |
| M1 | **Must fix** | H/D/F | CVaR of NPV is claimed in the abstract, introduction, methods, discussion, conclusion, and keywords, but no CVaR is computed and NPV under fire does not exist. The only implemented risk metric is a 20% lower-tail volume-at-risk with a constant margin. | `text/0_abstract.tex:8-9`; `text/2_methods.tex:61-70`; `text/5_conclusion.tex:8`; `notes/claims-register.md:105` |
| M2 | **Must fix** | B/C | No policy comparison under fire exists. One 24-ignition scenario is run on the baseline schedule only; the composition runs are production-only. RQ1's fire-risk half, RQ3, and RQ4's horizon half have no analysis. | `text/1_introduction.tex:61-68`; `text/3_results.tex:149-186`; `experiments/p4-risk/schedules/` |
| M3 | **Must fix** | D/E/F | The composition frontier is arithmetically wrong at 6% (53.3 > 51.9), the penalty weights are misdescribed (200 and 100,000, not "twice" and "five hundred times"), and "neither reduced the level" is contradicted by 5.16 vs 5.19. | `text/3_results.tex:111-142`; `experiments/tsa24-composition/summary.json` |
| M4 | **Must fix** | F/E | The fire table and abstract overclaim reproduction: the maximum's bootstrap interval is one-sided and not interpretable, the 90th percentile sits at the lower edge, and the table omits the share above 1,000 ha while the text says "two extreme-tail shares". | `text/3_results.tex:158-176`; `text/0_abstract.tex:20-22`; `notes/reference/fire-tail-uncertainty.md:29,45-47` |
| M5 | **Must fix** | D | The methods describe a model that was not run: a leader minimizing CVaR, absolute-deviation goal programming, "the highest even flow the estate sustains", and "policies are compared against each other". The code has no leader optimization, uses one-sided penalties, and has one fire schedule. | `text/2_methods.tex:61-106,129-130` |
| M6 | **Must fix** | A/E/G | The yield bridge is not a validation: 2.31 m3/ha/yr × 3.06 M ha = 7.07 M m3/yr is a maximum-MAI upper bound, not "reproduce the published productivity"; the land-base match is 0.32%, not "within 0.3%"; the 104-year median age and the 8.35/7.35 transition profile are unsourced. | `text/0_abstract.tex:12-14`; `text/3_results.tex:23-30`; `text/4_discussion.tex:25-40` |
| M7 | **Must fix** | E | Several numbers have no register row and several register rows name artifacts that do not exist (`tsa24-thlb.md`, `tsa24-yield-reconciliation.md`); the rotation numbers have no committed script or output. | `notes/claims-register.md:18-30,75-80`; `scripts/` |
| M8 | **Must fix** | G | The discussion says "Seven limitations" and lists five. The two limitations the change log says were added (clearcut only; leading-species grouping) are absent. The most important limitation — no fire-risk policy result — is not listed. | `text/4_discussion.tex:137-149`; `CHANGE_LOG.md:36` |
| M9 | **Must fix** | E/I | Data and code availability overclaims: no WS4 commit or API is cited, the calibration is not publicly archived, the composition and rotation code are missing, and the supplement says the benchmark artifact carries "the even-flow target used here", which is false. | `text/6_declarations.tex:1-16`; `text/99_online_supplement.tex:8-10,52-54` |
| M10 | **Must fix** | B | The gap is established against three papers, not the fire-risk forest-planning literature. "What is missing is a study that joins these pieces" is unsupported without a review of fuel treatment, stochastic harvest scheduling under fire, and BC TSA modelling. | `text/1_introduction.tex:19-43` |
| M11 | **Must fix** | H/I | Title, author block, date, keywords, and abstract overpromise. "Working title", "order of authors to be discussed", `\today`, "conditional value at risk", "dominates every other lever", "less than one percent", and "reproduce the published productivity" all need to go. | `main.tex:23-30`; `text/0_abstract.tex:11-31` |
| M12 | **Must fix** | A | The BC policy setting is asserted, not sourced. BC sets an AAC as a maximum, not a species-composition target; licensees are constrained by silviculture prescriptions and stocking standards. The paper models species choice from the model's treatment options, without those constraints, and a hypothetical composition target. | `text/1_introduction.tex:3-17`; `text/0_abstract.tex:3-5` |
| S1 | Should fix | F/I | One figure for five tables; three promised figures (Fig. 2-4) are missing. No two-level diagram, no composition figure, no fire ECDF. | `planning/paper-plan.md:61-70`; `text/` |
| S2 | Should fix | I | The discussion (1,705 words) is longer than the results (1,482) and nearly twice the plan target; the European finding is stated twice; the fire discipline is repeated in four sections. | `text/4_discussion.tex:119-133` |
| S3 | Should fix | F | Table 5 omits the share above 100 ha and 1,000 ha from the source report, does not state the simulated sample size (3,450), and does not say the simulated uncertainty was not bootstrapped. | `text/3_results.tex:164-175`; `notes/reports/p3-3-distribution-comparison.md:19-28` |
| S4 | Should fix | I | Per-period and per-year quantities are mixed in the same sentences and tables; 5.19 M m3/period and 5.19 M m3/yr are easy to confuse. | `text/3_results.tex:111-142`; `text/99_online_supplement.tex:100-110` |
| S5 | Should fix | D | The price mapping is misdescribed: the code prices Bl at 105.98 (Hem-Bal), while the text says 113.96 covers "spruce, pine, and balsam fir". There is no hemlock in the dataset. | `text/2_methods.tex:139-142`; `scripts/valuation.py:18-26` |
| S6 | Should fix | F | NPV is not computed for the composition runs; "economically favourable mixtures" and "the composition that looks best at the mean" imply an optimization the paper does not perform. | `text/1_introduction.tex:61-68`; `text/4_discussion.tex:155-156` |
| S7 | Should fix | E | `notes/reference/economics-sensitivity.md` is stale (12,248 base, -250 haul, 6,786 at 5%) and `tsa24-estate.md` still says 70 M m3/period and 1.2% above the AAC. The register cites the first as "same". | `notes/reference/economics-sensitivity.md:6-17`; `notes/reference/tsa24-estate.md:57-70` |
| S8 | Should fix | E | The estate validation claims three specific checks that the recorded validator output does not show (only "Dataset is valid"). | `text/3_results.tex:6-11`; `notes/reference/tsa24-estate.md:29-33` |
| S9 | Should fix | D/G | The fire run's limits are not in the methods: 24 ignitions, one per calibration tile (not a Monte Carlo), one 2023 weather season, current fuels, no holdout, five dropped schedule blocks. | `notes/reports/p3-4-scenario-definition.md:30-45` |
| S10 | Should fix | I | The cover letter contradicts the manuscript: "roughly 40 percent" vs 38%, "5.4 to about 5.9" vs 5.4 to 6.2, and a different title. | `submission/cover-letter.md:14-34` |
| C1 | Consider | A | Call the framework a "two-layer scenario analysis" rather than a bilevel model unless the leader is optimized. | throughout |
| C2 | Consider | F | Test the composition frontier's sensitivity to the aspen ceiling (e.g., ±10%). | `text/3_results.tex:127-142` |
| C3 | Consider | F | Report the aspen-specific rotation, not only the area-weighted mean. | `text/3_results.tex:188-205` |
| C4 | Consider | F | Add a no-fire counterfactual for the estate run, so the fire effect on volume is measurable. | `text/3_results.tex:178-186` |
| C5 | Consider | G | Clarify enterprise vs social discounting and the stumpage transfer. | `text/2_methods.tex:137-148` |
| C6 | Consider | I | Add a treatment/regeneration-options table and stocking assumptions. | `text/2_methods.tex:93-99` |

---

## A. Context: is the BC policy setting accurate and adequately sourced?

**A1 (M12). The two-level setting is institutionally real but analytically rhetorical.**
The introduction opens: "Forest management in British Columbia is decided at two levels that do not
share an objective" (`text/1_introduction.tex:3`). That is a strong empirical claim about BC
institutions, and it is supported by one citation, the AAC table. The AAC is a *maximum* set by the
Chief Forester, not a target, and licensees do not choose a landscape species composition. They must
comply with the Forest and Range Practices Act, silviculture prescriptions, and stocking standards.
The paper's enterprise chooses species to replant from the model's treatment options, without those
prescription and stocking constraints, and the composition aspiration is set by the analyst. The
model is a legitimate abstraction, but the text presents it as the actual policy problem.

Concrete problem: "a policy level chooses an allowable annual cut and a species-composition target"
(`text/0_abstract.tex:5-7`; `text/2_methods.tex:55-63`). BC does not set a landscape-wide
species-composition target for TSA24. If the authors have a real policy instrument in mind (e.g., a
species-diversification objective in a silviculture strategy), cite it. If not, say the composition
target is a hypothetical instrument used to trace the trade-off. The current wording will be read as
a misdescription of BC policy by any Canadian referee.

**A2 (M12). Unsourced BC claims.**
- "fire seasons that exceed the historical range and a timber supply that carries the legacy of
  beetle-killed pine and past harvest" (`text/1_introduction.tex:14-16`) has no citation. Add BC
  wildfire and MPB sources, or delete.
- "The Chief Forester sets an allowable annual cut ... with the duty to sustain the timber supply
  over time" (`text/1_introduction.tex:4-5`) needs the Forest Act/TSR citation, not only the AAC
  table.
- "the 2017 determination was 8.35 ... then 7.35" (`text/4_discussion.tex:34-36`) has no citation.
  The only 2017 source in the register is "BC AAC rationale, October 2017", which is not in
  `references.bib`. The bib's `peterson_williams_2015` is the **Williams Lake** rationale, not Prince
  George. A referee will catch this.

**A3. The 7.97 M ha gross area has no bib entry.**
The register cites "BC Prince George TSA page, 2026-11-21"
(`notes/claims-register.md:14`), but no such reference exists. Add it or remove the gross-area figure
(it is not used in any calculation).

**A4. The two-level framing is not a Stackelberg game.**
There is no leader objective solved, no follower best response, no equilibrium, and no feedback. The
policy layer is a set of exogenous targets; the enterprise layer is a goal program. The paper's own
methods say NPV is computed after the search and the enterprise is a satisficing scheduler
(`text/2_methods.tex:83-91`). That is honest, but it contradicts the abstract's "policy level chooses"
and the min-CVaR equation. Either solve a leader problem or call it a two-layer evaluation.

## B. Literature gap and contribution

**B1 (M10). The gap is real but not established against the relevant literature.**
The introduction reviews Fuchs et al. (2024), Topanotti et al. (2024), and Zelnik et al. (2025), then
says "What is missing is a study that joins these pieces" (`text/1_introduction.tex:37`). That is a
claim about the whole field, supported by three papers. Fire-risk forest planning has a large
literature on fuel treatments, fire-smart landscapes, stochastic harvest scheduling under fire, and
spatially explicit optimization. The paper cites none of it. A referee will name three or four
missing literatures and reject the novelty claim. Add a paragraph on (a) fire risk in forest
planning, (b) portfolio/diversification, (c) BC TSA/AAC modelling. Then qualify: "We are not aware of
a study that combines a policy-level composition aspiration, a real TSA estate, and a calibrated
process fire on that estate." That is defensible; "no study joins these pieces" is not.

**B2 (M2). The claimed contribution is not delivered.**
The three contributions (`text/1_introduction.tex:77-83`) are:

1. *A two-level formulation on a real estate.* Delivered as a scenario generator, not a solved
   bilevel problem. The real estate part is delivered well.
2. *A coupling to a calibrated, spatially explicit fire process, so that fuel structure, composition,
   and connectivity affect the risk the policy is meant to manage.* Not delivered as an analysis.
   The fire process is run once on the baseline schedule. Composition is not varied in the fire run,
   so the paper cannot say whether composition affects fire risk. The coupling is a machinery
   demonstration.
3. *An evaluation on downside risk, reported with sampling uncertainty.* Not delivered. No CVaR, no
   NPV-at-risk, no policy comparison. The fire distribution comparison carries historical sampling
   intervals, which is good, but that is calibration validation, not downside risk of a policy.

The paper should either complete the P4 paired analysis or rewrite the contribution around what is
delivered: the estate validation, the composition–production trade-off, and the fire-coupling
demonstration.

**B3. The introduction sets up a spatial question the paper cannot answer.**
"Together they suggest that the relevant composition decision is spatial and dynamic, not a single
landscape average" (`text/1_introduction.tex:33-35`), and then the paper models a single landscape
average. The authors declare this as a limitation, which is honest, but the gap statement makes the
paper's own design look inadequate. Reframe: the literature says the decision is spatial; this paper
takes the first step by quantifying the composition–production trade-off on a real estate, leaving
placement to future work. Do not claim the framework "was built to reach" the spatial question
(`text/5_conclusion.tex:25`) when the policy layer has no placement rule.

**B4 (S6). "Economically favourable mixtures" is not an analysis the paper performs.**
RQ1 asks "Which landscape-scale species mixtures best balance economic production capacity and fire
risk" (`text/1_introduction.tex:61-62`); RQ3 asks how "economically favourable mixtures" change with
risk attitude (`text/1_introduction.tex:65-66`). The paper computes no NPV by composition and no
fire risk by mixture. It computes a volume frontier. The words "best", "favourable", and "balance"
promise an optimization that does not exist. Rewrite the questions around what is measured: how far
the deciduous share can rise, and what it costs in volume.

## C. Translation of the gap into research questions

**C1 (M2). RQ1 is half-answerable; RQ3 and RQ4 are not answerable.**
- RQ1: "Which landscape-scale species mixtures best balance economic production capacity and fire
  risk under a stated fire regime?" The production half is answered by the composition runs; the
  fire-risk half is not. There is no mixture × fire analysis. Either split RQ1 into a production
  question (answered) and a fire-risk question (future work), or complete the fire analysis.
- RQ2: "What are the synergies and trade-offs between species diversification and the rotation length
  implied by the allowable cut?" The paper estimates rotation at one cut and compares two schedules;
  it does not vary the AAC, so "implied by the allowable cut" is not tested. Rewrite to "Does raising
  the deciduous share require a different rotation?" (answered: 102.2 vs 101.7 years).
- RQ3: "How do the economically favourable mixtures change with the decision maker's risk attitude?"
  No risk-attitude parameter, no CVaR confidence level, no risk-aversion run. Delete or declare
  future work.
- RQ4: "Over which planning horizons and discount rates does mixing become economically favourable?"
  Only the discount rate is varied, and only for the baseline schedule; no horizon run; no
  "mixing becomes favourable" analysis. Rewrite to "How does the discount rate change the value of
  the baseline schedule?" or add the runs.

**C2. The dropped fire-break question is handled honestly, but the framing undercuts it.**
The introduction declares the fifth question and the limitation (`text/1_introduction.tex:71-75`);
the discussion repeats it (`text/4_discussion.tex:141-144`); the conclusion returns to it
(`text/5_conclusion.tex:23-26`). That is good. The problem is that the abstract and title still
promise a fire-risk analysis, and the contribution claims spatial connectivity. The honesty is in the
limitation paragraph, not in the headline. Move the limitation into the abstract and the title's
scope.

**C3. The paper's policy scenarios are calibrated to its own result.**
The level target for the composition runs is 51.9 M m3/period, which is the plateau the baseline
search realized. The paper then says the enterprise meets the level target. That is partly circular:
the policy aspiration is set to what the model already does. The official AAC (6.92 M m3/yr) is never
used as a target. The paper should say: "We evaluate composition at the level the estate sustains,
not at the official AAC, because the estate cannot meet the official AAC under a flat flow. The
composition question is therefore conditional on the model's plateau." That is honest and avoids the
circularity.

## D. Methods: is the model described faithfully?

**D1 (M5). "Two-level" is not implemented as a bilevel program.**
The methods define a leader problem
`min_{A,σ*} CVaR_{5%}(NPV(A,σ*))` (`text/2_methods.tex:65-70`), "where the distribution of NPV arises
from the fire scenarios described below". No such distribution exists. No `NPV(A,σ*)` is computed
under fire. The equation is not a simplification; it is a different model. Delete it or replace it
with a scenario definition.

**D2 (M5). The enterprise goal program is not the equation shown.**
The equation uses absolute deviations `|H_t - A| + |S_t - σ*|` (`text/2_methods.tex:77-80`). Two
sentences later the paper says "WS4's minimum and maximum are the hinges of one-sided penalties, not
feasibility bounds" (`text/2_methods.tex:83-87`). Those are not the same objective. The actual WS4
search also includes an even-flow penalty anchored on period 1 with weight 10,000
(`text/99_online_supplement.tex:52`), which the equation omits. Either write the one-sided penalty
objective including the even-flow term, or delete the equation and describe the goal program in words
with the WS4 citation. Do not present a simplified equation as the implementation.

**D3 (M5). "The highest even flow the estate sustains" is not what was run.**
The search aspired to 70 M m3/period and realized 51.89–52.06 (`experiments/tsa24-evenflow/README.md:12-27`).
The plateau is evidence, not proof, of a maximum. Rewrite: "Six independent 100,000-generation
searches, all starting from a 70 M m3/period aspiration, converged to 51.89–52.06 M m3/period. We
interpret this plateau as the estate's sustained even-flow level; it is not a proven maximum." This
matters because the paper's central "25% below the AAC" claim rests on the plateau.

**D4 (M5). "Policies are compared against each other on identical fire draws" is false.**
The methods say this twice (`text/2_methods.tex:129-130`; `text/1_introduction.tex:53-54`). The code
has one fire scenario on one schedule (`experiments/p3-fire/scenario-estate-01.json`). The P4 ensemble
has two schedules (`baseline.csv`, `aspen-max.csv`) but no output, and P4.1/P4.2 are unchecked
(`fresh-fuchs-ws4/ROADMAP.md:114-116`). Rewrite to "the fire process is run once on the baseline
schedule; a paired policy comparison is future work."

**D5. "Satisficing" is defensible but needs a definition.**
The enterprise minimizes weighted deviations from aspirations; that is a goal program, which the
satisficing literature calls satisficing. The paper says "a satisficing scheduler responding to
policy targets, not a profit-maximizing agent" (`text/2_methods.tex:88-91`). Good. But "satisficing"
can imply a stopping rule, not an optimizer. Define it once: "satisficing in the sense of minimizing
weighted deviations from aspiration levels, not in the sense of a behavioral stopping rule." Then use
it consistently.

**D6. The fire scenario is mostly faithful, but the limits are missing.**
The methods correctly describe the calibrated surface-fire model, the FBP coupling, the 24 tiles, the
432 perimeters, and the 250 m support (`text/2_methods.tex:115-135`). Missing:
- The calibration is in-sample; no holdout (`notes/reports/p3-4-scenario-definition.md:35-36`).
- The estate run uses 24 ignitions, one per calibration tile, not a Monte Carlo of the 133-tile
  estate (`notes/reports/p3-4-scenario-definition.md:41-42`).
- One weather season (2023) with 90-day antecedent spin-up; no interannual variability
  (`notes/reports/p3-4-scenario-definition.md:39-40`).
- Current 2025 fuels, not projected fuels after harvest and fire
  (`notes/reports/p3-4-scenario-definition.md:44-45`).
- Clearcut only; no partial cutting or selection (`notes/reports/p3-4-scenario-definition.md:43`).
- Five schedule blocks dropped because the compiled dataset has no fragment mapping
  (`experiments/p3-fire/scenario-estate-01.json:1638-1644`).
Add these to the methods or the limitations. Do not leave them only in the code notes.

**D7 (M3). The composition frontier is described as implemented, but the description is wrong.**
The paper says "with the composition target weighted twice the level target" and "five hundred times
the level target" (`text/3_results.tex:113-115`). The artifact says weight 200 and weight 100,000,
and the README says "raising the composition weight by a factor of 500"
(`experiments/tsa24-composition/README.md:20-26`). The supplement says weight 200 and 100,000
(`text/99_online_supplement.tex:105-106`), which is correct, so the main text and supplement
contradict each other. Use the artifact values and say "weight 200" and "weight 100,000, a 500-fold
increase".

**D8 (M3). The composition target is absolute, not a share; the paper conflates them.**
The target is 5.19 M m3/period of aspen, which is 10% of 51.9 M m3/period
(`text/3_results.tex:111-112`). That is an absolute volume target, not a share target. The README
itself says "The absolute aspen target conflates 'more aspen' with 'a larger share'"
(`experiments/tsa24-composition/README.md:65`). The manuscript never says this. Add it, and report the
realized share beside the target, as the methods promise
(`text/2_methods.tex:85-87`).

**D9 (M6). The yield/growth bridge is not a validation.**
The paper says "the growth curves ... reproduce the published productivity to within 3 percent"
(`text/0_abstract.tex:12-14`). What is computed is 2.309 m3/ha/yr × 3.060 M ha = 7.07 M m3/yr
(`text/3_results.tex:26-28`), which is 2.2% above the official AAC in total (2.5% above the cut per
hectare). That is a maximum-MAI upper bound, not a reproduction of the TSR's yield curves. It shows
the curves' potential is not below the cut; it does not validate them. Rewrite as an upper-bound
consistency check, and delete "reproduce the published productivity" from the abstract.

**D10 (M9). The model and data versions are not cited.**
The methods cite the WS4 repository generically (`text/2_methods.tex:95-96`; `references.bib:119-125`),
but not the API or the artifact. The code uses `ws4.ecosystem.load_estate_grid`,
`load_calibrated_regions`, and `build_relative_fire_source` at `9918fb17`, with durable summaries at
`474dca6e` (`notes/reports/p3-2-estate-fire-run.md:3`;
`notes/reports/p164-8-handoff-review.md:97-98`). The supplement cites the dataset manifest
`c1304ed9` (`text/99_online_supplement.tex:8-10`). The calibration entry
(`references.bib:127-133`) points to the generic WS4 repository, not the calibration worktree; a
reader following it will not find the 432 perimeters or the fitted parameters. Add the API commit,
the artifact, and a calibration DOI or repository to the methods and the data-availability statement.
A reader cannot reproduce the fire run from a generic repo URL.

**D11 (M9). The supplement's "even-flow target used here" is false.**
S1 says the artifact "carries the compiled tables and the even-flow target used here"
(`text/99_online_supplement.tex:8-10`). The artifact's benchmark is 70 M m3/period; the schedule used
here is the GPU-GA r1 schedule that realizes 51.9 (`experiments/tsa24-evenflow/README.md:31-39`). S2
then says "70,000,000 ... in the benchmark; 51,900,000 in the restated runs"
(`text/99_online_supplement.tex:53`). This is confusing at best and wrong at worst. Rewrite S1 and S2
to distinguish the benchmark fixture from the model schedule.

## E. Implementation fidelity: can the numbers be reproduced?

I recomputed the non-fire numbers from `scripts/valuation.py` and
`experiments/tsa24-evenflow/species_periods.csv`, and traced the fire numbers to the P3 reports and
the scenario JSON. The following table is the result.

| Manuscript claim | Artifact | Result |
| --- | --- | --- |
| 5.90 M ha forest; 3.06 M ha managed; 2.84 M ha unmanaged (`text/2_methods.tex:8-10`) | Register cites `notes/reference/tsa24-thlb.md` (`notes/claims-register.md:18-20`) | **Fail.** The file does not exist in `fresh-fuchs-ws4/notes/reference/`. No committed derivation. |
| 458,708 blocks; 48 treatments; 10,326 curves; 99 accounts (`text/2_methods.tex:10,96-97`) | `notes/reference/tsa24-estate.md:35-45` | Pass. |
| 7.97 M ha gross area (`text/2_methods.tex:7`) | Register cites a BC page; no bib entry (`notes/claims-register.md:14`) | **Fail.** No citation or artifact. |
| 3,070,301 ha published THLB; -9,828 ha; -0.32% (`text/99_online_supplement.tex:28-29`) | Register cites "BC AAC rationale, October 2017"; no bib entry (`notes/claims-register.md:21-22`) | **Fail.** No artifact. Text says "within 0.3%" at `text/2_methods.tex:18`, `text/3_results.tex:25`, `text/4_discussion.tex:26`; 0.32 is not within 0.3. |
| Species shares Sx 44.9, Pl 29.4, Bl 16.3, At 5.3, Se 4.0, Ac 0.1 | Register cites `feature.SpeciesProp.managed.*` at offset 0 (`notes/claims-register.md:27`) | Pass in principle, but the compiled dataset is not committed, so not reproducible from the repo alone. |
| Harvested shares Sx 45.2, Pl 31.3, Bl 14.7, At 5.3, Se 3.4, Ac 0.1 | `experiments/tsa24-evenflow/species_periods.csv` | Pass. I recomputed 45.19, 31.32, 14.74, 5.25, 3.35, 0.14. |
| 51.9 M m3/period; 5.19 M m3/yr; 51.89-52.06 across seeds; 51.2-52.3 replayed | `experiments/tsa24-evenflow/summary.json` | Pass. |
| Even-flow penalty 1.3-2.7; level penalty about 515; six 100,000-generation searches | `experiments/tsa24-evenflow/README.md:16-27`; `summary.json` | Pass from README, but **no register rows** for the penalties, the generation count, or the six seeds. |
| 25% below the official AAC | Derived: 1 - 5.189/6.917231 = 24.98% | Pass arithmetic, but **no register row**. |
| 2.31 m3/ha/yr; 7.07 M m3/yr; within 2.5% of the cut per hectare | Register cites `notes/reference/tsa24-yield-reconciliation.md` (`notes/claims-register.md:23-24`) | **Fail.** The file does not exist. The 7.07 is an upper bound, not a validation. |
| 104-year median age (`text/4_discussion.tex:38`) | None | **Fail.** No artifact, no register row. |
| 1,037.9 M m3; 112,776 M CAD; 62,270 M CAD; 8,779 M CAD | `scripts/valuation.py` on `species_periods.csv` | Pass. I recomputed 1,037.897, 112,776.09, 62,270.19, 8,778.85. The 1,037.9 M m3 total has no register row. |
| Conifer margin 56.81-64.79; deciduous -2.25 | `scripts/valuation.py:156-175` | Pass. |
| 5% -> 4,769; 0% -> 62,270; 35 -> 8,752; 61.74 -> 9,035; 117 km -> 8,595 | `valuation.py:219-259` | Pass arithmetic. But 61.74 has no source in `notes/reference/economics-constants.md`, which documents 35-40. `notes/reference/economics-sensitivity.md` is stale: it reports 12,248, -250, 6,786 on the 70 M fixture. |
| 5.69% at weight 200; 5.94% at weight 100,000; 3.20 M m3/period; 6.18% of 5.18 | `experiments/tsa24-composition/summary.json` | Pass. |
| "Weighted twice"; "five hundred times"; "neither ... reducing the level" (`text/3_results.tex:113-116`) | `summary.json:2-16` | **Fail.** Weights are 200 and 100,000; the 100,000 run realizes 5.16 vs baseline 5.19. |
| 6% row: 53.3 M m3/period, 5.33 M m3/yr (`text/3_results.tex:136`) | None; derived 3.20/0.06 | **Fail.** 53.3 exceeds the 51.9 sustained level, so it is not a feasible point. The register omits the 6% row. |
| 8% -> 40.0; 10% -> 32.0; 15% -> 21.3 | Derived 3.20/share | Pass arithmetic, but the constant-aspen assumption is unstated. |
| 38% below the sustained level at 10% | 1 - (3.20/0.10)/51.9 = 38.3% | Pass. |
| Rotation 102.2 years; 101.7 years; 53,071 intervals; median 100; p10-p90 60-160 | Register cites "schedule and fragments" (`notes/claims-register.md:77-78`) | **Fail.** No script, output, or artifact path. `scripts/` contains no rotation code. |
| 30,000 ha/yr; 173 m3/ha | Derived 3,060,473/102.2; 5.19/30,000 | Pass arithmetic, but no script. |
| Fire median 23.8; p90 361.5; p95 1,100.9; >500 8.3%; >5,000 1.8%; max 20,770.4 | `notes/reports/p3-3-distribution-comparison.md:19-28` | Pass, except the maximum interval (see M4). |
| Fire max interval 15,069.3-25,114.8 (`text/3_results.tex:173`) | `notes/reference/fire-tail-uncertainty.md:29` gives 25,111.83 and says the interval is one-sided | **Fail.** The table's upper bound is the observed maximum, not the bootstrap bound; the interval is not interpretable. |
| 1,331 fragments; 16,331 ha grown; 10,444 ha applied; 1,015.9 M m3 | `experiments/p3-fire/scenario-estate-01.json:1630-1675` | Pass. |
| 680 ha grown/ignition; 435 ha applied/ignition; historical mean 512.9 ha | Derived from the totals; 512.9 only in `notes/reports/p3-2-estate-fire-run.md:52` | **Fail.** No register rows; no artifact for 512.9. |
| CVaR by policy | None | **Fail.** Register says "to compute" (`notes/claims-register.md:105`). |

**E1 (M7). Missing register rows.** Add rows for: 1,037.9 M m3 total harvested; 104-year median age;
512.9 ha historical mean; 680 and 435 ha per ignition; 5.16 M m3/yr in the 100,000-weight run; the
6% frontier row (or delete it); the 10,000 even-flow weight; 8.35 and 7.35 M m3/yr; 25%; 2.5%; the
200-year horizon; and the full historical fire table (median interval 20.85-30.16, p95 1,918.88 with
1,415.35-2,955.33, share above 500 of 10.0% with 7.6-12.5, maximum 25,114.8 with 15,069.3-25,114.8).
The 3,070,301 ha and -0.32% rows exist, but the 2017 rationale they name is not in
`references.bib` or the repository; add a citable source. The 3,450-fire row exists; cite it in the
Table 5 caption, which currently omits it.

**E2 (M7). Register rows that name nonexistent artifacts.** `tsa24-thlb.md` and
`tsa24-yield-reconciliation.md` are named but absent. The rotation row names "schedule and fragments"
but no path. The composition row names `summary.json`, which exists, but there is no run script. A
row marked `verified` against a missing file is worse than no row.

**E3 (M7). Stale artifacts that contradict the manuscript.**
- `notes/reference/economics-sensitivity.md:5-17` reports base NPV 12,248, haul -250, discount 5% ->
  6,786. The manuscript reports 8,779, -184, 4,769. Mark it superseded or update it.
- `notes/reference/tsa24-estate.md:57-70` still says the schedule delivers 70,000,000 m3 per period
  and sits 1.2% above the official cut. The manuscript says 51.9 and 25% below. Update it.
- `tests/data/tsa24_species_periods.csv` is the 70 M fixture (1,400 M m3 total), while
  `experiments/tsa24-evenflow/species_periods.csv` is the model schedule (1,037.9 M m3). The names
  are similar; a reader can pick the wrong one. Add a README note or rename the fixture.

**E4 (M9). The composition and rotation analyses are not reproducible.** 
`experiments/tsa24-composition/` contains only `README.md` and `summary.json`; there is no run
script, no seed/budget configuration file, and no species-period tables for the composition runs.
`scripts/` contains no rotation code. The supplement says "the analysis code ... that produce every
number in this paper are held in the project repository" (`text/99_online_supplement.tex:126-128`).
That is false today. Commit the scripts and outputs, or soften the claim.

## F. Results presentation and analysis

**F1 (M4). The fire comparison is framed as sampling uncertainty, but the text overclaims.**
The table caption correctly says the intervals are 5th-95th percentiles of 20,000 bootstrap resamples
(`text/3_results.tex:161-162`). But:
- The maximum's interval is one-sided by construction; the source note says "A bootstrap cannot
  exceed the observed maximum ... not interpretable" (`notes/reference/fire-tail-uncertainty.md:45-47`).
  The paper uses the maximum as a reproduction success in the abstract and results
  (`text/0_abstract.tex:20-22`; `text/3_results.tex:152-154`; `text/4_discussion.tex:110-112`).
  Delete the maximum from the reproduction claim, or footnote that the interval is one-sided.
- The p90 is 361.5 against a point estimate of 490.17 and an interval of 349.13-1,051.26. It is 26%
  below the point estimate and 3.5% above the lower bound. "Reproduced" is too strong; say "at the
  lower edge of the historical interval".
- The table omits the share above 1,000 ha (7.9%, 5.8-10.2%, simulated 5.5%) and the share above 100
  ha (26.2%, 22.7-29.6%, simulated 23.6%), both of which are in the source report
  (`notes/reports/p3-3-distribution-comparison.md:24-27`). The text says "the two extreme-tail shares
  sit at its lower edge" (`text/3_results.tex:154`), but the table shows only one. Add both rows or
  change "two" to "one".
- The simulated sample is 3,450 fires (`notes/reports/p3-3-distribution-comparison.md:7-9`), but the
  table does not say so, and it does not say the simulated uncertainty was not bootstrapped because
  the raw sizes were not persisted (`notes/reports/p3-3-distribution-comparison.md:12-15`). Add both.
- The abstract and Table 5 are consistent with each other — both treat the maximum as reproduced —
  but both are inconsistent with the source note, which says the maximum's interval is one-sided and
  not interpretable. That is the failure: the error is upstream of the table, in how the maximum is
  read.

**F2 (M4). "Never report an absolute fire size as a result" contradicts Table 5.**
The methods say "we ... never report an absolute fire size as a result"
(`text/2_methods.tex:130`). Table 5 reports absolute fire sizes (23.8, 490.17, 361.5, 1,100.9,
20,770.4 ha) and the abstract says "reproduces the historical median" (`text/0_abstract.tex:20`).
The distinction the paper wants is calibration comparison vs prediction; say that explicitly:
"We report absolute fire sizes only in the calibration comparison, never as predictions of future
fire." That resolves the contradiction without weakening the discipline.

**F3 (M3). The composition frontier is not a frontier.**
The table is an arithmetic identity: total = 3.20 / share, holding aspen at 3.20 M m3/period
(`text/3_results.tex:127-142`). It is not a set of model runs, not an NPV frontier, and not a
production possibility frontier. The 6% row's total (53.3) is infeasible because it exceeds 51.9; a
6% target at the sustained level would need 3.11 M m3/period of aspen, below the 3.20 ceiling. The
row is the wrong point, not the target. The
caption should say: "Arithmetic upper bound on total harvest for a given deciduous share, holding
aspen supply at 3.20 M m3 per period. These are not model runs; if aspen supply falls with the total,
the required total is lower and the cost is larger." Rename the table "Composition–production
trade-off implied by the aspen supply ceiling" and delete the 6% row or replace it with the
aspen-max run (6.18%, 51.8 M m3/period, 5.18 M m3/yr).

**F4 (M3). The short searches are not disclosed in the main text.**
The register marks the aspen ceiling "15-minute local search, not converged"
(`notes/claims-register.md:68`), and the supplement says "15-minute budget"
(`text/99_online_supplement.tex:56`). The main text says "an aspen-maximisation run bounds the cause"
(`text/3_results.tex:118`) without the caveat. A 15-minute local search from the baseline is a lower
bound on aspen supply and an upper bound on the cost of a share; the direction is robust to a 500-fold
weight change, but not to a longer search. Say so.

**F5 (M3). The units are a trap.**
The paper mixes 5.19 M m3/period (the level) and 5.19 M m3/yr (the annual mean) in the same
subsection (`text/3_results.tex:111-125`). The aspen target is 5.19 M m3/period = 0.519 M m3/yr, 10%
of the annual level; the aspen supply is 3.20 M m3/period = 0.320 M m3/yr, 6.2% of 5.18 M m3/yr. A
reader can easily conclude that aspen is 62% of the harvest. Add a units note and use one column per
period and one per year in the table.

**F6 (S6). The composition runs are not valued.**
The paper says "the economic price channel is almost silent; the physical volume channel is not"
(`text/4_discussion.tex:82-83`). That is an inference from volume, not an NPV calculation. The
composition summary has no species-period tables and no NPV. Either value the composition runs (add
their species-period tables and run `valuation.py`) or say "we do not compute NPV by composition;
the volume cost is a lower bound on the economic cost if margins are constant." The latter is honest
and sufficient for the paper's current claim.

**F7 (M1). The risk/CVaR claim is not supported by any artifact.**
The code's `cvar` function is a lower-tail mean of ending volume at level 0.2
(`experiments/p4-risk/run_ensemble.py:87-104`), and the summary reports `cvar20_volume_m3` and
`worst_value_cad` (`run_ensemble.py:311-318`). The record's metric is "ending standing volume, valued
at the mean net margin" (`run_ensemble.py:322`), with `MEAN_NET_MARGIN_CAD_PER_M3 = 59.99`
(`run_ensemble.py:41`). There is no discounting, no time path, no species composition, and no NPV.
The manuscript's 5% CVaR of NPV is not a rescaling of this metric; it is a different object. Even the
volume-at-risk ensemble has not been run: `experiments/p4-risk/` has no `ensemble.json`, and P4.1/P4.2
are unchecked (`fresh-fuchs-ws4/ROADMAP.md:114-116`). The register's `CVaR by policy | to compute`
(`notes/claims-register.md:105`) is the correct status; the manuscript must reflect it.

**F8. The estate coupling run is a machinery check, not a policy result.**
The results subsection presents 24 ignitions, 1,331 fragments, 16,331 ha grown, 10,444 ha applied, and
1,015.9 M m3 (`text/3_results.tex:178-186`). There is no no-fire counterfactual, so the fire effect on
volume is not measured. The run burns 10,444 ha, 0.18% of the 5.9 M ha estate. The code report says
"it is a scenario for coupling fire to harvest decisions ... not used for the comparison above"
(`text/3_results.tex:185-186`) and the p3-4 report says "one scenario is not a distribution"
(`notes/reports/p3-4-scenario-definition.md:32-34`). Good. But the subsection still reads like a
result. Retitle it "Coupling demonstration (not a policy result)" and add: "Because the same schedule
is not evaluated without fire, this run does not estimate a fire effect on volume or value. It shows
that the calibrated process runs end to end on the compiled estate." That is the honest claim.

**F9. The rotation analysis is thin and selection-biased.**
The paper estimates rotation from blocks harvested more than once, states the selection bias
(`text/3_results.tex:194-196`), and compares 102.2 to 101.7 years. That is fine as far as it goes,
but it does not vary the AAC, does not report species-specific rotations, and does not give an
uncertainty interval. The claim "the rotation is essentially invariant to the composition target"
(`text/3_results.tex:200`) is based on one alternative schedule (aspen-max), not a composition
target at the same level. Rewrite: "Between the baseline and the aspen-maximisation schedules, the
area-weighted rotation changes by 0.5 years; we cannot estimate the rotation–AAC relation because we
do not vary the cut." Add the aspen-specific rotation if the data allow.

**F10 (S1). One figure is not enough for this paper.**
The paper has one map (Fig. 1) and five tables. The plan promised a two-level diagram, an NPV-by-
composition figure, and a rotation figure (`planning/paper-plan.md:61-70`). At minimum, add:
(a) a schematic of the two layers and the target/penalty coupling; (b) a composition–production plot
with the aspen ceiling and the infeasible region; (c) an ECDF or bar chart of the simulated vs
historical fire sizes with the historical interval. The current table-only presentation makes the
central trade-off hard to see and hides the 6% infeasibility.

## G. Discussion: overreach, the European comparison, and limitations

**G1. The discussion overreaches in five places.**
- "That asymmetry is the central economic finding. A policy analyst who looks only at prices will
  conclude that composition is nearly free; a policy analyst who looks at the schedule will find that
  it costs a third of the harvest" (`text/4_discussion.tex:85-87`). The 38% figure is for a 10%
  share; an 8% share costs 23%; a 6% share costs almost nothing. "A third" is not general, and
  "nearly free" is a straw man. Rewrite with the actual points: 8% -> 40.0 M m3/period (23% below
  the sustained level); 10% -> 32.0 (38% below); 15% -> 21.3 (59% below).
- "The discount rate dominates every other lever" (`text/0_abstract.tex:16`; `text/5_conclusion.tex:15`).
  It dominates the *economic constants* in Table 3, not the composition lever. The composition
  trade-off at 10% removes 38% of volume; if margins are constant, that is roughly a 38% NPV effect,
  comparable to the 46% NPV effect of moving the discount rate from 3% to 5%. Rewrite: "Among the
  economic constants, the discount rate dominates; the composition target is a larger lever, but it
  operates through volume, not price."
- "The gap is therefore the cost of the flow rule we imposed, not a defect in the estate"
  (`text/4_discussion.tex:39-40`). The paper shows the land base matches and the maximum MAI is above
  the cut; it does not run a declining-profile counterfactual. Rewrite: "The gap is consistent with
  the flat-flow rule on an unregulated age structure; a declining-profile run would be needed to
  attribute it." The 104-year median age is unsourced (M6), so the mechanism is not established.
- "The comparison supports the discipline rather than undermining it"
  (`text/4_discussion.tex:110`). The comparison validates the calibration; it does not test a policy.
  Rewrite: "The comparison supports the calibration, not a policy conclusion."
- "Our framework is built to test whether that conclusion survives ... Our result qualifies that
  finding rather than contradicting it" (`text/4_discussion.tex:121-127`). The paper does not test
  the European finding. It establishes a supply limit (6.2%) and a thin tail. Rewrite: "We do not
  test the European finding. We establish a precondition that any such test on this estate must
  confront: the minority species is supply-limited, and the tail that would justify paying for
  diversification is the part of the distribution the model understates." That is a genuine
  qualification, not a claimed result.

**G2. The European paragraph is repeated.**
Lines 119-123 and 125-127 of `text/4_discussion.tex` state the same finding twice. Delete one. The
repetition makes the discussion look padded (1,705 words vs the plan's 900).

**G3 (M8). The limitations are incomplete and miscounted.**
The text says "Seven limitations" and lists five (`text/4_discussion.tex:137-149`). The change log
says two more were added ("clearcut only; leading-species grouping") (`CHANGE_LOG.md:36`), but they
are not in the file. Add them and the following, which a referee will otherwise supply:
- No NPV-at-risk, no CVaR, no policy comparison under fire; the process evaluation exposes ending
  volume and biomass, not species-resolved harvest.
- Composition tracked by leading species; mixed stands assigned to one species.
- Composition ceiling from 15-minute local searches, not converged optima.
- Only clearcut harvesting; no partial cutting or selection.
- NPV excludes road construction, administration, taxes, and risk premia; it is an operating margin,
  not a profit.
- Prices mix vintages: conifer 2026, deciduous 2018. The current text says "point values or documented
  ranges from a single period" (`text/4_discussion.tex:145-147`), which is false.
- One weather season (2023), current fuels, 24 ignitions, one per calibration tile; not a Monte
  Carlo of the estate.
- No AAC variation and no horizon variation, so no rotation–AAC or horizon–diversification result.
Change "Seven" to the correct count once the list is complete.

**G4. The policy implications are not results.**
"Risk attitude belongs in the analysis explicitly, because the composition that looks best at the
mean need not be the one that looks best in the tail" (`text/4_discussion.tex:155-156`) is a
recommendation for future work, not a finding. The paper has no tail analysis. Move it to the
future-work paragraph. "The allowable cut and the composition target should be evaluated together"
(`text/4_discussion.tex:153-155`) is not shown, because the paper does not vary the cut. Soften:
"Our framework can evaluate them together; here we evaluate the composition target at one cut."

**G5. The post-hoc valuation is not discussed.**
The methods say NPV is computed after the search, not optimized inside it
(`text/2_methods.tex:87-91`). The discussion never draws the implication: the schedules are not
economically efficient, and the NPV is an accounting value, not a maximum. The composition frontier
is a feasibility frontier, not an economic optimum. Add a paragraph: "Because the enterprise does not
optimize profit, the reported NPV is the value of a target-following schedule, not the maximum
attainable value. The composition trade-off is therefore a feasibility trade-off; an economic
optimum would require an NPV objective inside the search, which we do not attempt." This is essential
for an economics journal.

## H. Abstract, title, keywords

**H1 (M11). The title is a working title and does not name the paper.**
`\title{\textit{working title:}\\Tree-species diversification under forest fire risks}`
(`main.tex:23`). It promises a fire-risk analysis and gives no case, method, or result. A title that
matches the delivered paper: "The cost of tree-species diversification on a real forest estate: a
two-layer scenario analysis for the Prince George Timber Supply Area, British Columbia". If the fire
coupling is retained: "... with a calibrated fire-process coupling". Remove "working title:" and the
author-order placeholder (`main.tex:24`), and fix `\today` (`main.tex:30`).

**H2 (M1/M11). The abstract promises CVaR and fire-risk results it does not deliver.**
"risk is measured as the conditional value at risk of net present value"
(`text/0_abstract.tex:8-9`) is false. "The calibrated fire regime reproduces the historical median,
90th percentile, share above 500 hectare and maximum within the historical sampling interval"
(`text/0_abstract.tex:20-22`) overclaims the maximum and the p90. "The discount rate dominates every
other lever" (`text/0_abstract.tex:16`) is false with respect to the composition lever. "moves mean
value by less than one percent" (`text/0_abstract.tex:18`) is true only for 35-40 CAD/m3; at the
61.74 proxy it is 2.9%. "which reproduce the published productivity to within 3 percent"
(`text/0_abstract.tex:12-14`) is not a validation. Rewrite the abstract around the actual result:
the estate plateau, the composition ceiling, the volume cost, and the fire calibration comparison
with its caveats.

**H3. The abstract omits the paper's strongest result.**
The composition ceiling (5.4% -> about 6.2%) and the 38% volume cost of a 10% share are not in the
abstract. That is the paper's most defensible contribution. Add: "The deciduous share can rise from
5.4% to about 6.2% at the sustained level; a 10% share implies a total harvest of 32.0 M m3 per
period, 38% below the sustained level, holding aspen supply at 3.20 M m3 per period." Then the reader
knows what the paper actually establishes.

**H4 (M11). The keywords promise CVaR and wildfire risk.**
`conditional value at risk` and `wildfire risk` (`text/0_abstract.tex:30-31`) are not delivered.
Replace with `composition–production trade-off`, `fire-process coupling`, `allowable annual cut`.
Keep `two-level policy analysis` only if the paper is reframed as a two-layer scenario analysis; if
not, use `two-layer scenario analysis`.

**H5. The abstract is long.**
289 words including keywords; the plan target is 250 (`planning/paper-plan.md:51`). The fire and
CVaR sentences are the ones to cut. A 220-word abstract focused on the composition result will be
stronger.

## I. Presentation, structure, cross-references

**I1. The manuscript does not match its own change log.**
`CHANGE_LOG.md:36` says the hostile pass added two limitations (clearcut only; leading-species
grouping). They are absent from `text/4_discussion.tex:137-149`. Either the file was overwritten or
the log is wrong. This is exactly the kind of internal inconsistency a referee will use to doubt the
rest.

**I2. The conclusion contradicts the discussion on the gap.**
The conclusion says "we report the gap and its candidate explanations"
(`text/5_conclusion.tex:13`), while the discussion says "we can locate it" and "the gap is therefore
the cost of the flow rule" (`text/4_discussion.tex:22-40`). Align: either "the gap and the evidence
for the flow-rule explanation" or "candidate explanations".

**I3. The cover letter contradicts the manuscript.**
"roughly 40 percent" vs 38% (`submission/cover-letter.md:31`); "5.4 to about 5.9 percent" vs 5.4 to
6.2 (`submission/cover-letter.md:30-31`); a different title (`submission/cover-letter.md:14-15`).
Fix before submission.

**I4. The supplement and main text disagree on weights and the 6% row.**
S4 says weight 200 and 100,000 (`text/99_online_supplement.tex:105-106`); the main text says "twice"
and "five hundred times" (`text/3_results.tex:113-115`). S4's table has the correct weights, but it
does not include a 6% row; the main text table does, and that row is the invalid 53.3/5.33. Make the
main text match the supplement and delete the 6% row.

**I5. Table 5's maximum interval does not match the source note.**
The table says 15,069.3 to 25,114.8 (`text/3_results.tex:173`); the note says 15,069.30 to 25,111.83
(`notes/reference/fire-tail-uncertainty.md:29`). The p3-3 report repeats 25,114.8, so the discrepancy
is upstream, but the manuscript should not use a one-sided interval as a two-sided target. Fix both
the value and the interpretation.

**I6. The float placement warnings are cosmetic, but the empty acknowledgements file is not.**
`main.log` shows three `h -> ht` float warnings (lines 554, 565, 602) and three underfull boxes; these
are not defects. `text/9_acknowledgements.tex` is empty but is `\include`d (`main.tex:47`), which can
produce a blank page. Either add an acknowledgement or remove the include.

**I7. The "TSA~24" vs "TSA24" usage is inconsistent.**
The manuscript uses both (`text/2_methods.tex:6` vs `text/2_methods.tex:12`). Pick one and use it
everywhere, including the title/abstract.

**I8. The paper has no line-numbered table/figure cross-reference errors.**
`main.log` has 0 undefined references and 0 multiply-defined labels. The `\autoref` calls resolve.
This part is clean.

**I9. The supplement is part of the main PDF.**
The manuscript is 22 pages including the supplement. Many journals want the supplement separate.
Check the target journal's format; if separate, move `99_online_supplement.tex` out of `main.tex`
and provide it as a separate PDF.

**I10. The declarations still contain a TODO.**
`text/6_declarations.tex:28` says "% TODO: confirm the grant number and the funder wording with the
authors before submission." No placeholder may survive submission (AGENTS.md:20-21). Resolve it.

---

## Must-fix rewrites (concrete)

### M1. Remove the CVaR claim, or replace it with the metric that exists

**If the authors do not run P4:** delete every CVaR/NPV-at-risk claim.

- `text/0_abstract.tex:8-9`: delete "risk is measured as the conditional value at risk of net present
  value." Replace with: "We do not estimate NPV-at-risk: the process evaluation exposes ending volume
  and biomass, not species-resolved harvest, so we report a composition–production trade-off and a
  calibration comparison, not a fire-risk result."
- `text/1_introduction.tex:54-56`: delete "Risk is measured as the conditional value at risk of net
  present value, following Fuchs et al., so that the tail of the distribution, not only its mean, is
  part of the objective." Replace with: "We evaluate the schedule as an operating margin and report
  the fire process as a calibrated scenario; a risk-sensitive policy comparison is future work."
- `text/2_methods.tex:61-70`: delete the policy-level paragraph and the min-CVaR equation. Replace
  with: "We evaluate a set of policy scenarios. Each scenario is a pair $(A,\sigma^\ast)$: a harvest
  aspiration and a composition aspiration. We do not optimize over the pair; the policy layer is a
  scenario grid. The CVaR of NPV is not computed, because the process evaluation does not expose
  species-resolved harvest."
- `text/2_methods.tex:132-135`: delete "Downside risk is measured as the conditional value at risk
  across policy alternatives, never as a single policy's prediction." Replace with: "The fire process
  is used for a calibration comparison and a coupling demonstration; it is not used to rank policies
  in this paper."
- `text/5_conclusion.tex:8`: delete "risk is measured as conditional value at risk." Replace with:
  "the fire process is a calibrated scenario, not a risk metric."
- `text/4_discussion.tex:151-158`: move "Risk attitude belongs in the analysis explicitly..." to a
  future-work paragraph; it is not a result.
- `text/0_abstract.tex:31`: delete `conditional value at risk` from the keywords.

**If the authors do run P4:** replace the claim with the implemented metric, and name it precisely:
"volume-at-risk at the 20% lower tail of ending standing volume, valued at the mean net margin of
59.99 CAD/m3 (not NPV-at-risk)." Cite `experiments/p4-risk/run_ensemble.py:87-104,311-322`. Do not
call it CVaR of NPV. Do not use a 5% level if the code uses 20%.

### M2. Rewrite the research questions and the contribution to what is delivered

Replace `text/1_introduction.tex:61-68` with:

> We ask two questions that this design can answer. RQ1: How far can the deciduous share of harvest
> rise at the level the compiled estate sustains, and what does each point of share cost in total
> harvest? RQ2: Does raising the deciduous share require a different rotation? Two further questions
> motivate the work but are not answered here: how the favourable mixtures change with risk attitude,
> and how they change over planning horizons. Answering the first requires an NPV-at-risk ensemble
> that the current process evaluation does not support without a stated value conversion from
> volume; answering the second requires runs at other horizons. We return to both as limitations and
> future work.

Replace the contribution paragraph (`text/1_introduction.tex:77-83`) with:

> The contribution is threefold. First, a compiled and validated TSA24 estate, with a documented
> sustained-yield plateau and a 25% gap to the official cut that we report and bound rather than
> tune away.
> Second, a composition–production trade-off under a measured aspen supply ceiling, with the policy
> target treated as a penalty rather than a constraint, so the realized cut and composition are
> reported beside the aspiration. Third, a calibrated, spatially explicit fire process coupled to
> the estate, with a distribution comparison that carries the historical sampling uncertainty. We do
> not claim a solved bilevel optimum or an NPV-at-risk result; the fire process is a scenario and a
> coupling demonstration.

Add a sentence to the results: "No policy is ranked under fire in this paper; the 24-ignition run is
a coupling demonstration, not a policy comparison."

### M3. Fix the composition frontier table and text

Replace `text/3_results.tex:111-125` with:

> To test whether composition can be changed at the level the estate sustains, we set an aspen
> harvest aspiration of 5.19 M m3 per period (0.519 M m3/yr, ten percent of the 51.9 M m3/period
> level) and searched from the baseline schedule. With the composition penalty weight set to 200, the
> deciduous share rose from 5.4% to 5.69% and the level held at 5.19 M m3/yr. With the composition
> penalty weight set to 100,000 — a 500-fold increase — the share reached 5.94% and the level fell to
> 5.16 M m3/yr, 0.6% below the baseline. Neither reached ten percent, and neither bought the target by
> sacrificing a meaningful part of the level.
>
> An aspen-maximisation run bounds the cause. With no level or flow target and an unreachable aspen
> aspiration, the search realizes a mean of 3.20 M m3 per period of aspen (0.320 M m3/yr), 6.18% of a
> 5.18 M m3/yr total. The sustained mean aspen supply is therefore about 3.20 M m3 per period. A share
> target above about 6.2% must be paid for in level: at a constant aspen supply of 3.20 M m3/period,
> an eight percent share implies a total near 40.0 M m3/period (23% below the sustained level), a ten
> percent share near 32.0 (38% below), and a fifteen percent share near 21.3 (59% below).
>
> These are arithmetic upper bounds, not model runs. The aspen-maximisation run has no level target,
> and the composition runs are 15-minute local searches from the baseline, not converged optima. If
> aspen supply falls with the total, the required total is lower and the cost is larger.

Replace Table 4 (`text/3_results.tex:127-142`) with rows:

| Deciduous share [%] | Total level [M m3/period] | Mean annual [M m3/yr] | Status |
| ---: | ---: | ---: | --- |
| 5.4 (baseline) | 51.9 | 5.19 | model schedule |
| 5.69 (weight 200) | 51.9 | 5.19 | model run |
| 5.94 (weight 100,000) | 51.6 | 5.16 | model run |
| 6.18 (aspen max) | 51.8 | 5.18 | model run, no level target |
| 8 | 40.0 | 4.00 | arithmetic bound |
| 10 | 32.0 | 3.20 | arithmetic bound |
| 15 | 21.3 | 2.13 | arithmetic bound |

Delete the 6% row (53.3/5.33). It exceeds the 51.9 M m3/period sustained level and is not feasible.
If the authors want a 6% row, it must be "51.9 / 5.19, flow-limited, not run".

### M4. Fix the fire table and the abstract sentence

Replace the abstract fire sentence (`text/0_abstract.tex:20-22`) with:

> In the calibration comparison, the simulated distribution matches the historical median (23.8 vs
> 22.97 ha) and the share above 500 ha (8.3 vs 7.6-12.5%), sits at the lower edge of the historical
> interval for the 90th percentile (361.5 vs 349.1-1,051.3 ha), and is below it at the 95th
> percentile (1,100.9 vs 1,415.4-2,955.3 ha). We do not use the maximum as a reproduction target:
> its bootstrap interval is one-sided by construction.

Replace the fire table (`text/3_results.tex:164-175`) with rows for median, p90, p95, share above 100,
500, 1,000, and 5,000; remove the maximum row or add a footnote "one-sided, not interpretable". Add a
caption note: "Simulated sample: 3,450 fires from the regional calibration; its own sampling
uncertainty was not bootstrapped because the raw sizes were not persisted."

Replace `text/3_results.tex:152-156` with:

> The median and the share above 500 ha sit inside the historical interval. The 90th percentile sits
> at the lower edge: 361.5 ha against a point estimate of 490.17 and a 5th-95th interval of
> 349.13-1,051.26, 26% below the point estimate. The 95th percentile is below the interval, and the
> shares above 1,000 and 5,000 ha sit at or just below its lower bound. The central body is therefore
> consistent with the record; the upper tail is thin by more than historical sampling noise explains.
> No parameter was adjusted to lift it.

Replace `text/2_methods.tex:129-130` with: "We report absolute fire sizes only in the calibration
comparison, never as predictions of future fire."

### M5. Rewrite the methods' decision structure

Replace `text/2_methods.tex:53-91` with a description that matches the code:

> We represent two decision layers. A policy layer sets a harvest aspiration $A$ and a composition
> aspiration $\sigma^\ast$. An enterprise layer chooses the area to harvest in each period from each
> development type and age class, and the species to replant, by minimizing a weighted sum of
> one-sided penalties: the deviation of period harvest from $A$, the deviation of the even-flow
> profile from period 1, and the deviation of species composition from $\sigma^\ast$, subject to the
> area balance and the treatment options available on each block. The minimum and maximum in WS4 are
> the hinges of one-sided penalties, not feasibility bounds; a target is an aspiration, and the
> realized value is an outcome of the weighted compromise. We report the realized cut and composition
> beside every target, and we do not describe a target as a constraint that was met or violated.
>
> The model has no economic objective: net present value is computed from the schedule after the
> search, not optimized inside it. The enterprise is therefore a satisficing scheduler in the sense
> of minimizing weighted deviations from aspiration levels, not a profit-maximizing agent. The
> policy layer is a scenario grid, not an optimized leader: we do not solve $\min_{A,\sigma^\ast}$
> CVaR. An economic objective inside the search, and a leader problem over $(A,\sigma^\ast)$, are
> natural extensions and are not attempted here.

Replace `text/2_methods.tex:101-106` with:

> We run 20 periods of ten years. The reference schedule is the plateau to which six independent
> 100,000-generation searches converged under a 70 M m3/period aspiration: 51.89-52.06 M m3/period,
> a mean of 5.19 M m3/yr. We interpret this as the estate's sustained even-flow level, not a proven
> maximum. We evaluate one cut (the plateau) and a set of composition aspirations; we do not vary the
> cut.

### M6. Rewrite the yield/level bridge

Replace `text/3_results.tex:23-30` with:

> That level is about 25% below the official allowable annual cut of 6,917,231 m3/yr. The managed
> area matches the published timber harvesting land base to within 0.32%, so the gap is not the land
> base. The area-weighted maximum mean annual increment of the model's curves is 2.31 m3/ha/yr,
> which on the managed area gives 7.07 M m3/yr, about 2.2% above the official cut in total (2.5%
> above the cut per hectare). This is an upper-bound consistency check, not a validation of the
> growth curves: a maximum MAI is not a sustainable yield. The gap is consistent with holding a
> constant level from
> the first period on an unregulated age structure, where the official determination is a declining
> transition profile; we do not run a declining-profile counterfactual, so we cannot attribute the
> gap to the flow rule alone.

Replace the abstract clause `text/0_abstract.tex:12-14` with: "The managed area matches the published
timber harvesting land base to within 0.32%, and the model's maximum MAI implies a potential yield of
7.07 M m3/yr, about 2.2% above the official cut; this is an upper-bound check, not a reproduction of
the published yield curves."

Fix "within 0.3 percent" to "within 0.32 percent" at `text/2_methods.tex:18`, `text/3_results.tex:25`,
`text/4_discussion.tex:26`.

Add a source/artifact for the 104-year median age, or delete the clause at `text/4_discussion.tex:38`.
Add a citation for the 8.35/7.35 profile, or delete it. Do not cite `peterson_williams_2015`; it is
the Williams Lake rationale.

### M7. Fix the register and the missing artifacts

- Create `notes/reference/tsa24-thlb.md` with the managed/unmanaged area derivation and the
  `IFM(managed)` rule, or change the register row to the actual artifact.
- Create `notes/reference/tsa24-yield-reconciliation.md` with the 2.309 and 7.07 derivation, or
  change the row.
- Add a rotation script (e.g., `scripts/rotation.py`) and its output, or delete the rotation
  subsection. The register's "schedule and fragments" is not an artifact path.
- Add a composition run script and the species-period tables, or mark the composition results as
  "recorded, not reproducible from the repo".
- Add rows for the missing numbers in E1.
- Update `notes/reference/economics-sensitivity.md` to the model schedule or mark it superseded.
- Update `notes/reference/tsa24-estate.md:57-70` to the 51.9 plateau or mark the 70 M section
  superseded.
- Add the 61.74 price source to `notes/reference/economics-constants.md` or delete the 61.74 row from
  the manuscript and supplement.

### M8. Rewrite the limitations

Replace `text/4_discussion.tex:137-149` with a complete list and a correct count. At minimum, include:

> Twelve limitations bound what the paper can claim. First, the analysis covers one timber supply
> area. Second, growth is represented by compiled yield curves rather than individual-tree
> simulation. Third, the policy layer sets a landscape-wide composition share rather than a spatial
> placement rule, so the broadleaf fire-break question is not answered. Fourth, prices, costs, and
> stumpage are point values or documented ranges from mixed vintages: conifer prices are 2026, the
> deciduous price is a 2018 ten-year average. Fifth, NPV excludes road construction, administration,
> taxes, and risk premia; it is an operating margin, not a profit. Sixth, the fire model is
> calibrated in-sample, has no independent holdout, and its tail is thin and weakly identified.
> Seventh, the estate fire run uses 24 ignitions (one per calibration tile, on a 133-tile layer
> stack), one 2023 weather season, and current fuels; it is a coupling demonstration, not a Monte
> Carlo of the estate. Eighth, only clearcut harvesting is represented; partial cutting and selection are
> absent. Ninth, species composition is tracked by leading species, so mixed stands are assigned to
> one species. Tenth, the composition ceiling comes from 15-minute local searches, not converged
> optima. Eleventh, we do not estimate NPV-at-risk or any fire-risk policy comparison; the process
> evaluation exposes ending volume and biomass, not species-resolved harvest. Twelfth, we do not vary
> the AAC or the horizon, so we cannot estimate the rotation–AAC or horizon–diversification relation.

Adjust the count if the authors group items, but do not say "seven" and list five.

### M9. Rewrite data and code availability

Replace `text/6_declarations.tex:1-16` with:

> The compiled TSA24 dataset is the frozen `tsa24-public-artifact` (manifest prefix `c1304ed9`),
> derived from the public FEMIC TSA24 instance and built with the WS4 compiler. The estate model is
> WS4 at API commit `9918fb17`; the fire summaries and the calibrated estate run use the public API
> (`load_estate_grid`, `load_calibrated_regions`, `build_relative_fire_source`) and the durable
> artifacts at `474dca6e`. The calibration parameters and the 432 historical perimeters must be
> archived with the companion calibration study at a citable DOI or repository; a generic WS4 repo
> URL is not enough. The valuation is `scripts/valuation.py`; the estate fire run is
> `experiments/p3-fire/run_scenario.py`; the risk ensemble is `experiments/p4-risk/run_ensemble.py`.
> The composition and rotation scripts must be committed; the repository currently has neither. The
> repository will be archived with a DOI on acceptance.

Add the commit/API to the methods (`text/2_methods.tex:95-99`). Verify the Apache 2.0 claim: there is
no `LICENSE` file in the code repository; cite the upstream license or remove the claim.

Fix S1/S2 (`text/99_online_supplement.tex:8-10,52-54`): the artifact carries the compiled tables; the
70 M m3/period fixture is a benchmark, not the schedule used here; the schedule used here is the
GPU-GA r1 schedule, which realizes 51.9 M m3/period.

### M10. Add the missing literature

Add a paragraph after `text/1_introduction.tex:35` on fire-risk forest planning: fuel treatment
optimization, fire-smart landscapes, stochastic harvest scheduling under fire, and spatially explicit
risk. Add a paragraph on BC TSA/AAC modelling and the MPB legacy. Then replace "What is missing is a
study that joins these pieces" with "We are not aware of a study that combines a policy-level
composition aspiration, a real TSA estate, and a calibrated process fire on that estate." Cite the
closest works. This is a must because the current gap claim is not defensible against the field.

### M11. Rewrite the front matter and abstract

- Title: "The cost of tree-species diversification on a real forest estate: a two-layer scenario
  analysis for the Prince George Timber Supply Area, British Columbia" (or a close variant). Remove
  "working title:", the author-order placeholder, and `\today`.
- Abstract: lead with the estate plateau, the composition ceiling, the volume cost, and the fire
  calibration comparison. Delete the CVaR sentence, the "reproduce productivity" clause, "dominates
  every other lever", and "less than one percent" unless qualified. Add the 6.2% ceiling and the 38%
  cost at 10%.
- Keywords: `forest policy, species diversification, composition–production trade-off, fire-process
  coupling, allowable annual cut, British Columbia`.

### M12. Source or reframe the BC policy setting

Replace `text/1_introduction.tex:3-10` with:

> British Columbia sets an allowable annual cut for each timber supply area; the cut is a maximum,
> not a target. The enterprises that hold harvesting rights decide how to meet it, subject to
> silviculture prescriptions and stocking standards. We represent the policy problem as two layers —
> a policy aspiration and an enterprise response — and we treat the composition aspiration as a
> hypothetical policy instrument, because BC does not set a landscape-wide species-composition target
> for TSA24. The question is whether a more diverse species mix is compatible with the cut the estate
> can sustain, and at what cost in volume.

Cite the Forest Act/TSR process and, if one exists, a BC species-diversification policy. Delete or
source "fire seasons that exceed the historical range". Soften "the two objectives diverge" to "the
two layers can diverge in the model; we do not test whether they diverge in practice."

---

## What this pass does not cover

- I did not run WS4 or the P4 ensemble. The P4 ensemble has no output in the repository, so I cannot
  verify a volume-at-risk result; I can only verify that the metric is volume-based, at 20%, and not
  NPV.
- I did not verify the external BC policy documents (the AAC table, the 2017 rationale, the 8.35/7.35
  profile) against the live web. I checked whether the manuscript and the code repository carry a
  citable artifact; for several claims they do not.
- I did not verify the calibration itself (the 432 perimeters, the 3,450 simulated fires, the
  suppression parameters) against the calibration worktree. I read the P3 reports and treated them
  as the record.
- I did not inspect the study-area map visually. I checked that the figure exists and that the
  caption matches the TSA24 description.
- I did not verify the journal's formatting requirements. The manuscript is a generic `article` with
  double spacing and line numbers; the target journal is not named in the manuscript.

## Bottom line

The paper is a careful case study with a real estate, a reproducible economic valuation, and a
well-documented fire calibration. It is not a two-level policy model with CVaR of NPV, and it does
not contain a fire-risk policy result. The authors should either complete the risk analysis or
change the paper's claim. The fastest path to a submittable paper is the reframing: lead with the
composition–production trade-off (5.4% -> 6.2% at the sustained level; 10% costs 38% of volume),
keep the estate validation and the fire calibration comparison, and state plainly that the fire
process is a scenario and a coupling demonstration, not a policy ranking. That paper is honest,
useful, and publishable. The current one is not.

## Rewrite order

1. **Freeze the claim.** Choose one: (a) reframe as a composition–production case study with a fire
   coupling demonstration and remove CVaR/fire-risk claims; or (b) complete P4 and report
   volume-at-risk honestly, not NPV-at-risk. Do not submit a hybrid. (M1, M2)
2. **Rewrite the front matter.** Title, author block, date, abstract, keywords. (M11, M1, H2-H5)
3. **Rewrite the introduction.** Gap against the real literature, delivered contribution, two
   answerable RQs, two declared limitations. (M2, M10, M12, B1-B4, C1-C3)
4. **Rewrite the methods.** Delete the min-CVaR equation; write the actual goal program; state the
   plateau interpretation; describe the fire scenario limits; describe the composition and rotation
   methods; add the commit/API. (M5, M6, M9, D1-D11)
5. **Fix the composition results.** Weights 200/100,000; 5.16 vs 5.19; delete the 6% row; state the
   constant-aspen assumption and the short searches; add the units note. (M3, F3-F5)
6. **Fix the fire results.** Remove the max reproduction claim; add the >100 and >1,000 rows; state
   the 3,450 sample; separate the calibration comparison from the coupling demonstration; add the
   no-counterfactual caveat. (M4, F1-F2, F8)
7. **Fix the yield/economics.** 0.32%; upper-bound check; source the 104-year age and the 8.35/7.35
   profile; clarify the price mapping, the 61.74 source, the perspective, the mixed vintages, and the
   road-cost exclusion. (M6, S5-S7, G1-G5)
8. **Rewrite the discussion and conclusion.** Remove the overreach; say the paper does not test the
   European finding; add the post-hoc valuation caveat; complete the limitations. (G1-G5, M8)
9. **Fix declarations and data availability.** Commit/API, calibration archive, scripts, license,
   benchmark clarification. (M9)
10. **Fix the supplement and the claims register.** Every number with a row; every row with an
    existing artifact; mark superseded rows; delete out-of-scope TSA29 rows or label them. (M7, E1-E4)
11. **Fix presentation.** Figures, units, redundancy, cross-references, placeholders, cover letter.
    (S1-S10, I1-I10)
12. **Re-run this audit.** Recompute every number from the revised artifacts; a pass that finds
    nothing is evidence of a weak pass.

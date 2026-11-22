# Paper plan: tree-species diversification under forest fire risks

Status: draft plan, 2026-11-21.
Model of record for process: `fresh_daugherty_manuscript` (planned, drafted, then audited by
successive antagonistic referee passes that recomputed every number from tracked records).

## The paper in three sentences

Public forest policy in British Columbia sets a harvest level and expects species mixtures that
keep forests productive under fire risk, while the enterprises that carry out the harvest answer
to short-term profit. We formalise that as a bilevel problem on a real timber supply area, with the
policy level choosing the allowable cut and species-composition targets and the enterprise
responding with harvest and regeneration decisions under those constraints. We evaluate policies
on downside risk (CVaR) of the resulting net present value under a stated fire scenario, and show
where the two levels' objectives diverge.

## What the paper is, and is not

| It is | It is not |
| --- | --- |
| A methodological economics paper about two-level policy design | A fire-behaviour or fire-ecology paper |
| A policy analysis on one real management unit (TSA24, Prince George) | A provincial or national assessment |
| A relative comparison of policies under a stated fire scenario | A prediction of future fire sizes or burned area |

Consequence: fire enters as a **scenario**, and every fire number carries the scenario definition
and its sampling uncertainty. This is ADR 0002 in the code repository, and it governs the writing.

## Research questions and what answers each

Revised after the antagonistic review (2026-11-22): the paper claims only what was delivered.

| RQ | Question | Analysis | Status |
| --- | --- | --- | --- |
| RQ1 | What sustained harvest level does the compiled estate support under a flat even flow, and how does it compare with the official cut? | Six 100k-generation searches, land-base and MAI reconciliation | Answered: 5.19 million m3/yr, 25 percent below the cut; gap is the flow rule |
| RQ2 | How far can the deciduous share rise at that level, and what does it cost in volume? | Composition runs plus an aspen-maximisation run; constant-supply arithmetic | Answered: 5.4 to about 6.2 percent free; 10 percent costs 38 percent of level |
| RQ3 | Does raising the deciduous share require a different rotation? | Regeneration intervals, baseline versus aspen-max | Answered: 102.2 versus 101.7 years, no change |
| RQ4 | Does the calibrated fire regime reproduce the historical distribution, and can it be coupled to the estate? | 3,450-fire calibration versus 432 perimeters; 24-ignition estate run | Answered: central distribution inside the interval, tail below; coupling demonstrated |

Declared future work, not research questions in this paper:

- Spatial placement of broadleaf fuel breaks (needs a placement rule).
- Policy ranking under fire (needs composition varied in the fire run).
- Net-present-value-at-risk (needs species-resolved harvest accounts).

**Decision (W2.4, 2026-11-22):** the earlier questions about "economically favourable mixtures",
risk attitude, and planning horizons were removed. They implied an optimization and a fire-risk
comparison the paper does not perform. The review record is `review/AUDIT-03-ANTAGONISTIC.md`.

## Section plan

| Section | Target words | Content |
| --- | ---: | --- |
| Abstract | 250 | Question, method, three findings, one limitation |
| 1 Introduction | 900 | Policy tension, gap, five research questions, contribution |
| 2 Methods | 2000 | Region, bilevel formulation, estate model, fire scenario, economics |
| 3 Results | 1500 | Estate validation, the sustained level and its gap to the official cut, economics, sensitivities, composition surface, rotation |
| 4 Discussion | 900 | Interpretation, policy reading, limitations |
| 5 Conclusion | 250 | What a policy maker should take away |
| Supplement | — | Data provenance, model settings, sensitivity tables |

## Figures and tables

| Item | Content | Source artifact |
| --- | --- | --- |
| Fig. 1 | Model region | `figures/studyArea_map.pdf` (exists) |
| Fig. 2 | The two decision levels and their coupling | To draw |
| Fig. 3 | NPV by composition target and allowable cut | `fresh-fuchs-ws4` regulated LP surface |
| Fig. 4 | Implied rotation length by allowable cut | same |
| Table 1 | Landscape composition | estate summary |
| Table 2 | Prices, costs, and their provenance | `notes/reference/economics-constants.md` |
| Table 3 | Sensitivities | model schedule, `scripts/valuation.py` |
| Table 4 | Composition-production frontier | `experiments/tsa24-composition/summary.json` |

## What the pending calibration affects

Only the fire-scenario numbers: fire-size distributions, CVaR values, and any statement about
burned area. Everything else — the formulation, the estate, the even-flow result, the composition
surface, the rotation finding, the economics — is independent of it and can be written now.

Drafting rule: any sentence whose number is not yet final is marked `\pending{...}` in the LaTeX
and listed in the claims register. No placeholder may survive to submission.

## Claims register

Every number in the manuscript must cite a committed artifact in `fresh-fuchs-ws4` or in the
calibration repository. The register is `notes/claims-register.md`. A sentence without a row there
does not ship.

## Writing phases

| Phase | Deliverable | Exit criterion |
| --- | --- | --- |
| W0 Plan | This plan, claims register, revised outline | Maintainer accepts the plan |
| W1 Draft | Abstract to conclusion drafted, placeholders marked | Every section has prose; no empty section |
| W2 Audit | Antagonistic referee passes, numbers recomputed from records | Every claim traces to an artifact; defects fixed |
| W3 Submit | Submission package, cover letter, declarations | Maintainer approves submission |

## Risks

1. **The draft's methods still describe the old design** — a 10,000 ha Williams Lake subset and
   WS3. They must be rewritten for TSA24 and WS4, or the paper contradicts its own results.
2. **RQ2 cannot be answered** without the corridor policy. Name it as a limitation.
3. **The deciduous price is a 2018 average.** The composition result depends on it; the paper must
   present it as a range, not a point.
4. **The tail is weakly identified.** Report it with intervals, never as a point estimate.
5. **Author order and affiliations** are unresolved in the title block.

## Relation to prior work

This paper continues Jasper Fuchs's European work on tree-species diversification under
disturbance risk and must be written as a continuation of it, not alongside it.

| Prior work | What it established | What it did not do |
| --- | --- | --- |
| Fuchs et al. (2024), *Scientific Reports* 14:2140, `fuchs_severe_2024` | Stand-type portfolios across 24 planning units; spatially correlated extreme events; CVaR as the objective; top-down versus bottom-up planning | No process-based disturbance; homogeneous planning units; bare-land composition rather than an operating forest; German species and prices |
| Fuchs (2024), dissertation, `fuchs_dissertation_2024` | The economic limits of diversification as an adaptation strategy | Same scope limits as above |
| Topanotti, Fuchs et al. (2024), *Science Advances* 10:eadp6566, `topanotti_enhancing_2024` | Empirical evidence that enrichment can serve economic and ecological multifunctionality | Stand-scale and empirical; not a planning model |
| Zelnik et al. (2025), *Ecological Modelling* 509:111222, `zelnik_managing_2025` | Stand size and conifer/deciduous composition reduce landscape fire risk | Not an economic or policy model; no harvest or regeneration decisions |

### What this paper inherits

The two-level structure (a regional planner and local decision-makers), the CVaR objective, and the
portfolio reading of composition. The introduction should open from `fuchs_severe_2024` and name it
as the direct predecessor.

### What this paper adds

1. **Disturbance is a process, not a probability.** Fire spreads over the landscape with fuel,
   weather, terrain, and suppression, so firebreaks, fuel structure, and connectivity are
   representable. This is the step `zelnik_managing_2025` makes physically and this paper makes
   economically.
2. **A real management unit.** TSA24 with its actual age structure and an official allowable cut,
   rather than bare-land allocation of stylised stand types.
3. **Operating decisions.** Harvest scheduling and regeneration under policy constraints, rather
   than area shares of stand types across homogeneous units.
4. **A different species axis.** Interior BC conifer and deciduous, with BC prices, costs, and
   stumpage, rather than German spruce, beech, and Douglas-fir.

### Where the findings should meet

`fuchs_severe_2024` found that diversification did not buffer the economic consequences of extreme
events, and that severe events pushed allocation toward homogenisation and low-investment choices.

What this study can say so far is narrower: on the model-produced schedule, mean net present value
is insensitive to the deciduous log price across its full documented range (plus or minus 26
million CAD) and to haul distance (184 million CAD), while the discount rate halves it. That is a statement about
prices, not about composition. The composition surface on TSA24 has not been computed, so the
claim that mean NPV is insensitive to composition is **not yet established** and must not appear in
the manuscript until it is.

If the composition surface does turn out flat in the mean, the signal will be in the tail, which
is consistent with the European finding and with the CVaR framing. The discussion must make that
comparison explicitly, and must not present the BC case as contradicting the European result.

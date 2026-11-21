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

| RQ | Question | Analysis | Status |
| --- | --- | --- | --- |
| RQ1 | Which landscape mixtures balance production and fire risk? | Composition target × allowable cut surface, NPV and CVaR | Surface computed (perpetuity LP); CVaR pending fire scenario |
| RQ2 | How far can broadleaf be used as fire breaks before production suffers? | Spatially explicit composition targets for a corridor | **Not implemented.** Requires the corridor policy; currently out of scope |
| RQ3 | What are the synergies and trade-offs between diversification and rotation length? | Implied rotation length per allowable cut | Computed; the rotation–AAC relation is **non-monotonic**, which is itself a result |
| RQ4 | How do favourable mixtures change with risk attitude? | Vary the CVaR confidence level | Pending fire scenario |
| RQ5 | Over which planning horizons does mixing pay? | Discount-rate and horizon sensitivity | Computed: the discount rate dominates every other lever |

**Decision needed:** RQ2 is the weakest link. Either it becomes a named limitation with the current
draft, or the paper waits for the corridor policy. The plan assumes the former.

## Section plan

| Section | Target words | Content |
| --- | ---: | --- |
| Abstract | 250 | Question, method, three findings, one limitation |
| 1 Introduction | 900 | Policy tension, gap, five research questions, contribution |
| 2 Methods | 2000 | Region, bilevel formulation, estate model, fire scenario, economics |
| 3 Results | 1500 | Estate validation, even flow against the cut, composition surface, rotation, sensitivities |
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
| Table 3 | Sensitivities | `notes/reference/economics-sensitivity.md` |

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

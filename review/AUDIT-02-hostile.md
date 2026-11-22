# Audit pass 2: hostile reading of the argument

Date: 2026-11-22, on branch `feature/w1-draft`.
Method: read the draft as a referee trying to reject it, list every attack, and fix what can be fixed
without the fire calibration.

## Attacks that would reject the paper today

| Attack | Status | Action |
| --- | --- | --- |
| There are no fire results. The title, abstract, and methods promise a fire-risk analysis and the results contain none. | Valid. This is the only true blocker. | Fire section and the abstract sentence stay marked pending. The paper must not be submitted until they are filled. |

## Attacks that are now answered

| Attack | Response |
| --- | --- |
| "Bilevel" is a mathematical claim the model does not meet; the follower is not optimizing profit. | Wording changed to "two-level" throughout, keywords included. The methods state that the enterprise is a satisficing scheduler and that NPV is computed after the search. |
| The estimated rotation is a selection artefact. | Now stated: intervals come only from blocks harvested twice within the horizon, biased toward productive and accessible stands. |
| The model ignores partial cutting, the obvious tool for fine-scale composition. | Added as a sixth limitation. |
| Composition is tracked by leading species only. | Added as a seventh limitation. |
| The model does not reproduce the official cut. | Reconciled in Results and Discussion: land base matches, curves imply 7.07 million m3/yr, the gap is the flat-profile rule. The paper does not claim to reproduce the determination. |

## Attacks that remain open by design

| Attack | Planned response |
| --- | --- |
| The composition ceiling comes from 15-minute local searches, not converged optima. | Stated in the text, the register, and the experiment note. The direction is robust to a 500-fold weight change. A converged run is possible but not required for the claim. |
| A single case study cannot support general claims. | Stated as the first limitation. |
| Prices mix vintages (conifer 2026, deciduous 2018). | Stated as a limitation and reported as a range. |
| The fire calibration is not independently validated. | Stated as a limitation; comparative framing only. |
| CVaR is named but not computed. | Resolved when the fire run lands; until then the phrase is a method statement, not a result. |

## What this pass does not cover

- The fire numbers, because they do not exist yet.
- A full claims-vs-artifact sweep of the fire section, which pass 1 could not do.

## Verdict

The draft is coherent and honest about what it does not show. It is not submittable until the fire
results exist, and nothing in this pass can change that.

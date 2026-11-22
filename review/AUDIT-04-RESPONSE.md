# Response to the revision audit (AUDIT-04)

Date: 2026-11-22. Verification pass on the rewritten manuscript.

## Verdict addressed

The revision fixed the CVaR-of-NPV error but introduced a volume-at-risk claim without a result,
kept an infeasible 6 percent row, and left stale register and cover-letter text. All findings are
addressed below; the paper no longer claims any policy risk metric.

| ID | Disposition |
| --- | --- |
| V1 Volume-at-risk claimed without a result | Removed from abstract, introduction, methods, discussion, and conclusion. The paper now states explicitly that no policy risk ranking is reported. The paired ensemble is named as a natural extension, not a result. |
| V2 Infeasible 6 percent row | Removed from Table 4. The text states that a 6 percent share needs 3.11 million m3/period of aspen, below the 3.20 ceiling, so it is feasible at the sustained level and is not a binding row. The table reports 8, 10, and 15 percent only, under a "maximum total level" header. |
| V3 Rotation artifact incomplete | `scripts/rotation.py` now reports the share of managed area older than 100 years. Two artifacts are committed: `experiments/tsa24-evenflow/rotation.json` (102.15 years, 44.1 percent over 100) and `experiments/tsa24-composition/rotation-aspen-max.json` (101.72 years). The paper and register cite both. |
| V4 Fire wording contradicts methods and overclaims p90 | Methods now says absolute values are reported beside the interval but not interpreted as predictions. Results, abstract, and discussion say the median and share above 500 ha are inside, the p90 at the lower edge, and the p95 and tail below. |
| V5 False sensitivity sentence; risk metric underspecified | Sensitivity is limited to the three economic constants; the fire scenario has one weather season and is not a sensitivity axis. The risk-metric paragraph is replaced by a scope statement: no policy risk metric is reported. |
| V6 Register paths and missing rows | External notes are prefixed `fresh-fuchs-ws4:`; rows added for total volume, 25 percent gap, 2.5 percent MAI margin, even-flow weight and penalties, 8.35/7.35 transition, per-ignition areas, and the full historical fire table. No row the paper relies on is marked pending or to compute. |
| V7 Supplement price range | Supplement now varies the deciduous price over 35 to 40 CAD/m3, matching the main text. |
| V8 Flow-rule and discount overclaims | The flow-rule attribution is stated as an interpretation with no declining-profile counterfactual. "Dominates every other lever" is qualified to the economic constants. "A third of the harvest" is replaced by about 38 percent at a ten percent share. |
| V9 See V8 | — |
| V10 Cover letter stale | Rewritten to the current title, four contributions, 0.32 percent, 5.4 to 6.2 percent, 38 percent, no risk ranking, and no flow-rule overclaim. |

## Remaining before submission

1. Figures 2--4 (two-layer diagram, composition frontier, fire comparison).
2. Author decisions: order, funding wording, journal.
3. If the paired volume-at-risk ensemble finishes before submission, it can be added as a results
   subsection with its own claim; until then the paper does not claim it.

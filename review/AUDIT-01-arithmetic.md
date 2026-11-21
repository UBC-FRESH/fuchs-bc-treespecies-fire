# Audit pass 1: arithmetic and internal consistency

Date: 2026-11-21, on branch `feature/w1-draft` at commit `28b18cf`.
Scope: every number in the current draft that does not depend on the fire calibration.
Method: recompute each value from the named artifact, then compare with the text.

## Land base and study area

| Claim in text | Recomputed | Artifact | Result |
| --- | --- | --- | --- |
| 5.90 million ha of forest | 5,899,679.6 | `blocks.area_ha` sum | pass |
| 3.06 million ha managed | 3,060,473.1 | `IFM(managed)` blocks | pass |
| 2.84 million ha unmanaged | 2,839,206.5 | `IFM(unmanaged)` blocks | pass |
| 458,708 blocks | 458,708 | `blocks.parquet` rows | pass |
| 48 treatments, 10,326 curves, 99 accounts | 48, 10,326, 99 | compiled tables | pass |
| Published THLB 3,070,301 ha | 3,070,301 | 2017 AAC rationale | pass |
| Match within 0.3 percent | 0.32 percent | 9,828 / 3,070,301 | pass |

## Species shares

| Claim | Recomputed | Artifact | Result |
| --- | --- | --- | --- |
| Sx 44.9, Pl 29.4, Bl 16.3, At 5.3, Se 4.0, Ac 0.1 | same to one decimal | `feature.SpeciesProp.managed.*` at offset 0 | pass |
| Deciduous 5.4 percent of managed area | 5.39 | At + Ac over managed area | pass |
| Harvested Sx 45.2, Pl 31.3, Bl 14.7, At 5.3, Se 3.4, Ac 0.1 | same to one decimal | `experiments/tsa24-evenflow/species_periods.csv` | pass |
| Deciduous 5.4 percent of harvested volume | 5.37 | same | pass |

## Harvest level

| Claim | Recomputed | Artifact | Result |
| --- | --- | --- | --- |
| 51.9 million m3 per period | 51.89 mean of six seeds; 51.9 replayed | `experiments/tsa24-evenflow/summary.json` | pass |
| 5.19 million m3/yr | 5.189 | same | pass |
| Six seeds span 51.89 to 52.06 | 51.89 to 52.06 | same | pass |
| Replayed schedule 51.2 to 52.3 | 51.213 to 52.253 | same | pass |
| About 25 percent below 6,917,231 | 24.98 | 1 - 5.189/6.917 | pass |

## Yield reconciliation

| Claim | Recomputed | Artifact | Result |
| --- | --- | --- | --- |
| MAI 2.31 m3/ha/yr | 2.309 (2.308 at a 80-year floor) | compiled managed curves, area-weighted max MAI | pass |
| Implies 7.07 million m3/yr | 7.07 | 2.309 x 3,060,473 | pass |
| Within 2.5 percent of the cut per hectare | 2.5 | 2.309 / 2.253 | pass |

## Economics

| Claim | Recomputed | Artifact | Result |
| --- | --- | --- | --- |
| 1,037.9 million m3 harvested | 1,037.897 | `experiments/tsa24-evenflow/species_periods.csv` | pass |
| Revenue 112,776 million CAD | 112,776.1 | `valuation.total_revenue` | pass |
| Undiscounted net 62,270 million CAD | 62,270.2 | `valuation.net_value_by_period` sum | pass |
| NPV 8,779 million CAD at 3 percent | 8,778.8 | `valuation.npv` | pass |
| Conifer margin 56.81 to 64.79 | 56.81 to 64.79 | `unit_margin_cad_per_m3` | pass |
| Deciduous margin -2.25 | -2.25 | same | pass |
| Discount 5 percent gives 4,769, change -4,010 | 4,768.9, -4,010.0 | `valuation.npv_with_overrides` | pass |
| Discount 0 percent gives 62,270 | 62,270.2 | same | pass |
| Deciduous 35 and 40 give 8,752 and 8,805, plus or minus 26 | 8,752.4, 8,805.3, 26.4 | same | pass |
| Deciduous 61.74 gives +256 | 9,035.1, +256.3 | same | pass |
| Haul 117 km gives -184 | 8,595.2, -183.7 | same | pass |

## Internal consistency

| Check | Result |
| --- | --- |
| Every number in the text has a claims-register row | pass, except the fire section, marked pending |
| No superseded 70M figure remains in the narrative | pass (grep for 151518, 83465, 12248, 6786 returns nothing) |
| Enterprise described as a satisficing scheduler, not a profit maximiser | pass |
| Targets described as penalties, not constraints | pass |
| Tail claims comparative, with intervals | pass |
| LaTeX builds with 0 errors and 0 undefined references | pass, 19 pages |

## Findings to fix

None in the arithmetic. Two presentation issues remain and are not defects:

1. The abstract's fire sentence is a pending marker.
2. The results' composition subsection is a pending marker until the composition run is recorded.

## What this pass does not cover

- The fire comparison and CVaR, which depend on the calibration.
- Whether the official cut's transition profile is quoted correctly beyond the three values used
  (8.35, 7.35, 6.917 million m3/yr), which come from the BC TSA page.

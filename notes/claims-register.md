# Claims register

Rule: every number in the manuscript appears here with the artifact that produces it. A sentence
whose number is not in this table does not ship.

Status values: `verified` (reproduced from a committed artifact), `pending` (awaiting the fire
calibration), `to compute` (not yet produced).

## Landscape and estate

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Study area | TSA24, Prince George | `fresh-fuchs-ws4` ADR 0001 | verified |
| TSA gross area | about 7.97 million ha | BC Prince George TSA page, 2026-11-21 | verified |
| Blocks in the compiled estate | 458,708 | `notes/reference/tsa24-estate.md` | verified |
| Treatments, curves, accounts | 48, 10,326, 99 | same | verified |
| Official allowable cut | 6,917,231 m3/yr, effective 2025-08-28 | BC allowable annual cut table, verified 2026-11-21 | verified |
| Forested stand area in inventory | 6,016,466 ha | `tsa24.shp/stands.shp`, summed `area` over all features | verified |
| Species composition, stand area | Sx 33.1, Bl 25.3, Pl 24.0, At 6.9, Se 4.5, Fd 2.1, Ep 1.3, other conifers 2.8 percent | same, species code crosswalk to leading-species groups | verified |
| Deciduous share, stand area | 8.7 percent | same | verified |
| Harvested composition, reference schedule | Sx 46.7, Pl 29.5, Bl 14.8, At 5.8, Se 3.0, Ac 0.2 percent of harvested volume | `fresh-fuchs-ws4` `tests/data/tsa24_species_periods.csv` | verified |
| Deciduous share, harvested volume | 6.0 percent | same (`AT` + `ACT`) | verified |

## Even flow

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Periods | 20 periods of 10 years | `tests/data/tsa24_evenflow_periods.csv` | verified |
| Volume per period | 70,000,000 m3 | same | verified |
| Mean annual volume | 7,000,000 m3/yr | same | verified |
| Ratio to official cut | 1.012 | `tests/test_tsa24_validation.py` | verified |

## Economics

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Revenue | 151,518 million CAD | `scripts/valuation.py` on the fixture | verified |
| Log prices | 113.96 CAD/m3 (SPF), 105.98 (Hem-Bal) | `notes/reference/economics-constants.md` | verified |
| Harvest cost, tree-length ground system | 21.38 CAD/m3 | same | verified |
| Haul cost | 7.85 CAD/m3 at 90 km mean distance | same | verified |
| Silviculture cost | 10.02 CAD/m3, North Central zone | same | verified |
| Stumpage | 9.92 conifer, 0.50 deciduous CAD/m3 | same | verified |
| Discount rate | 3 percent real | same | verified |
| Undiscounted net | 83,465 million CAD | same | verified |
| NPV at 3 percent | 12,248 million CAD | same | verified |
| Conifer margin | 56.81 to 64.79 CAD/m3 | same | verified |
| Deciduous margin | -2.25 CAD/m3 | same | verified |
| Discount rate effect | 5 percent gives 6,786 million CAD | `notes/reference/economics-sensitivity.md` | verified |
| Deciduous price effect | -22 to +209 million CAD across 35 to 61.74 CAD/m3 | same | verified |
| Haul effect | -250 million CAD from 90 to 117 km | same | verified |

## Composition and rotation

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Sustainable cut ceiling (TSA29 mini) | about 31,990 m3/yr | `REPORT-H-anchor-reconciliation.md` | verified for TSA29 |
| Sustainable cut ceiling (TSA24 estate) | to compute | — | to compute |
| Rotation by allowable cut | non-monotonic: 149, 175, 180, 166 years | regulated LP surface | verified for TSA29 |
| Composition surface | to compute on TSA24 | — | to compute |

## Fire

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Historical fire sizes | 432 perimeters in 24 tiles, 1950 to 2024 | calibration repository, `tsa24-regime24/summary.json` | verified |
| Median, p90 | 22.97 ha, 490.17 ha | same | verified |
| p90 interval | 349 to 1,051 ha | `notes/reference/fire-tail-uncertainty.md` | verified |
| Share above 5,000 ha | 3.0 percent, interval 1.9 to 4.4 | same | verified |
| Simulated regime | region-level fit, 23 tiles | calibration repository, `tsa24-region-configs.json` | pending |
| CVaR by policy | to compute | — | to compute |

## Notes

- The TSA29 figures are retained for the anchor reconciliation but are **not** the paper's results.
  Anything derived from the 35,083 ha mini instance is out of scope for the manuscript.
- Fire claims are comparative; see ADR 0002.

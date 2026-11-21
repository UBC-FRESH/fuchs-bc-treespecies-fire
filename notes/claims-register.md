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
| Compiled forest area | 5,899,680 ha | `fresh-fuchs-ws4` `notes/reference/tsa24-thlb.md` | verified |
| Managed land base (model THLB) | 3,060,473 ha | same | verified |
| Unmanaged forest area | 2,839,207 ha | same | verified |
| Published THLB, 2017 base case | 3,070,301 ha | BC AAC rationale, October 2017 | verified |
| Model minus published THLB | -9,828 ha, -0.32 percent | same | verified |
| Species composition, managed area | Sx 44.9, Pl 29.4, Bl 16.3, At 5.3, Se 4.0, Ac 0.1 percent | `feature.SpeciesProp.managed.*` at offset 0 | verified |
| Deciduous share, managed area | 5.4 percent | same | verified |
| Harvested composition, model schedule | Sx 45.2, Pl 31.3, Bl 14.7, At 5.3, Se 3.4, Ac 0.1 percent of harvested volume | `fresh-fuchs-ws4` `experiments/tsa24-evenflow/species_periods.csv` | verified |
| Deciduous share, harvested volume | 5.4 percent | same (`AT` + `ACT`) | verified |

## Even flow

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Model-produced even flow | 51.89 to 52.06 million m3/period across six seeds; replayed schedule 51.2 to 52.3 | `fresh-fuchs-ws4` `experiments/tsa24-evenflow/summary.json` | verified |
| Model-produced mean annual volume | 5.19 million m3/yr | same | verified |
| Model-produced deciduous share | 5.4 percent | same | verified |
| Model-produced revenue, net, NPV | 112,776 / 62,270 / 8,779 million CAD | same | verified |
| Periods | 20 periods of 10 years | `tests/data/tsa24_evenflow_periods.csv` | verified as a fixture |
| Volume per period (benchmark fixture) | 70,000,000 m3 | same | **superseded**: fixture matches the target to 0.04 m3; the model sustains about 52M per period (`experiments/tsa24-evenflow/`) |
| Mean annual volume | 7,000,000 m3/yr | same | provenance unverified |
| Ratio to official cut | 1.012 | `tests/test_tsa24_validation.py` | provenance unverified |

## Economics

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Revenue (benchmark fixture) | 151,518 million CAD | `scripts/valuation.py` on the fixture | superseded by the model-produced schedule |
| Log prices | 113.96 CAD/m3 (SPF), 105.98 (Hem-Bal) | `notes/reference/economics-constants.md` | verified |
| Harvest cost, tree-length ground system | 21.38 CAD/m3 | same | verified |
| Haul cost | 7.85 CAD/m3 at 90 km mean distance | same | verified |
| Silviculture cost | 10.02 CAD/m3, North Central zone | same | verified |
| Stumpage | 9.92 conifer, 0.50 deciduous CAD/m3 | same | verified |
| Discount rate | 3 percent real | same | verified |
| Undiscounted net (benchmark fixture) | 83,465 million CAD | same | superseded by the model-produced schedule |
| NPV at 3 percent (benchmark fixture) | 12,248 million CAD | same | superseded by the model-produced schedule |
| Conifer margin | 56.81 to 64.79 CAD/m3 | same | verified |
| Deciduous margin | -2.25 CAD/m3 | same | verified |
| Discount rate effect (model schedule) | 5 percent gives 4,769 million CAD; 0 percent gives 62,270 million CAD | `fresh-fuchs-ws4` `experiments/tsa24-evenflow/summary.json` and `scripts/valuation.py` | verified |
| Deciduous price effect (model schedule) | -26 to +256 million CAD across 35 to 61.74 CAD/m3 | same | verified |
| Haul effect (model schedule) | -184 million CAD from 90 to 117 km | same | verified |

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

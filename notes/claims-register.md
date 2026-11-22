# Claims register

Rule: every number in the manuscript appears here with the artifact that produces it. A sentence
whose number is not in this table does not ship.

Status values: `verified` (reproduced from a committed artifact), `pending` (awaiting the fire
calibration), `to compute` (not yet produced).

## Landscape and estate

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Study area | TSA24, Prince George | `fresh-fuchs-ws4` ADR 0001 | verified |
| TSA gross area | about 7.97 million ha | `government_of_british_columbia_pg_rationale_2017` | verified |
| Blocks in the compiled estate | 458,708 | `notes/reference/tsa24-estate.md` | verified |
| Treatments, curves, accounts | 48, 10,326, 99 | same | verified |
| Official allowable cut | 6,917,231 m3/yr, effective 2025-08-28 | BC allowable annual cut table, verified 2026-11-21 | verified |
| Compiled forest area | 5,899,680 ha | `fresh-fuchs-ws4:notes/reference/tsa24-thlb.md` | verified |
| Managed land base (model THLB) | 3,060,473 ha | `fresh-fuchs-ws4:notes/reference/tsa24-thlb.md` | verified |
| Unmanaged forest area | 2,839,207 ha | `fresh-fuchs-ws4:notes/reference/tsa24-thlb.md` | verified |
| Published THLB, 2017 base case | 3,070,301 ha | `government_of_british_columbia_pg_rationale_2017` | verified |
| Model minus published THLB | -9,828 ha, -0.32 percent | `fresh-fuchs-ws4:notes/reference/tsa24-thlb.md` | verified |
| Area-weighted maximum MAI, model curves | 2.309 m3/ha/yr | `fresh-fuchs-ws4:notes/reference/tsa24-yield-reconciliation.md` | verified |
| Implied perennial yield on managed area | 7.07 million m3/yr | `fresh-fuchs-ws4:notes/reference/tsa24-yield-reconciliation.md` | verified |
| Model flat even flow | 5.19 million m3/yr | `experiments/tsa24-evenflow/summary.json` | verified |
| Cost of the flat-profile constraint | 1.88 million m3/yr | difference of the two above | verified |
| Total harvested volume | 1,037.9 million m3 | `experiments/tsa24-evenflow/species_periods.csv` | verified |
| Gap to official cut | 25 percent | 1 - 5.189/6.917 | verified |
| MAI above the cut per hectare | 2.5 percent | 2.309/2.253 | verified |
| Base even-flow weight | 10,000 (non-linear, reference period 1) | `experiments/tsa24-evenflow/evenflow_tsa24.yaml` (`min_weight: 10000`) | verified |
| Even-flow and level penalties | 1.3 to 2.7; about 515 | same | verified |
| 2017 transition profile | 8.35 then 7.35 million m3/yr; 6.917 in 2025 | `government_of_british_columbia_pg_rationale_2017`; AAC table | verified |
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
| Deciduous price effect (model schedule) | -26 to +26 million CAD across 35 to 40 CAD/m3 | same | verified |
| Haul effect (model schedule) | -184 million CAD from 90 to 117 km | same | verified |

## Composition

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Aspen supply ceiling | 3.20 million m3/period, 6.2 percent of a 5.18 million m3/yr total | `fresh-fuchs-ws4` `experiments/tsa24-composition/summary.json` | verified (15-minute local search, not converged) |
| Share response to target | 5.69 percent at weight 200; 5.94 percent at weight 100,000 (level 5.16) | same | verified |
| Target form | absolute aspen volume, 5.19 million m3/period, not a share | same | verified |
| Composition frontier | 8 percent implies 40.0 million m3/period; 10 percent 32.0; 15 percent 21.3; 6 percent is feasible at the sustained level | derived from the ceiling under constant aspen supply | verified |
| Cost of a 10 percent share | 38 percent of the sustained level | 1 - (3.20/0.10)/51.9 | verified |

## Rotation

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Realized rotation, baseline | 102.2 years area-weighted (median 100, p10-p90 60-160) | `experiments/tsa24-evenflow/rotation.json` | verified |
| Realized rotation, aspen-maximisation | 101.7 years | `experiments/tsa24-composition/rotation-aspen-max.json` | verified |
| Median managed age | 92 years area-weighted; 44 percent of managed area older than 100 years | both rotation artifacts | verified |
| Harvested area at a 102-year rotation | about 30,000 ha/yr | 3,060,473 / 102 | derived |
| Volume per harvested hectare | 173 m3/ha | 5.19 million / 30,000 | derived |

## Fire

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Historical fire sizes | 432 perimeters in 24 tiles, 1950 to 2024 | calibration repository, `tsa24-regime24/summary.json` | verified |
| Median, p90 | 22.97 ha, 490.17 ha | same | verified |
| p90 interval | 349 to 1,051 ha | `notes/reference/fire-tail-uncertainty.md` | verified |
| Share above 5,000 ha | 3.0 percent, interval 1.9 to 4.4 | same | verified |
| Share above 100 ha | 26.2 percent, interval 22.7 to 29.6 | `fresh-fuchs-ws4:notes/reports/p3-3-distribution-comparison.md` | verified |
| Share above 1,000 ha | 7.9 percent, interval 5.8 to 10.2 | same | verified |
| p95 | 1,918.88 ha, interval 1,415.35 to 2,955.33 | same | verified |
| Simulated regime | regional fit, 24 tiles plus median default; 3,450 fires | `fresh-fuchs-ws4` `notes/reports/p3-3-distribution-comparison.md`, WS4 commit `9918fb17` | verified |
| Simulated median, p90, p95 | 23.8, 361.5, 1,100.9 ha | same | verified |
| Simulated shares | above 100: 23.6 percent; above 500: 8.3; above 1,000: 5.5; above 5,000: 1.8 | same | verified |
| Simulated maximum | 20,770.4 ha | same | verified |
| Distribution verdict | median, p90 and share above 500 inside the historical interval; p95 below; shares above 1,000 and 5,000 at the lower edge | same | verified |
| Maximum | 20,770.4 ha simulated; historical 25,114.8 ha; interval one-sided and not used as a target | same | verified |
| Estate fire scenario | 24 ignitions, 1,331 fragments, 16,331 ha grown, 10,444 ha applied, ending volume 1,015.9 million m3 | `experiments/p3-fire/scenario-estate-01.json` | verified |
| Burned area per ignition | 680 ha grown, 435 ha applied | same, divided by 24 | verified |
| Policy risk ranking | not reported | paired ensemble: burned area 650 to 1,609 ha, ending volume varied in the third decimal of a percent | negative result, reported |
| Historical mean fire size | 512.9 ha | calibration `tsa24-regime24/summary.json` | verified |

## Notes

- The TSA29 figures are retained for the anchor reconciliation but are **not** the paper's results.
  Anything derived from the 35,083 ha mini instance is out of scope for the manuscript.
- Fire claims are comparative; see ADR 0002.

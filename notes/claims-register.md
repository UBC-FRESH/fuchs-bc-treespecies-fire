# Claims register

> Status note (2026-11-26): the AAC-level state convergence is the only production result cited
> in the manuscript. The earlier fixed-flow and fixed-plan rows below are retained as a historical
> archive and are not cited. No 60.7, 19:1, or ten-draw fire number may ship. The 6.935-6.938 mean
> includes the final reference period; the other 19 periods sit at the AAC, and the final period is
> 5.3 percent above the ceiling.

Rule: every number in the manuscript appears here with the artifact that produces it. A sentence
whose number is not in this table does not ship.

Status values: `verified` (reproduced from a committed artifact), `pending` (awaiting the fire
calibration), `to compute` (not yet produced).

## AAC-level revision (2026-11-26)

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| 2025 allowable annual cut | 6,917,231 m3/yr | BC AAC table; `government_of_british_columbia_aac_2026` | verified |
| State convergence | stage 1 lower-bound AAC minimum, nonlinear, weight 1, 1M; stage 2 even-flow vs final period (WS4 default reference) ±5 percent, weight 10,000, harvest plateau over 10 chunks of 50,000 iterations (0.1 percent harvest tolerance), 20M safety | `fresh-fuchs-ws4:experiments/plantation/enterprise/state/*/result.json`; `target-evenflow.yaml` | verified |
| CC level | 6.9354 Mm3/yr; 700,000 stage-2 iterations; converged | `.../state/cc/result.json` | verified |
| D26 level | 6.9384 Mm3/yr; 1,000,000 stage-2 iterations; converged | `.../state/cc_d26/result.json` | verified |
| D55 level | 6.9356 Mm3/yr; 750,000 stage-2 iterations; converged | `.../state/cc_d55/result.json` | verified |
| D84 level | 6.9355 Mm3/yr; 750,000 stage-2 iterations; converged | `.../state/cc_d84/result.json` | verified |
| Stage-1 harvest | CC 6.994, D26 7.359, D55 7.164, D84 7.183 Mm3/yr; all stage-1 lower-bound warm starts overshoot the AAC and did not converge | `.../state/*/result.json` stages | verified |
| Period profile | 19 periods at 6.91723 Mm3/yr (the AAC); final reference period 7.28 Mm3/yr (5.3 percent above the ceiling); 20-period mean 6.935-6.938 | `.../enterprise/prod-converged.json` period-species tables | verified |
| Total volume, 200 years | CC 1,387.1; D26 1,387.7; D55 1,387.1; D84 1,387.1 Mm3 | `.../enterprise/prod-converged.json` | verified |
| NPV3/NPV4/NPV5 | CC 11,628.4/8,295.7/6,306.5; D26 11,582.8/8,331.6/6,361.5; D55 11,329.9/8,256.4/6,349.9; D84 11,053.0/8,149.2/6,305.7 MCAD | same | verified |
| Delta NPV4 | D26 +36.0; D55 -39.3; D84 -146.5 MCAD | same | verified |
| Delta NPV by rate | D26 -45.6 at 3 percent, +55.0 at 5; D55 -298.5 at 3, +43.4 at 5; D84 -575.4 at 3, -0.8 at 5 | same | verified |
| Species volumes | CC SX 621.9, PLI 446.2, BL 189.7, AT 87.8, SE 38.9, ACT 2.6; D26 SX 773.6, PLI 241.4, BL 123.2, AT 213.4, SE 33.9, ACT 2.3; D55 SX 592.8, PLI 248.8, BL 127.0, AT 380.7, SE 35.6, ACT 2.2; D84 SX 437.7, PLI 247.0, BL 126.1, AT 506.1, SE 35.2, ACT 34.9 Mm3 | same | verified |
| Landscape deciduous share | CC 7.5; D26 15.7; D55 26.9; D84 36.6 percent | `.../enterprise/surface-converged-observed.json` | verified |
| Fire draws | 20 paired 200-year draws per scenario, seeds 101-120, same event sets across standards | `.../enterprise/surface-converged-observed.json`; `-calibrated.json` | verified |
| Observed fire, 4 percent | CC mean/CVaR20 172.5/221.1, net 8,074.6; D26 146.1/197.7, net 8,134.0; D55 126.6/173.9, net 8,082.5; D84 122.1/173.6, net 7,975.6 MCAD | `.../enterprise/surface-converged-observed-summary.json` | verified |
| Calibrated fire, 4 percent | CC 80.3/112.8, net 8,182.8; D26 55.0/89.1, net 8,242.5; D55 40.8/74.1, net 8,182.3; D84 37.7/73.5, net 8,075.7 MCAD | `.../enterprise/surface-converged-calibrated-summary.json` | verified |
| D26 CVaR difference | observed -23.4, calibrated -23.7; net +59.4/+59.7 MCAD | both summaries | verified |
| D55 CVaR difference | observed -47.2, calibrated -38.8; net +7.9/-0.5 MCAD | both summaries | verified |
| D84 CVaR difference | observed -47.5, calibrated -39.3; net -99.0/-107.2 MCAD | both summaries | verified |
| Cost per unit CVaR reduction | D55 0.83 observed, 1.01 calibrated; D84 3.08 observed, 3.73 calibrated MCAD no-fire cost per MCAD of CVaR20 reduction; 1 is break-even | both summaries | verified |
| Rate table | D26 obs/cal: 3% -4.1/-9.6, 4% +59.4/+59.7, 5% +70.6/+72.1, 8% +54.6/+56.1; D55: -221.6/-241.3, +7.9/-0.5, +76.5/+72.2, +86.2/+85.6; D84: -489.3/-514.6, -99.0/-107.2, +30.8/+27.6, +83.6/+82.8 MCAD | both summaries | verified |
| Rotation and treated area | 153,190 intervals; area-weighted mean 92.8 years, median 90, 10th-90th 60-140; treated area 5.56 Mha over 200 years, 27,797 ha/yr | `.../enterprise/rotation-converged.json` | verified |
| Volume per treated hectare | 249.5 m3/ha | `.../enterprise/rotation-converged.json` | verified |
| D55 ahead of D84 on net CVaR | at 3, 4, 5, 8 percent in both observed and calibrated scenarios; the 8 percent margin is 2.6 MCAD observed and 2.8 calibrated, a point estimate; D84's gross CVaR reduction is 0.5 MCAD larger calibrated and 0.3 larger observed | both summaries | verified |
| Paired bootstrap | 10,000 resamples, 95 percent intervals | `.../plantation/analyze_surface.py`; both summaries | verified |
| Paired bootstrap, 4 percent | D26 net +59.4 [55.9, 63.3] obs, +59.7 [57.8, 61.6] cal; D55 +7.9 [3.1, 13.7] obs, -0.5 [-2.9, 2.7] cal; D84 -99.0 [-102.7, -89.7] obs, -107.2 [-110.1, -102.0] cal MCAD | both summaries | verified |
| Aspen price, 4 percent | no-fire D26 +37.6/+36.0/+34.3; D55 -40.6/-39.3/-37.9; D84 -151.8/-146.5/-141.2 MCAD at 35/37.5/40 CAD/m3. Net CVaR D26 +57.8 to +61.1; D55 -2.2 to +9.5; D84 -112.8 to -93.4 | `.../enterprise/sensitivity-converged.json`; both fire summaries | verified |
| Haul, 4 percent | CC NPV4 8,295.7 at 90 km and 7,956.6 at 117 km (-339.1); standard differences unchanged at +36.0/-39.3/-146.5 MCAD | same | verified |
| Terminal period | excluding the final even-flow reference period: D26 +36.3, D55 -38.4, D84 -145.1 MCAD vs CC, within 1.4 MCAD of the full-horizon deltas | same | verified |
| Fragments with VRI fuel type | 438,601 | `.../t0-fuel-validation.json` | verified |
| Post-fire succession | burned stand re-typed from surviving cohorts; post-fire succession not modelled | `notes/reports/p4-dynamic-fuel.md` | verified |
| Calibrated fractional reduction | D55/D84 34 percent calibrated vs 21 percent observed, relative to CC CVaR20 loss (112.8 vs 221.1) | both summaries | derived |
| Fuel projection, t=0 | 63.1 percent from compiled AU composition; 66.7 percent from VRI conifer share; conifer classes 86 percent of disagreements; projection never produces C7/M2/M4 while the VRI grid carries all three; S1/O1B have no VRI counterpart | `.../t0-fuel-validation.json`; `notes/reports/p4-dynamic-fuel.md` | verified |
| Observed fire sizes | mean 704.5, median 23.7, p90 695.9, p95 2,047, max 72,317 ha; over-5,000 3.0 percent | `.../fire-regime/summary.json` | verified |
| Calibrated retention sizes | 3,450 sizes; mean 278.9, median 29.3, p90 379.5, p95 892.6, max 23,356.9 ha; over-5,000 1.10 percent | `.../fire/calibrated-retention-sizes.json` | verified |
| Severity range, D84 | 0.10-0.49 across floor 0.1-0.4 and wind 6.8-25 km/h | `.../severity-sensitivity.csv` | verified |
| Severity range, D55 | 1.01-1.04 | same | verified |
| Severity range, D26 (M2) | 1.03-1.24 | same | verified |
| Multi-year weather | 720 states; C1 median 1.112 (p10-p90 0.817-1.312), M1 1.033, C2 1.312; D1 0.267 at all states | `.../fire/severity-weather-range.json` | verified |
| Crown-closure floor | 5 percent for planted stands on pre-harvest fragments with VRI crown closure below 5 percent | `scripts/fuel_state.py` | verified |

> **Historical archive (not cited).** Everything below this line predates the AAC-level convergence and is retained for audit only. The manuscript uses only the AAC-level rows above.

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
| Model flat even flow | 5.19 million m3/yr | `experiments/tsa24-evenflow/summary.json` | superseded: the state-based convergence reaches 6.935-6.938; 5.19 was a fixed-flow GA search |
| Cost of the flat-profile constraint | 1.88 million m3/yr | difference of the two above | superseded |
| Total harvested volume | 1,037.9 million m3 | `experiments/tsa24-evenflow/species_periods.csv` | superseded; converged CC is 1,387.1 |
| Gap to official cut | 25 percent | 1 - 5.189/6.917 | superseded; retained only as the foil for the corrected search |
| MAI above the cut per hectare | 2.5 percent | 2.309/2.253 | verified |
| Base even-flow weight | 10,000 (non-linear, reference period 1) | `experiments/tsa24-evenflow/evenflow_tsa24.yaml` (`min_weight: 10000`) | verified |
| Even-flow and level penalties | 1.3 to 2.7; about 515 | same | verified |
| 2017 transition profile | 8.35 then 7.35 million m3/yr; 6.917 in 2025 | `government_of_british_columbia_pg_rationale_2017`; AAC table | verified |
| Species composition, managed area | Sx 44.9, Pl 29.4, Bl 16.3, At 5.3, Se 4.0, Ac 0.1 percent | `feature.SpeciesProp.managed.*` at offset 0 | verified |
| Deciduous share, managed area | 5.4 percent | same | verified |
| Harvested composition, model schedule | Sx 45.2, Pl 31.3, Bl 14.7, At 5.3, Se 3.4, Ac 0.1 percent of harvested volume | `fresh-fuchs-ws4` `experiments/tsa24-evenflow/species_periods.csv` | superseded by the converged species table |
| Deciduous share, harvested volume | 5.4 percent | same (`AT` + `ACT`) | superseded; converged CC is 6.5 |

## Even flow

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Model-produced even flow | 51.89 to 52.06 million m3/period across six seeds; replayed schedule 51.2 to 52.3 | `fresh-fuchs-ws4` `experiments/tsa24-evenflow/summary.json` | superseded; fixed-flow GA search |
| Model-produced mean annual volume | 5.19 million m3/yr | same | superseded |
| Model-produced deciduous share | 5.4 percent | same | superseded |
| Model-produced revenue, net, NPV | 112,776 / 62,270 / 8,779 million CAD | same | superseded |
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
| Discount rate effect (model schedule) | 5 percent gives 4,769 million CAD; 0 percent gives 62,270 million CAD | `fresh-fuchs-ws4` `experiments/tsa24-evenflow/summary.json` and `scripts/valuation.py` | superseded; see the converged NPV table |
| Deciduous price effect (model schedule) | -26 to +26 million CAD across 35 to 40 CAD/m3 | same | superseded; see `sensitivity-converged.json` |
| Haul effect (model schedule) | -184 million CAD from 90 to 117 km | same | superseded; converged schedule is -339.1 |

## Composition

**Superseded 2026-11-23.** These runs used a dataset with one treatment, `CC`, which
regenerates the same analysis unit. The 6.2 percent ceiling is a supply limit of that
instrument, not a biophysical limit. The deciduous-forward stocking standards can regenerate
conifer sites to aspen; see the next section.

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Aspen supply ceiling | 3.20 million m3/period, 6.2 percent of a 5.18 million m3/yr total | `fresh-fuchs-ws4` `experiments/tsa24-composition/summary.json` | verified (15-minute local search, not converged) |
| Share response to target | 5.69 percent at weight 200; 5.94 percent at weight 100,000 (level 5.16) | same | verified |
| Target form | absolute aspen volume, 5.19 million m3/period, not a share | same | verified |
| Composition frontier | 8 percent implies 40.0 million m3/period; 10 percent 32.0; 15 percent 21.3; 6 percent is feasible at the sustained level | derived from the ceiling under constant aspen supply | verified |
| Cost of a 10 percent share | 38 percent of the sustained level | 1 - (3.20/0.10)/51.9 | verified |

## Stocking standards and fuel projection

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| New plantation prescriptions | `CC_D26`, `CC_D55`, `CC_D84`: 26, 55, 84 percent deciduous targets | `fresh-fuchs-ws4` `experiments/plantation/stocking-summary.json` | verified |
| Compiled treatments, policy datasets | D26 39 (30 CC + 9 D26), D55 36 (24 CC + 12 D55), D84 33 (18 CC + 15 D84); CC baseline 48 | `.../derived/enterprise/compiled-cc_d26-summary.json` etc. | verified |
| Regenerated composition, conifer block | CC SX 83 / BL 17 (evaluated); D26 AT 26 / SX 74 (target); D55 AT 55 / SX 45 (target); D84 AT 84 / SX 16 (evaluated) | `experiments/plantation/build_stocking_recipe.py`; block 451 evaluation | verified |
| Species reset | regenerated cohorts take the target track's composition | WS4 `feature/species-harvest-account` commit `cc4dd8d6`; 14 management tests | verified |
| Fuel mapping, aspen VRI stands | 529 polygons at least 80 percent deciduous, 25+ years: 100 percent D1 | `fresh-fuchs-ws4` `experiments/plantation/vri-fuel-types.json` | verified |
| Fuel mapping, mixedwood VRI stands | 171 polygons 40-60 percent deciduous: M1 54 percent, M2 46 percent | same | verified |
| Fuel mapping, 20-30 percent deciduous | 357 polygons: C1 49, C2 28, C3 11, C4 10 percent; no M type | same | verified |
| Calibrated mixedwood threshold | 30 percent on both sides; BC 2017 uses 20 percent (sensitivity) | `scripts/fuel_projection.py` | verified |
| t=0 reproduction from AU composition | 63.1 percent agreement with the operational grid (VRI conifer: 66.7) | `fresh-fuchs-ws4` `experiments/plantation/t0-fuel-validation.json` | verified |
| TIPSY vs VRI crown closure | mean difference +17.3 percentage points, MAE 23.0, correlation 0.004, n=272,840 | same | verified |
| Severity normalizer, initial landscape | 0.7496 | same | verified |
| Severity multiplier, D84 (D1, 16 percent conifer) | 0.267 at the calibration weather | same; `experiments/plantation/severity-sensitivity.csv` | verified |
| Severity multiplier, D55 (M1, 45 percent conifer) | 1.011 | same | verified |
| Severity multiplier, D26 (C2/C1 under the calibrated rule) | 1.299 / 0.749 | same | verified |
| BC 20 percent threshold, D26 | M2, 1.203 | same | verified (sensitivity) |
| Policy surface | 3 harvest levels x 4 standards, 10 draws, 200 years, paired historical regime | `fresh-fuchs-ws4` `experiments/plantation/surface-ensemble.json` | superseded; see the AAC-level 20-draw surface |
| Fire loss, CC 100 percent | mean 243.8 M CAD (2.78 percent), CVaR20 304.3 M CAD (3.47 percent) | same | superseded; 20-draw surface below |
| Fire loss, D26 100 percent | mean 243.8 M CAD, CVaR20 304.3 M CAD; no risk change | same | superseded; 20-draw surface below |
| Fire loss, D55 100 percent | mean 238.5 M CAD, CVaR20 298.6 M CAD | same | verified |
| Fire loss, D84 100 percent | mean 236.3 M CAD, CVaR20 296.2 M CAD | same | verified |
| D84 CVaR20 reduction, 100 percent level | -8.1 M CAD (95 percent bootstrap interval -8.8 to -5.9) at a production cost of -153.8 M CAD; exchange rate 19.0 | same | superseded; 20-draw surface below |
| D84 CVaR20 reduction, 80 percent level | -6.4 M CAD at -123.0 M CAD; exchange rate 19.2 | same | superseded; 20-draw surface below |
| D84 CVaR20 reduction, 60 percent level | -4.9 M CAD at -93.4 M CAD; exchange rate 18.9 | same | verified |
| D55 CVaR20 reduction, 100 percent level | -5.7 M CAD (95 percent bootstrap interval -6.2 to -4.1) at -107.6 M CAD; exchange rate 19.0 | same | superseded; 20-draw surface below |
| Landscape deciduous share, 100 percent | CC 7.5, D26 16.7, D55 28.8, D84 39.7 percent | `fresh-fuchs-ws4` `experiments/plantation/no-fire/no-fire.json` | verified |
| Stand-level severity multiplier | D1 0.267, M1 1.011, C2 1.299, C1 0.749 | same | verified |
| No-fire baseline, CC 100 percent | 8,778.8 M CAD, 1,037.9 M m3; reproduces the P4 baseline exactly | `experiments/plantation/no-fire/no-fire.json` | verified |
| D26 minus CC, 100 percent level | +1.0 M CAD, +53.3 M m3; the standard is free volume under the calibrated mapping | same | superseded; 20-draw surface below |
| D55 minus CC, 100 percent level | -107.6 M CAD, -21.9 M m3 | same | verified |
| D84 minus CC, 100 percent level | -153.8 M CAD, -23.8 M m3 | same | superseded; 20-draw surface below |
| D84 minus CC, 80 percent level | -123.0 M CAD, -19.0 M m3 | same | superseded; 20-draw surface below |
| D84 minus CC, 60 percent level | -93.4 M CAD, -14.4 M m3 | same | verified |

## Rotation

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Realized rotation, baseline | 102.2 years area-weighted (median 100, p10-p90 60-160) | `experiments/tsa24-evenflow/rotation.json` | superseded; converged is 92.8 |
| Realized rotation, aspen-maximisation | 101.7 years | `experiments/tsa24-composition/rotation-aspen-max.json` | verified |
| Median managed age | 92 years area-weighted; 44 percent of managed area older than 100 years | both rotation artifacts | verified |
| Harvested area at a 102-year rotation | about 30,000 ha/yr | 3,060,473 / 102 | superseded; converged treated area is 27,797 ha/yr |
| Volume per harvested hectare | 173 m3/ha | 5.19 million / 30,000 | superseded; converged is 249.5 per treated hectare |

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
| Simulated regime | regional fit, 24 tiles plus median default; 3,450 fires | `fresh-fuchs-ws4` `notes/reports/p3-3-distribution-comparison.md`, WS4 commit `9918fb17` | superseded by P164.9 multi-year retention |
| Simulated median, p90, p95 | 23.8, 361.5, 1,100.9 ha | same | superseded by P164.9 multi-year retention |
| Simulated shares | above 100: 23.6 percent; above 500: 8.3; above 1,000: 5.5; above 5,000: 1.8 | same | superseded by P164.9 multi-year retention |
| Simulated maximum | 20,770.4 ha | same | superseded by P164.9 multi-year retention |
| Distribution verdict | median, p90 and share above 500 inside the historical interval; p95 below; shares above 1,000 and 5,000 at the lower edge | same | superseded by P164.9 multi-year retention |
| Maximum | 20,770.4 ha simulated; historical 25,114.8 ha; interval one-sided and not used as a target | same | superseded by P164.9 multi-year retention |
| Estate fire scenario | 24 ignitions, 1,331 fragments, 16,331 ha grown, 10,444 ha applied, ending volume 1,015.9 million m3 | `experiments/p3-fire/scenario-estate-01.json` | verified |
| Burned area per ignition | 680 ha grown, 435 ha applied | same, divided by 24 | verified |
| Policy risk ranking, uniform-severity baseline | superseded; the P4 exposure result was 260.9 M mean / 323.3 M CVaR20 under uniform mortality | `fresh-fuchs-ws4` `experiments/p4-risk/npv-ensemble.json` | superseded by the severity-model surface |
| Historical mean fire size | 512.9 ha | calibration `tsa24-regime24/summary.json` | verified |
| Burned area per 200-year draw | 1.61 to 2.41 M ha, 27 to 41 percent of the compiled forest | `fresh-fuchs-ws4` `experiments/plantation/surface-ensemble.json` | verified |

### Multi-year calibration and the fire-model bound (2026-11-24)

| Claim | Value | Artifact | Status |
| --- | --- | --- | --- |
| Multi-year calibration | 1950--2024 weather; 690 retained records (3,450 sizes at five draws each) from 720 potential-weather states; reference median 29.9, p90 370.1, p95 833.4, over-5,000 1.0 percent, max 24,147.1 ha | `fresh_ws4_fire_regime_repro:results/region-retention-summary.json` | verified |
| Calibration transfer | in-sample 1.337; potential/weather analogue 4.456; training median 5.873; temporal event median absolute bias 89.3 percent | `region-retention-multiyear-all.json`, `event-simulations-retention-pre2018.json` | verified |
| Full TSA fire record | 1,073 fires, 14.31 per year, 10,079 ha/yr, mean 704.5 ha, max 72,317 ha | `fresh-fuchs-ws4:experiments/fire-regime/tsa24-fire-history.json` | verified |
| Record versus calibration | the full record includes fires outside the 24 calibration tiles; the calibration is a 24-tile subset, max 25,114.8 ha | same; `region-retention-summary.json` | verified |
| Calibrated size sample replay | 3,450 sizes; median 29.3, p95 892.6, over-5,000 1.10 percent, max 23,356.9 ha | `fresh-fuchs-ws4:experiments/plantation/fire/calibrated-retention-sizes.json` | verified |
| Weather range, D1 | 0.267 at all 720 potential-fire weather states | `fresh-fuchs-ws4:experiments/plantation/fire/severity-weather-range.json` | verified |
| Weather range, C1 | median 1.112, 10th--90th 0.817--1.312; single state 0.749 (10th percentile) | same | verified |
| Weather range, M1 | median 1.033, 10th--90th 0.376--1.253; single state 1.011 | same | verified |
| Weather range, C2 | median 1.312, 10th--90th 1.245--1.331; single state 1.299 | same | verified |
| Observed-record 20-draw surface, 4 percent | CC mean 135.1, CVaR20 175.4; D84 mean 132.8, CVaR20 173.0; D84 difference -2.4 M CVaR at -50.3 M fixed-plan, ratio 20.9 (18.6--24.8); CVaR of net NPV -47.9 M | `fresh-fuchs-ws4:experiments/plantation/surface-20-summary.json`, `fire-surface-bounds.json` | superseded; see the AAC-level surface |
| Calibrated-retention 20-draw surface, 4 percent | CC mean 62.8, CVaR20 89.2; D84 mean 61.8, CVaR20 88.2; D84 difference -1.0 M CVaR at -50.3 M fixed-plan, ratio 52.4 (43.7--56.7); CVaR of net NPV -49.4 M | `fresh-fuchs-ws4:experiments/plantation/surface-20-calibrated-summary.json`, `fire-surface-bounds.json` | superseded; see the AAC-level surface |
| Floor 0.1 surface, 4 percent | D84 ΔCVaR -2.33, break-even 21.6; D55 -1.59/22.0; D26 +0.06 | `fresh-fuchs-ws4:experiments/plantation/surface-20-floor010-summary.json` | verified |
| Floor 0.4 surface, 4 percent | D84 ΔCVaR -2.56, break-even 19.7; D55 -1.85/18.9; D26 -0.02 | `fresh-fuchs-ws4:experiments/plantation/surface-20-floor040-summary.json` | verified |
| Threshold 20 percent surface, 4 percent | D84 ΔCVaR -2.43, break-even 20.7; D55 -1.70/20.5; D26 +0.42 penalty | `fresh-fuchs-ws4:experiments/plantation/surface-20-mixed020-summary.json` | verified |
| Observed D84 break-even by rate | 20.3 at 3 percent, 20.9 at 4, 24.2 at 5, 28.2 at 8 | `fresh-fuchs-ws4:experiments/plantation/surface-20-summary.json` | verified |
| Calibrated D84 break-even by rate | 49.9 at 3 percent, 52.4 at 4, 54.8 at 5, 61.7 at 8 | `fresh-fuchs-ws4:experiments/plantation/surface-20-calibrated-summary.json` | verified |
| Enterprise D84 cost and break-even | 60.6 M CAD at 4 percent; 25.1 per 1 M CVaR reduction if the fixed-plan fire benefit is held | `fresh-fuchs-ws4:experiments/plantation/enterprise/no-fire-enterprise.json` | superseded; converged D84 is -146.5 and 3.7 |

## Notes

- The TSA29 figures are retained for the anchor reconciliation but are **not** the paper's results.
  Anything derived from the 35,083 ha mini instance is out of scope for the manuscript.
- Fire claims are comparative; see ADR 0002.

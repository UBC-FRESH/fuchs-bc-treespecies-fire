# Dynamic fuel methods: working text for the manuscript

Status: working note 2026-11-23. The numbers are in `notes/claims-register.md`; the model is in
`fresh-fuchs-ws4:notes/reports/p4-dynamic-fuel.md`.

## Stocking standards

We add three plantation prescriptions to the FEMIC recipe. Each prescription transitions a
harvested analysis unit to a target analysis unit whose managed species-proportion curves
specify the desired mixture: 26, 55, or 84 percent deciduous. The WS4 management process
resets the regenerated cohorts to the target track's composition; without that step the track
changes but the species do not. The historical clearcut regenerates the same analysis unit,
which is 0 to 26 percent deciduous depending on the source. A standard is applied only where
it increases the deciduous share, so aspen blocks stay on the historical treatment.

The instrument is a policy lever, not a yield assumption: the target analysis units carry
their own managed yield curves, and the realized volume and value are outcomes of the
simulation.

## Fuel projection

The operational 2025 VRI fuel type is the baseline for every unharvested stand. For a
harvested stand we follow the BC fuel-typing chronology: slash (S1) for 0-5 years, open
herb/grass (O1B) for 6-24 years, and the species-based forest type from year 25. The forest
type uses the calibrated VRI-to-FBP mapping, with the 30 percent mixedwood threshold that the
fire calibration used. The BC 2017 algorithm's 20 percent threshold is a sensitivity.

We do not re-type the whole estate. Re-typing every stand from the compiled analysis-unit
composition reproduces only 63.1 percent of the operational grid, because the compiled dataset
carries one species mix per analysis unit while the VRI grid carries one per polygon. The
baseline grid therefore stays operational; only the states the policy creates are projected.

The mapping is consistent with the operational layer on real VRI stands: 529 polygons at
least 80 percent deciduous (25+ years) are all D1; 171 polygons at 40-60 percent deciduous are
M1 or M2; 357 polygons at 20-30 percent deciduous are conifer types, not mixedwood.

## Severity

A fire that reaches a stand kills a fraction of its biomass. We compute the FBP crown
fraction burned (CFB) for the stand's fuel type under the calibration weather (FFMC 93.8,
BUI 108.2, wind 6.8 km/h) and map it onto the model's severity bounds:

```
raw severity = 0.2 + 0.8 * CFB
```

We normalize by the initial-landscape area-weighted mean (0.7496), so a multiplier of 1.0 is
the calibrated landscape mean. The multiplier scales the burned-area mortality fraction in the
growth-fire adapter. The mapping is conditional: fire size and ignition frequency remain the
recorded 1950-2024 regime. Composition changes how severely a fire burns, not how large it
grows.

The gradient is non-linear. Under the calibrated 30 percent threshold, a 26 percent
deciduous standard stays on the conifer side (C2/C1) and does not reduce severity. A 55
percent standard is M1 and roughly neutral (1.011). Only an 84 percent standard becomes D1 and
cuts the multiplier to 0.267. Under the BC 20 percent threshold, the 26 percent standard
becomes M2 and reaches 1.203, still only 7 percent below closed spruce.

## Fire regime and risk metric

The fire regime is the full TSA24 record: 1,073 perimeters, 1950-2024, 14.31 fires/yr, sizes
sampled from the record. Each 200-year draw generates one event set and applies it to every
policy, so the policy comparison is paired. The no-fire NPV is evaluated once per policy; the
fire loss is the difference between the with-fire and no-fire NPV. CVaR20 is the mean of the
two worst of ten draws. Tail statements are comparative, with sampling uncertainty (ADR 0002).

## Policy surface

Three harvest levels (100, 80, and 60 percent of the committed even-flow schedule, as a
deterministic block sample that keeps each block's full harvest history) by four standards
(CC, D26, D55, D84). The no-fire baseline gives the production and value cost; the paired fire
ensemble gives the mean and tail loss. The surface is the answer to RQ1.

## What the model does not do

- Composition does not change fire size or ignition frequency. The historical size
  distribution is held fixed.
- The early post-harvest phases are identical across standards, so the measured effect is a
  lower bound.
- FBP D1 has no crown fuel, so the model cannot represent a severe surface fire in aspen. The
  deciduous severity is a floor.
- Post-fire fuel succession is not modelled; a burned stand is re-typed from its surviving
  cohorts.
- The severity mapping is an assumption. Report the 0.2 floor, weather, and CFB-to-mortality
  sensitivity.

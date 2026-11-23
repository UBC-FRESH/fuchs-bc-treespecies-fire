# Dynamic fuel results: working tables for the manuscript

Status: working note 2026-11-23. No-fire numbers are final; fire numbers are filled when the
paired ensemble finishes. The model is `fresh-fuchs-ws4:notes/reports/p4-dynamic-fuel.md`; the
claims are in `notes/claims-register.md`.

## No-fire surface

| Harvest level | Standard | NPV (M CAD) | Volume (M m3) | NPV vs CC (M CAD) | Volume vs CC (M m3) |
| ---: | --- | ---: | ---: | ---: | ---: |
| 100 % | CC | 8,778.8 | 1,037.9 | 0.0 | 0.0 |
| 100 % | D26 | 8,779.8 | 1,091.2 | +1.0 | +53.3 |
| 100 % | D55 | 8,671.2 | 1,016.0 | -107.6 | -21.9 |
| 100 % | D84 | 8,625.0 | 1,014.1 | -153.8 | -23.8 |
| 80 % | CC | 7,015.6 | 829.7 | 0.0 | 0.0 |
| 80 % | D26 | 7,016.5 | 872.2 | +0.8 | +42.5 |
| 80 % | D55 | 6,929.6 | 812.2 | -86.0 | -17.5 |
| 80 % | D84 | 6,892.6 | 810.7 | -123.0 | -19.0 |
| 60 % | CC | 5,247.6 | 620.7 | 0.0 | 0.0 |
| 60 % | D26 | 5,248.1 | 652.6 | +0.5 | +32.0 |
| 60 % | D55 | 5,182.4 | 607.4 | -65.2 | -13.2 |
| 60 % | D84 | 5,154.2 | 606.3 | -93.4 | -14.4 |

The CC 100 percent row reproduces the P4 baseline exactly (8,778.8 M CAD, 1,037.9 M m3), which
validates the species-reset branch and the no-fire bridge.

## Reading the production side

- **D26 is free volume.** It adds 32-53 M m3 and does not reduce NPV. The aspen yield curves
  add volume; the low aspen price offsets the value. The standard does not change the fuel
  type under the calibrated 30 percent mixedwood threshold (it stays C2/C1), so it buys no
  fire benefit. It is a production option, not a risk option.
- **D55 costs about 1.2 percent of NPV** and loses 1.3-2.1 percent of volume. Its fuel type is
  M1 and the severity multiplier is 1.011, essentially neutral. It is dominated by D26 on
  production and by CC on simplicity.
- **D84 costs about 1.8 percent of NPV** and loses about 2 percent of volume. Its fuel type is
  D1 and the severity multiplier is 0.267. It is the only standard with a material fire
  benefit.

The production costs are smaller than the old CC-only composition analysis implied, because
the new instrument can convert conifer sites rather than being limited to the existing aspen
supply.

## Fire surface

Ten paired draws of the full 1,073-fire regime, 200 years, composition-aware severity. The
four-draw correction (a 5 percent crown floor for planted stands, after 2,590 fallback events in
the first pass) has **zero** fuel-projection errors; the surface values are unchanged at the
reported precision.

| Harvest level | Standard | Mean loss (M CAD) | CVaR20 (M CAD) | Mean loss (%) | CVaR20 (%) |
| ---: | --- | ---: | ---: | ---: | ---: |
| 100 % | CC | 243.8 | 304.3 | 2.78 | 3.47 |
| 100 % | D26 | 243.8 | 304.3 | 2.78 | 3.47 |
| 100 % | D55 | 238.5 | 298.6 | 2.75 | 3.44 |
| 100 % | D84 | 236.3 | 296.2 | 2.74 | 3.43 |
| 80 % | CC | 193.2 | 239.7 | 2.75 | 3.42 |
| 80 % | D26 | 193.3 | 239.7 | 2.76 | 3.42 |
| 80 % | D55 | 189.1 | 235.2 | 2.73 | 3.39 |
| 80 % | D84 | 187.3 | 233.2 | 2.72 | 3.38 |
| 60 % | CC | 144.7 | 179.3 | 2.76 | 3.42 |
| 60 % | D26 | 144.7 | 179.4 | 2.76 | 3.42 |
| 60 % | D55 | 141.5 | 175.9 | 2.73 | 3.39 |
| 60 % | D84 | 140.2 | 174.4 | 2.72 | 3.38 |

## Reading the fire side

- **D26 is not a risk instrument.** Its fuel type is C2/C1 under the calibrated 30 percent
  threshold, and its CVaR20 is indistinguishable from CC (+0.01 M at 100 percent). It is a
  free-volume option with a real composition change: landscape deciduous share rises from
  7.5 to 16.7 percent without changing fire severity.
- **D55 and D84 are a priced tail hedge.** D55 cuts CVaR20 by 5.7 M at a production cost of
  107.6 M; D84 cuts it by 8.1 M at 153.8 M. The exchange rate is about **19 M CAD of
  production cost per 1 M CAD of CVaR20 reduction**, and it is remarkably stable across
  levels (18.9 to 19.2) and standards.
- The stand-level severity cut is large (D1 0.267), but the estate-level mean loss falls only
  from 243.8 to 236.3 M (3.1 percent) and CVaR20 from 304.3 to 296.2 M (2.7 percent). The
  reasons are structural: the unmanaged half of the estate keeps its VRI fuel, the standard
  converts stands gradually over the horizon, the conversion starts with a 25-year slash/open
  phase, and the NPV loss is dominated by early, discounted fires.
- The old P4 exposure baseline (260.9 M mean, 323.3 M CVaR20) is not the new CC baseline. The
  new model applies the VRI fuel-type severity multipliers; the new CC baseline is 243.8 M /
  304.3 M. The two are different models, not a policy effect.

## Policy reading

- A risk-neutral planner chooses **D26**: more volume, same NPV, same fire risk.
- A planner who values a 1 M CAD reduction in CVaR20 at more than about **19 M CAD** chooses
  D84. That is a very high marginal value of tail risk; the historical regime alone does not
  justify it.
- D55 lies on the same frontier as D84; it is not dominated, but it is an intermediate point,
  not a distinct strategy.
- The result is conditional on the recorded regime and the severity mapping. A more severe
  future regime, a larger managed fraction, a higher deciduous price, or a carbon value would
  move the exchange rate. The paper should state the conditions, not claim a universal
  ranking.

## What the manuscript should claim

1. The stocking standard is the policy lever; composition is an outcome, not an exogenous
   aspiration.
2. The fuel projection is consistent with the operational VRI layer; the calibrated 30 percent
   threshold makes D26 a conifer type, and the BC 20 percent sensitivity gives it M2 but only
   a 7 percent severity reduction.
3. The severity gradient is non-linear; only the aspen-dominated standard cuts the FBP crown
   fraction burned materially.
4. The surface reports a **conditional** policy ranking. The fire regime is the recorded
   1950-2024 distribution; composition changes severity, not fire size. Fire-break placement
   remains out of scope.
5. The production cost of D84 is small relative to the estate NPV; whether it is worth paying
   depends on the tail benefit and the planner's risk attitude. Report the paired CVaR
   difference with its sampling interval (ADR 0002).

# AUDIT-07: stocking-standard surface and the revised manuscript

Date: 2026-11-23. Scope: the manuscript at `feature/w1-draft` after the dynamic-fuel and
stocking-standard revision. Evidence: `fresh-fuchs-ws4` at `feature/p4-risk`, the WS4 branch
`feature/species-harvest-account` (`9848c210`), and the artifacts named below.

## Verified numbers

| Claim | Manuscript | Artifact | Verdict |
| --- | ---: | --- | --- |
| CC 100 % no-fire NPV / volume | 8,778.8 M CAD / 1,037.9 M m3 | `experiments/plantation/no-fire/no-fire.json` | verified |
| D26 100 % no-fire NPV / volume | 8,779.8 / 1,091.2 | same | verified |
| D55 100 % no-fire NPV / volume | 8,671.2 / 1,016.0 | same | verified |
| D84 100 % no-fire NPV / volume | 8,625.0 / 1,014.1 | same | verified |
| CC 100 % mean / CVaR20 loss | 243.8 / 304.3 M CAD | `surface-ensemble.json` | verified |
| D84 100 % mean / CVaR20 loss | 236.3 / 296.2 M CAD | same | verified |
| D55 100 % CVaR20 | 298.6 M CAD | same | verified |
| D84 CVaR20 difference | -8.1 M, 95 % bootstrap -8.8 to -5.9 | `surface.csv` | verified |
| D55 CVaR20 difference | -5.7 M, 95 % bootstrap -6.2 to -4.1 | same | verified |
| D26 CVaR20 difference | +0.03 M, bootstrap 0.00 to 0.09 | same | verified |
| D84 exchange rate, 100 % | 19.0 | -153.8 / -8.1 | verified |
| D84 exchange rate, 80 / 60 % | 19.2 / 18.9 | same | verified |
| Estate mean loss reduction | 3.1 % (243.8 to 236.3) | same | verified |
| Estate CVaR reduction | 2.7 % (304.3 to 296.2) | same | verified |
| Severity multipliers | 0.267 / 1.011 / 1.299 / 0.749 | `severity-sensitivity.csv`; note | verified |
| Normalizer | 0.7496 | `surface-ensemble.json` | verified |
| VRI mapping | 529 D1, 171 M1/M2, 357 conifer | `vri-fuel-types.json` | verified |
| t=0 agreement | 63.1 % (VRI conifer 66.7) | `t0-fuel-validation.json` | verified |
| TIPSY vs VRI crown | +17.3 pp, MAE 23.0, r=0.004, n=272,840 | same | verified |
| Fire regime | 1,073 fires, 14.31/yr, 10,079 ha/yr | `experiments/fire-regime/` | verified |

## Consistency

- The abstract, introduction, methods, results, discussion, conclusion, supplement, and cover
  letter all use the stocking-standard framing. No stale "composition is supply-limited" or "no
  policy ranking" claim remains, except the explicitly superseded historical statement.
- The old P4 uniform-mortality baseline (260.9 / 323.3 M CAD) is identified as a different model,
  not as a policy effect. The new CC baseline is 243.8 / 304.3 M CAD.
- The rotation claim is correctly narrowed: 102.2 vs 101.7 years is a property of the historical
  clearcut, not of the new standards; the new standards are evaluated on a fixed schedule.
- The fire-break question (RQ2) is declared open in the introduction, limitations, and conclusion.
- The fixed-plan design is stated in the introduction, methods, and limitations; the enterprise
  does not re-optimise per standard.
- The severity model is stated as conditional: it changes the severity of a fire that reaches a
  stand, not fire size or ignition frequency.
- The low-crown 5 percent floor and the 2,590 first-pass fallback calls are documented in the
  methods; the corrected surface has zero fallback events.

## Findings

1. **No blocking error.** The central exchange rate is robust to the low-crown correction: the
   corrected four-draw values are unchanged at the reported precision.
2. **Resolved provenance.** The landscape composition values (7.5, 16.7, 28.8, 39.7 percent)
   were checked against a deterministic no-fire rerun with the composition record. The values
   match at the reported precision, and the no-fire net present value and volume reproduce
   exactly. The claims register now cites `no-fire.json`.
3. **Major, correctly scoped.** The fixed-plan design does not re-optimise the enterprise
   schedule. The D84 production cost may change under a full response; the paper states this as
   the main production-side limitation. Do not describe the surface as a partial-equilibrium
   policy evaluation.
4. **Minor.** The abstract says the 26 percent standard has "no change in CVaR20." The point is
   +0.03 M with a bootstrap interval of 0.00 to 0.09; "no detectable change" is more precise. The
   results and discussion already say "indistinguishable."
5. **Minor.** The fire table caption says CVaR20 is the mean of the two worst draws; the text's
   bootstrap intervals are for the **paired difference**, not for the table's individual CVaR.
   The current wording distinguishes them; keep it that way.
6. **Minor.** The title says "a calibrated fire scenario." The paper now uses the recorded
   regime plus a calibrated model for validation and coupling. The title is not false; consider
   "recorded fire regime" in the final title if the journal allows a change.
7. **Minor.** The cover letter still uses the current title and the four contributions; it is
   consistent with the manuscript.

## Post-audit copyedit

A sentence-by-sentence editorial pass removed the remaining project-process language that a
co-author or referee would flag: ADR and phase labels, the abandoned FVS plan, commit hashes,
work-host and companion-repository references, internal file paths, solver diagnostics and
validator output, the superseded CC-only and aspen-max analyses, the 5 percent crown-floor
debugging paragraph, and the ten-item limitation list. The abstract and introduction were
condensed to three questions; the title subtitle now names the stocking-standard, production, and
tail-risk trade-offs; spelling is British throughout. No number changed. The PDF is 26 pages,
and a full-text check returns zero matches for ADR, P4, FVS, commit hashes, work host, companion,
benchmark, aspen-max, CC-only, and the old baseline comparisons. A final numerical check corrected
two denominators: the burned-area share is 27 to 41 percent of the compiled forest, not of the
managed estate, and the D55 volume loss is about 2.1 percent at every harvest level, not a
1.3-to-2.1 range.

## Verdict

**Submittable.** The model,
the numbers, the tail interval, and the limitations are in place. The paper's claim is narrow and
supported: the composition-aware severity mechanism works, D26 is free volume, D84 is a priced
tail hedge at about 19 to 1, and the fire-break placement question remains open.

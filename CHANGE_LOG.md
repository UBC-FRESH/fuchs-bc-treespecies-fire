# Change log

Newest entries last.

## 2026-11-21

- Imported the Overleaf project to GitHub (`a21882d Initial Overleaf Import`) and cloned it into
  the working environment.
- Added the paper plan (`planning/paper-plan.md`) and the claims register
  (`notes/claims-register.md`), plus `AGENTS.md` and this roadmap, so the manuscript follows the
  same planning and evidence discipline as `fresh_daugherty_manuscript`.
- Recorded the reconciliation problem in the plan: the draft's methods describe a 10,000 ha
  Williams Lake subset and WS3, while the model and results are TSA24 and WS4.
- Completed W0.2 (#3). Rewrote `text/2_methods.tex` for TSA24 and WS4: study area and species composition from the stand inventory, the bilevel formulation, the compiled estate, the fire scenario with its calibration and tail uncertainty, and the sourced economics. Added four bibliography entries for the prior European work and three for data and model sources. Declared the SI unit `\year`, which siunitx does not provide and which was breaking every volume-per-year quantity. Manuscript compiles with 0 errors and 0 undefined references. The study-area figure still shows the old Williams Lake area and is flagged in the text.
- Verified every number added by W0.2 against a source before closing the task. The harvested-composition column in the species table was traced to `fresh-fuchs-ws4/tests/data/tsa24_species_periods.csv` (Sx 46.7, Pl 29.5, Bl 14.8, At 5.8, Se 3.0, Ac 0.2 percent of harvested volume); the table now labels cottonwood separately instead of folding it into "others", and the claims register records the composition, prices, and costs with their artifacts. Manuscript compiles with 0 errors and 0 undefined references.

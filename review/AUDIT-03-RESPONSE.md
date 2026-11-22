# Response to the antagonistic review (AUDIT-03)

Date: 2026-11-22. Every must-fix is addressed below; the manuscript was rewritten, not patched
around.

## Reframing

The paper no longer claims a bilevel policy optimization or CVaR of NPV. It is a **two-layer
scenario analysis**: the composition aspiration is exogenous and hypothetical, the enterprise is a
satisficing goal program, and risk is reported as **volume-at-risk** on paired draws. The lead
result is the composition--production trade-off (5.4 to about 6.2 percent at no cost in level; a
10 percent share costs 38 percent of the harvest).

## Must-fix dispositions

| ID | Disposition |
| --- | --- |
| M1 CVaR/NPV-at-risk unsupported | Removed from abstract, methods, discussion, conclusion, keywords. Methods define volume-at-risk and state that NPV-at-risk needs species-resolved accounts. |
| M2 No policy comparison under fire | Contribution rewritten around what is delivered: estate validation, composition frontier, rotation invariance, calibrated fire comparison, one coupling run. The paired volume-at-risk ensemble is reported as a paired comparison, not a policy ranking. |
| M3 Composition frontier wrong at 6 percent, weights misdescribed | Table column now reads "level at which the share is reached"; 6 percent is stated as feasible at the sustained level. Weights 200 and 100,000; the 500-fold increase is over the 200 run; the 100,000 run's level is 5.16, stated. Absolute aspen target disclosed. |
| M4 Fire table and abstract overclaim | Abstract and results claim median, p90, and share above 500 inside the interval only. Table adds share above 100 and 1,000, states n=3,450, states the simulated values were not bootstrapped, and marks the maximum interval one-sided and not used. |
| M5 Methods describe a model not run | Leader min-CVaR equation deleted. Enterprise equation deleted and replaced by a description of the one-sided penalty goal program, including the even-flow term. "Highest even flow" replaced by "six searches converged to a plateau". "Policies are compared" replaced by the actual single coupling run and paired ensemble. |
| M6 Yield bridge not a validation | Rewritten as an upper-bound consistency check; "reproduce the published productivity" removed from the abstract; 0.32 percent stated; median age corrected to the area-weighted 92 years, sourced to `rotation.json`. Transition profile cited. |
| M7 Missing register rows and dead artifact paths | Added rows for total harvested volume, median managed age, historical mean, per-ignition areas, weights and realized level, frontier assumptions, rotation artifact, and the transition profile. External notes are prefixed `fresh-fuchs-ws4`. Rotation now has a tested script and a committed artifact. |
| M8 Limitations say seven, list five | Nine limitations, including the missing fire-risk policy result and the volume-only risk metric. |
| M9 Data/code availability overclaims | Declarations cite the API commit `9918fb17` and handoff `474dca6e`; calibration archive stated as companion study; supplement distinguishes the benchmark target from the model schedule. |
| M10 Gap not established | Added verified fuel-treatment and bilevel fuel-treatment references (Chung 2015; Wei 2012; Lagos et al. 2025) and narrowed the claim to what we know. |
| M11 Title, author block, date, keywords, abstract overpromise | Title given a scoped subtitle; working-title and author-order notes removed; fixed date; keywords revised; abstract rewritten. |
| M12 BC policy setting unsourced/misdescribed | Introduction now states that the AAC is a maximum, that silviculture is constrained by prescriptions and stocking standards, and that the composition aspiration is a hypothetical instrument. Cites the 2017 rationale. |

## Should-fix dispositions

- **S1 figures**: the two-level diagram, composition figure, and fire ECDF are not added; the portal
  and the tables carry the content. A figure pass remains before submission.
- **S2 discussion length**: rewritten from about 1,700 to about 1,500 words, with the European
  comparison stated once.
- **S3 fire table**: n, bootstrapping, and additional shares added.
- **S4 units**: per-period and per-year quantities are now labelled in every table.
- **S5 price mapping**: subalpine fir priced on Hem-Bal, stated in the methods.
- **S6 no composition NPV**: "economically favourable mixtures" removed with the old RQs.
- **S7 stale reference notes**: the code-repo notes still carry the benchmark fixture; the manuscript
  no longer cites them for current numbers.
- **S8 validation**: softened to "passes the validator, which checks schema invariants".
- **S9 fire limits**: in-sample, 24 ignitions, one weather season, current fuels, clearcut only, five
  dropped blocks; all in methods and limitations.
- **S10 cover letter**: title and numbers aligned.

## Still open before submission

1. The paired volume-at-risk ensemble must finish and its numbers enter the risk subsection.
2. Figures 2--4 remain to be produced.
3. Author order, funding wording, and journal remain author decisions.

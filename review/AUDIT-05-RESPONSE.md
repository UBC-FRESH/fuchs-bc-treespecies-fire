# Response to the third audit (AUDIT-05)

| ID | Fix |
| --- | --- |
| F1 173 m3/ha dimension error | Rewritten: 173 m3/ha is 73 percent of the 236 m3/ha that the area-weighted maximum MAI accumulates over a 102-year rotation. |
| F2 Categorical flow-rule attribution | Three places changed to "we interpret ... as the cost"; the abstract and introduction already carried the caveat. |
| F3 Dead register paths and wrong citations | `tsa24-thlb.md` and `tsa24-yield-reconciliation.md` restored onto the P4 branch (they existed only on the P1 audit branch). Weight row cites the benchmark target; share-above-100 cites P3.3; simulated shares above 100 and 1,000 added. |
| F4 Composition code and tables absent | Declarations and supplement now state exactly what is archived: baseline schedule, species-period table, composition summaries, fire record, valuation/rotation code, sensitivity runs; composition run directories remain on the work host. |
| F5 NPV exclusions | Added to methods and to the prices limitation: operating margin excluding road construction, administration, taxes, and risk premia. |
| S1 Undocumented "twice the level weight" | Rewritten as "weight 200 against a level weight of 100". |
| S2 Rotation-invariance overgeneralisation | Limited to "between the baseline and aspen-maximisation schedules" in results, discussion, introduction, and cover letter. |
| S3 p90 "reproduces" vs "lower edge" | Methods, results, and discussion now say the p90 sits at the lower edge; "central distribution consistent with the record". |
| S4 Supplement 6.20 vs 6.18 | Corrected to 6.18 percent. |

Verification: `pdflatex` builds with 0 errors, 0 undefined references, 0 overfull boxes.

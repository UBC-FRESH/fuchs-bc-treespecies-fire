# Cover letter (draft)

Status: draft, 2026-11-24. Before submission:

- [ ] choose the journal and replace `[Journal]`
- [ ] replace the bracketed scope sentence with the journal's remit
- [ ] confirm every author's approval
- [ ] confirm the funding statement in the manuscript

---

Dear Editor,

We submit for consideration in *[Journal]* the manuscript **"Deciduous-forward stocking standards
under a recorded fire regime: production and tail-risk trade-offs in the Prince George Timber Supply
Area"**.

The paper asks what deciduous-forward post-clearcut stocking standards cost in wood supply and
value, and whether the resulting composition changes fire severity and the tail of net present
value on a real management unit. It makes four contributions.

First, it reconciles the estate and the harvest level, and it tests the obvious explanation of the
gap. The compiled TSA~24 managed area matches the published timber harvesting land base to within
0.32 percent, but the model realises 5.19 million m3/yr under a flat even flow, about 25 percent
below the 2025 allowable annual cut. A 300-iteration simulated-annealing search at the official 2017
transition profile also realises about 5.2 million m3/yr. The shortfall is therefore not a flat-flow
artifact; the compiled land base and yield curves are the leading explanation. We report this as a
model result, not as a feasibility proof.

Second, it implements three deciduous-forward standards (26, 55, and 84 percent deciduous on
eligible treated stands) and an enterprise response: the even-flow schedule is re-optimised under
each standard. D26 adds 52.9 million m3, all aspen; net conifer volume is flat. At the fixed plan it
is a 0.5 million CAD gain, but the enterprise search turns it into a 1.4 million CAD cost. D55 and
D84 cost 42.5 and 60.6 million CAD in the enterprise response, about 0.7 and 1.0 percent of the CC
net present value. The realised landscape deciduous shares are 7.5, 16.7, 28.8, and 39.7 percent.

Third, it reports the production and tail-risk surface with the correct risk metric. The 84 percent
standard reduces the conditional fire loss by 2.4 million CAD at a fixed-plan cost of 50.3 million
CAD, a break-even of 20.9. But CVaR is translation-invariant: the CVaR of net present value is 47.9
million CAD lower, because the standard lowers the no-fire value by more than it lowers the loss. At
the enterprise cost of 60.6 million CAD, holding the fixed-plan fire benefit, the net CVaR is 58.2
million CAD lower and the break-even is 25.1. D84 is not a tail hedge. The result is conditional on
the recorded 1,073-fire regime; composition changes the severity of a fire that reaches a stand, not
the number or size of fires.

Fourth, it states the fire-model boundary. The policy surface uses the full observed fire-size
record. A calibrated-retention scenario, built from the companion multi-year 1950--2024 calibration,
replaces the observed sizes with 3,450 retained sizes. That scenario has a higher median but a lower
upper tail; it gives a smaller D84 benefit (1.0 million CAD) and a higher break-even (52.4). The
observed record is the more favourable of the two, so the conclusion is conservative with respect to
the calibrated model. The composition-aware fuel projection reproduces 63.1 percent of the 2025 VRI
fuel-type grid at t=0; the post-harvest types have no observational counterpart, and the D1 severity
multiplier is the model's 0.2 surface-mortality floor, not an estimate of D1 severity. The
fire-break placement question remains open.

The work continues the line of research on diversification under disturbance risk in European
forests (Fuchs et al., 2024, *Scientific Reports*), with two differences that matter for policy: the
disturbance is a process with spatial structure, and the decisions are made on an operating forest
under an allowable cut.

The manuscript is original and is not under consideration elsewhere. The authors declare no
financial competing interests; one author develops the open-source estate model used in the work,
which is declared in the manuscript.

Yours sincerely,

Jasper M. Fuchs, on behalf of the authors
ETH Zurich and University of British Columbia

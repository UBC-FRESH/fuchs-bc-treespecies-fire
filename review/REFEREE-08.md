# Referee pass 08: the central economic claim

Status: recorded 2026-11-23. Read-only hostile referee pass on `text/0_abstract.tex`
through `text/6_declarations.tex`, `text/99_online_supplement.tex`, and
`notes/claims-register.md`. Verdict: reject in present form.

## The finding that changes the paper

The paper defines CVaR20 as the mean loss in the worst two of ten draws. Net NPV is
no-fire NPV minus that loss, and CVaR is translation-invariant:

    CVaR20(net NPV) = no-fire NPV - CVaR20(loss)

At the ten-draw surface values:

| Policy | No-fire NPV | CVaR20 loss | CVaR20 net NPV |
| --- | ---: | ---: | ---: |
| CC | 8,778.8 | 304.3 | 8,474.5 |
| D84 | 8,625.0 | 296.2 | 8,328.8 |

D84 is **145.7 million CAD worse** in the tail of net NPV, not a hedge. The 8.1 million
is a reduction in the conditional fire loss; the 153.8 million is a reduction in certain
value. The 19:1 ratio is a cost per unit of conditional-loss reduction for a planner who
treats loss reduction as a separate objective. It is not a marginal rate of substitution
between certain value and tail risk.

The paper's own working note already said the historical regime alone does not justify
the 19:1. The manuscript turned the break-even into a recommendation. That is the
overclaim to remove.

## The other nine findings

1. Ten draws cannot identify CVaR20: it is the mean of two draws, and the bootstrap only
   resamples the same ten event sets. The ratio interval from the reported CVaR interval is
   about 17 to 26, not 18.9 to 19.2. The 60 and 80 percent cases are nested block
   subsamples of the same schedule, so the near-constant ratio is a scaling identity.
2. The event set is not the full record: fire sizes are resampled with replacement, annual
   counts are Poisson(14.31), and each fire is placed on a random burnable cell. The
   manuscript must say this.
3. The discount rate and aspen price sensitivities are missing from the surface. The
   no-fire table is at 3 percent only, while the discussion says the discount rate is the
   most important lever.
4. D84's 0.267 is the 0.2 surface-mortality floor, not an estimate of D1 severity. The
   multiplier ranges 0.11 to 0.49 over the documented floor and wind range. The CVaR
   benefit and the ratio are conditional on the floor and are an upper bound, not a point
   estimate.
5. The 63.1 percent fuel projection is a t=0 comparison, not a validation. The full
   crosstab shows confusion in the mixedwood and deciduous classes, and the post-harvest
   classes have no observational counterpart. The TIPSY-VRI crown-closure comparison is
   +17.3 percentage points with r = 0.004.
6. D26's "no fire benefit" is a weighted average of C1 (0.749) and C2 (1.299) assignments
   driven by pre-harvest crown closure, not a property of the 26 percent standard. D55
   reduces CVaR20 by 5.7 million, about 70 percent of D84's 8.1 at about 70 percent of the
   cost; it is not dominated by D26. The three standards are a three-point sample.
7. The fixed schedule does not support "the enterprise responds." The abstract and
   conclusion say the enterprise responds; the methods say it does not re-optimise. The
   enterprise response experiment is the fix.
8. "Free volume" is an all-aspen swap: D26 adds 53.3 million m3, all aspen; conifer volume
   is flat. The +1.0 million NPV is within the aspen-price uncertainty. It is not free
   conifer volume.
9. The 7.07 million m3/yr maximum MAI is an upper bound, not a harvest level. The official
   2017 transition profile starts at 8.35 million m3/yr, above that bound. The gap from
   the official cut is not solely the flow rule until a declining-profile counterfactual is
   run.

## Response

- Rerun the surface with 100 draws and four policies (CC, D26, D55, D84) at the 100
  percent level. Drop the nested 60/80 percent scaling cases from the main surface.
- Record decade-by-species volumes for every draw and revalue at 3, 4, 5, and 8 percent
  and at 35, 37.5, and 40 CAD/m3 aspen.
- Use the BC Ministry of Forests 4 percent real rate as the base for public-sector forestry
  investment analysis (BC silviculture training module, Lesson 4; Heaps and Pratt 1989
  recommend 3 to 5 percent). Report 3 percent as the federal social rate for environmental
  analysis, and 8 percent as the federal opportunity cost of capital. No rate is "best";
  the choice is normative and the range is shown.
- Build the four enterprise-response datasets and re-optimise the even-flow schedule under
  each standard. The fixed-plan surface becomes a direct-effect comparison, not the main
  claim.
- Run a declining-profile counterfactual to test the flow-rule attribution.
- Propagate the severity floor (0.1 and 0.4) and the BC 20 percent mixedwood threshold to
  the CVaR result.
- Rewrite the abstract, results, discussion, and conclusion around the corrected metric:
  D84 is not a tail hedge on timber value; it is a cost-effectiveness buy that requires a
  separate loss-reduction objective worth more than about 19:1.

## What does not change

The physical model, the calibration, the land base, the fire regime, and the measured
volumes. The change is in the economic interpretation and in the uncertainty statement.

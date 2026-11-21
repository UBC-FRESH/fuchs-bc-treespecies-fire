# Roadmap: fuchs-bc-treespecies-fire

Plan of record. One phase is one parent issue; one task is one child issue. Keep this file in step
with the issues and `CHANGE_LOG.md`.

## Issue Tracker Map

| Phase | Parent issue | Branch | Status |
| --- | --- | --- | --- |
| W0 Plan and reconcile the design | #1 | `feature/w0-plan` | complete |
| W1 Draft the manuscript | #5 | `feature/w1-draft` | active |
| W2 Audit the claims | #6 | `feature/w2-audit` | planned |
| W3 Submit | #7 | `feature/w3-submit` | planned |

## Phase W0: Plan and reconcile the design

Parent issue: #1
Branch: `feature/w0-plan`
Status: complete

Goal: fix the paper's argument, and reconcile the existing draft with where the model actually went.

- [x] W0.1 Write the paper plan and the claims register (#2)
- [x] W0.2 Reconcile the methods section with TSA24 and WS4 (#3)
- [x] W0.3 Decide the disposition of RQ2 (broadleaf fire breaks) (#4)

Acceptance criteria:

The plan and register exist, the methods section names the same landscape and model as the results,
and every research question has a stated analysis or an explicit limitation.

## Phase W1: Draft the manuscript

Parent issue: #5
Branch: `feature/w1-draft`
Status: active

Goal: a complete draft in which no section is an empty stub.

- [x] W1.1 Introduction (#9)
- [ ] W1.2 Methods
- [ ] W1.3 Results
- [ ] W1.4 Discussion and conclusion (#12)
- [ ] W1.5 Abstract (#13)

Acceptance criteria:

Every section has prose, every number is either final or marked pending and registered, and the
argument runs from the research questions to the conclusions without a gap.

## Phase W2: Audit the claims

Parent issue: #6
Branch: `feature/w2-audit`
Status: planned

Goal: every number recomputed from tracked records, by a reader trying to reject the paper.

- [ ] W2.1 Referee pass 1: internal consistency and arithmetic
- [ ] W2.2 Referee pass 2: claims against artifacts
- [ ] W2.3 Referee pass 3: hostile reading of the argument

Acceptance criteria:

Each pass is recorded in `review/` with its findings, the defects are fixed, and no claim lacks a
register row.

## Phase W3: Submit

Parent issue: #7
Branch: `feature/w3-submit`
Status: planned

Goal: a submission package the maintainer approves.

- [ ] W3.1 Submission package and declarations
- [ ] W3.2 Maintainer approval and submission

Acceptance criteria:

The package is complete, the register is fully verified, and the maintainer approved in writing.

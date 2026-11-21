# AGENTS.md

Working contract for the manuscript repository. Keep it short.

This repository is the manuscript for the Fuchs/WS4 paper: a bilevel policy model of forest
management under fire risk on the TSA24 landscape in British Columbia. The code and results live
in `UBC-FRESH/fresh-fuchs-ws4`; this repository holds only the paper.

## Session start

1. This file.
2. `ROADMAP.md`: the active phase.
3. `CHANGE_LOG.md`: the newest entries.
4. `planning/paper-plan.md` and `notes/claims-register.md`.

## Rules

- **Every number cites an artifact.** If a sentence carries a number, it has a row in
  `notes/claims-register.md` naming the committed artifact that produces it. No row, no shipment.
- **No placeholder survives submission.** Numbers that are not final are marked `\pending{...}` in
  the LaTeX and listed in the register as `pending` or `to compute`.
- **Fire is a scenario, not a prediction.** Tail claims are comparative and carry sampling
  uncertainty. This follows ADR 0002 in `fresh-fuchs-ws4`.
- **The model's parameters are not negotiable in prose.** If the text disagrees with the code, the
  text changes.
- **One bounded move per step.** Draft one section, or run one audit pass, then report.
- **Evidence over trust.** Cite commits, file paths, and command output.
- **Sanitized output.** No private data, credentials, or machine-specific paths.

## Review process

Modelled on `fresh_daugherty_manuscript`: after the draft is complete, run successive antagonistic
referee passes that recompute every number from tracked records. A pass that finds nothing is
evidence of a weak pass, not of a strong paper. Record each pass in `review/`.

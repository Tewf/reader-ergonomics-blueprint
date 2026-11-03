# 0005: Three checks, each its own CI step

**Decision:** the form of the topics, the link from a topic to a Lean declaration and the proof are three checks, each
its own step in CI.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/b9732b9814c71768f722691f3c5049ec2b8ed378/shapes/decision-record.md).

## Context

- A missing declaration, a failing proof and a malformed topic are three findings with three fixes.
- The first and second are exact and cheap; the third is costly and runs after them.

## Decision

- The topic check, then `checks/local/lean_link.py`, then `lake build` after `lake exe cache get`, failing on any `sorry`.
- The link check reads names, not meaning; it never calls Lean.
- Not in this build: comparator and a challenge file, and any model in the loop.

## Consequences

- A broken link is reported in seconds, before the long build.
- **Bad:** a name can exist and still prove another statement; only a person's audit of the statement catches that.

## See also

[Decisions](README.md); [the design](../design/first-build.md).

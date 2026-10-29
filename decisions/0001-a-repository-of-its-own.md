# 0001: A repository of its own

**Decision:** the AI-augmented strand is a repository of its own, carrying its history from reader-ergonomics-topic,
and it pins a release of the topic and of the standard by commit.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/shapes/decision-record.md).

## Context

- The strand began on a branch of reader-ergonomics-topic and joined its master as that repository's extension
  ([topic record 0012](https://github.com/Tewf/reader-ergonomics-topic/blob/092ae2fc2e07226b695e219e3eb14b40286faa25/decisions/0012-ai-augmented-topic-as-an-extension.md)).
- Its subject, checking reasoning, is what the topic's scope leaves out, and it is about to grow code and a proof
  assistant in CI while the topic stays stable. The maintainer moved it out the same day
  ([topic record 0016](https://github.com/Tewf/reader-ergonomics-topic/blob/092ae2fc2e07226b695e219e3eb14b40286faa25/decisions/0016-move-the-ai-augmented-strand-out.md)).

## Decision

- Its two folders came with their git history: the loop, now the front page, and the review of autoformalization.
- It pins reader-ergonomics-topic v0.6.0 and reader-ergonomics v1.13.0, each by commit; it links to neither from above.
- Its scope is the maintainer's: reasoning written as topics, a checker per part, Lean first, a model that interprets
  and guides and decides nothing.

## Consequences

- The topic is a dependency here, not a host: it is the second repository of the family to pin it, after
  reader-ergonomics-learning.
- **Bad:** a change to the topic reaches this repository only when its pin moves, and the history before the move
  lives in two repositories.

## See also

[Decisions](README.md); [0002](0002-call-it-a-blueprint.md), the name.

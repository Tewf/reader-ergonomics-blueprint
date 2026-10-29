# Contributing to this repository

For anyone changing this repository, person or language model. To apply the reader-ergonomics standard elsewhere,
read its [standard.md](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/standard.md); this file is about this repository only.

## Before writing

1. Read the standard at the release this repository checks against (v1.13.0), then the
   [topic](https://github.com/Tewf/reader-ergonomics-topic/blob/092ae2fc2e07226b695e219e3eb14b40286faa25/shapes/topic.md) (reader-ergonomics-topic v0.6.0), which every document here follows.
2. Every document here is a topic: a title, a summary right after it, and a line in its parent that lists it with
   that summary. A new folder gets a README.md, listed by the README above it, and a one-line `index.qmd` that
   includes it, because the site generator skips README files.
3. The scope is on the front page. A checker other than Lean waits for a review of assurance cases
   ([0002](decisions/0002-call-it-a-blueprint.md)).

## Rules for claims

- Every claim carries a grade: **measured**, **supported with caveat**, **convention** or **not supported**. A grade
  moves only with a cited source.
- Cite as `Author Year`; the entry goes once into [evidence/bibliography.md](evidence/bibliography.md), with a DOI,
  an arXiv id or a stable URL. A key names one work across the family (reader-ergonomics decision 0003): the family is
  listed under `[bibliography_keys]` in checks/config.toml, and CI checks every key against its bibliographies.
- Evidence against a rule goes into the review's `against.md`, never deleted to make a rule look stronger.
- A number read in a summary rather than in the source is marked "(secondary)".

## The model's place

- In the loop, and in the work on this repository: a model explains, proposes and translates; it decides nothing,
  and never splits the person's reasoning for them. Its output is checked by a program or read by the maintainer.

## Links

- Down to reader-ergonomics and to the topic: pinned to each release's commit, as CI is.
- Up: none.

## Before handing back

Run the checks against the release CI uses, extracted inside this repository, in `checks/out/standard`, which git and
the checks both skip:

```sh
rm -rf checks/out/standard && mkdir -p checks/out/standard
git -C ../reader-ergonomics archive 7a76cc6 | tar -x -C checks/out/standard   # the commit checks.yml pins
python3 checks/out/standard/checks/run.py . --tiers program,meaning --judge flag   # the repository, as CI runs it
```

- Fix every error. Read every warning.
- Answer the questions in `checks/out/needs-judgment.md` in `checks/judgments.toml`, each answer quoting in backticks
  a word or heading of its own file; a reason is never copied from another file's answer unread.
- Keep [llms.txt](llms.txt), [README.md](README.md) and [README.fr.md](README.fr.md) in step.
- A pin raise goes in [CHANGELOG.md](CHANGELOG.md), not in decisions/.

## House conventions

- No em dash or en dash in prose; use a comma, a colon, parentheses, or a hyphen for ranges.
- Commit messages follow the standard's commit shape: a subject of at most 72 characters, then why.
- A choice that shapes the repository gets a record in [decisions/](decisions/).
- The maintainer decides every push.

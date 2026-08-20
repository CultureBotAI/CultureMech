---
name: fetch-source
description: Robust curl pattern for `fetch-<source>` justfile recipes that download an external data release into data/raw/. Use whenever writing a new fetch-* recipe, or auditing/fixing an existing one that fails intermittently in CI — a bare `curl -o` with no retry or timeout turns one flaky network blip into a red PR.
---

# Fetch a source release

## The pattern

```
curl -fL \
  --retry 5 \
  --retry-delay 20 \
  --max-time <seconds> \
  -o <output-path> \
  "<url>"
```

- **`-f`** — fail on an HTTP error status (4xx/5xx) instead of writing the
  error page to disk as if it were data. Without this, a broken URL silently
  "succeeds," and the failure surfaces later and confusingly, when seeding
  chokes on malformed content.
- **`-L`** — follow redirects. Many source hosts (Zenodo, GitLab/GitHub raw,
  institutional mirrors) redirect at least once.
- **`--retry 5 --retry-delay 20`** — retry transient network failures (reset
  connections, 5xx, timeouts) instead of failing the whole `fetch-*` recipe —
  and therefore the PR — on one bad minute. A `fetch-*` recipe with no retry
  logic reds every consumer's CI on a single flaky network blip; this is the
  standard mitigation.
- **`--max-time <seconds>`** — a hard cap so a hung connection doesn't block
  CI indefinitely. Size it to the source: tens of seconds for a small file,
  up to the low thousands for a large bulk release.
- **`-o <output-path>`** — explicit output path. Don't rely on `-O`/`-J`
  remote-naming, which breaks silently when a URL has no clean trailing
  filename component (query strings, percent-encoded path segments).
- **Quote the URL.** Source URLs frequently contain characters (`%2F`, `?`,
  `&`) that an unquoted shell argument will word-split or glob-expand.

## Example

```
curl -fL \
  --retry 5 \
  --retry-delay 20 \
  --max-time 120 \
  -o data/raw/goldData.xlsx \
  "https://forge.univ-lyon1.fr/api/v4/projects/p1801153%2FProjet-M2/repository/files/GOLD%2Fdata%2FgoldData.xlsx/raw?ref=main"
```

## Wiring it into a justfile recipe

```
fetch-<source>:
    mkdir -p data/raw
    curl -fL --retry 5 --retry-delay 20 --max-time <seconds> \
      -o data/raw/<file> \
      "<url>"
```

For a recipe that fetches several files, repeat the full `curl` invocation
per file rather than looping over a list — each invocation keeps its own
`--max-time` budget and failure explicit and independently retryable, instead
of one shared timeout across an unknown number of files.

## When NOT to use this pattern

An API that requires pagination, auth headers, or JSON-body construction is
not a `fetch-*` justfile recipe's job — that belongs in the seeding/ingestion
script itself, in the language the rest of the pipeline is written in, with
its own retry/backoff appropriate to that API's semantics (rate limits,
pagination cursors, partial-failure handling). This pattern is for a single
bulk file (or small fixed set of files) fetched once per release.

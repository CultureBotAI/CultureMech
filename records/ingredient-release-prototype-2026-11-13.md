# Catalog ingredient release prototype — 2026-11-13

Request: verify the M5 CultureMech catalog-wide ingredient list, establish a
reproducible skill/method, and prepare the CultureMech → MIM SSSOM → KG-Microbe
release path as a prototype for later Mech transforms.

## Observed starting state

Read-only inspection found an existing `list-ingredients` skill and native
aggregation command. M5 CultureMech was at
`199cd9191881e8e929cd95ea0ed13aabe388e58c`; current upstream checked via GitHub
was `7b1d460ce57a66cb7fb10452ecc90e8bc48ee4f9`. The implementation branch uses
the latter in an isolated worktree.

The normalized corpus tree is identical at both revisions:
`3a8be65682bd248e4858bcbd24718d6fd530d9a3`. M5 reported no tracked changes under
the normalized corpus. Its schema, native occurrence collector and label-index
Git blobs also match the implementation base:

| Input | Git blob |
| --- | --- |
| Schema | `e9bbedaa4a7ec4aff04adfdf215bf35386006cc8` |
| Occurrence collector | `4431c19d194ec56965b0853da2820dff77bcfc55` |
| Packaged MIM label index | `c787048f0228fd1f2dbab2473a57c09e98beb332` |

The M5's existing October 31 outputs report 2,506 ingredient groups and 209,330
occurrences (205,253 mapped, 4,077 unresolved). Those are historical product
counts, not a certification against the subsequently updated schema. The pinned
MIM label-index metadata names source commit
`6643131b0f12ab40b66f98135245fca04027e0e9`, separate from the still-running
MIM stable-ID campaign. No campaign inputs or session prompts were modified.

## Scope and tracked findings

- [Issue 682](https://github.com/CultureBotAI/CultureMech/issues/682): provenance
  and currentness gap; addressed by the candidate-bundle wrapper, verifier,
  extended existing skill and integrated-release guide.
- [Issue 683](https://github.com/CultureBotAI/CultureMech/issues/683): ingredient
  mentions only in variant prose; documented explicitly, with scientific
  normalization left for separate curation. Structured separately modeled
  variant records remain included by the existing collector.

The new inventory method preserves native direct-containment and identity
semantics. It does not release the MIM campaign or install mappings into KGM.
The coordinated release gates are in [the guide](../docs/ingredient_release.md).

Independent read-only review of PR #684 at `93539bea6e` found two additional
issues before the full candidate was accepted:

- [Issue 685](https://github.com/CultureBotAI/CultureMech/issues/685): downstream
  verification needs an independently recorded manifest digest and explicit
  distinction from local consistency checks.
- [Issue 686](https://github.com/CultureBotAI/CultureMech/issues/686): the CLI's
  promise of relocated input verification exceeded its path-based scope check.

The initial local full-catalog attempt was stopped while still scanning, with
its incomplete evidence retained, so corrected producer code could be tested
through a new canary and full run. No successful bundle was published by that
attempt. The M5 adoption process was unaffected.

## Validation

Validation results will be appended after the one-record canary and full
structured-catalog candidate run. Generated products remain ignored; the
committed producer and the candidate manifest retain the reproducible recipe.

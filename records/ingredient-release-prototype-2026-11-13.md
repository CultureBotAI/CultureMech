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

The corrected producer is committed at
`d28c7c76036558b9352a3ca1b9b442a408d2b14d`. Both findings were cleared in an
independent read-only re-review; no remaining substantive findings were reported.
The skill also passed an independent plan/help/recipe forward-test, and both
repository and skill-creator validators passed.

The actual one-record canary used the native `caldococcus_medium.yaml` recipe
through the same CLI/environment as the full build. It produced 25 occurrences,
25 groups and zero errors. Both local-consistency and independently pinned
verification passed. Its scope is explicitly a subset; it does not prove
catalog-wide completion. Its reviewed canary manifest SHA256 is
`33ff51730de91d38431f1ab6f709a3a68972b3acbcb62327e998323988629d3b`.

The native aggregation and bundle tests passed (60 tests); Ruff and Black passed.
The same 60 tests also passed with two isolated test workers before the full
fast tier was launched. The worker helpers were installed only into an ignored
local directory; the shared Python environment was not modified. An earlier
pre-fix fast run was interrupted and replaced by the corrected-source run.

The full structured-catalog build completed from clean commit `d28c7c7603`.
Independent verification against its recorded manifest digest returned
`VERIFIED_CANDIDATE` with `externally_pinned_manifest` assurance:

| Measurement | Count |
| --- | ---: |
| Scanned YAML records | 15,915 |
| Records contributing direct occurrences | 15,570 |
| Records without direct occurrences | 345 |
| Ingredient groups | 2,506 |
| Mapped groups | 1,004 |
| Unmapped groups | 1,492 |
| Ambiguous groups | 10 |
| Occurrences | 209,330 |
| Mapped occurrences | 205,253 |
| Unresolved occurrences | 4,077 |
| Input errors | 0 |

Bundle: `output/ingredient-release-reviewed/`. Its manifest SHA256 is
`30c336713f5426c55b4756b298abd1fe959a773422ea1ec24fec05fe040bf4a3`.
Python was 3.13.12; the recorded PyYAML 6.0.3, jsonschema 4.26.0, LinkML 1.11.1
and linkml-runtime 1.11.1 versions match the committed lock entries.

Fresh read-only SHA256 checks on the M5 confirmed **all five existing ordinary
outputs are byte-identical to this rebuild**:

| Product | SHA256 |
| --- | --- |
| `ingredients_list.tsv` | `9ccbdb69c261c7901d42209271311f4e6b9e3885886dd15e8ca1e5404d2c1f48` |
| `ingredient_occurrences.tsv` | `e04bc9c22ee753e8456cd6aa7a972b7e6d3c2f114427c87aad44c09e38be236a` |
| `mapped_ingredients.yaml` | `456691b997fe3495994bf15db11e864e78bd5d89e87e5167398543729460e7b7` |
| `unmapped_ingredients.yaml` | `f584f5c2b66d4b55d6c7afa4a2b638138faa9275984df48bde8d437a193f10c3` |
| `ingredient_aggregation_errors.tsv` | `4ccba8b77ce80cf210105b5284b5953747729aba576ccdeecb81f7db84eb721b` |

This verifies the current structured list, despite its older modification time;
it does not establish that prose-only variant ingredients are captured or that
the active MIM campaign has exported its new mappings.

The local fast tier reported 16,090 passed, 23 skipped and seven setup failures:
six nested-worker tests strip `PYTHONPATH` and therefore could not see the
separately installed parallel-test helper; one saved-review test needed the
historical Git commit `71153bc25dfe85bf0ac858d786aadc52f92d69e2`. Fetching that
exact object and using an isolated interpreter with site-path access to the
existing dependencies corrected the validation environment. Both affected
modules then passed: **41 tests in 90.84 seconds**, including all seven earlier
failures. No production-code change or failure suppression was used.

All nine GitHub checks passed on implementation commit `d28c7c7603`, including
Fast tests (14m42s), Full corpus and integration suite (7m38s), Python quality
and wheel smoke, schema validation, consistency, plausibility, label drift,
history and vendored sync. This final follow-up records evidence only; it does
not change the producer or its source/artifact hashes.

Generated products remain ignored; the committed producer and candidate manifest
retain the reproducible recipe. The downstream integration checklist is
[issue 687](https://github.com/CultureBotAI/CultureMech/issues/687).

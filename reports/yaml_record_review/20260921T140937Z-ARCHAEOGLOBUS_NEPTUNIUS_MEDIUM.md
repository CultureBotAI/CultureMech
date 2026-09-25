# YAML Record Review: archaeoglobus_neptunius_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ARCHAEOGLOBUS_NEPTUNIUS_MEDIUM.yaml`
- Started UTC: 2026-09-21T14:08:56Z
- Finished UTC: 2026-09-21T14:09:37Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| ID | `CultureMech:001509` |
| Name | `archaeoglobus_neptunius_medium` |
| Original name | ARCHAEOGLOBUS NEPTUNIUS MEDIUM |
| Category | `archaea` |
| pH | 6.5 |
| Source identity | `mediadive.medium:399a`, ARCHAEOGLOBUS NEPTUNIUS MEDIUM |
| Source | DSMZ / MediaDive official medium 399a |
| Merge fingerprint | `4892a736ba046a58bb1f825465133d5abb1ee427e00a6c41fd0c029cbe17284b` |
| Merged from | `archaeoglobus_neptunius_medium` |

This file is a generated merge record derived from the maintained normalized
record at `data/normalized_yaml/archaea/archaeoglobus_neptunius_medium.yaml`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARCHAEOGLOBUS_NEPTUNIUS_MEDIUM.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARCHAEOGLOBUS_NEPTUNIUS_MEDIUM.yaml --out /private/tmp/ARCHAEOGLOBUS_NEPTUNIUS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARCHAEOGLOBUS_NEPTUNIUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 0 checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARCHAEOGLOBUS_NEPTUNIUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run | Not checked: no documented single-merge-record history validator exists. |

## Identity and Grounding

The generated record has the right medium identity. Its `mediadive.medium:399a`
CURIE matches the public MediaDive page and JSON export for DSMZ official
medium 399a, ARCHAEOGLOBUS NEPTUNIUS MEDIUM. The normalized owner and generated
merge have the same fingerprint, so this record is not stale.

An ignored-inclusive exact search across `data/normalized_yaml`,
`data/merge_yaml`, `data/culturemech_id_registry.tsv`,
`data/culturemech_recipe_catalog.tsv`,
`reports/media_content_review_manifest.tsv`, `data/raw`, and the
import-tracking duplicate and plausibility reports found one normalized owner,
this generated merge, the expected registry/catalog/index rows, and two
concentration-plausibility rows for this ID. No duplicate-merge report row was
found in that searched set.

Most exact chemical forms are grounded correctly. Two labels should still be
checked in the MIM/OAK resolver:

- `NiCl2 x 6 H2O` is grounded to generic nickel dichloride rather than an
  explicit hexahydrate term.
- `Calcium D-(+)-pantothenate` has `CHEBI:31345` but no
  `mediaingredientmech_chebi_term`, unlike the other vitamin rows.

## Evidence

The MediaDive JSON export represents medium 399a as a 1003 ml main solution
with three nested stock additions:

- 1 ml `Trace element solution SL-10` (`solution_id` 595).
- 1 ml `Selenite-tungstate solution` (`solution_id` 777).
- 1 ml `Wolin's vitamin solution (10x)` (`solution_id` 5980).

It separately exposes a final-composition export in which those 1 ml additions
are diluted into final medium. For example, `FeCl2 x 4 H2O` is 1.5 g/L in the
undiluted Trace element solution SL-10 recipe but 0.00149551 g/L in the final
medium; `Pyridoxine hydrochloride` is 0.1 g/L in the undiluted Wolin vitamin
stock but 0.0000997009 g/L in the final medium.

The generated CultureMech record flattened the stock recipes into the main
ingredient list using stock concentrations instead of MediaDive final
concentrations. That makes the trace, selenite-tungstate, and vitamin rows
approximately 1000-fold too high:

- `FeCl2 x 4 H2O` is `1.5 G_PER_L`; final should be about
  `0.00149551 G_PER_L`.
- `HCl` is `2.5 G_PER_L`; final should be about `0.00249252 G_PER_L`.
- `NaOH` is `0.5 G_PER_L`; final should be about `0.000498504 G_PER_L`.
- `Pyridoxine hydrochloride` is `0.1 G_PER_L`; final should be about
  `0.0000997009 G_PER_L`.
- The other stock-derived trace salts, selenite/tungstate salts, and vitamin
  rows show the same missing dilution pattern.

Preparation steps for the main solution and Trace element solution SL-10 were
imported verbatim enough to be recognizable, but the trace-stock preparation
is now a second top-level step with no `SolutionRecipe` boundary. The
Selenite-tungstate solution and Wolin vitamin solution boundaries are absent.

## Completeness

The record is complete for main identity, pH, base-medium ingredients, and the
two MediaDive preparation notes that were imported. It is materially incomplete
for stock representation:

- It does not preserve the three stock solution addition rows or their 1 ml
  volumes.
- It does not preserve the water rows or compositions for the three stocks as
  stock-local recipes.
- It uses stock recipe concentrations where it should either nest those
  concentrations under stock solutions or use final-composition values in the
  flat main recipe.

Empty target-organism and growth-evidence fields are acceptable for this
MediaDive source-only record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Three MediaDive stock additions were flattened as undiluted final ingredients. | MediaDive main solution 5954 adds 1 ml each of SL-10, Selenite-tungstate solution, and Wolin's vitamin solution; the CultureMech record has their internal stock `g_l` rows as top-level final ingredients. | Fix the MediaDive importer and repair `data/normalized_yaml/archaea/archaeoglobus_neptunius_medium.yaml`. |
| Major | Final concentrations for stock-derived rows are about 1000-fold too high. | The MediaDive composition export gives final `FeCl2 x 4 H2O` as 0.00149551 g/L and final `Pyridoxine hydrochloride` as 0.0000997009 g/L; the record stores 1.5 and 0.1 `G_PER_L`. | Import nested stocks as solutions or import the diluted composition export for flat final ingredients. |
| Major | Stock water rows and solution boundaries are missing. | The Medium 399a JSON includes separate 1000 ml stocks for SL-10, Selenite-tungstate, and Wolin's vitamin solution; no `solutions` entries or stock-local waters exist in the record. | Model `solution_id` 595, 777, and 5980 as referenced or inline stock recipes. |
| Minor | One imported stock preparation step is mis-scoped. | The SL-10 FeCl2/HCl preparation was imported as top-level step 2 rather than as Trace element solution SL-10 preparation. | Move the preparation step under the SL-10 stock when stock boundaries are restored. |
| Minor | Two exact ingredient groundings need follow-up. | `NiCl2 x 6 H2O` has a generic ChEBI term, and `Calcium D-(+)-pantothenate` lacks a `mediaingredientmech_chebi_term`. | Re-run exact MIM/OAK grounding checks for those labels. |

## Recommended Edits

1. Update the MediaDive importer to use solution boundaries from the medium JSON
   export or to use the already-diluted final composition export when emitting
   a flat recipe.
2. Repair `data/normalized_yaml/archaea/archaeoglobus_neptunius_medium.yaml` so
   `solution_id` 595, 777, and 5980 are represented as stock additions with
   `1 ml` amounts and stock-local compositions.
3. Move the Trace element solution SL-10 preparation note under its stock
   recipe.
4. Recheck `NiCl2 x 6 H2O` and `Calcium D-(+)-pantothenate` against the
   packaged MIM index and OAK before changing their terms.
5. Regenerate `data/merge_yaml/merged/ARCHAEOGLOBUS_NEPTUNIUS_MEDIUM.yaml`.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/archaea/archaeoglobus_neptunius_medium.yaml`
  and `just validate-strict data/normalized_yaml/archaea/archaeoglobus_neptunius_medium.yaml`
  after the normalized repair.
- Rerun `just validate-terms data/normalized_yaml/archaea/archaeoglobus_neptunius_medium.yaml`
  after exact grounding changes.
- Rerun `just verify-merges` and `just audit-merge-freshness` after regenerating
  merge outputs.
- Compare the repaired CultureMech values against
  `/download/medium/399a/json` and `/download/composition/399a/json`: stock
  recipes should retain their native `g_l`, while any flat final rows should
  match the final composition export.
- Rerun the concentration-plausibility report; this record should no longer be
  flagged for stock-scale `FeCl2 x 4 H2O` or vitamin-scale `Pyridoxine
  hydrochloride`.

## Additional Notes

The media content review manifest currently marks this normalized owner as
`PASS`, but that manifest operates on structural coverage metrics and did not
catch the MediaDive stock-dilution error described above.

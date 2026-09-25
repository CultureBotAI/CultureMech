# YAML Record Review: ARCHAEOGLOBUS medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml
- Started UTC: 2026-09-21T13:56:18Z
- Finished UTC: 2026-09-21T13:57:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:005188 |
| Name | archaeoglobus_medium |
| Original name | ARCHAEOGLOBUS medium |
| Category | archaea |
| Medium type | COMPLEX |
| Composition type | SEMI_DEFINED |
| Physical state | LIQUID |
| Source | KOMODO medium 399, source duplicate of DSMZ / MediaDive medium 399 |
| Source term | komodo.medium:399 |
| Generated record | data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml |
| Merge fingerprint | 69c04d2335cfb6c6206d2e27aebad33f8cdaf8d2e815b70e3633d5b728e741cc |

The target is a generated duplicate merge from two normalized source records:

| Source role | Path | ID | Source ID |
|---|---|---|---|
| KOMODO owner | data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml | CultureMech:005188 | komodo.medium:399 |
| DSMZ/MediaDive duplicate | data/normalized_yaml/archaea/archaeoglobus_medium.yaml | CultureMech:001508 | mediadive.medium:399 |

Any recipe fix should be made in both normalized owners, or in the shared
KOMODO/DSMZ import and repair path that generated them, and then propagated by
regenerating the merge.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml` | Passed, `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml --out /private/tmp/ARCHAEOGLOBUS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 active checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with the known `eutils` / `pkg_resources` warning. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone files under `history/`; no focused embedded `MediaRecipe.curation_history` validator is documented for a single generated merge record. |

## Identity and Grounding

The merge denotes the expected DSMZ 399 recipe. The canonical KOMODO owner says
`DSMZ Medium: 399 (mediadive.medium:399)`, the DSMZ/MediaDive duplicate uses
`mediadive.medium:399`, and the inspected DSMZ Medium 399 PDF is titled
`ARCHAEOGLOBUS MEDIUM`.

An ignored-file-inclusive bounded search for
`CultureMech:005188|CultureMech:001508|komodo\.medium:399|mediadive\.medium:399|KOMODO_399_ARCHAEOGLOBUS_medium|ARCHAEOGLOBUS_MEDIUM|data/normalized_yaml/bacterial/archaeoglobus_medium\.yaml|data/normalized_yaml/bacterial/KOMODO_399_ARCHAEOGLOBUS_medium\.yaml`
across `data/normalized_yaml`, `data/merge_yaml`,
`data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`,
`reports/media_content_review_manifest.tsv`,
`data/import_tracking/reports/concentration_plausibility.tsv`, and
`data/import_tracking/reports/merged_duplicates.tsv` found the two real
normalized owners under `data/normalized_yaml/archaea/`, the generated merge,
both registry/catalog/manifest rows, and six preexisting `DIFFERING_PARTS`
diagnostics for stock rows that were summed into base rows. `find
data/normalized_yaml` found no bacterial owner at either stale reciprocal
duplicate-link path embedded in the two source records.

Most base-medium ingredients are grounded to the intended ChEBI identities.
`Yeast extract` is correctly left ungrounded as an undefined component. One
stock ingredient needs exact-form review: the source supplies `NiCl2 x 6 H2O`,
but the record grounds it to `CHEBI:34887`, whose label is `nickel dichloride`
rather than an explicit hexahydrate.

## Evidence

The DSMZ Medium 399 PDF supports the final recipe: KCl 0.34 g,
`MgCl2 x 6 H2O` 4.00 g, `MgSO4 x 7 H2O` 3.45 g, NH4Cl 0.25 g,
`CaCl2 x 2 H2O` 0.14 g, K2HPO4 0.14 g, NaCl 18.00 g, yeast extract 0.50 g,
Na-L-lactate 1.50 g, 2.00 ml 0.1% `Fe(NH4)2(SO4)2 x 7 H2O`, 10.00 ml
Modified Wolin's mineral solution, 0.50 ml 0.1% sodium resazurin, 3.00 g
NaHCO3, 0.50 g `Na2S x 9 H2O`, and 1000.00 ml distilled water.

The record correctly normalizes the main grams, milligram-equivalent indicator,
and milliliter iron-stock additions by DSMZ's approximately 1.012 L final
volume. It does not correctly preserve the 10 ml Modified Wolin's mineral
solution boundary. The full stock formula is flattened into final-medium
`G_PER_L` rows, and three of those rows are summed with separate base-medium
rows:

| Component | DSMZ 399 base row | Modified Wolin stock row | Record row |
|---|---:|---:|---:|
| MgSO4 x 7 H2O | 3.45 g | 3.0 g per liter of stock | 6.40909 `G_PER_L` |
| CaCl2 x 2 H2O | 0.14 g | 0.1 g per liter of stock | 0.23834 `G_PER_L` |
| NaCl | 18.0 g | 1.0 g per liter of stock | 18.7866 `G_PER_L` |

The DSMZ stock-preparation paragraph says to first dissolve nitrilotriacetic
acid, adjust to pH 6.5 with KOH, add minerals, and adjust the final stock to
pH 7.0 with KOH. The record exposes that text as `preparation_steps[2]` of the
final medium instead of attaching it to Modified Wolin's mineral solution.

## Completeness

The record is complete enough for source identity, DSMZ 399's pH 6.9 final
medium handling, and the non-stock base ingredients. It is incomplete for the
stock boundary and duplicate linkage:

- Modified Wolin's mineral solution is missing as a 10 ml/L stock addition.
- All Modified Wolin components are flattened at their full stock
  concentrations.
- Three stock components were summed into final-medium base rows.
- DSMZ 399's 1000 ml distilled-water row is absent from both owners and the
  generated merge.
- Modified Wolin's 1000 ml distilled-water row is absent.
- Both owners point their reciprocal `SOURCE_DUPLICATE` links at
  `data/normalized_yaml/bacterial/...` paths that were not found; the real
  files live under `data/normalized_yaml/archaea/`.

The absent target organisms, variants beyond the source duplicate, and primary
growth references are not defects for this source recipe import; DSMZ medium
pages define recipes and do not, by themselves, assert strain-level growth
outcomes.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Modified Wolin's mineral solution was flattened into the final medium at 100% stock strength. | DSMZ 399 lists one 10.00 ml addition of Modified Wolin's mineral solution; the generated merge and both normalized owners store the stock solutes as final `G_PER_L` ingredients. | `data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml`, `data/normalized_yaml/archaea/archaeoglobus_medium.yaml`, or the DSMZ/KOMODO import and stock-nesting repair. |
| Major | Duplicate cleanup summed stock solutes with final-medium solutes. | DSMZ 399 has separate final-medium and stock rows for `MgSO4 x 7 H2O`, `CaCl2 x 2 H2O`, and NaCl. The records sum those pairs into 6.40909, 0.23834, and 18.7866 `G_PER_L`, and `data/import_tracking/reports/merged_duplicates.tsv` flags all three sums for both owners as `DIFFERING_PARTS`. | Both normalized owners; also audit the duplicate-merge rule that operated before stock boundaries were represented. |
| Major | DSMZ 399 water is missing. | DSMZ 399 lists 1000.00 ml distilled water in the final formulation and 1000.00 ml distilled water in Modified Wolin's mineral solution. Neither owner nor the generated merge contains either water row. | The DSMZ/MediaDive import or both normalized owners. |
| Major | Reciprocal source-duplicate paths are broken. | `data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml` points to `data/normalized_yaml/bacterial/archaeoglobus_medium.yaml`, and `data/normalized_yaml/archaea/archaeoglobus_medium.yaml` points to `data/normalized_yaml/bacterial/KOMODO_399_ARCHAEOGLOBUS_medium.yaml`; ignored-inclusive `rg` and `find` found the actual files only under `data/normalized_yaml/archaea/`. | Both normalized owners and the duplicate-link repair that assigned those paths. |
| Minor | `NiCl2 x 6 H2O` is not grounded to an explicit hexahydrate label. | DSMZ 399 supplies nickel chloride hexahydrate, but the record links the ingredient to `CHEBI:34887`, `nickel dichloride`. | Both normalized owners. |

No blockers found.

## Recommended Edits

1. In both normalized owners, replace the flattened Modified Wolin rows with a
   10 ml/L `Modified Wolin's mineral solution` stock that contains the DSMZ
   stock formula and the stock pH adjustment note.
2. Split the summed `MgSO4 x 7 H2O`, `CaCl2 x 2 H2O`, and NaCl rows back into
   final-medium base rows plus stock-solution components.
3. Add DSMZ 399's main 1000 ml distilled-water row, and decide whether Modified
   Wolin's 1000 ml stock water should be explicit in `solutions[].composition`
   or documented only in the stock preparation note.
4. Correct the reciprocal `SOURCE_DUPLICATE` paths so both owners point at the
   actual `data/normalized_yaml/archaea/` peer.
5. Verify whether a ChEBI term exists for nickel chloride hexahydrate and, if
   so, re-ground `NiCl2 x 6 H2O` away from the anhydrous `nickel dichloride`
   term.
6. Regenerate `data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml` and downstream
   pages/indexes from the maintained normalized records.

## Follow-up Checks

- Re-run open-schema, strict, term, and reference validation for both normalized
  owners after curation.
- Re-run duplicate-merge diagnostics and confirm this record no longer has
  `DIFFERING_PARTS` rows for final-medium ingredients.
- Inspect the regenerated merge to confirm Modified Wolin's mineral solution is
  a 10 ml/L stock, the three summed rows are restored to the DSMZ final-medium
  quantities, and no reciprocal path points at a nonexistent bacterial file.
- Inspect the rendered page and ensure the Modified Wolin preparation paragraph
  is attached to the stock rather than displayed as a final-medium step.

## Additional Notes

- `reports/media_content_review_manifest.tsv` marks both maintained owners as
  `PASS`, but that status is stale relative to the stock-boundary,
  duplicate-sum, and broken-path findings.
- The generated merge has not diverged scientifically from the normalized
  owners; the issues above are present in both source records and their
  generated merge.

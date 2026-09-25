# YAML Record Review: ARCHAEOGLOBUS FULGIDUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/archaeoglobus_fulgidus_medium__51a0bdbe.yaml
- Started UTC: 2026-09-21T13:50:17Z
- Finished UTC: 2026-09-21T13:51:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002575 |
| Name | archaeoglobus_fulgidus_medium |
| Original name | ARCHAEOGLOBUS FULGIDUS MEDIUM |
| Category | archaea |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| Source | MediaDive/JCM import for JCM Medium J213 |
| Source term | mediadive.medium:J213 |
| Maintained owner | data/normalized_yaml/archaea/archaeoglobus_fulgidus_medium.yaml |
| Generated record | data/merge_yaml/merged/archaeoglobus_fulgidus_medium__51a0bdbe.yaml |
| Merge fingerprint | 51a0bdbeefd673673f3d1b8cb53fb83a4c82aaef7b7b6b79576b6b23002f2072 |

The target is a generated one-source merge whose maintained input is
`data/normalized_yaml/archaea/archaeoglobus_fulgidus_medium.yaml`. The generated
file matches that owner plus the 2026-08-06 `merge_recipes.py` curation event,
`merge_fingerprint`, and `merged_from` metadata. Any fix should be made in the
normalized MediaDive/JCM owner or in the MediaDive importer and then propagated
by regenerating the merge.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/archaeoglobus_fulgidus_medium__51a0bdbe.yaml` | Passed, `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/archaeoglobus_fulgidus_medium__51a0bdbe.yaml --out /private/tmp/archaeoglobus_fulgidus_medium__51a0bdbe.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/archaeoglobus_fulgidus_medium__51a0bdbe.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 active checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/archaeoglobus_fulgidus_medium__51a0bdbe.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with the known `eutils` / `pkg_resources` warning. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone files under `history/`; no focused embedded `MediaRecipe.curation_history` validator is documented for a single generated merge record. |

## Identity and Grounding

The generated record identifies the expected JCM 213 source recipe. It names
`ARCHAEOGLOBUS FULGIDUS MEDIUM`, uses `mediadive.medium:J213`, links JCM
`GRMD=213`, and carries `ph_value: 6.9`, all of which agree with the inspected
JCM medium 213 page.

An ignored-file-inclusive bounded search for
`CultureMech:002575|mediadive\.medium:J213|JCM Medium J213|archaeoglobus_fulgidus_medium__51a0bdbe|data/normalized_yaml/archaea/archaeoglobus_fulgidus_medium\.yaml`
across `data/normalized_yaml`, `data/merge_yaml`,
`data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`,
`reports/media_content_review_manifest.tsv`,
`data/import_tracking/reports/concentration_plausibility.tsv`, and
`data/import_tracking/reports/merged_duplicates.tsv` found one normalized owner,
the generated merge, registry/catalog/manifest/index rows, and two existing
`DIFFERING_PARTS` diagnostics for the same record. It did not find a second
maintained normalized record for `mediadive.medium:J213` in the searched
corpus.

The simple base-medium ingredient groundings match the supplied chemical forms:
KCl, `MgCl2 x 6 H2O`, `MgSO4 x 7 H2O`, NH4Cl, `CaCl2 x 2 H2O`, K2HPO4, NaCl,
NaHCO3, `Fe(NH4)2(SO4)2 x 6 H2O`, `(NH4)2Ni(SO4)2 x 6 H2O`, sodium L-lactate,
resazurin, and `Na2S x 9 H2O` all resolve to appropriate ChEBI terms. Yeast
extract is correctly left ungrounded as an undefined component.

## Evidence

JCM medium 213 supports the base recipe and the first `preparation_steps`
description: KCl 0.34 g, `MgCl2*6H2O` 4.0 g, `MgSO4*7H2O` 3.45 g, NH4Cl
0.25 g, `CaCl2*2H2O` 0.14 g, K2HPO4 0.14 g, NaCl 18.0 g, NaHCO3 5.0 g,
`Fe(NH4)2(SO4)2*6H2O` 2.0 mg, `(NH4)2Ni(SO4)2*6H2O` 2.0 mg, trace minerals
from JCM medium 151 at 10.0 ml, yeast extract 0.5 g, sodium L-lactate 1.5 g,
resazurin 1.0 mg, `Na2S*9H2O` 0.5 g, and 990 ml distilled water.

JCM medium 151 and TOGO M142 support the trace-minerals stock formula behind
the 10 ml addition. That source lists trace stock concentrations for
nitrilotriacetic acid, `MgSO4*7H2O`, `MnSO4*xH2O`, NaCl, `FeSO4*7H2O`,
`CoSO4*7H2O`, `CaCl2*2H2O`, `ZnSO4*7H2O`, `CuSO4*5H2O`, `AlK(SO4)2`, `H3BO3`,
and `Na2MoO4*2H2O`, plus a stock-preparation paragraph about KOH and pH 7.0.

The inspected sources do not support the generated one-level ingredient list.
JCM medium 213 adds 10 ml of the trace-minerals stock; it does not add stock
components directly at their full stock concentrations. The YAML nevertheless
places nine trace rows beside final M213 ingredients, drops the 10 ml stock
amount, and sums three stock salts into same-named base salts:

| Component | JCM 213 base row | JCM 151 trace-stock row | Record row |
|---|---:|---:|---:|
| MgSO4*7H2O | 3.45 g | 3.0 g per liter of stock | 6.45 `G_PER_L` |
| CaCl2*2H2O | 0.14 g | 0.1 g per liter of stock | 0.24000000000000002 `G_PER_L` |
| NaCl | 18.0 g | 1.0 g per liter of stock | 19.0 `G_PER_L` |

## Completeness

The record is complete enough for source identity, several base-medium salts,
the pH 6.9 value, and the JCM 213 preparation paragraph. It is incomplete for
the stock boundary:

- It has no 990 ml distilled-water row from JCM 213.
- It has no 10 ml/L trace-minerals stock addition.
- It overstates the JCM 151 trace stock by using full stock concentrations as
  final-medium grams per liter.
- It merges stock `MgSO4*7H2O`, stock `CaCl2*2H2O`, and stock NaCl with their
  separate JCM 213 base-medium rows.
- It exposes the JCM 151 trace-minerals preparation paragraph as a second
  final-medium step instead of nesting that paragraph under the trace stock.
- It has no structured source note for the JCM 151 material even though roughly
  half of the ingredient rows come from that cross-referenced stock.

The absent target organisms, variants, and primary growth references are not
defects for this source recipe import; JCM medium pages describe recipes and do
not assert strain-level growth outcomes.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The trace-minerals stock was flattened into the final JCM 213 recipe at 100% stock concentration instead of being modeled as a 10 ml/L stock addition. | JCM medium 213 lists only `Trace minerals (see Medium No. 151)` at 10.0 ml. JCM medium 151 lists the trace formula per liter of stock. The YAML stores nine trace rows as final `G_PER_L` ingredients and drops the 10 ml stock amount. | `data/normalized_yaml/archaea/archaeoglobus_fulgidus_medium.yaml` or the MediaDive importer. |
| Major | The duplicate-ingredient cleanup summed stock rows with base-medium rows. | `MgSO4*7H2O` is 3.45 g in M213 and 3.0 g in M151 trace stock but appears as 6.45 `G_PER_L`; `CaCl2*2H2O` is 0.14 g in M213 and 0.1 g in M151 trace stock but appears as 0.24000000000000002 `G_PER_L`; NaCl is 18.0 g in M213 and 1.0 g in M151 trace stock but appears as 19.0 `G_PER_L`. `data/import_tracking/reports/merged_duplicates.tsv` already flags the `MgSO4` and NaCl rows as `DIFFERING_PARTS`; the same stock-boundary issue also affects CaCl2. | `data/normalized_yaml/archaea/archaeoglobus_fulgidus_medium.yaml`; also audit the duplicate-merge rule that operated before stock boundaries were represented. |
| Major | JCM 213 water is missing. | JCM medium 213 lists 990.0 ml distilled water; the YAML has no `Distilled water` ingredient. | `data/normalized_yaml/archaea/archaeoglobus_fulgidus_medium.yaml` or the MediaDive importer. |
| Major | The JCM 151 trace-minerals preparation paragraph is scoped as a final-medium step. | `preparation_steps[1]` describes dissolving nitrilotriacetic acid, KOH adjustment, and final pH 7.0 for the trace-minerals stock in JCM medium 151. It should be nested under the stock recipe, not executed after pressurizing JCM 213 inoculated bottles to 200 kPa. | `data/normalized_yaml/archaea/archaeoglobus_fulgidus_medium.yaml` or the MediaDive importer. |

No blockers found. No minor findings found.

## Recommended Edits

1. In `data/normalized_yaml/archaea/archaeoglobus_fulgidus_medium.yaml` or the
   MediaDive import transform, restore JCM medium 213 as the final recipe:
   fourteen final-medium ingredients, 990 ml water, and one 10 ml/L
   trace-minerals stock addition.
2. Move the JCM medium 151 trace-minerals formula into a structured stock
   recipe or structured nested solution. Do not flatten its ingredient
   concentrations into the M213 final recipe and do not multiply or sum them
   into M213 base salts.
3. Keep the JCM 213 pH 6.9 preparation paragraph on the final recipe, and scope
   the nitrilotriacetic-acid/KOH/pH 7.0 paragraph to the trace-minerals stock.
4. Audit the three `Merged 2 duplicates` rows and remove those annotations once
   stock rows are nested rather than mixed with final-medium ingredients.
5. Regenerate `data/merge_yaml/merged/archaeoglobus_fulgidus_medium__51a0bdbe.yaml`
   and downstream pages/indexes from the maintained normalized record.

## Follow-up Checks

- Re-run open-schema, strict, term, and reference validation for the normalized
  owner after curation.
- Re-run the merge generator and confirm the regenerated merge has separate
  base-medium and trace-stock scopes: M213 `MgSO4*7H2O` remains 3.45 g/L, M213
  `CaCl2*2H2O` remains 0.14 g/L, M213 NaCl remains 18.0 g/L, and the M151
  trace-stock values remain under the 10 ml/L stock.
- Re-run duplicate-merge diagnostics and confirm this record no longer has
  `DIFFERING_PARTS` rows for final-medium ingredients.
- Inspect the regenerated rendered page and ensure the trace-minerals
  preparation text is visibly attached to the stock, not to the JCM 213 final
  recipe.

## Additional Notes

- The sibling TOGO import `CultureMech:008658` models the same JCM medium 213
  recipe from `TOGO:M206`, but it preserves an empty `Trace minerals (see Medium
  [M142])` stock instead of flattening the JCM 151 stock. That sibling is
  scientifically closer on stock boundaries but still needs unit and stock
  expansion fixes of its own.
- `reports/media_content_review_manifest.tsv` marks the maintained MediaDive
  owner as `PASS`, but that status is stale relative to the current
  stock-boundary findings.

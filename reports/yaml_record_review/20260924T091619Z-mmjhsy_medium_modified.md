# YAML Record Review: mmjhsy_medium_modified

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mmjhsy_medium_modified.yaml
- Started UTC: 2026-09-24T09:14:47Z
- Finished UTC: 2026-09-24T09:16:19Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| CultureMech ID | CultureMech:000852 |
| Generated record | data/merge_yaml/merged/mmjhsy_medium_modified.yaml |
| Maintained owner | data/normalized_yaml/bacterial/mmjhsy_medium_modified.yaml |
| Merge fingerprint | 035f0a2bcef32f748a07d92b4c6e8e58fc601b7e78d11fd2d240b430e4d954a0 |
| Merged from | mmjhsy_medium_modified |
| Source import | MediaDive/DSMZ 1391 |

The generated record is a one-source merge of
`data/normalized_yaml/bacterial/mmjhsy_medium_modified.yaml`; the generated copy
only adds the `merge_recipes.py` curation event, `merge_fingerprint`, and
`merged_from`. Future corrections belong in the normalized owner and, for the
recurring nested-solution behavior, in `src/culturemech/import/mediadive_importer.py`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mmjhsy_medium_modified.yaml` | Passed; printed `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mmjhsy_medium_modified.yaml --out /private/tmp/mmjhsy_medium_modified.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. `/private/tmp/mmjhsy_medium_modified.strict.tsv` had 1 line, the header only. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mmjhsy_medium_modified.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 total checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mmjhsy_medium_modified.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; the only diagnostic was the known `eutils` `pkg_resources` deprecation warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `HistoryRecord` files under `history/`, not embedded `MediaRecipe.curation_history` events in a merged recipe. |

The repository-level `just` wrappers were not used for this record because this
checkout's default uv environment currently tries to build `llvmlite==0.46.0`
under Python 3.13 and exits in setuptools before these record checks can run.
The focused commands above reuse the cached Python 3.11 validator environment.

## Identity and Grounding

The source identity is coherent. MediaDive REST medium `1391` names `MMJHSY
MEDIUM (modified)`, marks DSMZ as the source, fixes pH at 6.8, and links to
`DSMZ_Medium1391.pdf`; the generated record uses `mediadive.medium:1391` and
keeps the same DSMZ PDF URL.

The parent recipe has 13 direct gram-scale ingredients, 5 ml Trace mineral
solution, 1000 ml distilled water, 1 ml Wolin's vitamin solution, and 0.1
percent NaHCO3 as a concentrated post-autoclave addition. The generated YAML
has no explicit row for either stock solution. It places all Trace mineral
solution ingredients and all Wolin's vitamin solution ingredients directly on
the parent at their stock g/L concentrations.

One chemical grounding is too broad: `NiCl2 x 6 H2O` is linked to
`CHEBI:34887` `nickel dichloride`, which omits the hexahydrate specified by
MediaDive.

## Evidence

Supported:

- MediaDive 1391 and the DSMZ PDF support the source identity, pH 6.8, complex
  liquid classification, yeast extract use, and the direct parent salts from
  NaCl through yeast extract.
- The two generated preparation steps preserve the parent DSMZ instructions to
  prepare under N2/CO2, adjust pH with NaOH, autoclave, add separately
  sterilized concentrated solutions, purge 80 percent H2 / 20 percent CO2, and
  compress 77 percent H2 / 20 percent CO2 / 3 percent O2 to 2 atm.

Unsupported or over-scoped:

- The source adds 5 ml Trace mineral solution to the parent; the generated YAML
  instead carries 16 trace-stock components as direct parent ingredients.
- The source adds 1 ml Wolin's vitamin solution to the parent; the generated
  YAML instead carries 11 vitamin-stock components as direct parent
  ingredients.
- The Wolin's vitamin solution instruction to filter through a 0.22 um pore is
  missing.
- The 0.1 percent NaHCO3 post-autoclave concentrated addition is represented
  only as a 1 g/L direct parent ingredient, losing the stock-addition context.
- `NiCl2 x 6 H2O` is not exactly grounded.
- `NaNO3` and `KI` still carry legacy `mediaingredientmech_term` fields instead
  of CHEBI-keyed `mediaingredientmech_chebi_term` fields.

## Completeness

The record has the correct parent-level pH and gas-handling text, but it is not
complete enough to reproduce DSMZ 1391 because it does not preserve either
concentrated stock addition. Following the flat ingredient list would add the
Trace mineral and Wolin's vitamin stocks at their undiluted stock
concentrations instead of at 5 ml/L and 1 ml/L.

Empty `target_organisms`, `references`, `growth_conditions`, storage metadata,
and variants are not defects. The DSMZ recipe establishes formulation and
preparation, not a strain-specific growth assertion.

Not checked: I did not perform a repository-wide search for separate normalized
solution records for MediaDive solutions 2253 or 242. The stock-boundary
findings are limited to this generated MediaRecipe, its one-source normalized
owner, MediaDive REST 1391, and the DSMZ 1391 PDF.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The Trace mineral solution and Wolin's vitamin solution stock additions were flattened into parent ingredients. | MediaDive `Main sol. 1391` references 5 ml solution 2253 and 1 ml solution 242; the generated YAML has neither stock reference. | `data/normalized_yaml/bacterial/mmjhsy_medium_modified.yaml`; recurring fix likely belongs in `src/culturemech/import/mediadive_importer.py`. |
| major | Stock concentrations were promoted to parent concentrations. | The generated trace elements and vitamins use each stock's g/L values even though the parent uses only 5 ml/L trace stock and 1 ml/L vitamin stock. | `data/normalized_yaml/bacterial/mmjhsy_medium_modified.yaml`; MediaDive solution import logic. |
| major | Wolin's vitamin solution sterilization was dropped. | MediaDive solution 242 has a filtration step with a 0.22 um pore, but the generated record has only the two parent gas-preparation steps. | `data/normalized_yaml/bacterial/mmjhsy_medium_modified.yaml`; MediaDive solution import logic. |
| major | The NaHCO3 stock-addition context was lost. | MediaDive stores NaHCO3 as a 0.1 percent post-autoclave concentrated addition; the generated record has only a direct 1 g/L ingredient. | `data/normalized_yaml/bacterial/mmjhsy_medium_modified.yaml`. |
| major | `NiCl2 x 6 H2O` is grounded to an anhydrous nickel chloride ChEBI term. | The source specifies nickel chloride hexahydrate; the generated record uses `CHEBI:34887` `nickel dichloride`. | `data/normalized_yaml/bacterial/mmjhsy_medium_modified.yaml`; ingredient grounding enrichment. |
| minor | The NaNO3 and KI MediaIngredientMech links are still in deprecated legacy form. | Both ingredients have CHEBI `term` values but still store `mediaingredientmech_term` fields. | `data/normalized_yaml/bacterial/mmjhsy_medium_modified.yaml`; MIM migration logic. |

## Recommended Edits

1. Preserve MediaDive solution 2253 as the 5 ml/L Trace mineral solution and
   solution 242 as the 1 ml/L Wolin's vitamin solution instead of flattening
   their components into MMJHSY.
2. Keep Wolin's 0.22 um filtration instruction on the Wolin's vitamin solution
   record.
3. Model NaHCO3 as a post-autoclave 0.1 percent concentrated addition, while
   retaining its equivalent final 1 g/L amount only in the correct context.
4. Re-ground `NiCl2 x 6 H2O` or leave it unresolved if the local resolver has no
   exact nickel chloride hexahydrate term.
5. Re-run MediaIngredientMech CHEBI-key migration for `NaNO3` and `KI`.

## Follow-up Checks

- Re-run the focused open-schema, strict-schema, reference, and term validators
  on `data/normalized_yaml/bacterial/mmjhsy_medium_modified.yaml` and the
  regenerated `data/merge_yaml/merged/mmjhsy_medium_modified.yaml`.
- Inspect the regenerated parent and verify that Trace mineral solution,
  Wolin's vitamin solution, and 0.1 percent NaHCO3 remain stock additions.
- Inspect the regenerated Wolin's vitamin solution and verify that its
  filtration step remains scoped to the stock rather than to the parent.
- Re-open MediaDive 1391 or the DSMZ 1391 PDF after regeneration to confirm the
  stock-addition amounts are still 5 ml/L and 1 ml/L.

## Additional Notes

The DSMZ PDF delegates the Trace mineral solution to DSMZ Medium 1121 and the
vitamin solution to Medium 141. This review used the MediaDive 1391 REST
payload for the expanded stock formulas because MediaDive includes those
solutions inline with DSMZ 1391.

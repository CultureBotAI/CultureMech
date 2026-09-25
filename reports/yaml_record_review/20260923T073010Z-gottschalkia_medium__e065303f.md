# YAML Record Review: gottschalkia_medium__e065303f

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gottschalkia_medium__e065303f.yaml
- Started UTC: 2026-09-23T07:28:57Z
- Finished UTC: 2026-09-23T07:30:10Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:001903` |
| Name | `gottschalkia_medium` |
| Original name | `GOTTSCHALKIA MEDIUM` |
| Category | `bacterial` |
| Canonical media term | `mediadive.medium:76` |
| Merged sources | `clostridium_acidiurici_medium`, `gottschalkia_medium` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gottschalkia_medium__e065303f.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/gottschalkia_medium__e065303f.yaml --out /private/tmp/gottschalkia_medium__e065303f.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/gottschalkia_medium__e065303f.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/gottschalkia_medium__e065303f.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This generated record correctly groups MediaDive DSMZ 76 with KOMODO 76 as source duplicates.

A gitignore-independent exact search for `mediadive.medium:76`, `komodo.medium:76`, `DSMZ_Medium76`, `gottschalkia_medium`, and `clostridium_acidiurici_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found the expected MediaDive DSMZ 76 parent, KOMODO 76 parent, this generated duplicate group, source indexes, and the separate Togo M2532 import of the same DSMZ PDF.

Most ingredient grounding is narrow. `NiCl2 x 6 H2O` is grounded to an anhydrous nickel dichloride term rather than to a hexahydrate term.

## Evidence

DSMZ Medium 76 adds 1 ml/l Trace element solution SL-10 and 1 ml/l Selenite-tungstate solution to the final medium. The final medium has 1000 ml Distilled water; the SL-10 stock has 990 ml Distilled water; the Selenite-tungstate stock has 1000 ml Distilled water.

The generated record expands both 1 L stock formulas directly into top-level ingredients. Every SL-10 and Selenite-tungstate stock ingredient is therefore 1000x too high in the final formula: for example, 1.5 g/l FeCl2 x 4H2O and 0.5 g/l NaOH are stock concentrations, not final-medium concentrations. The generated record also lacks explicit rows for the 1 ml/l stock additions and lacks the final-medium and stock water rows.

DSMZ also adds 6 ml of `FeSO4 x 7 H2O` as a 0.1% w/v solution in 0.1 N H2SO4 and 0.5 ml of Sodium resazurin as a 0.1% w/v solution. The generated FeSO4 and Sodium resazurin masses are plausible final g/l amounts, but the source solution attributes are not represented structurally.

## Completeness

The KOMODO/DSMZ duplicate grouping and basal ingredient table are sound, but the generated formula is not complete enough for DSMZ 76 while the two required stock solutions are flattened at stock strength and water rows are missing. Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects by themselves.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | SL-10 and Selenite-tungstate were flattened at 1000x the final concentration. | DSMZ 76 adds 1 ml/l of each stock; the generated record promotes the 1 L stock concentrations for FeCl2, ZnCl2, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, Na2MoO4, NaOH, Na2SeO3, and Na2WO4 directly to final g/l rows. | MediaDive/KOMODO DSMZ 76 solution expansion. |
| Major | Source water rows and stock identities are missing. | DSMZ 76 has 1000 ml final water, 990 ml SL-10 stock water, 1000 ml Selenite-tungstate stock water, and two 1 ml/l stock addition rows; the generated record has none of those structured rows. | MediaDive/KOMODO DSMZ 76 normalization. |
| Major | FeSO4 and resazurin source-solution attributes are flattened to masses only. | DSMZ 76 adds 6 ml `FeSO4 x 7 H2O` in 0.1% w/v 0.1 N H2SO4 and 0.5 ml 0.1% w/v Sodium resazurin; the generated record has final FeSO4 and resazurin masses but loses the source solution concentration context. | MediaDive compound-with-attribute handling. |
| Major | Nickel chloride hexahydrate is grounded to the anhydrous salt. | The SL-10 source row is `NiCl2 x 6 H2O`; the generated CHEBI term is `CHEBI:34887` / `nickel dichloride`. | CHEBI grounding for hydrate-specific salts. |
| Minor | Togo M2532 is a split import of the same DSMZ 76 PDF. | `data/merge_yaml/merged/GOTTSCHALKIA_MEDIUM.yaml` comes from Togo M2532 and links to `DSMZ_Medium76.pdf`, while this generated record only merges MediaDive DSMZ 76 with KOMODO 76. | Duplicate grouping for Togo/MediaDive/KOMODO DSMZ 76 records. |

## Recommended Edits

1. Model `Trace element solution SL-10` and `Selenite-tungstate solution` as separate 1 ml/l stock additions.
2. Keep stock recipes and stock water rows scoped under their own `solutions` entries instead of flattening them into final ingredients.
3. Restore the 1000 ml/l final Distilled water row.
4. Preserve the FeSO4 and Sodium resazurin source-solution attributes.
5. Reground `NiCl2 x 6 H2O` to a hydrate-specific CHEBI term if one is available.
6. After Togo M2532 is repaired, confirm it joins the same DSMZ 76 source-duplicate cluster.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated DSMZ 76 record.
- Compare the final record against the DSMZ Medium 76 PDF, MediaDive 76, KOMODO 76, and Togo M2532.
- Confirm SL-10 and Selenite-tungstate ingredient amounts remain scoped to stock recipes rather than final-liter concentrations.
- Re-run the exact gitignore-independent search for `mediadive.medium:76`, `komodo.medium:76`, `DSMZ_Medium76`, `gottschalkia_medium`, and `clostridium_acidiurici_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify the duplicate group is intentional.

## Additional Notes

None found.

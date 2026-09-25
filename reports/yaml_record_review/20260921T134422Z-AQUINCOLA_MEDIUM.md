# YAML Record Review: AQUINCOLA medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AQUINCOLA_MEDIUM.yaml
- Started UTC: 2026-09-21T13:43:39Z
- Finished UTC: 2026-09-21T13:44:23Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| Stable ID | CultureMech:003898 |
| Name | aquincola_medium |
| Original name | AQUINCOLA medium |
| Category | bacterial |
| Source | KOMODO Medium 1178 copied from DSMZ / MediaDive Medium 1178 |
| Reviewed artifact | data/merge_yaml/merged/AQUINCOLA_MEDIUM.yaml |
| Merged sources | data/normalized_yaml/bacterial/KOMODO_1178_AQUINCOLA_medium.yaml; data/normalized_yaml/bacterial/aquincola_medium.yaml |

The reviewed record is the generated canonical merge for two source duplicates: a KOMODO 1178 import and a DSMZ/MediaDive 1178 import.

An ignored-file-inclusive exact search for `AQUINCOLA_MEDIUM`, `Aquincola`, `aquincola_medium`, and `AQUINCOLA` covered `data/normalized_yaml`, `data/merge_yaml`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `reports/media_content_review_manifest.tsv`, `data/import_tracking/reports/concentration_plausibility.tsv`, and `data/import_tracking/reports/merged_duplicates.tsv`. It found exactly the two normalized owners that feed this generated merge, plus generated indexes, registry/catalog rows, and manifest rows for those owners.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AQUINCOLA_MEDIUM.yaml`; no issues found. |
| Strict schema | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AQUINCOLA_MEDIUM.yaml --out /private/tmp/AQUINCOLA_MEDIUM.strict.tsv --workers 1 --quiet`; 1 file scanned, 0 error rows. |
| Reference validator | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AQUINCOLA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; 1 file validated, 0 total active checks. |
| Term validator | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AQUINCOLA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`; only the upstream `eutils`/`pkg_resources` deprecation warning was emitted. |
| Embedded curation history | Not checked: this repository exposes `just validate-history` for standalone `history/` files, not a focused `MediaRecipe.curation_history` check for one merged recipe. |

Mechanical validators pass.

## Identity and Grounding

The generated record denotes the right DSMZ source medium. DSMZ Medium 1178 and live MediaDive Medium 1178 are `AQUINCOLA MEDIUM`, and the KOMODO owner explicitly cites DSMZ Medium 1178. The two normalized inputs are exact source duplicates, and no extra Aquincola source owner was found in the searched paths listed above.

The only ChEBI-grounded direct chemical rows, Fructose and Agar, are correctly grounded. Yeast extract and Peptone are undefined mixtures and are correctly left ungrounded.

## Evidence

DSMZ Medium 1178 supports a simple base formulation:

| Component | Source amount |
| --- | ---: |
| Yeast extract | 1.0 g |
| Peptone | 1.0 g |
| Fructose | 0.5 g |
| Distilled water | 1000.0 ml |

It then states `pH 7.0` and says agar may be added at 15 g/L to solidify the medium.

The generated record preserves the three non-water base ingredients, the final pH, and a 15 g/L Agar row. It omits the 1000 ml distilled water row and models the optional agar addition as a required top-level ingredient plus `SOLID_AGAR` physical state.

## Completeness

The source is short and contains no stock solutions, preparation sequence beyond pH and optional agar, organism growth claims, variants, or required atmosphere. Empty solution, target-organism, and variant slots are acceptable here.

The missing final water row is the only ingredient omission. The optional agar note is retained, but the base liquid form is not explicit because `physical_state` is only `SOLID_AGAR`.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| major | Final distilled water is missing. | DSMZ Medium 1178 and MediaDive Medium 1178 list `Distilled water 1000.0 ml`; the generated merge and both normalized owners contain only Yeast extract, Peptone, Fructose, and Agar. | Add the final water row to the DSMZ/MediaDive owner and propagate it through the KOMODO duplicate before regenerating the merge. |
| minor | Optional agar is modeled as required. | DSMZ says agar may be added at 15 g/L to solidify the medium. The YAML sets `physical_state: SOLID_AGAR` and includes Agar as a top-level ingredient, so the liquid base variant is not represented. | Preserve the liquid base recipe and model agar as a solidifying optional variant or clearly scoped modification. |

No blocker findings: identity, duplicate linkage, pH, and direct non-water ingredients match DSMZ Medium 1178.

## Recommended Edits

1. Add `Distilled water` at 1000 ml/L to `data/normalized_yaml/bacterial/aquincola_medium.yaml` and mirror that fix through `data/normalized_yaml/bacterial/KOMODO_1178_AQUINCOLA_medium.yaml`.
2. Represent the 15 g/L agar row as an optional solidification of the pH 7.0 base medium, or otherwise make the record explicit that it is only the solidified variant.
3. Regenerate `data/merge_yaml/merged/AQUINCOLA_MEDIUM.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validators on both normalized source records.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating the Aquincola merge.
- Recompare the regenerated record against DSMZ Medium 1178 and live MediaDive Medium 1178, checking the water row and agar optionality.

## Additional Notes

None found.

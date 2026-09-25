# YAML Record Review: pelagicoccus_agar

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/pelagicoccus_agar__922e0a8a.yaml`
- Started UTC: 2026-09-24T20:12:00Z
- Finished UTC: 2026-09-24T20:12:04Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pelagicoccus_agar__922e0a8a.yaml`, a generated `MediaRecipe` merge record.

- ID: `CultureMech:003004`
- Label: `pelagicoccus_agar`
- Category: `bacterial`
- Source term: `mediadive.medium:J659`
- Physical state: `SOLID_AGAR`
- Maintained owner: `data/normalized_yaml/bacterial/pelagicoccus_agar.yaml`
- Generated from: `pelagicoccus_agar`

## Validation

- Passed: open LinkML validation of `data/merge_yaml/merged/pelagicoccus_agar__922e0a8a.yaml` against `src/culturemech/schema/culturemech.yaml` as `MediaRecipe`; no issues found.
- Passed: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pelagicoccus_agar__922e0a8a.yaml --out /private/tmp/pelagicoccus_agar__922e0a8a.strict.tsv --workers 1 --quiet`; the TSV contained only its header, so strict validation found 0 errors.
- Passed: focused `linkml-reference-validator validate data data/merge_yaml/merged/pelagicoccus_agar__922e0a8a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; 0 references were checked.
- Passed: focused `linkml-term-validator validate-data data/merge_yaml/merged/pelagicoccus_agar__922e0a8a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`.
- Not checked: embedded `curation_history`; the documented `just validate-history` target validates standalone `history/` YAML rather than `MediaRecipe.curation_history` embedded in generated records.

## Identity and Grounding

`mediadive.medium:J659` resolves to JCM Medium J659, "PELAGICOCCUS AGAR", and links to `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=659`. JCM Medium 659 is Pelagicoccus Agar and supports the `SOLID_AGAR` state, pH 7.5, 55.1 g/L Marine agar 2216, and 9.1 g/L R2A agar.

The generated record's source identity, category, physical state, source pH, and source accession are coherent. Its component representation is stale relative to the 2026-09-11 maintained repair in `data/normalized_yaml/bacterial/pelagicoccus_agar.yaml`.

## Evidence

- MediaDive J659 represents 1000 ml Main solution with 55.1 g Marine agar 2216, 9.1 g R2A agar, 750 ml Artificial seawater, and 250 ml Distilled water.
- JCM Medium 659 prints the same final formula and gives pH 7.5.
- MediaDive and JCM both scope 24 g NaCl, 7 g MgSO4 x 7 H2O, 5.3 g MgCl2 x 6 H2O, 0.7 g KCl, 0.1 g CaCl2 x 2 H2O, and water to the separate 1000 ml Artificial seawater stock.
- The generated record carries the Artificial seawater salts as direct final-medium ingredients and has no 750 ml Artificial seawater solution or 250 ml Distilled water row.
- The generated record grounds `Marine agar 2216` and `R2A agar` to generic agar chemistry instead of treating both as opaque commercial complex products.

## Completeness

The generated record is materially incomplete because it lacks the final 750 ml/L Artificial seawater addition, the 250 ml/L final Distilled water addition, and the nested Artificial seawater solution that owns the salt recipe. It also lacks the repaired `variant_children` that connect this JCM 659 solid parent to the TOGO M675 source duplicate and TOGO M676 liquid physical-state variant.

Empty optional fields are not defects.

An ignored-inclusive exact search of `data`, `src`, and `scripts` for `mediadive.medium:J659`, `CultureMech:003004`, `GRMD=659`, `data/normalized_yaml/bacterial/pelagicoccus_agar.yaml`, and `RESOLVED_JCM_659_PELAGICOCCUS_AGAR` found the maintained owner, this generated record, sibling generated records from the TOGO M675 and M676 imports, and the September repair script.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated record flattens the Artificial seawater stock into final-medium ingredients and drops two final solution components. | MediaDive J659 and JCM 659 both define a 750 ml Artificial seawater addition plus 250 ml Distilled water in the final medium, with NaCl, MgSO4 x 7 H2O, MgCl2 x 6 H2O, KCl, CaCl2 x 2 H2O, and 1 L water scoped to the Artificial seawater stock. The generated record has the stock salts as top-level `ingredients` and omits the 750 ml/L stock and 250 ml/L final water rows. | Future source-level edits belong in `data/normalized_yaml/bacterial/pelagicoccus_agar.yaml`; its 2026-09-11 repair already has the Artificial seawater stock nested under `solutions`. |
| Major | The two opaque commercial agar products are over-grounded as generic agar. | `Marine agar 2216` is grounded to `CHEBI:2509` agar, and `R2A agar` has `mediaingredientmech_chebi_term: CHEBI:2509`. The sources identify both rows as commercial complex powders, not pure agar. | `data/normalized_yaml/bacterial/pelagicoccus_agar.yaml`, already repaired with `Marine agar 2216 (BD-Difco)` and `R2A agar (BD-Difco)` left ungrounded. |
| Minor | The generated preparation step attaches a liquid-variant comment to the solid parent recipe. | JCM 659 has a comment about preparing a liquid medium with Marine broth and R2A broth. The generated solid record turns that note into a `MIX` preparation step, while the maintained owner keeps only the solid formulation's mix and pH-adjust steps and links the liquid formulation as a variant. | `data/normalized_yaml/bacterial/pelagicoccus_agar.yaml`, already repaired with `variant_children` for the M675 source duplicate and M676 liquid variant. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/pelagicoccus_agar__922e0a8a.yaml` from `data/normalized_yaml/bacterial/pelagicoccus_agar.yaml` so the generated record carries the repaired Artificial seawater solution, final Distilled water row, opaque commercial agar rows, and variant child links.
2. If regeneration still flattens Artificial seawater or preserves `CHEBI:2509` on the commercial products, fix the merge/import logic that reads nested `solutions` and opaque commercial ingredients before rerunning the merge generator.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on the regenerated generated record.
- Diff the regenerated `pelagicoccus_agar__922e0a8a.yaml` against `data/normalized_yaml/bacterial/pelagicoccus_agar.yaml` and confirm it includes a 750.0 ml/L Artificial seawater stock with six child components, 250.0 ml/L Distilled water, ungrounded Marine agar and R2A agar rows, pH 7.5, and both `variant_children`.
- Manually recheck the regenerated parent against MediaDive J659 and JCM Medium 659 before closing the issue, because JCM 659 also contains a separate liquid-variant comment that should not be emitted as a solid-medium preparation step.

## Additional Notes

TOGO M675 and M676 were inspected as sibling records because the maintained JCM 659 owner now links them explicitly: M675 imports the same solid agar recipe, while M676 captures the liquid formulation described in the JCM 659 comment.

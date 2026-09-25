# YAML Record Review: alkaliphilus_succinacidus_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/alkaliphilus_succinacidus_medium__ee8b5e3e.yaml`
- Started UTC: 2026-09-21T11:12:59Z
- Finished UTC: 2026-09-21T11:13:48Z
- Verdict: needs curation

## Target

| Field | Observed value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:002981` |
| Name | `alkaliphilus_succinacidus_medium` |
| Original name | `ALKALIPHILUS SUCCINACIDUS MEDIUM` |
| Source identity | JCM Medium J634, `mediadive.medium:J634` |
| Generated status | Generated one-source merge |
| Generated path | `data/merge_yaml/merged/alkaliphilus_succinacidus_medium__ee8b5e3e.yaml` |
| Maintained input | `data/normalized_yaml/bacterial/alkaliphilus_succinacidus_medium.yaml` |

The generated record is a one-source merge of the normalized JCM record for Alkaliphilus succinacidus medium.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/alkaliphilus_succinacidus_medium__ee8b5e3e.yaml` | Passed; no issues found. |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/alkaliphilus_succinacidus_medium__ee8b5e3e.yaml --out /private/tmp/alkaliphilus_succinacidus_medium__ee8b5e3e.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 `ERROR` rows emitted. |
| Reference | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/alkaliphilus_succinacidus_medium__ee8b5e3e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/alkaliphilus_succinacidus_medium__ee8b5e3e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Documented focused validator | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints are unavailable in this checkout because project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before target-specific validation. The no-project commands above exercise the same schema and validation code with Python 3.11.

## Identity and Grounding

The ID, source accession, label, and normalized owner all agree that this record denotes Alkaliphilus succinacidus medium from JCM J634:

- `id: CultureMech:002981`
- `name: alkaliphilus_succinacidus_medium`
- `media_term.preferred_term: JCM Medium J634`
- `media_term.term.id: mediadive.medium:J634`
- `notes: Source: JCM | Link: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=634`

Direct source verification is incomplete. The JCM `GRMD=634` endpoint returned a JCM "Medium data" page stating "Nothing found." TOGO M648 still names the recipe `Alkaliphilus Succinacidus Medium`, carries `original_media_id: JCM_M634`, and preserves the same JCM URL as `src_url`, so the formulation can be checked against an imported mirror but not against the original JCM page.

Ingredient grounding is mostly exact for simple salts and hydrated salts. `Yeast extract` is the only ungrounded component in the JCM record.

## Evidence

Inspected source documents:

- JCM `GRMD=634`, fetched from `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=634`
- TOGO Medium M648 API, fetched from `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M648`

Supported by TOGO M648:

- The Alkaliphilus succinacidus medium identity, source derivation from `JCM_M634`, and original JCM URL.
- The ingredient set: KH2PO4, K2HPO4, (NH4)2SO4, NaCl, MgSO4 x 7H2O, CaCl2 x 2H2O, sodium succinate, yeast extract, L-cysteine HCl x H2O, Na2S x 9H2O, and resazurin.
- The normalized amounts in the JCM record, including 1 mg/L resazurin represented as 0.001 g/L.
- The pH 7.2 adjustment, N2-CO2 80:20 cooling and vessel atmosphere, autoclaving after butyl-stopper sealing, separate 5% reducing-stock preparation under N2, and anaerobic addition of the cysteine and sulfide stocks before inoculation.

Unsupported or only indirectly supported:

- The cited JCM endpoint no longer serves medium number 634, so JCM itself did not directly support any scientific claim during this review.
- The generated JCM record has an active TOGO-sourced sibling at `data/normalized_yaml/bacterial/TOGO_M648_Alkaliphilus_Succinacidus_Medium.yaml` with the same medium name and original JCM accession, but the two records remain separate generated outputs.

## Completeness

Consequential gaps:

- The original JCM page is unavailable, and the record has no durable archived source URL or alternate primary source.
- The JCM and TOGO imports of the same original JCM medium are not reconciled into one canonical output.
- `Yeast extract` has no ontology grounding.
- Target organisms are absent; no focused growth-evidence search was performed during this review.

Empty optional slots correctly left empty:

- No target organism was asserted, so there is no unsupported growth claim in this generated record.
- No storage condition was asserted in the inspected source mirror.
- No discussion or quality flags were asserted.

Bounded absence checks:

- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -type f -name '*alkaliphilus_succinacidus_medium__ee8b5e3e.md'` search found no pre-existing report for this generated record before this report was written.
- A gitignore-independent `rg --no-ignore --hidden` search over `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for `alkaliphilus_succinacidus_medium`, `ALKALIPHILUS SUCCINACIDUS MEDIUM`, `J1074`, and `ee8b5e3e` found the JCM normalized owner, this generated JCM output, the separate TOGO M648 normalized owner, and an older uppercase TOGO M648 generated artifact.

## Findings

### Blocker

None found.

### Major

1. **The same original JCM_M634 recipe remains split across JCM and TOGO records instead of one canonical generated record.**

   Evidence: `data/merge_yaml/merged/alkaliphilus_succinacidus_medium__ee8b5e3e.yaml` is generated only from `alkaliphilus_succinacidus_medium.yaml`, while `data/normalized_yaml/bacterial/TOGO_M648_Alkaliphilus_Succinacidus_Medium.yaml` carries the same name plus `Original source: JCM - JCM_M634` and `Original URL: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=634`. The adjacent TOGO record contains a 1 g/L resazurin import error, explicit 1 L distilled water, and variable gas pseudo-ingredients, so it fingerprints separately despite deriving from the same JCM recipe.

   Owner: fix the TOGO M648 normalized record or TOGO importer normalization for resazurin, water, and gas pseudo-ingredients, then rerun duplicate merging so the JCM and TOGO imports collapse or are deliberately source-linked.

### Minor

1. **The cited primary JCM URL is stale.**

   Evidence: fetching `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=634` returned a JCM medium search page for medium number 634 with no recipe body. The TOGO M648 mirror preserves the imported JCM_M634 recipe, but the record's direct `notes` URL is no longer enough to verify the formula.

   Owner: add a durable mirror citation, archived URL, or source note to `data/normalized_yaml/bacterial/alkaliphilus_succinacidus_medium.yaml`, then regenerate.

2. **Yeast extract is ungrounded.**

   Evidence: the `Yeast extract` ingredient lacks both `term` and `mediaingredientmech_chebi_term`, although the amount itself is source-supported.

   Owner: map yeast extract in `data/normalized_yaml/bacterial/alkaliphilus_succinacidus_medium.yaml` to the accepted FoodOn yeast-extract term during ingredient enrichment, then regenerate.

## Recommended Edits

1. Reconcile `data/normalized_yaml/bacterial/TOGO_M648_Alkaliphilus_Succinacidus_Medium.yaml` with `data/normalized_yaml/bacterial/alkaliphilus_succinacidus_medium.yaml`: correct TOGO M648 resazurin from 1 g/L to 1 mg/L, remove or remodel distilled water and gas pseudo-ingredients, and make the two records merge or link as duplicate imports of JCM_M634.
2. Add a durable provenance note or archive for the now-unavailable JCM `GRMD=634` source URL on the JCM normalized owner.
3. Ground `Yeast extract` to the accepted FoodOn yeast-extract term.
4. Regenerate `data/merge_yaml/merged/` and rendered products from the normalized inputs.

## Follow-up Checks

- Rerun schema, strict, reference, and term validators on the corrected JCM and TOGO normalized records.
- Rerun duplicate merging and verify that the JCM J634 and TOGO M648 imports no longer produce unreconciled canonical outputs for the same original medium.
- Manually compare the regenerated record against TOGO M648 to confirm 1 mg/L resazurin, pH 7.2, and the 5% anaerobic reducing-stock procedure are preserved.
- Run the concentration-plausibility report and confirm the `INDICATOR_UNIT_SLIP` row for `TOGO_M648_Alkaliphilus_Succinacidus_Medium.yaml` is gone.

## Additional Notes

- This review is read-only. It intentionally leaves `data/merge_yaml/merged/alkaliphilus_succinacidus_medium__ee8b5e3e.yaml`, its normalized owner, the adjacent TOGO owner, and generated pages unchanged.
- Generated files under `data/merge_yaml/merged/` are derived artifacts. Corrections belong in `data/normalized_yaml/bacterial/alkaliphilus_succinacidus_medium.yaml`, `data/normalized_yaml/bacterial/TOGO_M648_Alkaliphilus_Succinacidus_Medium.yaml`, or the import/merge/enrichment logic that owns the bad transform.

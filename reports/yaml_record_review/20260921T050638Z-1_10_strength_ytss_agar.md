# YAML Record Review: 1_10_strength_ytss_agar

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/1_10_strength_ytss_agar.yaml`
- Started UTC: 20260921T050354Z
- Finished UTC: 20260921T050638Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:008905` |
| Slug | `1_10_strength_ytss_agar` |
| Original name | `1/10-strength YTSS agar` |
| Category | `bacterial` |
| Generated or maintained | Generated merge artifact |
| Maintained owner | `data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml` |
| Source accession | `TOGO:M2318` |
| Merge fingerprint | `55db27a079d929e4ad99f4d6e7169fd54be01a1d5f689c8c6bd7d1c93ad10976` |

Reviewed the generated singleton merge for TOGO Medium M2318. The exact ID/accession/fingerprint search over ignored and hidden YAML files in `data/normalized_yaml` and `data/merge_yaml/merged` found only this merge artifact plus the maintained normalized owner. An exact search over the TSV/JSON catalogs found the same ID only in `data/culturemech_recipe_catalog.tsv`, `data/normalized_yaml/recipe_index.json`, `data/normalized_yaml/bacterial_index.json`, and `data/normalized_yaml/by_source_togo_index.json`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/1_10_strength_ytss_agar.yaml` | Passed with no output |
| Strict validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/1_10_strength_ytss_agar.yaml --out /private/tmp/1_10_strength_ytss_agar.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 `ERROR` rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/1_10_strength_ytss_agar.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/1_10_strength_ytss_agar.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded `curation_history` | Not checked | Not checked: no focused validator is documented for generated merge-file `MediaRecipe.curation_history`; the repository's `validate-history` target validates standalone history files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints were not usable in this Python 3.13 checkout because project setup attempts to build `llvmlite==0.46.0` and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project `uv` invocations above use the repository schema and focused validator scripts without resolving the broken project environment.

## Identity and Grounding

- The generated record denotes a single TOGO record, `TOGO:M2318`, with the TOGO name `1/10-strength YTSS agar`; both the TOGO live API and the record's `media_term.term.label` agree on that accession and name.
- `TOGO:M2318` returns a four-item component list: distilled water at 1 L, yeast extract at 0.4%, sea salts at 20 g/L, and tryptone at 0.25%.
- The generated merge is stale relative to the maintained normalized owner. The owner has already converted the TOGO `1 L` water value to `1000 ML_PER_L`, added ingredient-level `source` and TOGO-specific notes, added `references`, restored the exact `FOODON:03315426` grounding for yeast extract, and marked the record `ingredients_curated`; none of that Sep 11 repair is present in `data/merge_yaml/merged/1_10_strength_ytss_agar.yaml`.
- The identity is internally inconsistent as an agar record. M2318 is named `1/10-strength YTSS agar`, and the TOGO comment says Jannaschia sp. strain CCS1 was isolated on that agar, but neither the generated merge nor the normalized owner carries an agar or gelling-agent ingredient and both set `physical_state: LIQUID`.
- The TOGO ingredient amounts are not source-aligned for a 1/10-strength recipe. Moran et al. 2007, DOI `10.1128/AEM.02580-06`, states that CCS1 was isolated on 1/10-strength YTSS agar and parenthetically defines full-strength YTSS as the `0.4%` yeast extract plus `0.25%` tryptone formulation. TOGO M2318 and the CultureMech record copy those full-strength percentages into a 1/10-strength record.

## Evidence

- The TOGO live API at `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid` was queried with `gm_id=M2318`; the static `/medium/M2318` page is only a JavaScript shell, and the frontend bundle shows that the app posts `gm_id=M2318` to the same `gmdb_medium_by_gmid` SPARQList endpoint.
- The TOGO response supports the record name, the `TOGO:M2318` accession, the four imported component identities, water as `1 L`, yeast extract as `0.4%`, sea salts as `20 g/L`, and tryptone as `0.25%`.
- The TOGO response does not support `physical_state: LIQUID`; it labels the medium as agar and contains no explicit liquid/solid field.
- The TOGO response does not provide agar concentration, pH, sterilization, incubation, or preparation steps.
- The nearest primary source is Moran et al. 2007. Its Methods section supports that Jannaschia sp. strain CCS1 was isolated from Bodega Head, CA seawater on 1/10-strength YTSS agar, but it does not list an agar amount or a complete 1/10-strength formulation.
- A public protocols.io YTSS Medium PDF, DOI `10.17504/protocols.io.dbq2mv`, was inspected as a bounded cross-check. It lists both 1/2 and 1/10 YTSS recipes per 500 ml and shows 1/10 YTSS with 0.25 g tryptone, 0.4 g yeast extract, 10 g sea salts, and 7.5 to 9 g agar per 500 ml. This is compatible with M2318's identity but conflicts with the TOGO import's yeast-extract and tryptone strengths.

## Completeness

- Consequential gap: agar medium identity is not represented in either `physical_state` or `ingredients`.
- Consequential gap: the 1/10-strength label is not reconciled with the imported full-strength YTSS percentages for yeast extract and tryptone.
- Consequential gap: no pH, sterilization, or preparation steps are carried. The inspected TOGO source does not provide them.
- Consequential provenance gap: the generated merge preserves only a free-text TOGO URL in `notes`; the normalized owner has a structured TOGO `references` row, but no original Moran et al. or protocols.io reference.
- Empty target-organism claims are correctly empty; the record has no specific organism assertion to validate, and the TOGO M2318 detail response contains only a free-text CCS1 isolation comment.
- A gitignore-independent search under `data/raw`, `data/import_tracking`, and `data/reference` found TOGO importer documentation and a `deep_research_priority.json` inventory entry for this record, but no cached raw M2318 payload or local original-source link for this formulation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale relative to the Sep 11 maintained repair. It still records distilled water as `1 G_PER_L`, lacks per-ingredient TOGO source annotations, lacks the structured `references` row, lacks the normalized owner's `data_quality_flags`, and leaves yeast extract ungrounded. | `data/merge_yaml/merged/1_10_strength_ytss_agar.yaml` has the Aug 6 merge output; `data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml` has the Sep 11 `RESOLVED_SPARSE_TOP_SCORE15` repair with `1000 ML_PER_L`, `source: TOGO M2318`, `references`, and `FOODON:03315426`. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml`. |
| Major | `physical_state: LIQUID` and the missing agar ingredient contradict the TOGO/Moran agar identity. | TOGO M2318 is named `1/10-strength YTSS agar`, and its embedded Moran et al. 2007 comment says CCS1 was isolated on 1/10-strength YTSS agar. Neither the generated record nor the maintained owner lists agar or another solidifying agent. | `data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml` |
| Major | The yeast-extract and tryptone strengths are over-stated for a 1/10-strength recipe. | Moran et al. 2007 identifies `0.4%` yeast extract and `0.25%` tryptone as full-strength YTSS; TOGO M2318 applies those exact percentages to a 1/10-strength recipe. The protocols.io YTSS Medium PDF lists lower 1/10 YTSS yeast extract and tryptone amounts. | `data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml` |
| Minor | Original-source provenance is too thin for a conflicted database import. | TOGO `src_url` is empty and CultureMech preserves only `https://togomedium.org/medium/M2318`; the TOGO comment text is traceable to Moran et al. 2007, and the protocols.io YTSS protocol gives a concrete 1/10-strength agar formulation. | `data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml` |

## Recommended Edits

1. Regenerate the merge layer from the normalized owner so the generated record stops publishing the stale `1 G_PER_L` water amount and missing Sep 11 reference/flag/source repairs.
2. Curate `data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml` against TOGO M2318 plus original YTSS sources before the next regeneration.
3. Change the maintained `physical_state` to a solid agar state and add an explicit agar row only after selecting an inspected source for the agar amount. The TOGO/Moran sources establish the agar identity, but not the agar concentration.
4. Correct the maintained yeast-extract and tryptone concentrations for 1/10-strength YTSS or add a `data_quality_flags`/discussion item that records the TOGO-versus-primary conflict if the curator decides to preserve the live TOGO values verbatim.
5. Add structured references for Moran et al. 2007 and any selected complete 1/10 YTSS protocol so downstream users can distinguish the TOGO API assertion from the original strain-isolation evidence and later lab formulations.

## Follow-up Checks

- Re-run `just validate-strict data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml` or the no-project strict equivalent after the normalized edit.
- Re-run `just validate-terms data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml` or the no-project term equivalent after adding agar and any new ontology grounding.
- Re-run `just validate-references data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml` or the no-project reference equivalent after adding DOI/URL references.
- Re-run the merge generator and verify that `data/merge_yaml/merged/1_10_strength_ytss_agar.yaml` contains the repaired concentrations, solid agar state, structured references, and new agar row.

## Additional Notes

- `data/raw/togo/README.md` documents the same SPARQList endpoint shape used by the live TOGO frontend; no local `data/raw/togo/M2318*` payload was present to diff against the live response.
- The protocols.io PDF is an independent cross-check, not a direct source for TOGO M2318. It should be reconciled manually with the intended CultureMech record before importing its 1/10-strength YTSS values.

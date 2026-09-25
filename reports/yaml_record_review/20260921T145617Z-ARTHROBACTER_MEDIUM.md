# YAML Record Review: ARTHROBACTER medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ARTHROBACTER_MEDIUM.yaml`
- Started UTC: 2026-09-21T14:56:17Z
- Finished UTC: 2026-09-21T14:56:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:005114` |
| Label | `arthrobacter_medium` |
| Source identity | KOMODO `378`, enriched from DSMZ / MediaDive Medium 378 |
| Generated status | Generated merge under `data/merge_yaml/merged/`; do not edit in place |
| Maintained owners | `data/normalized_yaml/bacterial/KOMODO_378_ARTHROBACTER_medium.yaml`; `data/normalized_yaml/bacterial/arthrobacter_medium.yaml` |
| Merge provenance | `merged_from` lists KOMODO 378 and DSMZ / MediaDive 378 as source duplicates |

This review covers exactly `data/merge_yaml/merged/ARTHROBACTER_MEDIUM.yaml`. `find reports/yaml_record_review -name '*ARTHROBACTER_MEDIUM.md' -print` searched the ignored `reports/yaml_record_review/` tree and found no prior report named for this target.

`rg --no-ignore --hidden -n 'ARTHROBACTER medium|ARTHROBACTER MEDIUM|komodo.medium:378|KOMODO_378' data/raw data/normalized_yaml` searched the existing raw and normalized data trees, including ignored files, for the KOMODO label and ID. It found the normalized KOMODO file and generated indexes, but no local raw KOMODO source capture.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARTHROBACTER_MEDIUM.yaml` | Passed with exit 0 and no issues emitted. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARTHROBACTER_MEDIUM.yaml --out /private/tmp/ARTHROBACTER_MEDIUM.strict.tsv --workers 1 --quiet` | Passed with exit 0. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARTHROBACTER_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARTHROBACTER_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The only emitted message was the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | `just validate-history` | Not checked: the repository exposes this validator for standalone `history/*.yaml` records, not for embedded `MediaRecipe.curation_history` blocks in one merged recipe. |

The project `just` wrappers were not rerun in this pass because this checkout currently resolves through Python 3.13 and attempts to build `llvmlite==0.46.0`, which fails before any target-specific YAML validation. The no-project commands above exercise the narrow validators against this one generated record.

## Identity and Grounding

The KOMODO and DSMZ owners are legitimate source duplicates. The KOMODO normalized owner says KOMODO 378 cites DSMZ Medium 378, links to `data/normalized_yaml/bacterial/arthrobacter_medium.yaml` as `SOURCE_DUPLICATE`, and has the same physical state, pH, ingredient set, and concentrations. The DSMZ owner points back to the KOMODO owner with the same relationship.

DSMZ / MediaDive Medium 378 reports `ARTHROBACTER MEDIUM`, complex medium, pH 7.0, and the same PDF link stored in the DSMZ owner. The DSMZ PDF itself lists the same salts, mannitol, yeast extract, and trace salts shown in the generated record. The chemical groundings align with the hydrated forms and salts printed by DSMZ.

## Evidence

DSMZ Medium 378 lists the following per liter: K2HPO4 1.770 g, KH2PO4 0.680 g, NaCl 0.140 g, CaCl2 0.132 g, MgSO4 x 7 H2O 0.200 g, Mannitol 10.000 g, Yeast extract 0.080 g, FeSO4 x 7 H2O 2.500 mg, H3BO3 2.900 mg, CoSO4 x 7 H2O 1.200 mg, CuSO4 x 5 H2O 0.100 mg, MnCl2 x 4 H2O 0.090 mg, Na2MoO4 x 2 H2O 2.500 mg, ZnSO4 x 7 H2O 1.200 mg, and Distilled water 1000.000 ml.

The generated YAML carries all DSMZ solute rows and converts the milligram trace salts to grams per liter correctly. It omits the final 1000 ml distilled-water row that both the DSMZ PDF and MediaDive 378 REST payload contain.

The DSMZ source instructs pH adjustment to 7.0 and incubation under 5% O2 plus 95% N2. The DSMZ normalized owner carries that as `preparation_steps`; the KOMODO owner and the generated canonical carry only `ph_value: 7.0`, so the incubation atmosphere is dropped after the KOMODO record wins the merge.

## Completeness

Consequential gaps:

- `Distilled water` at 1000 ml is missing from both maintained owners and the generated record.
- The incubation atmosphere from DSMZ is missing from the generated record.
- Neither maintained owner has a formal `references` list for the DSMZ PDF, MediaDive 378 REST endpoint, or the KOMODO source table.

Optional `target_organisms` are absent. That is acceptable because the DSMZ recipe and inspected MediaDive source do not contain curated growth evidence for a specific strain.

## Findings

| Severity | Finding | Evidence | Maintained owner for a fix |
|---|---|---|---|
| Major | The DSMZ 1000 ml water row is missing. | DSMZ Medium 378 and MediaDive 378 both list `Distilled water 1000.000 ml`; neither normalized owner nor the generated merge includes a water ingredient. | Add the water row to `data/normalized_yaml/bacterial/arthrobacter_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_378_ARTHROBACTER_medium.yaml`, then regenerate. |
| Major | The generated canonical drops DSMZ incubation atmosphere. | The DSMZ owner has a preparation step saying to adjust pH to 7.0 and incubate under 5% O2 + 95% N2; the generated KOMODO canonical has only `ph_value: 7.0`. | Add the DSMZ pH/incubation step to the KOMODO duplicate, or make merge generation preserve identical source-duplicate preparation from the DSMZ parent. |
| Minor | Formal source references are absent. | Source URLs are embedded only in free-text `notes`; the reference validator ran 0 checks. | Add `references` entries to the two normalized owners for DSMZ Medium 378 and the inspected MediaDive 378 REST source, and add the KOMODO table URL if the source is recoverable. |
| Minor | The KOMODO import timestamp is malformed. | The first `curation_history` timestamp is `2026-01-27T01:15:02.fZ`, which is not a valid ISO timestamp. | Normalize that timestamp in the KOMODO owner through a guarded curation-history cleanup. |

## Recommended Edits

1. Add `Distilled water` at `1000.0 ML_PER_L` to both maintained Arthrobacter Medium owners.
2. Preserve the DSMZ pH/incubation instruction in the KOMODO owner or in merge logic so the generated canonical keeps the 5% O2 / 95% N2 atmosphere.
3. Add formal `references` for the DSMZ PDF and MediaDive 378 REST record; locate and add a KOMODO source URL before adding a KOMODO reference.
4. Normalize the malformed KOMODO import timestamp.
5. Regenerate `data/merge_yaml/merged/ARTHROBACTER_MEDIUM.yaml` after the normalized owners are corrected.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/arthrobacter_medium.yaml` and `just validate data/normalized_yaml/bacterial/KOMODO_378_ARTHROBACTER_medium.yaml`.
- Run `just validate-references` for both edited owners after adding formal references.
- Run `just verify-merges` and confirm KOMODO 378 still merges with DSMZ / MediaDive 378 as a source duplicate.
- Run the same open-schema, strict, reference, and term validators against the regenerated `ARTHROBACTER_MEDIUM.yaml`.
- Manually compare the regenerated output against the DSMZ PDF and verify the water row and 5% O2 / 95% N2 instruction are present.

## Additional Notes

- The duplicate relationship itself looks sound; unlike the preceding artificial-water records, this merge does not appear overbroad.
- The source exact search covered `data/raw` and `data/normalized_yaml` with ignored files included. It did not find a raw KOMODO source capture in those existing trees.

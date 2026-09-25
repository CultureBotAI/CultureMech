# YAML Record Review: Anaerobic Alkaline YE Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml
- Started UTC: 2026-09-21T12:12:37Z
- Finished UTC: 2026-09-21T12:13:47Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:007563`
- Label: `Anaerobic Alkaline YE Medium`
- Category: `bacterial`
- Source identity on canonical merge: TOGO `M1047`, original source JCM `M993`
- Generated status: generated merge record with fingerprint `74716baf312eb9bc8ad41268aa9788ef5f2a389c6981fa914e3c0bfef74ac94a`
- Merge lineage: two sources, `data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml`
- Maintained owner for future record edits: the two normalized source records own their imported data, while merge matching rules own the erroneous cross-source collapse

## Validation

- Open schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml`
  - Result: passed; no issues found
- Strict schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml --out /private/tmp/Anaerobic_Alkaline_YE_Medium.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 total checks
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed
- Embedded curation history: Not checked. The documented `just validate-history` recipe validates standalone records under `history/`; I did not find a focused embedded `MediaRecipe.curation_history` validator for one merge file.

## Identity and Grounding

The record's canonical identity is TOGO `M1047`, `Anaerobic Alkaline YE Medium`, derived from JCM medium `993`. The inspected TOGO M1047 API payload reports `original_media_id: JCM_M993` and a JCM `GRMD=993` source URL, and the inspected JCM 993 page is `ANAEROBIC ALKALINE YE MEDIUM`.

The generated merge is an identity failure. It also merged TOGO `M1145`, `Alkaliphilus Lact Medium`, which the live TOGO payload maps to JCM `M1076`; the inspected JCM 1076 page is `ALKALIPHILUS LACT MEDIUM`, has different salinity, different water volume, a maltose addition, different carbonate chemistry, a different sulfide stock volume, and final pH 8.2. Those are related alkaline anaerobic media, not duplicate source views of the same medium.

The actual duplicate source for the M1047/JCM 993 recipe is the MediaDive J993 normalized owner at `data/normalized_yaml/specialized/anaerobic_alkaline_ye_medium.yaml`, which is still emitted separately as `data/merge_yaml/merged/anaerobic_alkaline_ye_medium__1a061f54.yaml`.

## Evidence

Supported:

- TOGO M1047 and JCM 993 support the source identity, the M1047 name, 2 g NaCl, 1 g NH4Cl, 0.1 g KH2PO4, 0.1 g K2HPO4, 0.1 g KCl, 0.1 g MgCl2.6H2O, 3 g Tris base, 3 g Na2S2O3.5H2O, 1 ml trace element solution, 1 mg resazurin, and 900 ml distilled water.
- JCM 993 supports adjusting the base mix to pH 9.0 with NaOH, autoclaving under N2, replacing the gas phase after cooling with N2-CO2 4:1 v/v, then adding 20 ml of 10 percent yeast extract, 30 ml of 8 percent NaHCO3, and 8 ml of 5 percent Na2S.9H2O from sterile anaerobic stocks.
- TOGO M1145 and JCM 1076 support Alkaliphilus Lact Medium as a distinct JCM 1076 formulation with 20 g NaCl, 950 ml water, 10 ml 10 percent yeast extract, 20 ml 0.5 M maltose, 20 ml 8 percent Na2CO3, 6 ml 5 percent Na2S.9H2O, and final pH around 8.2.

Unsupported or over-scoped:

- The merged M1047 record uses the M1145 water and NaCl amounts, so the M1047 formulation is reported as 950 ml water and 20 g NaCl instead of 900 ml water and 2 g NaCl.
- The stock additions are recorded as empty solution stubs with `G_PER_L` units: 1 for trace elements, 30 for 8 percent NaHCO3, 20 for 10 percent yeast extract, and 8 for 5 percent Na2S.9H2O.
- The M1047 1 mg resazurin addition is recorded as `1 G_PER_L`, overstating the source row by three orders of magnitude.
- The M1047 NaOH pH adjustment, N2 autoclave atmosphere, and N2-CO2 headspace replacement were promoted to variable-concentration top-level ingredients instead of preparation or atmosphere conditions.
- No JCM preparation steps survive in the generated record.
- The merge synonym says `alkaliphilus_lact_medium` is a synonym of Anaerobic Alkaline YE Medium, even though the inspected source pages distinguish JCM 993 from JCM 1076.

## Completeness

Consequential gaps:

- The generated record must be split back into two source identities: TOGO M1047/JCM 993 and TOGO M1145/JCM 1076.
- The M1047 source record needs correct water, NaCl, resazurin, and stock-addition units.
- The M1145 source record needs to remain separate and preserve maltose, sodium carbonate, its lower sulfide and yeast-extract stock volumes, and final pH 8.2.
- The TOGO M1047 source record should reconcile with the MediaDive J993 source record after both are source-faithful.
- Structured preparation steps are missing for both input records.
- No structured `references` entries capture TOGO or JCM evidence beyond prose `notes` fields.

Correctly empty or not scored:

- `target_organisms` and `growth_metrics` are empty. The inspected TOGO and JCM sources are recipe sources and do not provide primary strain-growth evidence.
- Empty stock `composition` arrays are not themselves sufficient to fail the record; the failure is that source milliliter additions were converted to `G_PER_L` unknown-solution stubs rather than represented as volume additions with source stock identities.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*Anaerobic_Alkaline_YE_Medium.md' -print` found no prior report for this generated record before the report was written; `find` included ignored report files.
- `rg --no-ignore --hidden -F 'M1145' data/normalized_yaml data/merge_yaml data/culturemech_recipe_catalog.tsv data/culturemech_id_registry.tsv` found the Alkaliphilus Lact normalized owner and this generated merge, plus unrelated records that reference M1145 as a different source accession.
- `rg --no-ignore --hidden -F 'GRMD=993' data/normalized_yaml data/merge_yaml` found the M1047 normalized owner and merge plus the MediaDive J993 normalized owner and separate merge.

## Findings

| ID | Severity | Finding | Maintained owner |
| --- | --- | --- | --- |
| F1 | blocker | `merge_recipes.py` merged TOGO M1047/JCM 993 with TOGO M1145/JCM 1076 even though the inspected source pages are different named media with different formulations and pH behavior. | Merge matching rules plus `data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml` |
| F2 | blocker | The resulting canonical record has the M1047 media term but M1145-scale 950 ml water and 20 g NaCl, so it no longer faithfully denotes either input recipe. | `data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml`, regenerated from corrected normalized inputs and merge rules |
| F3 | major | All source stock additions are represented as `G_PER_L` unknown-solution stubs rather than milliliter additions of 8 percent bicarbonate/carbonate, 10 percent yeast extract, 5 percent sodium sulfide, trace elements, and M1145 maltose stock. | The two normalized TOGO source records and the TOGO importer |
| F4 | major | Resazurin is `1 G_PER_L` even though both inspected JCM sources use 1 mg per recipe. | The two normalized TOGO source records |
| F5 | major | NaOH, carbon dioxide, and N2 were promoted to variable ingredients instead of pH-adjustment and atmosphere conditions. | The two normalized TOGO source records and the TOGO importer |
| F6 | major | JCM preparation text was not imported, including pH 9.0 adjustment, N2 autoclaving, N2-CO2 4:1 gas replacement, sterile anaerobic stock addition, and the M1145 final pH 8.2 check. | The two normalized TOGO source records and the TOGO importer |
| F7 | minor | TOGO and JCM source evidence appears only in prose `notes`; there are no structured `references`, so the reference validator performs zero checks. | The two normalized TOGO source records |

## Recommended Edits

1. Change the merge rules or source fingerprints so TOGO M1047/JCM 993 and TOGO M1145/JCM 1076 never collapse into one canonical medium.
2. Reconcile TOGO M1047 with the MediaDive J993 record after both represent the JCM 993 recipe source-faithfully.
3. Restore the M1047 base quantities to 900 ml water and 2 g NaCl, and leave M1145 with 950 ml water and 20 g NaCl in its own record.
4. Restore the M1047 stock additions as 1 ml trace element solution, 20 ml 10 percent yeast extract, 30 ml 8 percent NaHCO3, and 8 ml 5 percent Na2S.9H2O; restore the M1145 stock additions as 1 ml trace element solution, 10 ml 10 percent yeast extract, 20 ml 0.5 M maltose, 20 ml 8 percent Na2CO3, and 6 ml 5 percent Na2S.9H2O.
5. Convert the 1 mg resazurin rows to mg-aware or correctly normalized concentrations.
6. Move NaOH, N2, and CO2 out of top-level ingredients and into pH-adjustment or atmosphere preparation fields.
7. Add structured preparation steps and source references for TOGO M1047/JCM 993 and TOGO M1145/JCM 1076.
8. Regenerate `data/merge_yaml/merged/*.yaml` and verify the output now has separate JCM 1076 and JCM 993 canonical records, with M1047 and MediaDive J993 collapsed or otherwise reconciled as intended.

## Follow-up Checks

- Re-run open schema, strict schema, reference validation, and term validation on both normalized TOGO owners.
- Re-run the same focused validators on the regenerated merge or merges that replace `data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration to prove the corrected source records are reflected in generated merge output.
- Manually compare regenerated M1047 and M1145 outputs with TOGO M1047, TOGO M1145, JCM 993, and JCM 1076 to verify the source identities, water and NaCl amounts, all stock volumes, resazurin units, atmosphere handling, and pH values.
- Search ignored and tracked data again for `GRMD=993`, `GRMD=1076`, `TOGO:M1047`, `TOGO:M1145`, and `mediadive.medium:J993` to confirm no stale wrong merge or duplicate source split remains.

## Additional Notes

- Direct `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` were not used for this report because the project `uv` environment attempted to build `llvmlite==0.46.0` under Python 3.13 and failed before target-specific validation. The no-project Python 3.11 commands above were used as focused equivalents.
- The TOGO public `/medium/M1047` and `/medium/M1145` pages are SPA shells; the live source identity was checked through `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid`.
- Review of the specialized MediaDive J993 sibling is left for the adjacent generated record `data/merge_yaml/merged/anaerobic_alkaline_ye_medium__1a061f54.yaml`.

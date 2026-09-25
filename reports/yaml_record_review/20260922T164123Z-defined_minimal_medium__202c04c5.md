# YAML Record Review: defined_minimal_medium

- Repository: `CultureBotAI/CultureMech`
- Record: `data/merge_yaml/merged/defined_minimal_medium__202c04c5.yaml`
- Started UTC: 2026-09-22T16:40:10Z
- Finished UTC: 2026-09-22T16:41:19Z
- Verdict: needs curation

## Target

- Reviewed generated record: `data/merge_yaml/merged/defined_minimal_medium__202c04c5.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:009638`
- Name / original name: `defined_minimal_medium` / `Defined minimal medium`
- Source term: `TOGO:M3197`, label `Defined minimal medium`
- Maintained owner: `data/normalized_yaml/bacterial/defined_minimal_medium.yaml`
- Merge provenance: `merge_recipes.py` merged one source, `defined_minimal_medium.yaml`, on fingerprint `202c04c5891c8ffe24419e8b89728b452466737049aa8891abc4d5fc08d918be`.
- Exact ignored-file-inclusive search for `CultureMech:009638`, `TOGO:M3197`, `M3197`, the merge fingerprint, and `source: defined_minimal_medium.yaml` across `data/normalized_yaml/bacterial`, `data/merge_yaml/merged`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, and `reports/yaml_record_review` resolved this target to the maintained normalized owner and reviewed generated merge.

## Validation

| Check | Result |
|---|---|
| Open schema, equivalent to `just validate-schema data/merge_yaml/merged/defined_minimal_medium__202c04c5.yaml` | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`. |
| Strict closed schema | Passed with `scripts/validate_strict.py`: one file scanned, zero files with errors, zero error rows. |
| Reference integrity | Passed with `linkml-reference-validator validate data ... --target-class MediaRecipe`; the validator reported zero checks. |
| Term labels | Passed with `linkml-term-validator validate-data ... --labels -c conf/oak_config.yaml`. |
| Embedded `curation_history` | Not checked separately: `just validate-history` targets standalone `history/*.yaml` records, not `MediaRecipe.curation_history` entries embedded in a medium YAML. The embedded event shape was still covered by schema and strict validation. |

## Identity and Grounding

- The generated file denotes TOGO Medium M3197, a `Defined minimal medium`; the generated merge, normalized owner, ID registry, recipe catalog, TOGO API, and initial import event agree on this source identity.
- The generated record is stale relative to its owner. The maintained normalized owner has a `2026-09-02T07:38:01.295419+00:00` `repair_merged_duplicates.py` event that collapsed the water row back to `1.0 G_PER_L`; this generated merge lacks that event and still has `2.0 G_PER_L`.
- `medium_type: COMPLEX` and `composition_type: UNDEFINED` are not supported. TOGO M3197 is a chemically defined minimal medium with printed millimolar base salts, sodium succinate, sodium nitrate, and a defined Vishniac and Santer trace-elements stock.
- The existing ingredient groundings are chemically broad but mostly plausible for the source labels. The stock's `CaCl2` member has no grounding because it is missing from the YAML altogether.

## Evidence

- The TOGO M3197 comment gives exact final-medium concentrations: `29 mmol/L` Na2HPO4, `11 mmol/L` KH2PO4, `10 mmol/L` NH4Cl, `0.4 mmol/L` MgSO4, `30 mmol/L` sodium succinate, `20 mmol/L` NaNO3, and `2 mL/L` Vishniac and Santer trace elements solution.
- The same comment gives the trace-stock composition: `130 mmol/L` EDTA, `7.64 mmol/L` ZnSO4, `25 mmol/L` MnCl2, `18.5 mmol/L` FeSO4, `0.89 mmol/L` `(NH4)6Mo7O24`, `6.4 mmol/L` CuSO4, `6.72 mmol/L` CoCl2, and `37.4 mmol/L` CaCl2.
- TOGO parsed the named base and trace components into rows but did not attach most quantities to those rows. The source's numeric values remained in `comments[0].comment`, and the import then defaulted thirteen non-water rows to `VARIABLE`.
- The trace-stock `CaCl2` text in the TOGO comment was not imported at all; the YAML has no calcium chloride member for Vishniac and Santer trace elements.
- The `solutions` row stores `Vishniac and Santer trace elements solution` as `2 G_PER_L`, but TOGO says the final recipe adds `2 mL/L`.
- The only inspected TOGO payload had an empty `src_url`. Its formulation comment cites `Crutzen et al., 2008`, but the record has no DOI, PMID, title, or original URL for that source.

## Completeness

- Consequential gaps:
  - Six final-medium ingredient quantities and seven trace-stock quantities are present in source text but lost as `VARIABLE`.
  - The final-medium `2 mL/L` trace-stock addition is represented with the wrong unit family.
  - The CaCl2 trace-stock member is missing.
  - The generated merge has a stale `2.0 G_PER_L` water sum that the normalized owner already repaired to `1.0`.
  - Provenance stops at TOGO and an unresolved `Crutzen et al., 2008` note.
- Empty optional slots correctly left empty:
  - TOGO M3197 says *Paracoccus denitrificans* was grown in this medium, but the inspected API payload does not provide strain, growth conditions, growth metric, or the full Crutzen source; the record should not invent a target-organism evidence object from that text alone.
- Bounded searches:
  - Ignored-file-inclusive exact search for `CultureMech:009638`, `TOGO:M3197`, and the merge fingerprint under `reports/yaml_record_review` found no existing review report for this generated file.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Thirteen source-supported ingredient quantities were replaced by `VARIABLE`. | TOGO M3197's comment prints millimolar values for six final ingredients and seven Vishniac and Santer trace-stock solutes, but the YAML has `VARIABLE` for all of them. | `data/normalized_yaml/bacterial/defined_minimal_medium.yaml` and the TOGO comment parser for M3197-style inline concentrations. |
| Major | The Vishniac and Santer stock addition has the wrong unit family. | The source says the final medium is supplemented with `2 mL/L` Vishniac and Santer trace elements solution; the YAML stores `2 G_PER_L`. | `data/normalized_yaml/bacterial/defined_minimal_medium.yaml` and the TOGO solution migrator. |
| Major | The stock composition is incomplete. | TOGO M3197 lists `37.4 mmol/L CaCl2` inside the trace-elements stock, but no CaCl2 row appears in the normalized or generated YAML. | `data/normalized_yaml/bacterial/defined_minimal_medium.yaml` and the TOGO importer. |
| Major | The generated merge is stale relative to the normalized owner. | The generated water row is `2.0 G_PER_L` with `Merged 2 duplicates`, but the normalized owner has `1.0 G_PER_L` and a 2026-09-02 `REPAIRED_SUMMED_DUPLICATE_MERGE` event. | Regenerate `data/merge_yaml/merged/defined_minimal_medium__202c04c5.yaml` from `data/normalized_yaml/bacterial/defined_minimal_medium.yaml`. |
| Major | The medium is classified as complex/undefined despite a defined source formulation. | TOGO M3197 exposes only defined phosphate, nitrogen, succinate, sulfate, and trace-salt components. | `data/normalized_yaml/bacterial/defined_minimal_medium.yaml`. |
| Minor | The primary article is unresolved. | TOGO cites `Crutzen et al., 2008` in the formulation comment but exposes `src_url: ""`, and the YAML has no `references` entry. | `data/normalized_yaml/bacterial/defined_minimal_medium.yaml`. |

## Recommended Edits

1. Repair `data/normalized_yaml/bacterial/defined_minimal_medium.yaml` by transcribing the six final-medium millimolar quantities from TOGO's M3197 comment.
2. Replace the `2 G_PER_L` trace-stock row with a 2 mL/L solution addition and keep the Vishniac and Santer stock composition nested.
3. Add all eight Vishniac and Santer stock members with their source millimolar concentrations, including the missing `37.4 mmol/L CaCl2` row.
4. Reclassify the medium as defined rather than complex/undefined.
5. Locate the full Crutzen et al. 2008 source cited by TOGO, verify the strain and formulation against the TOGO snippet, and add a narrow reference only if the primary source is found.
6. Regenerate the merge output so the 2026-09-02 water repair appears in `data/merge_yaml/merged/defined_minimal_medium__202c04c5.yaml`.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/defined_minimal_medium.yaml`, `just validate-strict data/normalized_yaml/bacterial/defined_minimal_medium.yaml`, `just validate-terms data/normalized_yaml/bacterial/defined_minimal_medium.yaml`, and `just validate-references data/normalized_yaml/bacterial/defined_minimal_medium.yaml`.
- Regenerate merges, then run the merge freshness check to prove the generated M3197 record reflects the normalized repair.
- Manually compare the repaired YAML against the TOGO M3197 comment: six final-medium millimolar quantities, a 2 mL/L Vishniac and Santer addition, eight trace-stock solutes including CaCl2, no `VARIABLE` concentrations for source-supported quantities, and a single final-medium water row.

## Additional Notes

- The generated record has no preparation or pH fields; the inspected TOGO M3197 payload did not provide those details.
- This report did not edit any YAML record or append a curation event.

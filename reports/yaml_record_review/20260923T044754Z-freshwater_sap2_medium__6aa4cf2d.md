# YAML Record Review: freshwater_sap2_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/freshwater_sap2_medium__6aa4cf2d.yaml
- Started UTC: 2026-09-23T04:46:25Z
- Finished UTC: 2026-09-23T04:47:54Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:002201` / `freshwater_sap2_medium`, a stale two-source merge of MediaDive/JCM J1018 with `LB_noSalt`.
- Compared it with maintained sources `data/normalized_yaml/bacterial/freshwater_sap2_medium.yaml`, `data/normalized_yaml/bacterial/lb_nosalt.yaml`, and the TOGO M1078 Freshwater SAP2 snapshot.
- Cross-checked the MediaDive REST payload for JCM J1018, the live JCM GRMD=1018 endpoint, and the TOGO M1078 API snapshot.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass with 0 error rows.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- `mediadive.medium:J1018` identifies MediaDive's JCM Medium 1018 snapshot for FRESHWATER SAP2 MEDIUM; the live JCM GRMD=1018 page now returns "Nothing found".
- Exact ignored-inclusive lookup for `mediadive.medium:J1018`, `CultureMech:002201`, `freshwater_sap2_medium`, and `lb_nosalt` covered normalized and generated YAML; it found the maintained MediaDive owner, the maintained TOGO M1078/M1079 related SAP2 owners, the maintained `lb_nosalt` owner, index entries, and the stale generated files.
- September curation resolved MediaDive J1018 and TOGO M1078 as source-equivalent snapshots of JCM Medium 1018, but this generated file predates that repair and still has no TOGO references or source-duplicate link.
- The generated `LB_noSalt` synonym and `merged_from: lb_nosalt` are stale artifacts. Maintained `lb_nosalt.yaml` is CultureBotHT LB without salt, a distinct 10 g/L tryptone plus 5 g/L yeast-extract formulation.

## Evidence

- MediaDive J1018 lists Main sol. J1018 as 1 g Tryptone, 1 g Yeast extract, and 1000 ml Distilled water.
- TOGO M1078 lists the same retired JCM 1018 broth as 1 L Distilled water, 1 g Yeast extract (BD-Difco), and 1 g Tryptone (BD-Difco), with a comment to add 15 g/L agar for solid medium.
- The maintained MediaDive owner was repaired on 2026-09-06 to add the missing 1000 ml/L Distilled water row, vendor-qualified BD-Difco ingredient names, FOODON grounding for yeast extract, source references, and a source-duplicate relationship to TOGO M1078.
- The generated file still has only 1 g/L Tryptone and 1 g/L Yeast extract, lacks Distilled water, lacks the BD-Difco source labels and FOODON term, and still claims an old two-source merge with `lb_nosalt`.
- Current maintained `lb_nosalt.yaml` records CultureBotHT `LB_noSalt` as 10 g/L Tryptone plus 5 g/L Yeast Extract, so it no longer matches the 1 g/L Freshwater SAP2 broth.

## Completeness

- The 1 L water row present in both MediaDive J1018 and TOGO M1078 is missing.
- TOGO M1078/M1079 references and reciprocal Freshwater SAP2 source-duplicate or physical-state relationships are missing.
- Curated FOODON/MICRO term grounding from the maintained MediaDive and CultureBotHT owners is absent from the generated merge.
- A distinct CultureBotHT medium is still represented as a synonym/source of JCM 1018.

## Findings

- Major: generated Freshwater SAP2 is stale relative to the September normalized repair and omits the required 1 L Distilled water row.
- Major: the generated record still merges Freshwater SAP2 Medium with the distinct CultureBotHT `LB_noSalt` recipe.
- Major: the generated record has not picked up the maintained JCM/TOGO source-duplicate relationships, so equivalent MediaDive J1018 and TOGO M1078 snapshots remain as separate generated records.
- Minor: BD-Difco source labels and curated yeast-extract grounding are absent from generated YAML.

## Recommended Edits

- Regenerate merge YAML from the maintained September-normalized `freshwater_sap2_medium.yaml`, `TOGO_M1078_Freshwater_SAP2_Medium.yaml`, `TOGO_M1079_Freshwater_SAP2_Medium.yaml`, and `lb_nosalt.yaml`.
- Confirm `freshwater_sap2_medium` and TOGO M1078 merge as source-equivalent JCM 1018 broth snapshots with 1000 ml/L Distilled water, 1 g/L Yeast extract (BD-Difco), and 1 g/L Tryptone (BD-Difco).
- Confirm `LB_noSalt` remains separate with 10 g/L Tryptone and 5 g/L Yeast Extract and is not emitted as a Freshwater SAP2 synonym.
- Preserve the 15 g/L agar note only as solid-medium preparation guidance for the broth or in the explicit TOGO M1079 solid variant.

## Follow-up Checks

- After regeneration, rerun open-schema, strict, reference, and term validation on the generated Freshwater SAP2 YAML.
- Confirm no generated SAP2 record lists `merged_from: lb_nosalt`.
- Confirm the generated MediaDive/TOGO source-equivalent broth has a Distilled water row at 1000 ml/L.
- Confirm `LB_noSalt` retains CultureBotHT source references and the 10 g/L plus 5 g/L CultureBotHT concentrations.

## Additional Notes

- The generated file is derived data and predates the 2026-09-06 SAP2 graph repair. The maintained normalized sources already contain the corrected SAP2 and `LB_noSalt` formulas.

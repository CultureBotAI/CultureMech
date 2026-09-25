# YAML Record Review: LIMNOCHORDIA LN MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/limnochordia_ln_medium.yaml
- Started UTC: 2026-09-23T19:45:19Z
- Finished UTC: 2026-09-23T19:48:07Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:015867 |
| Name | limnochordia_ln_medium |
| Original name | LIMNOCHORDIA LN MEDIUM |
| Category | bacterial |
| Medium/composition type | COMPLEX / UNDEFINED |
| Physical state | LIQUID |
| Structured pH | 6.5 |
| Media grounding | jcm.grmd:1435 |
| Source provenance | JCM Medium 1435 |
| Generated file | data/merge_yaml/merged/limnochordia_ln_medium.yaml |
| Maintained owner | data/normalized_yaml/bacterial/JCM_J1435_LIMNOCHORDIA_LN_MEDIUM.yaml |
| Merge fingerprint | 9ab2d2d0efd76930eed8abe58acf285794a7e37b0fc93342b61b92b161a58a5e |

The reviewed target is a generated one-source JCM GRMD merge. Future fixes belong in `data/normalized_yaml/bacterial/JCM_J1435_LIMNOCHORDIA_LN_MEDIUM.yaml`, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/limnochordia_ln_medium.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/limnochordia_ln_medium.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The live JCM GRMD 1435 source resolves to `LIMNOCHORDIA LN MEDIUM`, and it supports the JCM source accession, label, pH 6.5 endpoint, bacterial category, complex liquid classification, and main recipe captured in this generated record.

JCM 1435 also links `Trace vitamins` to Medium 197. That JCM 197 page provides the external vitamin stock composition, so the generated record's plain top-level `Trace vitamins* (see Medium No. 197 )` row preserves the source text but not the resolvable stock composition.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:015867`, `jcm.grmd:1435`, `GRMD=1435`, the maintained filename, the merge fingerprint, and the shared slug found this generated record, its maintained owner, and normalized source indexes.

## Evidence

Supported in the inspected JCM GRMD 1435 source:

- The basal recipe has 0.78 g K2HPO4, 0.7 g KH2PO4, 0.04 g EDTA 2Na, 0.01 g FeSO4 x 7 H2O, 0.25 g MgSO4 x 7 H2O, 0.1 g CaCl2 x 2 H2O, 0.2 g NaCl, 10 ml trace element solution, 0.5 mg resazurin, and 940 ml distilled water.
- The post-cooling additions are 25 ml 8 percent NaHCO3 solution, 5 ml 10 percent glucose solution, 5 ml 10 percent yeast extract solution, 5 ml 1.0 M sodium thiosulfate solution, and 10 ml trace vitamins from Medium 197.
- The per-liter prior-to-use addition is 5 ml 5 percent L-cysteine-HCl-H2O solution.
- JCM 1435 defines the trace-element stock as a 1 L solution containing nitrilotriacetic acid, FeCl2 x 4 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnCl2, CuCl2 x 2 H2O, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, NaCl, Na2SeO3, Na2WO4 x 2 H2O, and distilled water.
- JCM 1435 supports the N2-CO2 80:20 gas mix, anaerobic aseptic addition of sterile stocks, final pH adjustment to 6.5, and trace-element stock pH and final-volume steps.

Unsupported or incomplete in the generated record:

- The trace-element stock rows are flattened as top-level ingredients at stock concentration even though JCM 1435 uses only 10 ml/L of that stock in the main recipe.
- The maintained owner had 30 imported rows, then `dedupe_identical_ingredients.py` removed one CaCl2 x 2 H2O row because the flattened basal row and flattened stock row both had 0.1 g/L. JCM lists both in different solution contexts.
- The JCM 197 trace-vitamin stock is not modeled, leaving a 10 ml/L reference to another JCM medium without its 10-component vitamin composition.
- CoCl2 x 6 H2O and NiCl2 x 6 H2O are grounded to anhydrous CHEBI terms.
- The page-level JCM autoclave default, 121 C for 15 min, is not represented.
- The generated record has no structured JCM GRMD 1435 or JCM GRMD 197 references.

## Completeness

The generated target is complete for the JCM 1435 medium identity, basal component names and quantities, post-autoclave stock names and volumes, trace-element stock component names, pH values, and gas-condition text.

It is incomplete for nested stock-solution structure, the trace-element CaCl2 x 2 H2O stock row removed by duplicate cleanup, the linked Medium 197 trace-vitamin composition, exact hydrate grounding for CoCl2 x 6 H2O and NiCl2 x 6 H2O, page-level autoclave conditions, and structured source references. Empty optional organism, incubation, storage, and growth-evidence fields are acceptable for this review because the inspected JCM pages do not list a strain, incubation condition, storage condition, or primary growth result.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | `Trace element solution` is represented both as a 10 ml/L main-medium ingredient and as flattened stock-strength ingredients. | JCM 1435 adds 10 ml trace element solution to the medium, then defines that 1 L stock below the main recipe. The YAML lists the stock rows, such as 12.8 g/L nitrilotriacetic acid and 1.0 g/L FeCl2 x 4 H2O, as top-level medium ingredients. | `data/normalized_yaml/bacterial/JCM_J1435_LIMNOCHORDIA_LN_MEDIUM.yaml` |
| Major | One CaCl2 x 2 H2O source row was deleted after flattening conflated two contexts. | JCM 1435 lists 0.1 g CaCl2 x 2 H2O in the basal recipe and another 0.1 g in the trace-element stock; the August dedupe event removed one apparently identical row, so a source stock component is gone. | `data/normalized_yaml/bacterial/JCM_J1435_LIMNOCHORDIA_LN_MEDIUM.yaml` or the duplicate-removal logic |
| Major | The linked Medium 197 trace-vitamin stock is unresolved. | JCM 1435 requests 10 ml `Trace vitamins* (see Medium No. 197 )`; the inspected JCM 197 page defines a 10-component vitamin stock, but the generated record leaves only an ungrounded top-level stock label. | `data/normalized_yaml/bacterial/JCM_J1435_LIMNOCHORDIA_LN_MEDIUM.yaml` |
| Major | Hydrated cobalt and nickel chlorides are over-broadly grounded. | The source names CoCl2 x 6 H2O and NiCl2 x 6 H2O, while the YAML maps them to CHEBI:35696 / cobalt dichloride and CHEBI:34887 / nickel dichloride. | `data/normalized_yaml/bacterial/JCM_J1435_LIMNOCHORDIA_LN_MEDIUM.yaml` |
| Minor | JCM's page-level autoclave temperature and time are missing. | The source states that media are sterilized by autoclaving at 121 C for 15 min unless otherwise stated; the YAML records autoclaving under N2-CO2 but omits the default temperature and duration. | `data/normalized_yaml/bacterial/JCM_J1435_LIMNOCHORDIA_LN_MEDIUM.yaml` or the JCM importer |
| Minor | Structured references are missing. | The generated target carries only a free-text JCM URL in `notes`, and the reference validator performed zero checks. | `data/normalized_yaml/bacterial/JCM_J1435_LIMNOCHORDIA_LN_MEDIUM.yaml` |

## Recommended Edits

1. Move the 13 retained trace-element stock rows under a nested `Trace element solution` at 10 ml/L, restore the deleted stock CaCl2 x 2 H2O row inside that solution, and preserve the 1 L stock water/final-volume context.
2. Resolve `Trace vitamins* (see Medium No. 197 )` as a nested 10 ml/L solution with the JCM 197 vitamin composition.
3. Keep the five other post-autoclave stock additions as 25, 5, 5, 5, and 5 ml/L stock additions rather than converting them to inferred final masses.
4. Replace the CoCl2 x 6 H2O and NiCl2 x 6 H2O CHEBI groundings with hydrate-specific terms if they are available in the ingredient index; otherwise keep the exact JCM preferred terms unresolved.
5. Add the JCM default autoclave condition, 121 C for 15 min, to the preparation detail.
6. Add structured references for JCM GRMD 1435 and the linked JCM GRMD 197 trace-vitamin source.
7. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated record against JCM 1435 for the 10 ml trace-element stock, the restored trace-element CaCl2 x 2 H2O row, the 10 ml JCM 197 trace-vitamin stock, and the post-autoclave addition blocks.
- Re-run an ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:015867`, `jcm.grmd:1435`, `GRMD=1435`, and `JCM_J1435_LIMNOCHORDIA_LN_MEDIUM` after regeneration to confirm the source owner, source indexes, and regenerated merge agree.

## Additional Notes

The preferred terms imported from JCM retain exact middle-dot source text in the YAML. Future edits should normalize display punctuation only through an established importer or label-canonicalization path so hydrate identities are not accidentally changed.

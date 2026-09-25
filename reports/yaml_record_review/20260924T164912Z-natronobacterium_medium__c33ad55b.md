# YAML Record Review: NATRONOBACTERIUM MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/natronobacterium_medium__c33ad55b.yaml
- Started UTC: 2026-09-24T16:49:11Z
- Finished UTC: 2026-09-24T16:49:12Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:001304`, a source-duplicate merge of DSMZ Medium 205 `NATRONOBACTERIUM MEDIUM` with JCM Medium 166.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to DSMZ Medium 205 and is linked to JCM Medium 166 as a source duplicate.

An exact repository search including ignored and hidden files for `mediadive.medium:205`, `mediadive.medium:J166`, `TOGO:M2321`, `CultureMech:001304`, `CultureMech:002525`, `DSMZ_Medium205`, `natronobacterium_medium`, and `jcm_medium_no_166` found this generated DSMZ/JCM merge, the direct normalized DSMZ and JCM owners, an active KOMODO DSMZ 205 projection, and an active TOGO M2321 import of DSMZ Medium 205.

The DSMZ ingredient `Na3-citrate x 2 H2O` is grounded to the broader sodium citrate term, not to a hydrate-specific trisodium citrate dihydrate term.

## Evidence

DSMZ Medium 205 lists 15.0 g Casamino acids, 3.0 g Na3-citrate x 2 H2O, 2.5 g glutamic acid, 2.5 g MgSO4 x 7 H2O, 2.0 g KCl, 250.0 g NaCl, and 20.0 g agar per 1000.0 ml final volume.

JCM Medium 166 lists the same masses for Casamino acids, trisodium citrate, glutamic acid, MgSO4 . 7H2O, KCl, NaCl, and agar, but the JCM citrate row is not explicitly hydrated.

DSMZ instructs adding distilled water to 1000.0 ml, dissolving agar by heating before adding sodium chloride, adjusting to pH 7.0 before autoclaving, and adjusting to pH 8.5 with sterile 5% Na2CO3 after heat sterilization.

JCM instructs adding components to distilled water and bringing the volume to 1.0 L, adjusting pH to 7.0, and readjusting pH to 8.5 with sterile 5% Na2CO3 after autoclaving.

## Completeness

The generated record has the expected major salts and organics, but it does not preserve the distilled-water-to-1 L step as a structured ingredient.

The source-duplicate merge preserves only the DSMZ hydrated citrate spelling, so the JCM anhydrous-or-unspecified `Trisodium citrate` row is not distinguishable after merge.

## Findings

- Major: The DSMZ and JCM records are not exact source duplicates because JCM Medium 166 lists `Trisodium citrate` while DSMZ Medium 205 lists `Na3-citrate x 2 H2O`; the generated merge collapses both to the DSMZ hydrated row.
- Major: The 1000.0 ml or 1.0 L water makeup step from both sources is missing from the structured ingredient list.
- Major: The active KOMODO and TOGO imports of DSMZ Medium 205 remain outside the source-duplicate merge.
- Minor: `Na3-citrate x 2 H2O` is grounded to a sodium citrate term rather than to an exact dihydrate term.

## Recommended Edits

- Revisit the duplicate relationship between `data/normalized_yaml/archaea/natronobacterium_medium.yaml` and `data/normalized_yaml/bacterial/jcm_medium_no_166.yaml`; keep the citrate hydration conflict explicit or split the JCM record as a source variant rather than an exact duplicate.
- Add the distilled-water-to-1 L final volume to the maintained DSMZ and JCM owners.
- Collapse or link `data/normalized_yaml/archaea/KOMODO_205_NATRONOBACTERIUM_medium.yaml` and `data/normalized_yaml/archaea/TOGO_M2321_Natronobacterium_Medium.yaml` with the curated DSMZ Medium 205 owner.
- Re-ground `Na3-citrate x 2 H2O` to a hydrate-specific term where one is available, or document the term as unresolved.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natronobacterium_medium__c33ad55b.yaml` and verify the DSMZ-vs-JCM citrate wording is not silently collapsed.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored and hidden files for `mediadive.medium:205`, `komodo.medium:205`, and `TOGO:M2321` to verify all DSMZ 205 imports are linked or collapsed.

## Additional Notes

None found.

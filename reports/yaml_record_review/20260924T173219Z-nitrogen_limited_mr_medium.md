# YAML Record Review: Nitrogen-limited MR medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/nitrogen_limited_mr_medium.yaml
- Started UTC: 2026-09-24T17:30:54Z
- Finished UTC: 2026-09-24T17:32:19Z
- Verdict: pass with minor issues

## Target
Reviewed `CultureMech:007295`, `nitrogen_limited_mr_medium`, generated from `data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml`.

The record represents MediaDB medium 391, "Nitrogen-limited mr medium".

## Validation
- Open LinkML validation passed with `No issues found`.
- Strict validation passed; the strict TSV had only the header row.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: the available `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding
The record is grounded to the intended MediaDB medium. MediaDB medium 391 is "Nitrogen-limited mr medium" and the MediaDB page lists `Cupriavidus necator H16` as the organism with three growth-data records.

An exact hidden/no-ignore search of `data/normalized_yaml` and `data/merge_yaml` for `MEDIADB:391`, `MediaDB Medium 391`, the original title, the normalized slug, and the importer source phrase found only one normalized owner and this one generated YAML.

## Evidence
The MediaDB tab-delimited export for medium 391 lists the same 13 compounds and concentrations as the generated YAML: D-Fructose 111.0, citrate 4.164, calcium chloride anhydrous 0.09011, dibasic sodium phosphate 33.34, potassium dihydrogen phosphate 49.01, magnesium sulfate 4.587, manganese sulfate 0.01121, ammonium chloride 33.65, ferrous sulfate 0.1798, zinc sulfate 0.03825, cupric sulfate 0.02002, sodium borate 0.0002622, and molybdic acid ammonium salt tetrahydrate 0.0004045. MediaDB reports molar concentrations, matching the YAML's `MILLIMOLAR` units.

The MediaDB medium page lists source 140 as Park JM et al. 2011, title "Genome-scale reconstruction and in silico analysis of the Ralstonia eutropha H16 for polyhydroxyalkanoate synthesis, lithoautotrophic growth, and 2-methyl citric acid production", with PubMed ID 21711532. The generated `media_term` and `notes` preserve MediaDB identity, but the import history incorrectly says the reference is Mazumdar et al. 2014 PLOS One.

The preparation block is generic importer text. MediaDB does not provide a pH value or a filter-sterilization instruction for medium 391, so `Adjust pH if specified in original formulation` and `Sterilize by filtration (0.22 um) to preserve heat-sensitive components` should not be treated as source-backed recipe instructions.

## Completeness
The formula, organism grounding, and MediaDB ID are complete enough to pass. The stale curation-history citation and generic preparation placeholders are minor because they do not alter the 13-component composition.

## Findings
- The importer history cites Mazumdar et al. 2014 PLOS One, but live MediaDB source 140 for medium 391 cites Park JM et al. 2011 and PMID 21711532.
- The pH-adjustment and 0.22 um filter-sterilization preparation steps are generic placeholders rather than instructions present on MediaDB medium 391.

## Recommended Edits
- Correct the MediaDB import provenance for medium 391 to Park JM et al. 2011 / PMID 21711532.
- Remove generic generated preparation steps unless MediaDB provides a medium-specific pH or sterilization instruction.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/nitrogen_limited_mr_medium.yaml` after the provenance/preparation cleanup.
- Re-run open, strict, reference, and term validation on the regenerated artifact.
- Re-check that the regenerated 13-compound molar formula still matches MediaDB medium 391.

## Additional Notes
None.

# YAML Record Review: Nitrogen-free plant nutrient solution for soybean growth
- Repository: CultureMech
- Record: data/merge_yaml/merged/nitrogen_free_plant_nutrient_solution_for_soybean_growth.yaml
- Started UTC: 2026-09-24T17:27:27Z
- Finished UTC: 2026-09-24T17:28:21Z
- Verdict: needs curation

## Target
Reviewed `CultureMech:015438`, `nitrogen_free_plant_nutrient_solution_for_soybean_growth`, generated from `data/normalized_yaml/specialized/Nitrogen_free_plant_nutrient_solution_for_soybean_growth.yaml` and merged with `data/normalized_yaml/specialized/nitrogen_free_b_d_medium_for_lotus_japonicus_growth.yaml`.

The canonical owner represents a soybean sfSynCom nutrient solution supported by `CommunityMech:000064` and `PMID:40052412`.

## Validation
- Open LinkML validation passed with `No issues found`.
- Strict validation passed; the strict TSV had only the header row.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: the available `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding
The soybean source is relevant: PubMed resolves `PMID:40052412` to Li et al. 2025, "A simplified SynCom based on core-helper strain interactions enhances symbiotic nitrogen fixation in soybean", and the imported snippet is from that article abstract.

The merged Lotus source is a distinct record: `PMID:34312531` is Wippel et al. 2021, "Host preference and invasiveness of commensal bacteria in the Lotus and Arabidopsis root microbiota". It is associated with `CommunityMech:000040` and a "Nitrogen-free B&D medium for Lotus japonicus growth" owner, not the soybean sfSynCom medium.

An exact hidden/no-ignore search of `data/normalized_yaml` and `data/merge_yaml` for both slugs plus `CommunityMech:000064` and `PMID:40052412` found exactly these two specialized normalized owners in the merge set and this one generated YAML.

## Evidence
The two normalized owners are not source duplicates. The soybean owner uses 1.0 mM potassium phosphate, 1.0 mM magnesium sulfate, 2.0 mM calcium chloride, 100 uM Iron-EDTA, 25 C, 16 h light / 8 h dark at light intensity 250, and a Leonard jar or pot with vermiculite context. The Lotus owner uses 0.7 mM potassium phosphate, 0.5 mM magnesium sulfate, 1.0 mM calcium chloride, 50 uM Iron-EDTA, 21 C, 16 h light / 8 h dark at light intensity 100, and a growth pouch or square plate context.

The generated merged record keeps the soybean concentrations, temperature, light intensity, and notes, then records the Lotus medium only as a synonym and `merged_from` source. That loses the Lotus concentration values and `PMID:34312531` provenance while making the soybean medium look like the canonical version of both records.

The soybean evidence itself remains weak. The one `PMID:40052412` snippet supports the constructed sfSynCom and its nodulation effect but does not quote the plant nutrient solution formula or growth conditions; its explanation is an auto-filled placeholder rather than a curated rationale.

## Completeness
The generated artifact is not a faithful medium record because it conflates two different plant systems and two different nutrient formulations. Even if both formulas need source-level strengthening, they should remain separate until a curator verifies that they are genuinely equivalent under a named recipe.

## Findings
- The merge collapsed soybean `CommunityMech:000064` / `PMID:40052412` and Lotus `CommunityMech:000040` / `PMID:34312531` into one generated record even though their concentrations and growth conditions differ.
- The generated artifact discards the Lotus concentration set, temperature, vessel context, and PMID provenance.
- The remaining soybean `source_data.evidence` supports the biological sfSynCom result but not the exact four-component nutrient recipe, and its explanation is still an auto-filled placeholder.

## Recommended Edits
- Prevent `data/normalized_yaml/specialized/Nitrogen_free_plant_nutrient_solution_for_soybean_growth.yaml` and `data/normalized_yaml/specialized/nitrogen_free_b_d_medium_for_lotus_japonicus_growth.yaml` from fingerprinting as source duplicates.
- Regenerate separate soybean and Lotus records, preserving their different calcium, magnesium, phosphate, Iron-EDTA, temperature, vessel, and light-intensity values.
- Recurate the soybean record from `PMID:40052412`, replacing the placeholder evidence explanation with a snippet and rationale that explicitly support the nutrient solution formula.
- Recurate the Lotus B&D record from `PMID:34312531` as its own generated medium rather than as a synonym of the soybean medium.

## Follow-up Checks
- Re-run open, strict, reference, and term validation on both regenerated artifacts.
- Re-run an exact hidden/no-ignore search for both CommunityMech IDs, PMIDs, and slugs and confirm they no longer collapse to one active generated YAML.

## Additional Notes
None.

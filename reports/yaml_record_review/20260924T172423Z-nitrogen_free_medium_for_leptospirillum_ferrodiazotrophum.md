# YAML Record Review: Nitrogen-Free Medium for Leptospirillum ferrodiazotrophum
- Repository: CultureMech
- Record: data/merge_yaml/merged/nitrogen_free_medium_for_leptospirillum_ferrodiazotrophum.yaml
- Started UTC: 2026-09-24T17:24:23Z
- Finished UTC: 2026-09-24T17:25:46Z
- Verdict: needs curation

## Target
Reviewed `CultureMech:015436`, `nitrogen_free_medium_for_leptospirillum_ferrodiazotrophum`, generated from `data/normalized_yaml/bacterial/Nitrogen_Free_Medium_for_Leptospirillum_ferrodiazotrophum.yaml`.

The record represents a CommunityMech-imported nitrogen-free medium for `Leptospirillum ferrodiazotrophum`, supported by `PMID:16204553`.

## Validation
- Open LinkML validation passed with `No issues found`.
- Strict validation passed; the strict TSV had only the header row.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: the available `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding
The PMID is relevant. PubMed resolves `PMID:16204553` to Tyson et al. 2005, "Genome-directed isolation of the key nitrogen fixer Leptospirillum ferrodiazotrophum sp. nov. from an acidophilic microbial community", and the PMC full text describes the selective isolation of `Leptospirillum` group III strain UBA1 from Richmond Mine acid mine drainage.

An exact hidden/no-ignore search of `data/normalized_yaml` and `data/merge_yaml` for the CommunityMech ID, PMID, original title, normalized slug, and normalized owner filename found only one normalized owner and one generated YAML for this record.

## Evidence
The source-data snippets in the YAML are literal support for the biological story: a Richmond Mine AMD sample enriched in `Leptospirillum` group III was homogenized, filtered, serially diluted into nitrogen-free liquid medium, and a terminal dilution grew autotrophically while oxidizing ferrous iron as the sole energy source.

The concrete CultureMech ingredient list is not directly supported by the Tyson et al. methods. The full text states that the isolate was grown in nitrogen-free modified 9K medium, made nitrogen-free by removing ammonium sulfate and calcium nitrate, prepared at pH 1.2, serially diluted to 10^-10, then incubated in the dark at 37 C while shaken at 150 rpm for 21 days. The generated YAML instead has only 30 g/L Iron(II) sulfate, 0.4 g/L magnesium sulfate, and 0.05 g/L monopotassium phosphate, with pH 1.7 and temperature 33 C.

The medium is also missing the 9K basis as provenance. Tyson et al. cite Silverman and Lundgren 1959 for 9K medium, but the YAML cites only the Tyson paper and does not explain why its salt concentrations differ from a nitrogen-free 9K recipe or why other 9K salts were omitted.

The aerobic flag is reasonable for an iron-oxidizing chemolithoautotroph whose growth was coupled to ferric iron production. The acid mine drainage source-environment note is relevant to the isolation context.

## Completeness
The record is structurally valid but chemically underspecified. It captures the concept of a nitrogen-free, ferrous-iron medium for `L. ferrodiazotrophum`, but it does not provide a source-backed reconstruction of the modified 9K recipe used in the paper and it disagrees with the source text on pH and incubation temperature.

## Findings
- The three-ingredient formula is not sufficient evidence-backed nitrogen-free modified 9K; the record omits the modified-9K salt context described by Tyson et al.
- `ph_value: 1.7` conflicts with the Tyson methods, which prepared the nitrogen-free 9K medium at pH 1.2.
- `temperature_value: 33.0` conflicts with the Tyson methods, which incubated all serial dilutions at 37 C.
- The recipe is missing source-backed preparation/incubation details: nitrogen-source omission, pH 1.2 preparation, 10^-10 serial dilution endpoint, dark incubation, 150 rpm shaking, and 21 day incubation.

## Recommended Edits
- Recurate `data/normalized_yaml/bacterial/Nitrogen_Free_Medium_for_Leptospirillum_ferrodiazotrophum.yaml` from Tyson et al. 2005 and the cited 9K source instead of leaving the unexplained three-salt CommunityMech formula as canonical.
- Replace `ph_value: 1.7` with the source-backed pH 1.2 if this record is meant to represent the isolation medium.
- Replace `temperature_value: 33.0` with 37 C for the serial-dilution isolation condition, or remove the temperature if a verified recipe-specific temperature cannot be curated.
- Add preparation notes for removing ammonium sulfate and calcium nitrate from 9K, using ferrous sulfate as the primary energy source, and incubating the liquid serial dilutions in the dark with shaking.
- Add a structured citation to `PMID:16204553`, not only `source_data.evidence` snippets, and add the Silverman and Lundgren 1959 9K citation when the base formula is reconstructed.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/nitrogen_free_medium_for_leptospirillum_ferrodiazotrophum.yaml` from the corrected normalized owner.
- Re-run open, strict, reference, and term validation on the regenerated artifact.
- Re-check the regenerated formula against the Tyson methods and the cited 9K source before accepting the generated record.

## Additional Notes
None.

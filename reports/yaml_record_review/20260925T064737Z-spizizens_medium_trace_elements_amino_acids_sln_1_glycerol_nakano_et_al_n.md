# YAML Record Review: spizizens_medium_trace_elements_amino_acids_sln_1_glycerol_nakano_et_al_n

- Repository: CultureMech
- Record: data/merge_yaml/merged/spizizens_medium_trace_elements_amino_acids_sln_1_glycerol_nakano_et_al_n.yaml
- Started UTC: 2026-09-25T06:45:42Z
- Finished UTC: 2026-09-25T06:47:37Z
- Verdict: pass with minor issues

## Target

Reviewed the generated record for MediaDB Medium 215, a Nakano et al. Spizizen medium variant with trace elements, amino acids, and 1 percent glycerol, assigned `CultureMech:007109`.

## Validation

- LinkML validation: Passed; no issues found.
- Strict validation: Passed; the TSV contained only the header, with 0 error rows.
- LinkML reference validation: Passed; 0 reference checks were run and all passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record is a single-source MediaDB import for `MEDIADB:215`. MediaDB Medium 215 is named `Spizizen's medium + trace elements + amino acids sln + 1% glycerol; nakano et al`, is associated with source 77, and that source page cites Nakano et al., 1997, Journal of Bacteriology, PMID 9352926.

The generated medium identity still contains an old MediaDB SQL-parser artifact: both `original_name` and `media_term.term.label` end with `Nakano et al','N`. The normalized source file has already repaired those strings to `Nakano et al`, so the generated record is stale relative to the current normalized YAML.

## Evidence

MediaDB's tab-delimited export for medium 215 lists 34 compounds and millimolar amounts. The generated record carries the same 34 source names and amounts, including `Glycerol` 108.589, the 16 amino-acid-solution rows from `L-Glutamate` 0.339836 through `Threonine` 0.419745, and the shared Spizizen trace-element/mineral rows from `Calcium chloride anhydrous` through `Zinc Chloride`.

The MediaDB medium page lists B. subtilis JH642 as the one organism associated with this formulation, and growth-data record 416 confirms B. subtilis JH642 with source 77 and growth rate 0.260411 1/h.

## Completeness

The generated record preserves the MediaDB formula, concentration units, medium type, and defined composition. It has generic MediaDB-derived preparation steps rather than Nakano-specific protocol text, but MediaDB does not expose a preparation procedure on the medium 215 page or its tab-delimited export.

## Findings

- Medium: The generated merge predates the August 31 MediaDB name repair. The target still has the medium-name artifact `Nakano et al','N` and a truncated ingredient `preferred_term: '''Iron(III'`, while `data/normalized_yaml/bacterial/spizizens_medium_trace_elements_amino_acids_sln_1_glycerol_nakano_et_al_n.yaml` already has `Nakano et al` and `Iron(III) chloride`.
- Low: The generated record predates later normalized groundings for `Aspartate`, `Lysine`, and `Threonine`; those rows now carry CHEBI terms in the normalized YAML but remain ungrounded in the generated target.
- Low: The generated `Iron(III) chloride` row has no CHEBI term because it is still the stale truncated ingredient row. MediaDB's export supplies PubChem 24380 and CHEBI 30808 for that compound.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/spizizens_medium_trace_elements_amino_acids_sln_1_glycerol_nakano_et_al_n.yaml` from the repaired normalized YAML so the fixed MediaDB names and later MIM groundings are reflected in generated output.
- After regeneration, confirm that `Iron(III) chloride` is grounded or queued for grounding against the MediaDB CHEBI 30808 identifier.

## Follow-up Checks

- Consider grounding `Glutamine` and `DL-Serine`; MediaDB's export supplies CHEBI 28300 and CHEBI 17822 for those rows, but they remain ungrounded in the normalized YAML.

## Additional Notes

None found

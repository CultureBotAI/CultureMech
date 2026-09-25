# YAML Record Review: NORRIS FERROPLASMA MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/norris_ferroplasma_medium__4b6cf948.yaml
- Started UTC: 2026-09-24T17:49:27Z
- Finished UTC: 2026-09-24T17:49:27Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002877`
- Name: `norris_ferroplasma_medium`
- Original name: `NORRIS FERROPLASMA MEDIUM`
- Media term: `mediadive.medium:J526`, JCM Medium J526
- Category: `archaea`
- Source owner: `data/normalized_yaml/archaea/norris_ferroplasma_medium.yaml`
- Merge state: singleton, `merged_from: norris_ferroplasma_medium`

## Validation

- Open LinkML schema validation: passed; exited 0 with no diagnostics.
- Strict validation: passed; `/private/tmp/norris_ferroplasma_medium__4b6cf948.strict.tsv` contained only the TSV header.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

- The direct JCM identity is correct. Live JCM GRMD 526 and the MediaDive J526 mirror both identify the source as `NORRIS FERROPLASMA MEDIUM`.
- The exact hidden, no-ignore search for `mediadive.medium:J526`, `JCM Medium J526`, `GRMD=526`, `norris_ferroplasma_medium`, and `NORRIS FERROPLASMA MEDIUM` found this direct JCM source, this generated record, a TOGO M527 mirror in `data/normalized_yaml/archaea/TOGO_M527_Norris_Ferroplasma_Medium.yaml`, and a separate TOGO-generated `data/merge_yaml/merged/NORRIS_FERROPLASMA_MEDIUM.yaml`. Ignored files were included.
- The same search also found `kg_microbe_match: mediadive.medium:J526` annotations on unrelated Schaechter salt media; those are not duplicate JCM 526 source records.

## Evidence

- JCM 526 lists 0.5 g MgSO4 x 7 H2O, 0.4 g ammonium sulfate, 0.1 g KCl, 0.2 g KH2PO4, 10.0 g FeSO4 x 7 H2O, 0.1 g Yeast extract (BD-Difco), and 1.0 L distilled water.
- JCM 526 instructs preparation by mixing all ingredients except FeSO4 x 7 H2O, adjusting pH to 1.2 with H2SO4, autoclaving, and then adding filter-sterilized FeSO4 x 7 H2O.
- The generated direct JCM target has the six substantive final ingredients at matching gram-per-liter values, `ph_value: 1.2`, and the same autoclave/filter-addition instruction.
- TOGO M527 mirrors the same JCM GRMD 526 source, including the same formula and pH comment, but it is emitted as a separate generated record.

## Completeness

- The direct JCM generated target is compositionally complete for JCM 526.
- The corpus is incomplete at the identity layer because the TOGO M527 mirror has not been merged with this MediaDive/JCM J526 record.

## Findings

- Major: source identity is split. `mediadive.medium:J526` and TOGO M527 both mirror JCM GRMD 526, but the active merged YAML still contains two separate Norris Ferroplasma records.
- Minor: the TOGO M527 mirror in `NORRIS_FERROPLASMA_MEDIUM.yaml` lacks `ph_value: 1.2` and turns the pH-adjustment reagent H2SO4 into a variable top-level ingredient rather than a preparation detail.

## Recommended Edits

- Pair direct JCM J526 and TOGO M527 as source duplicates.
- Make the direct JCM/MediaDive record the canonical composition or otherwise preserve its pH 1.2 and FeSO4-after-autoclave preparation semantics when merging.
- Rebuild the generated records so only one Norris Ferroplasma target remains.

## Follow-up Checks

- Confirm the regenerated Norris Ferroplasma record lists both direct JCM J526 and TOGO M527 provenance.
- Confirm the regenerated record preserves pH 1.2 and does not list H2SO4 as a final ingredient.
- Run open schema, strict, reference, and term validation on the regenerated target.

## Additional Notes

- None found.

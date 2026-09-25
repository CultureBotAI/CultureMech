# YAML Record Review: Thermococcus Medium (pH 6.0)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermococcus_medium_ph_6_0__a8e449c1.yaml`
- Started UTC: 2026-09-25T09:59:10Z
- Finished UTC: 2026-09-25T10:01:05Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009724`
- Merge fingerprint: `a8e449c13e5077f302afadf992e9a630e9c8e75f0beec6144652e97c67690b61`
- Merged sources: `KOMODO_184_DESULFUROCOCCUS_medium`, `KOMODO_723_PICROPHILUS_medium`, `TOGO_M165_Sulfolobus_Medium_B`, `TOGO_M345_Thermococcus_Medium_pH_6.0`, `salt_base_solution_medium_1189`, `salt_solution_medium_592`, `trace_element_solution_medium_882`, `wolfes_mineral_elixir_medium_792`
- Media term: `TOGO:M345`
- Source medium: TOGO M345 / JCM 350, "Thermococcus Medium (pH 6.0)"

## Validation

- LinkML schema validation: Passed with `No issues found`.
- Strict schema validation: Passed; 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed. The only stderr output was the expected `eutils` warning about `pkg_resources`.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not the embedded `MediaRecipe.curation_history` array in this merged YAML.

## Identity and Grounding

- The generated record is stale relative to `data/normalized_yaml/archaea/TOGO_M345_Thermococcus_Medium_pH_6.0.yaml`: the normalized source has already been repaired as a TOGO M273 pH variant with 1 L of parent medium, pH 6.0, and 1.0 N H2SO4 retained verbatim.
- The generated merge grouped the TOGO M345 H2SO4 adjustment with unrelated recipes for Desulfurococcus medium, Picrophilus medium, Sulfolobus Medium (B), and several bacterial KOMODO submedia that only share sparse acid/salt-solution signatures.
- TOGO M345 and JCM 350 define a pH variant of Thermococcus Medium, not a generic H2SO4 solution family.
- The generated `solutions` row stores the 1 L Thermococcus Medium parent as `1` `G_PER_L`; the repaired normalized source correctly stores the row as `1` `L` and links it to `CultureMech:009290`.

## Evidence

- TOGO API `M345` reports JCM M350, pH 6.0, 1 L of Thermococcus medium M273, and a 1.0 N H2SO4 final pH adjustment.
- The JCM 350 HTML page reports the same 1 L parent-medium row and the same pH 6.0 readjustment after reduction.
- The repaired normalized TOGO M345 file has a `repair_archaea_ph_wrappers_score20.py` curation event on 2026-09-10 and now records `parent_media`, `variant_relationship: PH_VARIANT`, an L-unit solution, and an `ADJUST_PH` preparation step.
- Exact ignored-file search found all eight stale `merged_from` sources; the KOMODO Desulfurococcus/Picrophilus recipes and bacterial submedia are separate named media or stock solutions, not aliases of TOGO M345.

## Completeness

- Required scalar fields, the TOGO media term, curation history, stale synonyms, and `merged_from` are present.
- The generated output lacks the repaired normalized source's `parent_media`, `variant_relationship`, `variant_modifications`, `ph_value`, curated `notes`, L-unit solution, and preparation step.
- No organisms or strain links are expected for this medium-level import.

## Findings

- High - The generated merge is stale and omits the already-curated TOGO M345 pH-wrapper repair present in normalized YAML.
- High - Sparse acid-wrapper fingerprinting over-merged TOGO M345 with seven unrelated KOMODO/TOGO stock or acid-adjusted medium records.
- High - The 1 L Thermococcus Medium parent is represented as an empty 1 g/L `Unknown solution`.
- Medium - Stale synonyms and `categories` now imply the Thermococcus pH variant is also Desulfurococcus, Picrophilus, and bacterial stock media.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/thermococcus_medium_ph_6_0__a8e449c1.yaml` from current normalized YAML so the 2026-09-10 TOGO M345 repair propagates.
- Exclude parent-medium pH wrappers and single acid adjustments from exact source-duplicate fingerprinting that ignores the `parent_media` target.
- Split the unrelated KOMODO and TOGO records back into their own merge groups before regenerating `merged_from`, `synonyms`, and `categories`.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated TOGO M345 branch.
- Re-run exact ignored-file search for `TOGO_M345_Thermococcus_Medium_pH_6.0`, `KOMODO_184_DESULFUROCOCCUS_medium`, `KOMODO_723_PICROPHILUS_medium`, `TOGO_M165_Sulfolobus_Medium_B`, `salt_base_solution_medium_1189`, `salt_solution_medium_592`, `trace_element_solution_medium_882`, and `wolfes_mineral_elixir_medium_792` to confirm the over-merge is gone.
- Compare the regenerated TOGO M345 parent and H2SO4 fields against TOGO API `M345` and JCM 350.

## Additional Notes

None found.

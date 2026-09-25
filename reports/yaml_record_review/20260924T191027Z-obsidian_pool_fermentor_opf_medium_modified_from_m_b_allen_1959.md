# YAML Record Review: obsidian_pool_fermentor_opf_medium_modified_from_m_b_allen_1959

- Repository: CultureMech
- Record: data/merge_yaml/merged/obsidian_pool_fermentor_opf_medium_modified_from_m_b_allen_1959.yaml
- Started UTC: 2026-09-24T19:10:27Z
- Finished UTC: 2026-09-24T19:11:43Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/obsidian_pool_fermentor_opf_medium_modified_from_m_b_allen_1959.yaml`, a generated bacterial `MediaRecipe` with id `CultureMech:009237` and source term `TOGO:M2682`.

The generated record has one source owner, `data/normalized_yaml/bacterial/obsidian_pool_fermentor_opf_medium_modified_from_m_b_allen_1959.yaml`.

## Validation

- LinkML open-schema validation: passed; no issues found.
- Strict validation: passed; `/private/tmp/obsidian_pool_fermentor_opf_medium_modified_from_m_b_allen_1959.strict.tsv` contained only the header row.
- Reference validation: passed; the validator reported 0 configured checks for this record.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The source identity is correct: this is TOGO Medium M2682, Obsidian Pool fermentor medium modified from M. B. Allen, 1959.

This generated record is stale relative to its single normalized owner. The normalized record already has a 2026-09-12 `RESOLVED_TOGO_M2682_OBSIDIAN_POOL_SCORE15` curation action that corrected the same source's microliter stock additions, repaired hydrated-salt groundings, nested the Li/W/Se/Ni stock, and added the 85 C N2/CO2 incubation conditions.

## Evidence

Checked the generated record, the repaired normalized owner, an ignored-inclusive exact repository search for `TOGO:M2682` and the OPF slug, the purpose-built `repair_togo_m2682_obsidian_pool_score15.py` script and test references surfaced by that search, and the fetched TOGO M2682 REST payload.

TOGO M2682 distinguishes final-liter rows from small stock additions. The source adds 30 uL of 1 mg/ml Na2MoO4 stock, 180 uL of 10 mg/ml MnCl2 stock, 22 uL of 10 mg/ml ZnSO4 stock, 5 uL of 10 mg/ml CuCl2 stock, 10 uL of 1 mg/ml CoSO4 stock, 180 uL of 25 mg/ml Na2B4O7 stock, 30 uL of 1 mg/ml VOSO4 stock, 1 ml Wolfe's Vitamin Solution, and 10 uL of a Li/W/Se/Ni stock containing 1 mg/ml of each solute.

## Completeness

The generated YAML is materially incomplete and overstates several trace metal concentrations by orders of magnitude:

- The seven first stock additions are emitted as 30 to 180 G_PER_L final ingredients instead of 0.01 to 4.5 MG_PER_L final additions.
- The Li/W/Se/Ni stock is both represented as a bogus 10 G_PER_L top-level ingredient and flattened to top-level 1 G_PER_L component rows.
- Final distilled water is `1000 G_PER_L`, and the 1 ml water inside the Li/W/Se/Ni stock appears as a second top-level `1 G_PER_L` distilled-water ingredient.
- Wolfe's Vitamin Solution is present as an empty solution at `1 G_PER_L`; the repaired owner keeps it as a 1 ML_PER_L undefined 1000X supplement.
- The generated record omits `temperature_value: 85.0`, `incubation_atmosphere: ANAEROBIC`, and the N2/CO2 80:20 bubbling annotation.
- Several repaired terms and CHEBI mirrors are absent from the generated copy, including the sodium thiosulfate and sodium sulfide repairs, the MgSO4 x 7 H2O mirror repair, and the inline Na2SeO3 stock grounding.

## Findings

- BLOCKER: The generated record predates the September M2682 repair and encodes microliter stock-addition volumes as gram-per-liter concentrations.
- BLOCKER: The Li/W/Se/Ni stock is flattened into final-medium rows instead of being nested under a stock solution added at 0.01 ML_PER_L.
- MAJOR: Final 1000 ml water and the 1 ml stock water are both emitted as G_PER_L water ingredients.
- MAJOR: Wolfe's Vitamin Solution has the wrong unit and still carries the `_x0008_` source artifact in its label.
- MAJOR: Anaerobic 85 C N2/CO2 incubation metadata from the source has not propagated into generated YAML.

## Recommended Edits

- Regenerate this merged record from the current normalized owner so the `RESOLVED_TOGO_M2682_OBSIDIAN_POOL_SCORE15` edits are reflected in `data/merge_yaml/merged`.
- Confirm the regenerated record has 1000 ML_PER_L final distilled water, no second top-level distilled-water ingredient, and no `G_PER_L` units on microliter stock additions.
- Confirm the regenerated record carries `temperature_value: 85.0`, `incubation_atmosphere: ANAEROBIC`, and `aeration: N2/CO2 (80:20) bubbled at 20 ml/min`.
- Confirm `Wolfe's Vitamin Solution (1000X)` is a 1 ML_PER_L solution and `LiCl/Na2WO4/NaSeO3/Ni(NH4)2(SO4) stock` is a 0.01 ML_PER_L solution with four nested 1 G_PER_L stock components.

## Follow-up Checks

- Run an ignored-inclusive exact search for `TOGO:M2682` and `obsidian_pool_fermentor_opf_medium_modified_from_m_b_allen_1959` to confirm the generated record has no duplicate sibling after regeneration.
- Re-run open-schema, strict, reference, and term validation after generated YAML is rebuilt.

## Additional Notes

None found.

# YAML Record Review: thiomonas_cuprina_medium__4eb1060c

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thiomonas_cuprina_medium__4eb1060c.yaml`
- Started UTC: 2026-09-25T13:08:30Z
- Finished UTC: 2026-09-25T13:08:30Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009548`
- Name: `thiomonas_cuprina_medium`
- Source grounding: TOGO Medium M3036, original source NBRC_M929-3

## Validation

- Schema validation: passed with no issues.
- Strict validation: passed with zero errors; `/private/tmp/thiomonas_cuprina_medium__4eb1060c.strict.tsv` was header-only.
- Reference validation: passed with zero checks.
- Term validation: passed after the known EUtils warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The `media_term` points to `TOGO:M3036`, the yeast-extract NBRC 929 variant.
- NBRC 929 is a single base medium with three post-autoclave alternatives: sterile sulfur powder 0.05%, sulfidic ore 2%, or yeast extract 0.05%. M3036 corresponds to the yeast extract choice.
- The scoped source search found the related NBRC 929 sibling variants, including TOGO M3034 and M3035, but did not find a second M3036 record. The search included ignored and hidden files.

## Evidence

- NBRC 929 lists the main salts as KCl 0.33 g, MgCl2 x 6 H2O 2.75 g, MgSO4 x 7 H2O 3.45 g, NH4Cl 1.25 g, CaCl2 x 2 H2O 0.14 g, K2HPO4 0.18 g, KH2PO4 0.14 g, NaCl 0.5 g, 1 ml trace element solution, and 1 L distilled water.
- The main recipe is adjusted to pH 3.5 with sulfuric acid before autoclaving.
- The NBRC trace element solution is a separate 1 L stock containing MgSO4 x 7 H2O 30 g, MnSO4 x H2O 5 g, NaCl 10 g, FeSO4 x 7 H2O 1 g, CoCl2 x 6 H2O 1.8 g, CaCl2 x 2 H2O 1 g, ZnSO4 x 7 H2O 1.8 g, CuSO4 x 5 H2O 0.1 g, KAl(SO4)2 x 12 H2O 0.18 g, H3BO3 0.1 g, Na2MoO4 x 2 H2O 0.1 g, (NH4)2Ni(SO4)2 x 6 H2O 2.8 g, Na2WO4 x 2 H2O 0.1 g, Na2SeO4 0.1 g, and 1 L water.
- M3036 adds yeast extract as the NBRC 929 0.05% post-autoclave variant.

## Completeness

- The record has the main salts, trace stock components, sulfuric acid pH adjustment, and yeast extract alternative.
- The generated record has no `target_organisms`; there are no growth claims to verify.

## Findings

- The 1 ml/L NBRC trace element stock has been flattened into final ingredient rows at stock concentration, and overlapping salts were then summed with the main salts.
- `MgSO4 x 7 H2O`, `NaCl`, and `CaCl2 x 2 H2O` are inflated to `33.45`, `10.5`, and `1.1400000000000001` g/L because the generator added whole-stock g/L values to main-recipe values.
- Stock water was added to main water as `2.0` `G_PER_L`, which loses the solvent unit and double-counts water.
- The `solutions` entry stores `Trace element solution*` as `1` `G_PER_L` with `name: Unknown solution`; the source uses 1 ml stock per liter of parent medium.
- Yeast extract is recorded as `VARIABLE`, even though the NBRC variant specifies 0.05% w/v.

## Recommended Edits

- Model the NBRC trace element solution as a 1 L stock dosed at 1 ml/L, or convert its components to final 0.001x concentrations without merging them into the source stock rows.
- Convert the M3036 yeast extract alternative to 0.05% w/v, or retain the percent expression in a way that does not imply an unknown amount.
- Preserve NBRC 929 as one base recipe with M3034, M3035, and M3036 as sulfur, sulfidic-ore, and yeast-extract variants instead of unrelated duplicates.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after stock reconstruction.
- Cross-check M3034, M3035, and M3036 so the same NBRC 929 trace stock is fixed consistently.

## Additional Notes

- Empty optional fields were not treated as defects.

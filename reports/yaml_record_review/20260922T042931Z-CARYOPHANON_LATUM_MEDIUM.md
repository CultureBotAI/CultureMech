# YAML Record Review: CARYOPHANON LATUM medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/CARYOPHANON_LATUM_MEDIUM.yaml`
- Started UTC: 2026-09-22T04:26:20Z
- Finished UTC: 2026-09-22T04:29:31Z
- Verdict: needs curation

## Target

`CARYOPHANON_LATUM_MEDIUM.yaml` is the generated `MediaRecipe` for KOMODO Medium 34, `CultureMech:005063`, merged with DSMZ/MediaDive Medium 34 and the KOMODO 34_513 DSM 513 wrapper.

The record was merged from three normalized owners on fingerprint `d9ea864bcf5fc7e6872a66ab9605803a08f1461a5012e5bec6bd951e1a8c5fae`:

- `data/normalized_yaml/bacterial/KOMODO_34_CARYOPHANON_LATUM_medium.yaml`
- `data/normalized_yaml/bacterial/caryophanon_latum_medium.yaml`
- `data/normalized_yaml/bacterial/medium_34_modified_for_dsm_513.yaml`

## Validation

- LinkML validation against `MediaRecipe`: pass.
- `scripts/validate_strict.py`: pass with 0 strict errors.
- `linkml-reference-validator`: pass; 1 file checked, 0 reference checks.
- `linkml-term-validator`: pass.
- Embedded `curation_history`: not checked; the available `just validate-history` target validates standalone files under `history/`, not embedded history events inside merged YAML.

## Identity and Grounding

The duplicate topology is sound. KOMODO Medium 34 explicitly points to DSMZ Medium 34, DSMZ and MediaDive list `CARYOPHANON LATUM MEDIUM`, and the KOMODO 34_513 wrapper carries the same DSMZ 34 formula.

The ingredient list has two term-level defects:

- `Trypticase` is a peptone mixture and already has a legacy `MediaIngredientMech:000263` mixture mapping, but it also has an invalid primary CHEBI term of `CHEBI:78018` / dodecylphosphocholine.
- `Tris-HCl buffer` is the source buffer basis and is grounded only to `CHEBI:9754` / tris; it should be represented as a 10 mM Tris/HCl buffer at pH 7.8 rather than as pure tris.

## Evidence

DSMZ Medium 34 and MediaDive medium 34 agree on the formula:

- 2 g/L yeast extract
- 2 g/L Trypticase (BBL)
- 2 g/L soy peptone
- 1 g/L Na-acetate
- 0.1 g/L Na-glutamate
- 0.2 mg/L thiamine-HCl x 2 H2O
- 0.05 mg/L biotin
- 1 g/L K2HPO4
- 0.27 g/L MgSO4 x 7 H2O
- 1000 ml 10 mM Tris/HCl buffer at pH 7.8

The generated record converts the final buffer row to `Tris-HCl buffer`, `value: 1000`, `unit: G_PER_L`. KOMODO's source table instead reports the buffer as a finite Tris row of 1.58 g/L and 0.01 mol/L, matching the 10 mM source concentration.

The DSMZ/MediaDive Trypticase row carries a BBL vendor qualifier. The generated record drops that qualifier and maps Trypticase to dodecylphosphocholine, which is chemically unrelated.

## Completeness

The pH 7.8 value and `Adjust pH to 7.8` preparation instruction are preserved. The KOMODO-derived canonical record does not keep that preparation step directly, but the merged DSMZ owner does and the generated record inherits it before the merge metadata.

The generated record has no target organism or strain growth evidence.

## Findings

- Needs curation: `1000 ml` of 10 mM Tris/HCl buffer was modeled as `1000 G_PER_L`.
- Needs curation: `Trypticase` is incorrectly grounded to `CHEBI:78018` / dodecylphosphocholine and still retains a legacy `mediaingredientmech_term` rather than a modern CHEBI mirror or no primary chemical term.
- Minor: the BBL qualifier on the source Trypticase row was dropped.
- Minor: no source-backed target organism or growth evidence has been curated.

## Recommended Edits

- Represent the Tris/HCl buffer as a structured buffer basis, a 10 mM concentration, or a correctly calculated Tris/HCl mass rather than 1000 g/L.
- Remove the erroneous dodecylphosphocholine grounding from `Trypticase`; keep it ungrounded as a mixture or map it through the supported peptone MediaIngredientMech term pattern.
- Preserve the BBL source qualifier for Trypticase.
- Add organism-level growth evidence if a DSMZ or KOMODO strain record documents growth on Medium 34.

## Follow-up Checks

- Regenerate `CARYOPHANON_LATUM_MEDIUM.yaml` and confirm that the DSMZ/KOMODO/34_513 source-duplicate merge remains a three-record merge after repairing the buffer row.
- Compare the regenerated buffer row against the DSMZ 34 PDF, MediaDive 34 JSON, and KOMODO 34 final per-liter table.
- Re-run LinkML, strict, reference, and term validation after the term repairs.

## Additional Notes

Generated `data/merge_yaml/merged` files are derived. Apply durable fixes to the normalized DSMZ Medium 34 owner, the two KOMODO Medium 34 owners, or the MediaDive `ml` buffer import path before regenerating this output.

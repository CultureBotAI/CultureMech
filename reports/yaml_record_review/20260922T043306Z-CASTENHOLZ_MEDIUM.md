# YAML Record Review: CASTENHOLZ MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml`
- Started UTC: 2026-09-22T04:29:45Z
- Finished UTC: 2026-09-22T04:33:06Z
- Verdict: pass with minor issues

## Target

`CASTENHOLZ_MEDIUM.yaml` is the generated `MediaRecipe` for KOMODO Medium 86, `CultureMech:006701`, merged with DSMZ/MediaDive Medium 86 and two KOMODO DSM strain wrappers.

The generated record was merged from four normalized owners on fingerprint `cbf5a2c0d53742b61681e8db2484468b7537a33c1dcc2cf235962423507ed805`:

- `data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml`
- `data/normalized_yaml/bacterial/castenholz_medium.yaml`
- `data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml`
- `data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml`

## Validation

- LinkML validation against `MediaRecipe`: pass.
- `scripts/validate_strict.py`: pass with 0 strict errors.
- `linkml-reference-validator`: pass; 1 file checked, 0 reference checks.
- `linkml-term-validator`: pass.
- Embedded `curation_history`: not checked; the available `just validate-history` target validates standalone files under `history/`, not embedded history events inside merged YAML.

## Identity and Grounding

The source-duplicate topology is supported. KOMODO 86 cites DSMZ Medium 86, the two KOMODO DSM wrappers carry the same ingredient signature, and the DSMZ, MediaDive, and KOMODO formulas agree on all ingredient amounts.

Most defined salts have valid CHEBI primary terms and matching `mediaingredientmech_chebi_term` mirrors. `KNO3` and `NaNO3` have valid primary CHEBI terms for potassium nitrate and sodium nitrate, but their mirrors are still in the legacy `mediaingredientmech_term` form.

`Tryptone` and `Yeast extract` are reasonably ungrounded as mixtures. The bacterial, liquid, complex, and pH 8.2 metadata are source-consistent.

## Evidence

DSMZ Medium 86 lists the following in 1000 ml water:

- 100 mg nitrilotriacetic acid
- 60 mg CaSO4 x 2 H2O
- 100 mg MgSO4 x 7 H2O
- 8 mg NaCl
- 103 mg KNO3
- 689 mg NaNO3
- 140 mg Na2HPO4 x 2 H2O
- 0.47 mg FeCl3 x 6 H2O
- 2.20 mg MnSO4 x H2O
- 0.50 mg ZnSO4 x 7 H2O
- 0.50 mg H3BO3
- 25 micrograms CuSO4 x 5 H2O
- 25 micrograms Na2MoO4 x 2 H2O
- 46 micrograms CoCl2 x 6 H2O
- 1 g Tryptone
- 1 g yeast extract

The generated grams-per-liter rows match MediaDive's normalized values for those DSMZ masses: for example, NaCl is 0.008 g/L, FeCl3 x 6 H2O is 0.00047 g/L, and both 25 microgram rows are `2.5e-05 G_PER_L`.

## Completeness

DSMZ and MediaDive include one preparation instruction, `Adjust pH to 8.2 with NaOH.` The canonical generated record does not retain a `preparation_steps` block after the KOMODO/DSMZ merge, even though `ph_value: 8.2` is present.

No target organism or DSM strain growth evidence is present; the DSM 11376 and DSM 11377 KOMODO wrappers are captured only as source-duplicate synonyms, not as growth observations.

## Findings

- Minor: the merge dropped the DSMZ/MediaDive pH-adjustment preparation step.
- Minor: `KNO3` and `NaNO3` retain legacy `mediaingredientmech_term` mirrors despite having correct primary CHEBI terms.
- Minor: the DSM 11376 and DSM 11377 wrappers are represented as source duplicates, but no structured strain-growth evidence was curated from those wrappers.

## Recommended Edits

- Preserve the `Adjust pH to 8.2 with NaOH` preparation step from the DSMZ/MediaDive Medium 86 owner when generating the canonical KOMODO/DSMZ merge.
- Replace the KNO3 and NaNO3 legacy mirrors with `mediaingredientmech_chebi_term` entries matching `CHEBI:63043` and `CHEBI:63005`.
- Add strain-specific growth evidence for the DSM 11376 and DSM 11377 wrappers if those KOMODO IDs should assert cultivation support.

## Follow-up Checks

- Regenerate `CASTENHOLZ_MEDIUM.yaml` after mirror cleanup and confirm the four-record source-duplicate merge is unchanged.
- Re-run LinkML, strict, reference, and term validation after preserving the preparation step.

## Additional Notes

Generated `data/merge_yaml/merged` files are derived. Apply durable fixes to the DSMZ/KOMODO Medium 86 normalized owners or to merge metadata preservation before regenerating this output.

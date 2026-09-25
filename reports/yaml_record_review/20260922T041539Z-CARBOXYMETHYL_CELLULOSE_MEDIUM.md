# YAML Record Review: CARBOXYMETHYL CELLULOSE medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml`
- Started UTC: 2026-09-22T04:12:10Z
- Finished UTC: 2026-09-22T04:15:39Z
- Verdict: pass with minor issues

## Target

`CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml` is the generated `MediaRecipe` for KOMODO Medium 1111, `CultureMech:003813`, `carboxymethyl_cellulose_medium`.

The generated record merges two source owners on fingerprint `fdbb30c0f0eeb297b004dbb48e87b4ed760f1bfe904761bb0a166578b49e55db`:

- `data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml`
- `data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml`

## Validation

- LinkML validation against `MediaRecipe`: pass.
- `scripts/validate_strict.py`: pass with 0 strict errors.
- `linkml-reference-validator`: pass; 1 file checked, 0 reference checks.
- `linkml-term-validator`: pass.
- Embedded `curation_history`: not checked; the available `just validate-history` target validates standalone files under `history/`, not embedded history events inside merged YAML.

## Identity and Grounding

The identity and duplicate topology are correct. KOMODO 1111 and DSMZ/MediaDive 1111 use the same medium number, the live KOMODO page links to DSMZ Medium 1111, and the DSMZ and MediaDive sources list the same eight non-water ingredients at the same gram-per-liter concentrations.

The physical-state and broad classification fields are also appropriate: DSMZ 1111 contains 6 g/L agar and is a complex bacterial solid medium.

Seven of the eight direct ingredient rows have primary CHEBI terms and `mediaingredientmech_chebi_term` mirrors. Casitone is appropriately left ungrounded as a mixture. The carboxymethyl cellulose grounding should be revisited: the current `CHEBI:85146` maps to generic carboxymethylcellulose, while DSMZ qualifies the compound as carboxymethyl cellulose, sodium salt, high viscosity, and the local MediaIngredientMech label index maps that wording to `CHEBI:234035`.

## Evidence

The DSMZ 1111 PDF lists exactly:

- 1 g/L `(NH4)2SO4`
- 1 g/L `MgSO4 x 7H2O`
- 1 g/L `CaCl2 x 2H2O`
- 0.2 g/L `FeCl3`
- 1 g/L `K2HPO4`
- 2 g/L `Casitone`
- 15 g/L `Carboxymethyl cellulose`
- 6 g/L `Agar`
- 1000 ml distilled water

The MediaDive 1111 JSON represents the same formula, including `autoclaved separately` as an attribute on the K2HPO4 row and `Difco` as an attribute on the Casitone row. The KOMODO 1111 page has the same medium name, same DSMZ Medium 1111 instruction link, and the same ingredient masses.

## Completeness

The generated record omits the explicit 1000 ml distilled-water row, which is acceptable for a direct gram-per-liter media recipe but should not be re-imported from `mediadive_2232_Main_sol_1111.yaml` as `1000 PERCENT_V_V`.

No pH is recorded in the generated YAML because none is supplied by DSMZ, MediaDive, or KOMODO. No `target_organisms` or growth evidence are present; that is a coverage gap, not a contradiction in the formula itself.

The source note that the carboxymethyl cellulose sodium salt, high viscosity product works well is preserved as a generic `MIX` preparation step. The more operational source qualifiers, `K2HPO4 (autoclaved separately)` and `Casitone (Difco)`, are not preserved in structured form.

## Findings

- Minor: the generated record loses the `autoclaved separately` qualifier from the K2HPO4 ingredient.
- Minor: the generated record loses the `Difco` qualifier from the Casitone ingredient.
- Minor: the carboxymethyl cellulose row is grounded to generic `CHEBI:85146`; review whether DSMZ's sodium-salt note should be preserved in the preferred label and grounded to the local MediaIngredientMech sodium-salt mapping.
- Minor: the maintained MediaDive main-solution owner stores 1000 ml water as `1000 PERCENT_V_V`.
- Minor: no source-backed target organism or strain growth evidence has been curated.

## Recommended Edits

- Preserve the MediaDive row attributes for `K2HPO4` and `Casitone`, either as ingredient notes or preparation metadata.
- Review the carboxymethyl cellulose sodium-salt qualifier against `src/culturemech/data/mediaingredientmech/label_index.csv` and align the CHEBI mirror if `CHEBI:234035` is the intended normalized term.
- Fix `mediadive_2232_Main_sol_1111.yaml` so the source 1000 ml water basis is not represented as `PERCENT_V_V`.
- Add organism-level growth evidence if a strain is found to use DSMZ 1111.

## Follow-up Checks

- Regenerate this merged YAML and confirm that the KOMODO 1111 / DSMZ 1111 source-duplicate collapse remains a two-record merge.
- Re-run LinkML, strict, reference, and term validation after preserving the lost row attributes.

## Additional Notes

Generated `data/merge_yaml/merged` files are derived. Apply durable fixes to the DSMZ/MediaDive 1111 normalized owner, the KOMODO 1111 owner, the MediaDive solution import, or importer metadata handling before regenerating this output.

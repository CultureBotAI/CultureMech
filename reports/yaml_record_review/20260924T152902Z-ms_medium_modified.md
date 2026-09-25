# YAML Record Review: ms_medium_modified

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ms_medium_modified.yaml
- Started UTC: 2026-09-24T15:27:10Z
- Finished UTC: 2026-09-24T15:29:02Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| CultureMech ID | CultureMech:003856 |
| Name | ms_medium_modified |
| Original name | MS-MEDIUM (MODIFIED) |
| Category | bacterial |
| Source identity | komodo.medium:1145 plus mediadive.medium:1145 |
| Reviewed artifact | Generated merge output |
| Maintained owners | data/normalized_yaml/bacterial/KOMODO_1145_MS-MEDIUM_MODIFIED.yaml; data/normalized_yaml/bacterial/ms_medium_modified.yaml |
| Merge status | Generated from a KOMODO/DSMZ source duplicate pair |

## Validation

| Check | Result |
| --- | --- |
| Open schema validation with `linkml-validate` | Passed; exited 0 with no diagnostics |
| Strict validation with `scripts/validate_strict.py` | Passed with 0 errors |
| Reference validation with `linkml-reference-validator` | Passed; 0 reference checks |
| Term validation with `linkml-term-validator` | Passed |
| Embedded `curation_history` validation | Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML |

## Identity and Grounding

The source identity is recognizable: DSMZ/MediaDive Medium 1145 is `MS-MEDIUM (MODIFIED)`, and the generated output correctly records that KOMODO Medium 1145 is a source duplicate of `mediadive.medium:1145`.

An exact gitignore-independent search for `CultureMech:003856`, `CultureMech:000583`, `komodo.medium:1145`, and `mediadive.medium:1145` under `data/normalized_yaml` and `data/merge_yaml` found the KOMODO owner, the DSMZ/MediaDive owner, their generated merge, and generated indexes. No third KOMODO or MediaDive 1145 record was found in those record corpora.

The generated ingredient graph is not an exact representation of DSMZ Medium 1145. DSMZ defines a 1 L main solution containing 800 ml anaerobic double-distilled water, 200 ml MS Buffer, 20 ml Solution A, 1.5 ml Solution B, and 10 ml Solution C. The normalized owners flatten stock-solution-internal concentrations into the final medium. That produces final-medium rows such as 100 g/L NH4Cl from Solution A, 200 g/L K2HPO4 x 3 H2O from Solution B, and full-strength trace-metal g/L values from Solution C.

Most primary chemical groundings are exact at the compound-label level. `NiSO4 x 6 H2O` is over-broad: DSMZ lists nickel sulfate hexahydrate, but the record asserts generic `CHEBI:53001` / `nickel sulfate`.

## Evidence

Supported source claims:

- MediaDive REST confirms Medium 1145 as a non-complex DSMZ recipe named `MS-MEDIUM (MODIFIED)`.
- The source main solution supports 5 g/L elemental sulphur, 2 g/L NaS2O3 x 5 H2O, 7 g/L MgSO4 x 7 H2O, 0.48 g/L KCl, 0.4 g/L CaCl2 x 2 H2O, and 0.8 g/L MgCl2 x 6 H2O.
- The source supports a nested MS Buffer stock at 200 ml/L, Solution A at 20 ml/L, Solution B at 1.5 ml/L, and Solution C at 10 ml/L.
- The DSMZ/MediaDive owner preserves source preparation steps for anaerobic preparation under N2, 4% O2 addition for microaerophilic conditions, MS Buffer saturation with CO2, Solution A pH 4, Solution C pH 3.0, and repeated 100 C heat sterilization.

Unsupported or stale generated claims:

- The generated record converts 800 ml water to `800 G_PER_L`.
- It stores MS Buffer, Solution A, Solution B, and Solution C stock concentrations as final-medium g/L values rather than scaling them by the source stock volumes.
- It merges the main-solution 0.4 g/L CaCl2 x 2 H2O with the unscaled 40 g/L CaCl2 x 2 H2O stock concentration from Solution A, yielding 40.4 g/L instead of a final 1.2 g/L.
- It merges the main-solution 0.8 g/L MgCl2 x 6 H2O with the unscaled 100 g/L MgCl2 x 6 H2O stock concentration from Solution A, yielding 100.8 g/L instead of a final 2.8 g/L.
- It drops all DSMZ preparation steps in the generated merge because the selected canonical source is the older KOMODO-derived duplicate.

## Completeness

The generated output includes all named non-water compounds from the DSMZ REST payload after flattening, but it loses the stock-solution structure and source preparation boundary.

Consequential gaps:

- Water, MS Buffer, Solution A, Solution B, and Solution C need to be represented as volumes and nested solutions rather than as final solutes.
- Solution A, B, and C ingredients need final-medium contributions scaled by 20/1000, 1.5/1000, and 10/1000 respectively.
- DSMZ preparation steps need to survive source-duplicate merging.
- `NiSO4 x 6 H2O` needs an exact hexahydrate grounding, not generic nickel sulfate.

The generated `timestamp: 2026-01-27T01:15:01.fZ` curation-history value is syntactically valid YAML but is not a valid timestamp; this remained untested because embedded `curation_history` validation was unavailable for one merged recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Nested stock concentrations are flattened as final medium concentrations. | DSMZ Medium 1145 adds Solution A at 20 ml/L, Solution B at 1.5 ml/L, and Solution C at 10 ml/L; the YAML stores Solution A's 100 g/L NH4Cl, Solution B's 200 g/L K2HPO4 x 3 H2O, and Solution C's trace g/L values without volume scaling. | data/normalized_yaml/bacterial/KOMODO_1145_MS-MEDIUM_MODIFIED.yaml; data/normalized_yaml/bacterial/ms_medium_modified.yaml |
| Major | Duplicate compound cleanup merged stock concentrations with final main-solution concentrations. | DSMZ lists 0.4 g/L final CaCl2 x 2 H2O plus 40 g/L in a 20 ml/L stock, but the YAML adds them to `40.4 G_PER_L`; DSMZ likewise lists 0.8 g/L final MgCl2 x 6 H2O plus 100 g/L in the same 20 ml/L stock, but the YAML adds them to `100.8 G_PER_L`. | data/normalized_yaml/bacterial/KOMODO_1145_MS-MEDIUM_MODIFIED.yaml; data/normalized_yaml/bacterial/ms_medium_modified.yaml |
| Major | The generated source-duplicate merge loses the DSMZ preparation instructions. | `data/normalized_yaml/bacterial/ms_medium_modified.yaml` has six DSMZ-derived preparation steps, but the generated merge keeps the KOMODO-derived ingredient-only canonical record and has no `preparation_steps`. | merge logic |
| Major | `NiSO4 x 6 H2O` is grounded to generic nickel sulfate. | MediaDive Solution C lists `NiSO4 x 6 H2O`; the record asserts `CHEBI:53001` / `nickel sulfate`, while the local ChEBI structure index has the exact hexahydrate as `CHEBI:53437`. | data/normalized_yaml/bacterial/KOMODO_1145_MS-MEDIUM_MODIFIED.yaml; data/normalized_yaml/bacterial/ms_medium_modified.yaml |
| Minor | One imported KOMODO curation-history timestamp is malformed. | The generated record contains `timestamp: 2026-01-27T01:15:01.fZ`, which is not a valid ISO timestamp. | data/normalized_yaml/bacterial/KOMODO_1145_MS-MEDIUM_MODIFIED.yaml |

## Recommended Edits

1. Rework the DSMZ/MediaDive 1145 and KOMODO 1145 normalized owners to preserve MS Buffer, Solution A, Solution B, and Solution C as nested solutions or to scale each nested ingredient by its added volume before flattening.
2. Repair the duplicate-ingredient cleanup so it never sums a main-solution final concentration with an unscaled stock-solution concentration.
3. Make the DSMZ/MediaDive record the canonical source or otherwise merge duplicate-source metadata without dropping DSMZ `preparation_steps`.
4. Re-ground `NiSO4 x 6 H2O` to exact `CHEBI:53437` if that term is accepted by the current MediaIngredientMech/OAK workflow.
5. Repair the malformed KOMODO curation-history timestamp.
6. Rerun the merge generator so `data/merge_yaml/merged/ms_medium_modified.yaml` reflects the scaled final recipe and preserves the DSMZ preparation steps.

## Follow-up Checks

1. Re-run open schema, strict, reference, and term validation on the regenerated merged record.
2. Re-diff the regenerated recipe against `https://mediadive.dsmz.de/rest/medium/1145`, with explicit checks for final CaCl2 x 2 H2O, MgCl2 x 6 H2O, NH4Cl, K2HPO4 x 3 H2O, and Solution C trace-metal amounts.
3. Confirm the regenerated merge has DSMZ anaerobic, microaerophilic, CO2-saturation, pH-adjustment, and 100 C heat-sterilization steps.
4. Run the exact gitignore-independent `komodo.medium:1145` and `mediadive.medium:1145` duplicate searches again after regeneration to make sure the source duplicate pair still resolves exactly once.

## Additional Notes

- This source is solution-rich; downstream fixes should avoid flat string edits and preserve the DSMZ REST solution IDs 2296, 2297, 2298, 2299, and 2300.
- The exact duplicate search above included ignored files.

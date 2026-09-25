# YAML Record Review: BBL_ACTINOMYCES_BROTH

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BBL_ACTINOMYCES_BROTH.yaml
- Started UTC: 2026-09-21T19:09:51Z
- Finished UTC: 2026-09-21T19:12:28Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path reviewed | `data/merge_yaml/merged/BBL_ACTINOMYCES_BROTH.yaml` |
| Maintained owners | `data/normalized_yaml/bacterial/KOMODO_1029_BBL_ACTINOMYCES_BROTH.yaml`; `data/normalized_yaml/bacterial/bbl_actinomyces_broth.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:003541` |
| Name | `bbl_actinomyces_broth` |
| Original name | `BBL ACTINOMYCES BROTH` |
| Source | KOMODO Medium `1029`; DSMZ/MediaDive Medium `1029` |
| Merge status | Generated two-source merge from `KOMODO_1029_BBL_ACTINOMYCES_BROTH` and `bbl_actinomyces_broth` |

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with the no-project LinkML invocation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`, and the generated BBL Actinomyces Broth merge. |
| Strict schema | Passed with the no-project invocation of `scripts/validate_strict.py`: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | Passed with 0 reference checks because this KOMODO/DSMZ merge has no populated `references` list or evidence objects. |
| Term validator | Passed with `linkml-term-validator validate-data` against the generated BBL Actinomyces Broth merge. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for the standalone `history/` tree, not a focused one-record `MediaRecipe.curation_history` check. |
| Project `just` wrappers | Not rerun here: direct `just validate-schema`, `just validate-strict`, and `just validate-terms` fail before target-specific validation in this checkout while the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13. The equivalent no-project Python 3.11 validators above exercised the target record. |

## Identity and Grounding

- The generated merge denotes DSMZ/KOMODO Medium 1029, BBL Actinomyces Broth, with canonical ID `CultureMech:003541` and a `SOURCE_DUPLICATE` parent link to the DSMZ/MediaDive copy `CultureMech:000450`.
- The inspected DSMZ Medium 1029 PDF supports the same label, final pH 6.9, and the ten BBL 210920 formula rows imported into both normalized copies.
- The generated merge lacks the DSMZ/MediaDive parent's two handling steps about screw-capped Wheaton tubes and Hungate tubes.
- `Potassium Phosphate` is grounded to `CHEBI:63036` / potassium dihydrogen phosphate, but the inspected source does not specify the monobasic form.
- Exact gitignore-independent searches for `CultureMech:003541`, `CultureMech:000450`, `komodo.medium:1029`, `mediadive.medium:1029`, `DSMZ_Medium1029.pdf`, `Source: KOMODO, ID: 1029`, and `Source: DSMZ, ID: 1029` covered `data/raw`, `data/import_tracking`, `data/normalized_yaml`, and `data/merge_yaml`. They found the KOMODO owner, DSMZ/MediaDive parent owner, generated merge, generated indexes, and ungrounded-ingredient import reports, but no local raw KOMODO or DSMZ dump.

## Evidence

- The DSMZ PDF gives a top-level recipe of 57.0 g commercial BBL Actinomyces broth in 1000.0 ml distilled water. The YAML expands the commercial BBL 210920 composition but omits the distilled water row.
- The PDF lists `Potassium Phosphate` 15.0 g, `Ammomium Sulfate` 1.0 g, `Magnesium Sulfate` 0.2 g, `Calcium Chloride` 0.01 g, `Infusion Broth` 25.0 g, `Dextrose` 5.0 g, `L-Cysteine x HCL` 1.0 g, `Pancreatic Digest of Casein` 4.0 g, `Yeast Extract` 5.0 g, and `Soluble Starch` 1.0 g; the generated merge preserves the same numeric gram-per-litre values.
- Both source copies leave `Infusion Broth`, `Pancreatic digest of casein`, and `Yeast extract` ungrounded, which is appropriate for complex commercial or digest ingredients that are not exact small molecules.
- The DSMZ/MediaDive normalized owner carries preparation steps for screw-capped Wheaton tubes and anaerobic Hungate handling; those do not survive into the generated two-source merge.
- The generated merge retains `L-Cysteine HCl` as a legacy `mediaingredientmech_term`.

## Completeness

- Consequential gaps:
  - The generated merge omits distilled water even though the DSMZ top-level formulation explicitly brings the commercial broth to 1000.0 ml with water.
  - `Potassium Phosphate` needs a generic or unresolved phosphate-salt representation unless an inspected source supports the monobasic salt.
  - The source-specific Wheaton/Hungate handling instruction from the DSMZ/MediaDive duplicate is lost in the generated merge.
  - The first KOMODO import event has a malformed timestamp, `2026-01-27T01:15:01.fZ`.
  - One ingredient still retains a legacy MIM identifier after the June 2026 MIM migration.
- Correctly empty optional slots:
  - `Infusion Broth`, `Pancreatic digest of casein`, and `Yeast extract` are explicitly unresolved complex ingredients rather than forced to narrow CHEBI terms.
  - `target_organisms` and `growth_metrics` are absent; the inspected DSMZ recipe gives a medium formulation, not a strain-specific growth assay.
- Bounded negative searches:
  - Exact gitignore-independent searches found no local raw KOMODO or DSMZ Medium 1029 dump under `data/raw` or `data/import_tracking`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge drops the source water row. | DSMZ Medium 1029 says to use 1000.0 ml distilled water with the commercial BBL broth, while the generated merge contains no water ingredient or final-volume preparation that preserves that row. | Both normalized owners or the KOMODO/DSMZ import and merge rules. |
| Major | One ingredient grounding is over-specific. | The source says `Potassium Phosphate`; the YAML grounds it to `CHEBI:63036` / potassium dihydrogen phosphate without source evidence for that exact salt. | Both normalized owners. |
| Major | The generated merge omits source-specific handling steps from the DSMZ/MediaDive duplicate. | `data/normalized_yaml/bacterial/bbl_actinomyces_broth.yaml` has screw-capped Wheaton tube and anaerobic Hungate-tube instructions, but the generated merge has no `preparation_steps`. | Merge rules for duplicate MediaRecipe records and the DSMZ/MediaDive normalized owner. |
| Minor | One ingredient still uses a legacy MIM identifier. | `L-Cysteine HCl` retains `mediaingredientmech_term: MediaIngredientMech:000223` while the migration converted the other six MIM links in this record to CHEBI-keyed links. | Both normalized owners. |
| Minor | The KOMODO curation history includes a malformed timestamp. | The first `komodo-web-import` event stores `2026-01-27T01:15:01.fZ`, which is not an ISO timestamp. | `data/normalized_yaml/bacterial/KOMODO_1029_BBL_ACTINOMYCES_BROTH.yaml`. |

## Recommended Edits

1. Add the DSMZ top-level distilled-water make-up row or an equivalent final-volume preparation to the normalized representation.
2. Replace the `Potassium Phosphate` grounding with a source-faithful unresolved or generic phosphate representation unless an inspected primary source identifies the monobasic salt.
3. Preserve the DSMZ/MediaDive tube-handling preparation when merging the KOMODO and DSMZ source duplicates, or intentionally scope it to the DSMZ duplicate with a source-specific note.
4. Replace the legacy `L-Cysteine HCl` MediaIngredientMech link with the CHEBI-keyed representation.
5. Normalize the malformed KOMODO import timestamp without rewriting unrelated history.

## Follow-up Checks

- Rerun open-schema LinkML validation, `scripts/validate_strict.py`, `linkml-term-validator`, and the reference validator on both normalized owners and the regenerated merge.
- Re-extract `DSMZ_Medium1029.pdf` and manually compare the top-level 57 g/L BBL Actinomyces broth, water row, pH, BBL 210920 subcomposition, and anaerobic handling against the YAML.
- Regenerate the generated merge and run `just verify-merges` plus `just audit-merge-freshness`.
- Confirm `L-Cysteine HCl` no longer contains `mediaingredientmech_term`.

## Additional Notes

- A third KOMODO-derived sibling, `data/normalized_yaml/bacterial/bbl_actinomyces_broth_medium_1029.yaml`, is listed in `data/import_tracking/reports/missing_compositions.tsv` as a compositionless Medium 1029 record; it is outside this generated merge but should be reconciled when Medium 1029 duplicates are cleaned up.
- Exact gitignore-independent searches included ignored files where present.

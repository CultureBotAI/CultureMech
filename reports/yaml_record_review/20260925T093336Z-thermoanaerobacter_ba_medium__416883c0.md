# YAML Record Review: THERMOANAEROBACTER (BA) MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoanaerobacter_ba_medium__416883c0.yaml`
- Started UTC: `2026-09-25T09:33:36Z`
- Finished UTC: `2026-09-25T09:34:36Z`
- Verdict: needs curation

## Target
Generated bacterial recipe `CultureMech:001812`, `thermoanaerobacter_ba_medium`, with medium term `mediadive.medium:671` and label `THERMOANAEROBACTER (BA) MEDIUM`.

It is a merge of three source records: the MediaDive DSMZ 671 import `thermoanaerobacter_ba_medium`, the KOMODO DSMZ 671 record `modified_ba_medium`, and the KOMODO cellulose variant `modified_ba_medium_replace_cellobiose_with_cellulose`.

## Validation
- LinkML schema validation: passed; `linkml-validate` reported `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The record is correctly grounded to MediaDive/DSMZ medium 671, and its generated synonyms correctly carry the two KOMODO DSMZ 671 source IDs.

The same DSMZ 671 source remains split into `data/merge_yaml/merged/thermoanaerobacter_ba_medium.yaml`, whose TOGO branch contains `TOGO:M2728` and `TOGO:M2730` imports that also cite `DSMZ_Medium671.pdf`.

The ingredient-level CHEBI groundings reviewed in the flattened main list are internally consistent, including `MgSO4 x 7 H2O` to `CHEBI:31795`, `Na2SeO3 x 5 H2O` to `CHEBI:131361`, and `Na2WO4 x 2 H2O` to `CHEBI:63939`.

## Evidence
DSMZ Medium 671 and MediaDive medium 671 specify NH4Cl, NaCl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, K2HPO4 x 3 H2O, 10 ml Modified Wolin's mineral solution, yeast extract, sodium resazurin, Na2CO3, cellobiose, optional Avicel cellulose, 1 ml Wolin's vitamin solution 10x, Na2S x 9 H2O, and water in the main recipe.

The generated record converted the direct main rows to 1011 ml-normalized values, but then appended the undiluted stock recipes into the top-level `ingredients` list. For example, Modified Wolin's mineral solution should enter as a 10 ml/L stock addition, not as 1.5 g/L top-level nitrilotriacetic acid, 3 g/L top-level MgSO4 x 7 H2O, and the rest of the stock contents at their 1000 ml stock concentrations.

The same flattening affects the vitamin stock. Wolin's vitamin solution 10x is added at 1 ml per liter of medium, but its stock components appear in the final record as direct `G_PER_L` rows such as `0.02` for `Biotin`, `0.1` for `Pyridoxine hydrochloride`, and `0.001` for `Vitamin B12`.

NaCl and CaCl2 from the main solution were also merged with their Modified Wolin stock rows, inflating them to `1.0989119999999999 G_PER_L` and `0.149456 G_PER_L` respectively instead of keeping the stock contribution nested.

## Completeness
The generated MediaDive/KOMODO branch preserves the main DSMZ preparation notes, including anoxic sparging, sterile addition of cellobiose, vitamins, sulfide, and carbonate from anoxic stocks, and the optional cellulose adaptation note.

It also preserves the D-xylose substitution for DSM 29083 and DSM 25963 only indirectly as a separate KOMODO cellulose variant. A regenerated canonical DSMZ 671 record should preserve optional cellulose and strain-specific D-xylose as explicit optional or variant semantics rather than leave source-equivalent records split across generated branches.

## Findings
1. Needs curation: Modified Wolin's mineral solution and Wolin's vitamin solution 10x are flattened into top-level ingredients at stock concentrations, which makes the final recipe quantitatively wrong.
2. Needs curation: the DSMZ 671 identity is split across this MediaDive/KOMODO branch and the TOGO branch in `thermoanaerobacter_ba_medium.yaml`.
3. Needs curation: optional cellulose adaptation and strain-specific D-xylose substitution should be modeled explicitly when the source records are normalized, so the canonical record does not rely on duplicate KOMODO variants to preserve them.

## Recommended Edits
1. Normalize `thermoanaerobacter_ba_medium`, `modified_ba_medium`, and `modified_ba_medium_replace_cellobiose_with_cellulose` in `data/normalized_yaml`, not the generated merge file, so DSMZ 671 keeps Modified Wolin's mineral solution and Wolin's vitamin solution 10x as nested stock additions.
2. Fold the TOGO M2728 and M2730 imports into the same canonical source identity as `mediadive.medium:671` and `komodo.medium:671` after both branches have been normalized.
3. Retain the DSMZ preparation steps while making optional Avicel cellulose and strain-specific D-xylose substitutions explicit in variant metadata.

## Follow-up Checks
After source edits and merge regeneration, re-run schema, strict, reference, and term validation on the generated DSMZ 671 record.

Run an exact duplicate search with ignored files included for `mediadive.medium:671`, `komodo.medium:671`, `TOGO:M2728`, `TOGO:M2730`, and `DSMZ_Medium671` and confirm they now resolve to one generated canonical record.

## Additional Notes
Exact duplicate-source searches included ignored files.

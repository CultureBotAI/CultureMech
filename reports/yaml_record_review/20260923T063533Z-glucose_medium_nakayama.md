# YAML Record Review: glucose_medium_nakayama

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glucose_medium_nakayama.yaml
- Started UTC: 2026-09-23T06:34:03Z
- Finished UTC: 2026-09-23T06:35:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:005291` |
| Name | `glucose_medium_nakayama` |
| Original name | `GLUCOSE medium (NAKAYAMA)` |
| Category | `bacterial` |
| Canonical media term | `komodo.medium:452` |
| Direct source duplicate | `data/normalized_yaml/bacterial/glucose_medium_nakayama.yaml`, `mediadive.medium:452` |
| KOMODO source duplicate | `data/normalized_yaml/bacterial/KOMODO_452_GLUCOSE_medium_NAKAYAMA.yaml`, `komodo.medium:452` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glucose_medium_nakayama.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glucose_medium_nakayama.yaml --out /private/tmp/glucose_medium_nakayama.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glucose_medium_nakayama.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glucose_medium_nakayama.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

The duplicate identity is correct: the KOMODO 452 parent states DSMZ Medium 452 provenance and the direct MediaDive parent is DSMZ Medium 452, `GLUCOSE MEDIUM (NAKAYAMA)`.

A gitignore-independent exact search for `komodo.medium:452`, `mediadive.medium:452`, `DSMZ_Medium452.pdf`, and `KOMODO_452_GLUCOSE_medium_NAKAYAMA` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found only the two maintained parents, their generated index references, and this generated merge.

The retained ingredient groundings are mostly narrow: glucose, KH2PO4, K2HPO4, magnesium sulfate heptahydrate, sodium chloride, manganese(II) sulfate pentahydrate, copper(II) sulfate pentahydrate, iron(2+) sulfate heptahydrate, and agar agree with the DSMZ labels. Peptone and yeast extract remain ungrounded complex ingredients.

## Evidence

DSMZ 452 is a main recipe plus three separately autoclaved stock solutions:

| Source component | DSMZ amount |
|---|---:|
| Glucose | 10 g in the main recipe |
| Peptone | 10 g in the main recipe |
| Yeast extract | 15 g in the main recipe |
| Agar | 10 g in the main recipe |
| Distilled water | 980 ml in the main recipe |
| Solution A | 10 ml into the main recipe |
| Solution B | 10 ml into the main recipe |
| Solution C | 1 ml into the main recipe |

Solution A is a 100 ml stock containing 0.5 g KH2PO4 and 0.5 g K2HPO4. Solution B is a 100 ml stock containing 3 g MgSO4 x 7 H2O, 0.1 g NaCl, 0.1 g MnSO4 x 5 H2O, and 0.01 g CuSO4 x 5 H2O. Solution C is a 100 ml stock containing 0.1 g FeSO4 x 7 H2O and 2 g Na3-Citrate.

The generated record flattens the stock strengths as if they were final-medium g/l values: for example, DSMZ uses 10 ml of the 30 g/l MgSO4 stock, but the generated record stores 30 g/l MgSO4 in the final recipe. The 1 ml Solution C addition is inflated even more: FeSO4 x 7 H2O appears as 1 g/l and Na3-citrate appears as 20 g/l instead of 0.001 g and 0.02 g per liter of final medium.

The direct MediaDive parent retained the preparation step `Autoclave all solutions separately, final pH is 6.8.`; the generated merge dropped it.

## Completeness

The generated record is not complete enough for reuse because it omits stock solution boundaries, source dilution volumes, all four water rows, and the autoclave instruction. A reader following the flattened values would make a chemically different medium.

Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects in this generated two-parent merge.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Solution A, B, and C ingredients are encoded at 100 ml stock strength, not at the amount added to DSMZ 452. | DSMZ 452 adds 10 ml Solution A, 10 ml Solution B, and 1 ml Solution C to the main recipe; the generated record has 5 g/l KH2PO4, 5 g/l K2HPO4, 30 g/l MgSO4 x 7 H2O, 1 g/l NaCl, 1 g/l MnSO4 x 5 H2O, 0.1 g/l CuSO4 x 5 H2O, 1 g/l FeSO4 x 7 H2O, and 20 g/l Na3-citrate as independent final-medium rows. | MediaDive/KOMODO import normalization for DSMZ 452 or the two maintained parents under `data/normalized_yaml/bacterial/`. |
| Major | The generated merge lost the only preparation step from the direct MediaDive parent. | The source and direct parent say to autoclave all solutions separately and give final pH 6.8; the generated merge has no `preparation_steps`. | `scripts/merge_recipes.py` or merge overlay handling for source-duplicate parents. |
| Minor | The generated canonical source is the KOMODO derivative instead of the direct DSMZ/MediaDive source. | The generated record uses `media_term.id: komodo.medium:452`; the direct source parent uses `mediadive.medium:452`. | Merge selection policy or a duplicate overlay for DSMZ 452. |
| Minor | The DSMZ water rows are missing. | DSMZ 452 has 980 ml water in the main recipe and 100 ml water in each of Solutions A, B, and C; the generated record has no water or solution rows. | MediaDive/KOMODO import normalization for DSMZ 452. |
| Minor | The KOMODO parent has a malformed original import timestamp. | `KOMODO_452_GLUCOSE_medium_NAKAYAMA.yaml` contains `timestamp: 2026-01-27T01:15:02.fZ`. | `data/normalized_yaml/bacterial/KOMODO_452_GLUCOSE_medium_NAKAYAMA.yaml`. |

## Recommended Edits

1. Rework DSMZ 452 upstream so Solution A, Solution B, and Solution C are represented as stock solutions with their 10 ml, 10 ml, and 1 ml main-medium additions instead of independent final-medium ingredients.
2. Preserve the source instruction to autoclave all solutions separately and final pH 6.8 through the generated merge.
3. Prefer `mediadive.medium:452` as the canonical source accession while keeping `komodo.medium:452` as a duplicate alias.
4. Decide whether DSMZ water rows should be represented; if yes, restore the 980 ml main-medium water row and the 100 ml stock water rows upstream.
5. Repair the malformed KOMODO import timestamp.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation after regenerating `data/merge_yaml/merged/glucose_medium_nakayama.yaml`.
- Compare the regenerated solution structure against the live MediaDive 452 payload or DSMZ 452 PDF and verify that all stock amounts, addition volumes, water rows, and the separate-autoclave instruction are retained.
- Re-run the exact gitignore-independent search for `komodo.medium:452`, `mediadive.medium:452`, `DSMZ_Medium452.pdf`, and `KOMODO_452_GLUCOSE_medium_NAKAYAMA` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify only the expected duplicate pair remains.

## Additional Notes

`Na3-citrate` is grounded to `CHEBI:53258` with label `sodium citrate`. That is plausible for the anhydrous DSMZ label and should be revisited only if the curation model starts distinguishing sodium citrate hydrates or protonation states in these recipe rows.

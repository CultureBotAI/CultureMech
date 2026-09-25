# YAML Record Review: PETROTOGA AR80 MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/petrotoga_ar80_medium__5f6b639b.yaml
- Started UTC: 2026-09-24T20:37:09Z
- Finished UTC: 2026-09-24T20:37:09Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record path | `data/merge_yaml/merged/petrotoga_ar80_medium__5f6b639b.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/petrotoga_ar80_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:003231` |
| Name | `petrotoga_ar80_medium` |
| Original name | `PETROTOGA AR80 MEDIUM` |
| Media term | `mediadive.medium:J883` |
| Generated status | Generated merge output from `data/normalized_yaml/bacterial/petrotoga_ar80_medium.yaml` |

The generated record resolves exactly to the MediaDive/JCM J883 PETROTOGA AR80
MEDIUM direct import. An ignored-inclusive search over `data`, `src`, and
`scripts` for `mediadive.medium:J883`, `GRMD=883`, `CultureMech:003231`, and
`petrotoga_ar80_medium` also found the same JCM 883 source represented through
TOGO M924 in `data/normalized_yaml/bacterial/TOGO_M924_Petrotoga_AR80_Medium.yaml`
and `data/merge_yaml/merged/PETROTOGA_AR80_MEDIUM.yaml`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/petrotoga_ar80_medium__5f6b639b.yaml` | Passed; no issues found. |
| Strict repository validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/petrotoga_ar80_medium__5f6b639b.yaml --out /private/tmp/petrotoga_ar80_medium__5f6b639b.strict.tsv --workers 1 --quiet` | Passed; the TSV had only its header line, so 0 errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/petrotoga_ar80_medium__5f6b639b.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/petrotoga_ar80_medium__5f6b639b.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run. | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in one generated YAML file. |

## Identity and Grounding

The J883 identity is correct: MediaDive REST for `J883` returned one medium named
`PETROTOGA AR80 MEDIUM`, pH 7.8, source `JCM`, and the same JCM URL stored in
the generated `notes`. The record's bacterial category, liquid physical state,
complex medium type, and semi-defined composition type also match the source
recipe, because the formulation combines defined salts, defined vitamins, and
yeast extract.

The chemical groundings in this record are plausible for the spelled compounds
that remain after flattening. No wrong CHEBI identity was found in this direct
J883 import.

## Evidence

MediaDive J883 supports the top-level medium identity and the main preparation
sentence. It gives a `Main sol. J883` with pH 7.8 and this final formulation:
10 g NaCl, 7 g MgSO4 x 7 H2O, 0.34 g KCl, 0.25 g NH4Cl, 0.14 g CaCl2 x 2 H2O,
0.14 g KH2PO4, 0.1 g yeast extract, 1 ml Trace mineral solution, 10 ml Trace
vitamins, 0.2 mg resazurin, 0.5 g L-Cysteine HCl x H2O, and 1000 ml distilled
water in a 1011 ml final solution.

The generated record does not preserve the two named stock solutions that
MediaDive exposes. MediaDive has a separate 1000 ml `Trace mineral solution`
containing salts such as 3 g MgSO4 x 7 H2O, 1 g NaCl, 644 mg MgSO4 x 7 H2O,
178.1 mg ZnSO4 x 7 H2O, 100 mg FeSO4 x 7 H2O, 100 mg CoCl2 x 6 H2O, 75.5 mg
CaCl2 x 2 H2O, and 10 mg each of CuSO4 x 5 H2O, AlK(SO4)2, H3BO3, and
Na2MoO4 x 2 H2O. It also has a separate 1000 ml `Trace vitamins` stock with
milligram-scale biotin, folic acid, pyridoxine hydrochloride, thiamine HCl,
riboflavin, nicotinic acid, calcium pantothenate, vitamin B12,
p-Aminobenzoic acid, and lipoic acid.

Flattening those stock recipes into the final ingredient list created
concentrations that MediaDive does not state as final-liter concentrations. The
most visible examples are NaCl `10.8912` g/L from `[Merged 2 duplicates:
9.8912, 1.0]`, MgSO4 x 7 H2O `10.56784` g/L from `[Merged 3 duplicates:
6.92384, 3.0, 0.644]`, and CaCl2 x 2 H2O `0.21397699999999997` g/L from
`[Merged 2 duplicates: 0.138477, 0.0755]`.

The exact JCM URL in the MediaDive metadata and local notes returned an HTML
page saying "Nothing found" for medium number 883 during this review, so the
active source check used MediaDive REST and TOGO's JCM_M883 derivative rather
than a live JCM source page.

## Completeness

The generated record omits all three source water rows: the 1000 ml distilled
water in `Main sol. J883`, the 1000 ml distilled water in `Trace mineral
solution`, and the 1000 ml distilled water in `Trace vitamins`.

The generated record also lacks any `solutions:` entries for `Trace mineral
solution` or `Trace vitamins`, even though the source main recipe adds them as
1 ml and 10 ml aliquots. Their stock recipe ingredients are present only as
final ingredients, which loses solution membership, aliquot amount, and stock
volume.

No empty optional field was material to this review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The stock solutions were flattened into the final ingredient list and several stock concentrations were summed with main-solution concentrations. | MediaDive J883 represents a 1011 ml main solution plus 1000 ml `Trace mineral solution` and 1000 ml `Trace vitamins` recipes; the generated direct import has no `solutions:` section and encodes summed final entries such as `10.8912` g/L NaCl, `10.56784` g/L MgSO4 x 7 H2O, and `0.21397699999999997` g/L CaCl2 x 2 H2O. | `data/normalized_yaml/bacterial/petrotoga_ar80_medium.yaml` and the MediaDive import path that flattens nested solutions |
| Major | The same JCM M883/PETROTOGA AR80 recipe still survives as a TOGO sibling instead of merging with the direct MediaDive/JCM record. | An ignored-inclusive search over `data`, `src`, and `scripts` found `CultureMech:010345` in `data/normalized_yaml/bacterial/TOGO_M924_Petrotoga_AR80_Medium.yaml` and `data/merge_yaml/merged/PETROTOGA_AR80_MEDIUM.yaml`; that record cites `TOGO:M924`, `original_media_id: JCM_M883`, and the same `GRMD=883` JCM URL. | `data/normalized_yaml/bacterial/petrotoga_ar80_medium.yaml`, `data/normalized_yaml/bacterial/TOGO_M924_Petrotoga_AR80_Medium.yaml`, and merge source-matching logic |

## Recommended Edits

1. Recurate `data/normalized_yaml/bacterial/petrotoga_ar80_medium.yaml` from
   MediaDive J883 with three separate scopes: `Main sol. J883`, `Trace mineral
   solution`, and `Trace vitamins`.
2. Keep only the final-solution salts, yeast extract, resazurin, cysteine, the
   1000 ml main water row, and 1 ml/10 ml stock aliquots in the main recipe;
   move the trace mineral and trace vitamin ingredients into their own
   `solutions:` records with their own 1000 ml water rows.
3. Preserve pH 7.8 and the MediaDive preparation text on the main solution.
4. Update the source duplicate merge mapping so TOGO M924/JCM_M883 is
   recognized as the same source recipe as `mediadive.medium:J883`, or manually
   merge `CultureMech:010345` into the J883 owner with TOGO listed as
   supporting provenance instead of keeping a generated sibling record.

## Follow-up Checks

1. Regenerate the merged YAML and rerun the open schema, strict, reference, and
   term validators on the regenerated PETROTOGA AR80 MEDIUM output.
2. Manually compare the regenerated recipe to MediaDive J883 and verify that no
   stock ingredient appears as a final ingredient unless it is also present in
   `Main sol. J883`.
3. Use an ignored-inclusive exact search for `GRMD=883`, `JCM_M883`,
   `TOGO:M924`, and `mediadive.medium:J883` under `data`, `src`, and `scripts`
   to verify that the merged corpus no longer has separate MediaDive and TOGO
   YAML outputs for the same JCM 883 source recipe.

## Additional Notes

The JCM URL being dead did not block the review because both the local
MediaDive import and the live MediaDive REST payload retain enough structured
J883 data to check the generated recipe. The TOGO M924 payload also identifies
the same unavailable JCM page as its original source.

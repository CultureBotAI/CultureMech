# YAML Record Review: mpycy_agar_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mpycy_agar_medium__650fe64d.yaml
- Started UTC: 2026-09-24T14:17:15Z
- Finished UTC: 2026-09-24T14:19:40Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/mpycy_agar_medium__650fe64d.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:002221`
- Label: `mpycy_agar_medium`
- Original label: `MPYCY AGAR MEDIUM`
- Category: `bacterial`
- Media source: MediaDive/JCM `J1037`
- Generated status: generated merge output from one normalized source on fingerprint `650fe64d4bd454c5cb60ace6103433cbc32e256aaab5f50b2ba26bb623113cad`
- Maintained owner: `data/normalized_yaml/bacterial/mpycy_agar_medium.yaml`

The generated record matches its maintained normalized owner except for the generated merge metadata.

## Validation

Validation was run on the generated merged YAML.

- Open LinkML schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mpycy_agar_medium__650fe64d.yaml`
  - Result: passed; exited 0 with no diagnostics.
- Strict validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mpycy_agar_medium__650fe64d.yaml --out /private/tmp/mpycy_agar_medium__650fe64d.strict.tsv --workers 1 --quiet`
  - Result: passed with 0 errors; `/private/tmp/mpycy_agar_medium__650fe64d.strict.tsv` contained only its header row.
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mpycy_agar_medium__650fe64d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 0 reference checks were evaluated.
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mpycy_agar_medium__650fe64d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed after the known `eutils` / `pkg_resources` warning.
- Embedded merge history:
  - Result: not checked. The repository history validator targets standalone `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record denotes the agar-plate form of JCM GRMD 1037, `MPYCY AGAR MEDIUM`.

The direct JCM GRMD 1037 page, the live MediaDive `J1037` JSON, TOGO `M1101`, and TOGO `M1102` all point at the same JCM page:

| Source | ID | Role |
| --- | --- | --- |
| JCM | `1037` | MPYCY source page with 7.6-7.8 agar pH and 7.4-7.6 liquid pH |
| MediaDive | `J1037` | expanded import of the JCM page as an agar medium |
| TOGO | `M1101`, original `JCM_M1037` | agar variant with `Agar (if necessary)` |
| TOGO | `M1102`, original `JCM_M1037-2` | liquid variant without agar |

An exact gitignore-independent search of `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:002221`, bounded `mediadive.medium:J1037`, bounded `ID: J1037`, and `GRMD=1037` found this MediaDive record, its normalized owner, repaired TOGO `M1101` and `M1102` normalized records, and their generated outputs. Ignored files were included.

The simple CHEBI groundings are narrow for sodium pyruvate, agar, ammonium sulfate, magnesium sulfate heptahydrate, potassium chloride, calcium chloride dihydrate, the vitamin compounds, and iron trichloride hexahydrate. `Casamino acids`, `Yeast extract`, and `Na2HPO4-NaH2PO4 buffer` are appropriately ungrounded.

## Evidence

JCM GRMD 1037 makes `MPYCY AGAR MEDIUM` from a main recipe plus `5 ml` Solution A and `8 ml` Solution B from GRMD 1036. GRMD 1036 defines Solution A as a 1 L salt stock, Solution B as a short phosphate/vitamin/FeCl3 mixture, and GRMD 296 defines the vitamin mix stock used inside Solution B.

The MediaDive-derived top-level CultureMech rows mix three levels of that hierarchy:

| Source level | Source addition | CultureMech row(s) | Status |
| --- | ---: | --- | --- |
| JCM 1037 main solution | 5 ml Solution A into `1000 ml` water plus additives | `(NH4)2SO4`, `MgSO4 x 7 H2O`, `KCl`, `CaCl2 x 2 H2O` at Solution A stock strengths | stock flattened |
| JCM 1037 main solution | 8 ml Solution B into `1000 ml` water plus additives | `Na2HPO4-NaH2PO4 buffer` as `2 G_PER_L` | volume row converted to the wrong mass unit |
| JCM 1036 Solution B | 5 ml vitamin stock into Solution B | ten vitamin rows at vitamin-stock strengths | nested stock flattened |
| JCM 1036 Solution B | 1 ml FeCl3 stock into Solution B | `FeCl3 x 6 H2O` at `0.5 G_PER_L` stock strength | nested stock flattened |

The main JCM 1037 rows for maltose monohydrate, sodium pyruvate, Casamino acids, yeast extract, and agar are imported from MediaDive's final-volume grams-per-liter conversion.

The preparation text is source supported: pH is adjusted separately for agar plates and liquid medium, the main medium is autoclaved at 115C for 20 min, Solution B is filter-sterilized and added aseptically, and FeCl3 solution is prepared just before use.

## Completeness

The reviewed record is incomplete as a structured recipe because it has no `Solution A`, `Solution B`, `Vitamins mix solution`, or `FeCl3 solution 0.5 g/L` representation. The maintained TOGO `M1101` and `M1102` records were repaired on 2026-09-11 to model those pieces as nested `solutions`, but the reviewed MediaDive owner still has the older flattened import shape.

The exact supplier attributes for `Casamino acids (BD-Difco)` and `Yeast extract (BD-Difco)` are absent from the reviewed record.

Empty optional fields are not defects in this record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Solution A, Solution B, the vitamin mix, and the ferric chloride stock are flattened into top-level stock-strength ingredients. | JCM GRMD 1037 calls for 5 ml Solution A and 8 ml Solution B; GRMD 1036 and GRMD 296 define subordinate stock recipes that the reviewed YAML imports as final top-level `G_PER_L` rows. | `data/normalized_yaml/bacterial/mpycy_agar_medium.yaml` |
| Major | The `Na2HPO4-NaH2PO4 buffer` addition is stored with wrong mass semantics. | MediaDive and JCM model that buffer as a `2 ml` volume row inside 8 ml of Solution B; CultureMech stores `2 G_PER_L`. | `data/normalized_yaml/bacterial/mpycy_agar_medium.yaml` |
| Major | A direct agar duplicate remains separate. | TOGO `M1101` also represents the JCM GRMD 1037 agar variant, and its maintained record already models the stock hierarchy under `solutions`. | `data/normalized_yaml/bacterial/mpycy_agar_medium.yaml`; `data/normalized_yaml/bacterial/TOGO_M1101_MPYCY_Agar_Medium.yaml`; merge de-duplication logic |
| Minor | The exact complex-ingredient suppliers are lost. | JCM GRMD 1037 and MediaDive identify both `Casamino acids` and `Yeast extract` as `BD-Difco`; the reviewed record drops those attributes. | `data/normalized_yaml/bacterial/mpycy_agar_medium.yaml` |
| Minor | The `media_term` CURIE uses a MediaDive-local identifier for a JCM source. | The direct provider is JCM GRMD 1037; `mediadive.medium:J1037` is a MediaDive ID for that JCM page rather than the JCM identifier itself. | `data/normalized_yaml/bacterial/mpycy_agar_medium.yaml` |

## Recommended Edits

1. Replace the flattened Solution A, Solution B, vitamin, and FeCl3 rows in `data/normalized_yaml/bacterial/mpycy_agar_medium.yaml` with the same nested-stock structure already curated in `data/normalized_yaml/bacterial/TOGO_M1101_MPYCY_Agar_Medium.yaml`.
2. Add a cross-source duplicate mapping so the MediaDive `J1037` agar record and TOGO `M1101` collapse to one maintained agar recipe.
3. Preserve TOGO `M1102` as the liquid sibling from the same JCM page instead of merging it with the agar variant.
4. Restore `BD-Difco` on the Casamino acids and yeast extract rows, either in each preferred term or in ingredient notes.
5. Regenerate `data/merge_yaml/merged/mpycy_agar_medium__650fe64d.yaml` and remove the separate stale generated `MPYCY_AGAR_MEDIUM.yaml` direct duplicate through the normal merge pipeline.

## Follow-up Checks

- Re-run open schema validation on the regenerated canonical MPYCY agar merged YAML.
- Re-run `scripts/validate_strict.py` and verify that the TSV remains header-only.
- Re-run `linkml-reference-validator` and `linkml-term-validator` to confirm every retained CHEBI and MediaIngredientMech grounding still resolves.
- Re-fetch JCM GRMD 1037, 1036, and 296 plus MediaDive `J1037`; verify that the canonical agar record has main additives, Solution A, Solution B, vitamin stock, and FeCl3 stock at the proper nesting level.
- Re-fetch TOGO `M1101` and `M1102` and repeat the exact ignored-inclusive search for `GRMD=1037`, `JCM_M1037`, and `JCM_M1037-2` to verify that the agar duplicate is removed while the liquid sibling remains distinct.

## Additional Notes

- The generated TOGO files are stale relative to the 2026-09-11 normalized curation that repaired `TOGO_M1101_MPYCY_Agar_Medium.yaml` and `TOGO_M1102_MPYCY_Agar_Medium.yaml`; they should be regenerated as part of duplicate consolidation.

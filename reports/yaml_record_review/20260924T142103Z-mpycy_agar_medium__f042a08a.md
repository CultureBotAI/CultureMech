# YAML Record Review: mpycy_agar_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mpycy_agar_medium__f042a08a.yaml
- Started UTC: 2026-09-24T14:20:28Z
- Finished UTC: 2026-09-24T14:21:03Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/mpycy_agar_medium__f042a08a.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:007621`
- Label: `mpycy_agar_medium`
- Original label: `MPYCY Agar Medium`
- Category: `bacterial`
- Media source: `TOGO:M1102`, original `JCM_M1037-2`
- Generated status: generated merge output from one normalized source on fingerprint `f042a08a29035d3656e9690c6295efd211c6a9bd3acc3b2dfa88a2b2db8a50a6`
- Maintained owner: `data/normalized_yaml/bacterial/TOGO_M1102_MPYCY_Agar_Medium.yaml`

The generated record is stale relative to its maintained owner: the owner was repaired on 2026-09-11 with nested solutions, pH range, preparation steps, sterilization metadata, and references that are absent from this generated YAML.

## Validation

Validation was run on the generated merged YAML.

- Open LinkML schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mpycy_agar_medium__f042a08a.yaml`
  - Result: passed with `No issues found`.
- Strict validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mpycy_agar_medium__f042a08a.yaml --out /private/tmp/mpycy_agar_medium__f042a08a.strict.tsv --workers 1 --quiet`
  - Result: passed with 0 errors; `/private/tmp/mpycy_agar_medium__f042a08a.strict.tsv` contained only its header row.
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mpycy_agar_medium__f042a08a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 0 reference checks were evaluated.
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mpycy_agar_medium__f042a08a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed after the known `eutils` / `pkg_resources` warning.
- Embedded merge history:
  - Result: not checked. The repository history validator targets standalone `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record is intended to denote TOGO `M1102`, the liquid MPYCY variant extracted from JCM GRMD 1037.

TOGO `M1102` reports `original_media_id: JCM_M1037-2` and the same JCM GRMD 1037 URL used by the agar sibling. It differs from TOGO `M1101` by omitting the optional agar row and by using the source page's liquid-medium pH range.

An exact gitignore-independent search of `data/normalized_yaml` and `data/merge_yaml/merged` found `CultureMech:007621`, `TOGO:M1102`, and `JCM_M1037-2` only in `data/normalized_yaml/bacterial/TOGO_M1102_MPYCY_Agar_Medium.yaml` and this generated output. Ignored files were included. A broader bounded `M1102` search also hits unrelated NBRC and JCM numeric IDs, so bare `M1102` is not a safe identity anchor.

The generated file retains only sodium pyruvate and water groundings. The maintained normalized owner has additional groundings for maltose and all components of Solution A, the vitamin mix, and the FeCl3 solution.

## Evidence

TOGO `M1102` carries the liquid MPYCY main rows from JCM GRMD 1037:

- `Maltose monohydrate`, `0.5 g`
- `Sodium pyruvate`, `0.4 g`
- `Casamino acids (BD-Difco)`, `0.3 g`
- `Yeast extract (BD-Difco)`, `0.3 g`
- `Solution A`, `5 ml`, referenced to TOGO `M1100` / JCM 1036
- `Solution B`, `8 ml`, referenced to TOGO `M1100` / JCM 1036

The generated YAML carries the four non-water main ingredients correctly, but it represents both stock additions as empty placeholder solutions:

| Source row | Generated row | Status |
| --- | --- | --- |
| `5 ml` Solution A | `Unknown solution`, `5 G_PER_L`, empty `composition` | wrong unit and missing stock composition |
| `8 ml` Solution B | `Unknown solution`, `8 G_PER_L`, empty `composition` | wrong unit and missing stock composition |

The 2026-09-11 maintained owner already fixes those rows to `5.0 ML_PER_L` Solution A and `8.0 ML_PER_L` Solution B and expands their source-supported compositions.

## Completeness

The generated file is materially incomplete:

- It has no `ph_range`, while JCM GRMD 1037 specifies 7.4-7.6 for liquid medium.
- It has no preparation steps or sterilization metadata, while JCM GRMD 1037 specifies pH adjustment, autoclaving at 115C for 20 min, and filter sterilization of Solution B.
- It has no structured Solution A, Solution B, vitamin mix, or FeCl3 stock composition.
- It has no references to TOGO `M1100`, JCM GRMD 1036, TOGO `M290`, or JCM GRMD 296.

Those gaps are already corrected in `data/normalized_yaml/bacterial/TOGO_M1102_MPYCY_Agar_Medium.yaml`; the generated merge product needs to be regenerated.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated YAML is stale relative to the 2026-09-11 repaired normalized owner. | The owner has nested `solutions`, `ph_range`, `preparation_steps`, `sterilization`, `data_quality_flags`, and `references`; the generated output lacks all of those newer fields. | Generated merge pipeline |
| Major | Solution A and Solution B are represented as empty `Unknown solution` rows with `G_PER_L` units. | TOGO/JCM specify `5 ml` Solution A and `8 ml` Solution B; the generated rows have empty compositions and concentrations of `5 G_PER_L` and `8 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1102_MPYCY_Agar_Medium.yaml`; generated merge pipeline |
| Minor | The generated file drops the liquid pH range and preparation semantics. | JCM GRMD 1037 distinguishes liquid pH 7.4-7.6 from agar pH 7.6-7.8 and says to autoclave at 115C for 20 min and filter-sterilize Solution B. | Generated merge pipeline |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/mpycy_agar_medium__f042a08a.yaml` from `data/normalized_yaml/bacterial/TOGO_M1102_MPYCY_Agar_Medium.yaml`.
2. Confirm the regenerated liquid record includes Solution A, Solution B, Vitamins mix solution, FeCl3 solution, liquid `ph_range: 7.4-7.6`, sterilization metadata, and all six references currently present in the maintained owner.
3. Keep this TOGO `M1102` liquid record separate from the TOGO `M1101` agar record and from the MediaDive `J1037` agar duplicate.
4. If the merge pipeline cannot preserve nested solutions from normalized records, repair the merge/import logic rather than editing generated YAML by hand.

## Follow-up Checks

- Re-run open schema validation on the regenerated liquid MPYCY merged YAML.
- Re-run `scripts/validate_strict.py` and verify that the TSV remains header-only.
- Re-run `linkml-reference-validator` and `linkml-term-validator` to confirm the references and nested solution groundings resolve.
- Compare the regenerated output byte-for-field against `data/normalized_yaml/bacterial/TOGO_M1102_MPYCY_Agar_Medium.yaml` to confirm the 2026-09-11 repair is no longer lost.
- Re-fetch TOGO `M1102`, JCM GRMD 1037, JCM GRMD 1036, and JCM GRMD 296 if any further MPYCY stock fields are edited.

## Additional Notes

- The generated file's `name` and `original_name` still say `mpycy_agar_medium` even though TOGO `M1102` represents the no-agar liquid sibling. This was preserved by the 2026-09-11 normalized repair, so renaming was treated as out of scope for this generated-output review.

# YAML Record Review: Desulfovibrio Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_medium__7feaf544.yaml`
- Started UTC: 2026-09-22T20:41:55Z
- Finished UTC: 2026-09-22T20:42:48Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:009765` for `desulfovibrio_medium__7feaf544`, a TOGO import of JCM Medium 389 through TOGO M384.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, exit 0 with a header-only TSV and 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target is grounded to `TOGO:M384`, and the original source note identifies `JCM_M389` at JCM GRMD 389. A gitignore-independent search for exact M384/J389 context found the reviewed TOGO M384 file, the MediaDive J389 duplicate `data/normalized_yaml/bacterial/desulfovibrio_medium.yaml`, and related wrapper/variant media that reference JCM Medium 389.

The generated record is stale. Its normalized source, `data/normalized_yaml/bacterial/TOGO_M384_Desulfovibrio_Medium.yaml`, has September 2026 exact-source repairs that are absent from this August 2026 generated YAML.

## Evidence

TOGO M384 and direct JCM GRMD 389 agree on the printed formulation: 1 L distilled water, 2 g magnesium sulfate heptahydrate, 1 g yeast extract, 0.1 g calcium chloride dihydrate, 1 g ammonium chloride, 0.5 g dipotassium phosphate, 0.5 mg resazurin, 0.5 g ferrous sulfate heptahydrate, 1 g sodium sulfate, 2 g sodium lactate, 0.1 g ascorbic acid, and 0.1 g sodium thioglycolate.

JCM 389 uses FeSO4, sodium thioglycolate, and ascorbic acid as delayed additions dissolved in small water aliquots, then adjusts with NaOH and handles the medium under nitrogen.

## Completeness

The generated record contains the right main chemical list, but two source units are wrong and two process reagents were promoted into variable ingredients.

The current normalized TOGO M384 record has already repaired the same surface: it stores resazurin as 0.5 `MG_PER_L`, water as 1.0 `L`, removes NaOH and N2 from the ingredients, adds `ph_range` 6.8-7.0, adds curated references, and splits the single long JCM preparation comment into ordered steps.

## Findings

- High: Resazurin was converted from 0.5 mg/L to 0.5 G/L in the generated record.
- Medium: The 1 L distilled-water row was copied as 1 `G_PER_L`; the repaired normalized record stores it as 1.0 `L`.
- Medium: NaOH and N2 were promoted to variable top-level ingredients even though the JCM source uses NaOH only for pH adjustment and N2 only as the gas stream for anoxic handling.
- Medium: The generated record lacks the curated pH range 6.8-7.0 and the six ordered preparation steps already present in the normalized source.
- Medium: JCM Medium 389 provider paths are not reconciled in generated output: this TOGO M384 record generates separately while the MediaDive J389 `desulfovibrio_medium.yaml` import is merged into `MODIFIED_DESULFOVIBRIO_MEDIUM.yaml`.

## Recommended Edits

- Regenerate `data/merge_yaml/merged` from the current `data/normalized_yaml/bacterial/TOGO_M384_Desulfovibrio_Medium.yaml` so the fixed units, `ph_range`, references, and split preparation steps reach generated output.
- Reconcile the MediaDive J389 and TOGO M384 provider records so exact JCM 389 duplicates merge or are explicitly related as exact source duplicates.
- Re-check JCM 389 wrapper children, especially Modified Desulfovibrio Medium and Desulfovibrio Marine Medium, after the parent duplicate is repaired.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Confirm the regenerated M384 record has no NaOH or N2 ingredient rows, keeps resazurin at 0.5 mg/L, and keeps distilled water as 1.0 L.
- Confirm the generated JCM 389 and JCM 834 records no longer mix base Desulfovibrio Medium with Modified Desulfovibrio Medium.

## Additional Notes

None found.

# YAML Record Review: HD-MEDIUM, 1:10 diluted, modified
- Repository: CultureMech
- Record: data/merge_yaml/merged/hd_medium_1_10_diluted_modified.yaml
- Started UTC: 2026-09-23T11:38:33Z
- Finished UTC: 2026-09-23T11:40:35Z
- Verdict: needs curation

## Target

Reviewed the generated KOMODO ModelSEED 1135 branch for DSMZ Medium 1135, `HD-MEDIUM, 1:10 diluted, modified`, at `data/merge_yaml/merged/hd_medium_1_10_diluted_modified.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hd_medium_1_10_diluted_modified.strict.tsv`.
- Reference validation: passed.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record carries `CultureMech:003844`, the name `hd_medium_1_10_diluted_modified`, and a `komodo.medium:1135` media term for `HD-MEDIUM, 1:10 diluted, modified`. The source notes explicitly say the composition was copied from DSMZ Medium 1135, and the source PDF and MediaDive record both resolve that identifier to the same modified 1:10 HD medium at pH 5.5.

The generated set also has a separate direct DSMZ/MediaDive branch, `data/merge_yaml/merged/hd_medium_1_10_diluted_modified__33364d2d.yaml`, for the same DSMZ Medium 1135 recipe. This KOMODO branch is therefore still source-duplicated rather than merged with the direct DSMZ import.

## Evidence

MediaDive 1135 and the DSMZ PDF list Solution A with casein peptone 0.50 g, glucose 0.10 g, yeast extract 0.25 g, MES 1.95 g, either 1000 ml double-distilled water for liquid medium or 500 ml double-distilled water for solid medium, and a Solution B with 1.5% washed agar in 500 ml double-distilled water. They also state that the recipe is adjusted to pH 5.5 with NaOH/HCl, sterilized separately, and that Solution A and Solution B are combined at 50 C for solid medium.

The generated record instead has a single unconditional water ingredient with `value: '2000.0'`, `unit: G_PER_L`, and a merge note for `1000.0, 500.0, 500.0`. It also has unconditional `Agar` at 15 g/L, adds `NaOH` as a variable ingredient because it was extracted from the KOMODO pH buffer note, omits HCl, and has no `preparation_steps`.

## Completeness

The major solute amounts and pH are present, but the record loses the alternative liquid and solid scopes that make the water volumes meaningful. It also omits the source preparation text for separate sterilization, post-cooling combination at 50 C, and incubation at 20 C for 4 days.

## Findings

- The three DSMZ water rows for distinct liquid and solid branches were deduplicated into one `2000.0 G_PER_L` ingredient. That is not a physical concentration for either medium: the liquid recipe uses 1000 ml in Solution A, while the solid recipe uses 500 ml in Solution A plus 500 ml in Solution B.
- The solid Solution B was flattened into top-level `Agar` without preserving that the agar branch applies only to solid medium.
- `NaOH` is represented as a variable recipe ingredient while `HCl` is absent, even though the source only names NaOH/HCl as pH-adjustment reagents.
- DSMZ preparation instructions copied into the direct import branch are absent from this KOMODO-derived branch.
- The KOMODO and DSMZ branches for the same DSMZ Medium 1135 recipe were left as separate generated records.

## Recommended Edits

- Preserve DSMZ 1135's liquid and solid alternatives instead of summing the `Double distilled water` rows across mutually exclusive scopes.
- Keep Solution B and agar scoped to the solid-medium branch.
- Encode the pH 5.5 adjustment as a preparation action using NaOH/HCl rather than as an unconditional `NaOH` ingredient.
- Carry over the DSMZ preparation instructions for separate sterilization and Solution A/Solution B combination at 50 C.
- Merge or alias the KOMODO and direct DSMZ branches so that the generated output has one curated representation of DSMZ Medium 1135.

## Follow-up Checks

- Re-run generated-record validation after import fixes to ensure the corrected branch-aware recipe still passes open schema, strict, reference, and term validation.
- Diff this KOMODO branch against `hd_medium_1_10_diluted_modified__33364d2d` after regeneration to confirm the source duplicate has been removed.

## Additional Notes

None.

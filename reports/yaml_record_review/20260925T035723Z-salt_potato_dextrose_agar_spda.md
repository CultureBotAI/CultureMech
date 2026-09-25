# YAML Record Review: salt_potato_dextrose_agar_spda

- Repository: CultureMech
- Record: data/merge_yaml/merged/salt_potato_dextrose_agar_spda.yaml
- Started UTC: 2026-09-25T03:57:23Z
- Finished UTC: 2026-09-25T03:57:23Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:010350`, `salt_potato_dextrose_agar_spda`, from `data/merge_yaml/merged/salt_potato_dextrose_agar_spda.yaml`.

The record is a single-source TOGO M929 import with JCM_M888 listed as TOGO's original source.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to TOGO M929, `Salt Potato-Dextrose Agar (SPDA)`.

The live JCM `GRMD=888` page currently returns "Nothing found", so the original JCM_M888 formulation was not independently confirmed during this review.

## Evidence

TOGO M929 lists 1 L distilled water, 20 g NaCl, 10 g glucose, 15 g agar, and 200 g peeled and cut potato.

TOGO preserves a preparation comment to boil the potatoes for 20 min, strain through a fine sieve, add glucose, NaCl, and agar, boil until dissolved, avoid using new potatoes, and adjust pH to 5.4-5.6.

TOGO also notes that commercial potato dextrose agar supplemented with NaCl can be used.

## Completeness

The five source ingredient rows are present.

The pH 5.4-5.6 range, potato-extraction instructions, and commercial-substitution comment are absent from the generated record.

## Findings

The generated record treats `Potato, peeled and cut` as a direct 200 g/L ingredient, but the source uses the potato as an extraction substrate that must be boiled and strained before glucose, NaCl, and agar are dissolved.

The generated record drops the 5.4-5.6 pH adjustment.

The generated record drops the source note that commercial potato dextrose agar supplemented with NaCl can be used.

The TOGO 1 L distilled-water row is represented as `1 G_PER_L`, which preserves the row but not the source volume unit.

## Recommended Edits

Add preparation steps for boiling 200 g peeled and cut potato, straining the infusion, dissolving glucose, NaCl, and agar, and adjusting pH to 5.4-5.6.

Represent the source potato row as the input to a potato extract or infusion rather than as a direct final-medium solute.

Preserve the commercial potato dextrose agar substitution as a note.

## Follow-up Checks

After regeneration, confirm `salt_potato_dextrose_agar_spda` carries the pH 5.4-5.6 adjustment and a potato-infusion preparation step.

Recheck the JCM_M888 source URL later; if JCM restores that page, compare it against TOGO M929.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.

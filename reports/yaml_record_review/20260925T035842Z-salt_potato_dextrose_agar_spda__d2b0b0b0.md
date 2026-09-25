# YAML Record Review: salt_potato_dextrose_agar_spda__d2b0b0b0

- Repository: CultureMech
- Record: data/merge_yaml/merged/salt_potato_dextrose_agar_spda__d2b0b0b0.yaml
- Started UTC: 2026-09-25T03:58:42Z
- Finished UTC: 2026-09-25T03:58:42Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:003236`, `salt_potato_dextrose_agar_spda`, from `data/merge_yaml/merged/salt_potato_dextrose_agar_spda__d2b0b0b0.yaml`.

The record is a single-source MediaDive/JCM J888 import for `SALT POTATO-DEXTROSE AGAR (SPDA)`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to JCM Medium J888 via MediaDive.

The live JCM `GRMD=888` page currently returns "Nothing found", but MediaDive J888 and TOGO M929 both retain JCM 888 / JCM_M888 provenance for the same Salt Potato-Dextrose Agar formulation.

## Evidence

MediaDive J888 lists 200 g peeled and cut potato, 10 g glucose, 20 g NaCl, 15 g agar, and 1000 ml distilled water.

MediaDive also preserves the source instructions to boil potatoes for 20 min, strain through a fine sieve, add glucose, NaCl, and agar, boil until dissolved, avoid using new potatoes, and adjust pH to 5.4-5.6.

The source comment notes that commercial potato dextrose agar supplemented with NaCl can be used.

## Completeness

The non-water ingredient rows, pH 5.5 value, potato-extraction instructions, and commercial-substitution note are present.

The 1000 ml distilled-water row is absent.

## Findings

The direct MediaDive generated record is a duplicate split from the TOGO M929 `salt_potato_dextrose_agar_spda` record. Both preserve the same JCM_M888/JCM J888 source identity and the same NaCl, glucose, agar, and potato formula.

The generated record still treats `Potato` as a direct 200 g/L ingredient. The preparation text makes the recipe usable, but the 200 g potato is an extraction substrate for a boiled and strained infusion rather than a final solute.

The water row from MediaDive is absent.

## Recommended Edits

Regenerate the TOGO and MediaDive imports with matching pH, water, and potato-infusion semantics so the two SPDA source paths collapse into one generated record with both `TOGO:M929` and `mediadive.medium:J888` provenance.

Represent the potato row as an input to an infusion or extract rather than a direct final-medium solute.

Preserve the commercial potato dextrose agar substitution note after merging.

## Follow-up Checks

After regeneration, confirm only one generated `salt_potato_dextrose_agar_spda` record remains.

Confirm the surviving generated record has the 5.4-5.6 pH adjustment, the boil/strain potato-infusion instructions, and both TOGO M929 and JCM J888 source identifiers.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.

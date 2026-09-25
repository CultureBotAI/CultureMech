# YAML Record Review: acidic_diluted_asm_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml`
- Started UTC: 2026-09-21T08:54:42Z
- Finished UTC: 2026-09-21T08:56:47Z
- Verdict: needs curation

## Target

Generated merge record `ACIDIC_DILUTED_ASM_MEDIUM.yaml` is a singleton merge from `data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml`. It represents TOGO M850, whose original source is JCM Medium 815 / ACIDIC DILUTED ASM MEDIUM.

## Validation

- PASS: open LinkML schema validation with `linkml-validate`.
- PASS: strict schema layer validation with `scripts/validate_strict.py`.
- PASS: linkml-reference-validator on this generated record.
- PASS: linkml-term-validator on this generated record.
- Not checked: embedded `MediaRecipe.curation_history` entries; no focused generated-record history validator is documented, and `just validate-history` targets standalone `history/` files.

## Identity and Grounding

The TOGO M850 identity is correct but split from the direct JCM 815 import. TOGO M850 reports `original_media_id: JCM_M815`, points at the same `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815` source page, and snapshots the same ACIDIC DILUTED ASM MEDIUM recipe that is imported directly as `data/normalized_yaml/bacterial/acidic_diluted_asm_medium.yaml` / `mediadive.medium:J815`.

The related DILUTED ASM MEDIUM records are not duplicates of this target. JCM 816 and TOGO M851 are pH variants that prepare Acidic Diluted ASM Medium from JCM 815 and then adjust to pH 6.7, so they are correctly represented as child media rather than merged into the acidic parent.

## Evidence

- Primary JCM source `GRMD=815`: source page fetched from JCM during review. It lists a basal recipe with NH4Cl, MgSO4.7H2O, CaCl2.2H2O, 0.1 ml trace element solution, 0.1 ml iron stock solution, and 1 L distilled water; a 2.0 ml phosphate buffer stock post-autoclave addition; pH adjustment to 3.0 with sterile 1 N HCl; 100 ml filter-sterilized methane gas in each sealed bottle headspace; and three separate 1 L stock solutions for trace elements, iron, and phosphate buffer.
- TOGO source M850: API record fetched during review. Its metadata identifies `JCM_M815`, `GRMD=815`, and pH 3.0, and its component blocks preserve separate basal, phosphate-buffer, trace-element, and iron-stock sections before CultureMech normalization flattens them.
- Local ignored-inclusive exact source-ID search: found one normalized direct JCM source for exact `mediadive.medium:J815`, one normalized TOGO source for exact `TOGO:M850`, and two separate generated outputs, `acidic_diluted_asm_medium__1cac1e6e.yaml` and `ACIDIC_DILUTED_ASM_MEDIUM.yaml`.

## Completeness

The generated target is not complete enough for use. It has no `ph_value`, no `preparation_steps`, and no methane headspace instruction even though upstream JCM and TOGO both say the completed medium is adjusted to pH 3.0 with sterile 1 N HCl and dispensed under 100 ml methane gas in 120 ml serum bottles.

It also does not preserve stock-solution boundaries. The target leaves the `Trace element solution` and `Iron stock solution` entries as empty `solutions`, keeps all trace/iron stock constituents as if they were final medium ingredients at full stock strength, and carries `Phosphate buffer stock solution` as an empty 2 `G_PER_L` solution while also lifting KH2PO4 and Na2HPO4.2H2O to final top-level ingredients.

## Findings

- CRITICAL: The TOGO M850 normalized source flattened three stock solutions into final ingredients. JCM 815 calls for only 0.1 ml of trace element solution, 0.1 ml of iron stock solution, and 2.0 ml of phosphate buffer stock per medium preparation; the generated record instead exposes stock-solution formula concentrations such as 0.4 `G_PER_L` ZnSO4.7H2O, 4.5 `G_PER_L` EDTA.Fe(III), 37.425 `G_PER_L` KH2PO4, and 48.95 `G_PER_L` Na2HPO4.2H2O as final medium rows.
- MAJOR: The main source duplicate is split. TOGO M850 and the direct JCM J815 import are the same `GRMD=815` recipe, but they generated separate records because TOGO introduced variable HCl/methane ingredient rows, empty stock-solution shells, water rows, and flattened stock solutes.
- MAJOR: The generated target drops pH 3.0 and both preparation steps. HCl and methane are kept as variable top-level ingredients, but the generated record no longer says that 1 N HCl is a sterile pH adjustment and methane gas is a 100 ml headspace addition after the 20 ml aliquots are sealed.
- MAJOR: Water handling is arithmetically invalid after merge generation. The TOGO normalized source had already collapsed four identical `Distilled water 1 L` rows to one malformed `1.0 G_PER_L` row; the generated singleton re-expanded the curation note into `4.0 G_PER_L`, summing the water rows from the basal recipe and three stock solutions.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml` from the source component hierarchy: keep NH4Cl, MgSO4.7H2O, CaCl2.2H2O, and water in the basal recipe; represent trace element, iron, and phosphate buffer stocks as `solutions` with `ML_PER_L` additions of 0.1, 0.1, and 2.0 respectively; and move each stock formula into the corresponding solution `composition`.
- Restore source-level conditions from TOGO/JCM: `ph_value: 3.0`, a sterile 1 N HCl pH-adjustment instruction, the 20 ml serum-bottle dispensing instruction, and the 100 ml filter-sterilized methane headspace addition.
- Normalize the direct `data/normalized_yaml/bacterial/acidic_diluted_asm_medium.yaml` source to the same stock-preserving representation, then regenerate merged YAML so `TOGO_M850_Acidic_Diluted_ASM_Medium` and `acidic_diluted_asm_medium` produce one source-duplicate merge for JCM 815.
- Keep `diluted_asm_medium` / JCM 816 and `TOGO_M851_Diluted_ASM_Medium` as pH-variant children that consume the curated Acidic Diluted ASM parent and adjust it to pH 6.7.

## Follow-up Checks

- After regeneration, confirm exact `TOGO:M850` and exact `mediadive.medium:J815` occur in one generated JCM 815 record rather than two split `acidic_diluted_asm_medium` records.
- Confirm the regenerated JCM 815 parent still has reciprocal `PH_VARIANT` links to the JCM 816 / TOGO M851 Diluted ASM Medium children.
- Re-run schema, strict, reference, and term validation on both corrected JCM 815 normalized inputs and the generated merge record.

## Additional Notes

Several hydrate groundings in the TOGO import are less specific than their labels, including CoCl2.6H2O grounded to generic cobalt dichloride, NiCl2.6H2O grounded to generic nickel dichloride, and Na2HPO4.2H2O grounded to generic disodium hydrogen phosphate. The stock-boundary errors dominate this review, but the hydrate terms should be refreshed after the formula hierarchy is corrected.

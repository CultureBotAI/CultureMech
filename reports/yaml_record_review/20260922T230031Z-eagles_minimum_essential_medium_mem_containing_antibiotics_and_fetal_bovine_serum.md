# YAML Record Review: eagles_minimum_essential_medium_mem_containing_antibiotics_and_fetal_bovine_serum

- Repository: CultureMech
- Record: data/merge_yaml/merged/eagles_minimum_essential_medium_mem_containing_antibiotics_and_fetal_bovine_serum.yaml
- Started UTC: 2026-09-22T22:57:22Z
- Finished UTC: 2026-09-22T23:00:31Z
- Verdict: needs curation

## Target

Generated TOGO M2847 record `CultureMech:009389`, named `eagles_minimum_essential_medium_mem_containing_antibiotics_and_fetal_bovine_serum`.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation against `scripts/validate_strict.py`: passed with 0 error rows.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the focused history validator targets standalone files under `history/`, not inline `MediaRecipe.curation_history` entries.

## Identity and Grounding

The record accurately carries the TOGO M2847 identity and title, but that title is literature-prose rather than a stable commercial recipe name. The Togo payload has no upstream `src_url`; the embedded source sentence comes from Ohashi et al., "Demonstration of Antigenic and Genotypic Variation in Orientia tsutsugamushi Which Were Isolated in Japan, and Their Classification into Type and Subtype", Microbiology and Immunology 40(9), 627-638, 1996.

The biological context also needs a curator decision. The source used this Eagle's MEM mixture to homogenize mite pools before inoculating the homogenate onto L929 monolayers for Orientia tsutsugamushi isolation; that is not a normal free-living bacterial culture-medium recipe.

Amphotericin B and penicillin are grounded, streptomycin is grounded in the normalized source but lost its primary `term` in the generated record, and the Eagle's MEM commercial base plus fetal bovine serum are not grounded to chemical terms, which is acceptable for those complex products.

## Evidence

Togo's M2847 payload and the source article sentence specify a small amount of Eagle's minimum essential medium from Nissui containing 20 ug/ml amphotericin B, 100 units/ml penicillin, 150 ug/ml streptomycin, and 2% fetal bovine serum.

The generated YAML instead records fetal bovine serum as `2 PERCENT_W_V`, streptomycin as `150 G_PER_L`, amphotericin B as `20 G_PER_L`, Eagle's MEM as `1 G_PER_L`, and penicillin as `VARIABLE`.

## Completeness

The ingredient list has all five named components, but only fetal bovine serum has the correct magnitude. Two antibiotic units are wrong by a factor of 1000, the penicillin activity concentration from the source sentence is missing, the base MEM is modeled as a gram-per-litre ingredient instead of the 1 L carrier medium, and the percentage basis for fetal bovine serum is ambiguous.

No target organism or source article metadata is preserved in the record. If this medium remains in scope, the relevant bacterium is O. tsutsugamushi and the host-cell workflow should be noted because L929 cells, not an axenic bacterial culture, were inoculated.

## Findings

- Streptomycin was imported as `150 G_PER_L` instead of 150 ug/ml, equivalent to 0.150 g/L.
- Amphotericin B was imported as `20 G_PER_L` instead of 20 ug/ml, equivalent to 0.020 g/L.
- Penicillin was defaulted to `VARIABLE` even though the source sentence gives 100 units/ml.
- `fetal bovine serum 2%` was coerced to `PERCENT_W_V`; serum percentages in mammalian-cell media are volume fractions unless the source says otherwise.
- `Eagle's minimum essential medium (MEM) (Nissui Co., Tokyo)` is represented as `1 G_PER_L`, but the source says the antibiotics and serum were contained in Eagle's MEM and does not give a dry-mass recipe.
- The record lacks the Ohashi et al. article citation and target context needed to explain why a mammalian-cell MEM mixture appears in a bacterial medium collection.

## Recommended Edits

- Decide whether Togo M2847 is in scope for CultureMech; if retained, mark it as a host-cell isolation medium for O. tsutsugamushi rather than as a generic bacterial liquid medium.
- Convert streptomycin and amphotericin B from `ug/ml` to valid low-mass concentrations or add direct unit support for micrograms per millilitre.
- Preserve penicillin as 100 units/ml with an activity unit instead of a variable concentration.
- Represent Eagle's MEM as the 1 L base medium and fetal bovine serum as 2% volume/volume if the schema can carry it.
- Add a citation or structured source note for the 1996 Microbiology and Immunology article instead of relying only on TOGO's source-less M2847 page.
- Preserve the normalized source's streptomycin grounding through merge generation.

## Follow-up Checks

- Re-run open, strict, reference, and term validators after recuration.
- Compare the rebuilt record against Togo M2847 and the source article sentence listing amphotericin B, penicillin, streptomycin, and fetal bovine serum.
- Search with ignored files included for stale `150 G_PER_L`, `20 G_PER_L`, and defaulted `penicillin` values after rebuilding TOGO records with `ug/ml` and `units/ml`.

## Additional Notes

An ignored-inclusive local search for `M2847`, `100  units/ml`, `ampho-tericin`, and the long Eagle's MEM sentence found generated/index references to M2847 but no local copy of the underlying source article text.

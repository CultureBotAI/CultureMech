# YAML Record Review: peptone_corn_agar__00aba887

- Repository: CultureMech
- Record: data/merge_yaml/merged/peptone_corn_agar__00aba887.yaml
- Started UTC: 2026-09-24T20:21:19Z
- Finished UTC: 2026-09-24T20:21:19Z
- Verdict: needs curation

## Target

Generated bacterial MediaRecipe `CultureMech:002840`, `peptone_corn_agar`, from the maintained direct JCM/MediaDive owner `data/normalized_yaml/bacterial/peptone_corn_agar.yaml`.

The record represents JCM medium 48 / MediaDive medium J48, PEPTONE CORN AGAR. The generated recipe has 5 g/L corn steep liquor, 5 g/L peptone, 10 g/L starch, 5 g/L NaCl, 0.5 g/L CaCl2 x 2 H2O, 16 g/L agar, pH 7.2, a `mediadive.medium:J48` media term, and the source preparation note that corn steep liquor powder may be substituted.

## Validation

- Open LinkML validation: Passed; exited 0 with no issues.
- Strict validator: Passed; `/private/tmp/peptone_corn_agar__00aba887.strict.tsv` was header-only, so there were 0 strict errors.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The direct JCM/MediaDive identity is internally consistent: the record is grounded as `mediadive.medium:J48` and has no strain-specific variant suffix or mixed source identity.

An exact ignored-inclusive search found a second generated JCM 48 recipe at `data/merge_yaml/merged/PEPTONE_CORN_AGAR.yaml`, derived from `data/normalized_yaml/bacterial/TOGO_M40_Peptone_Corn_Agar.yaml`. That sibling is TOGO M40 and names JCM `JCM_M48` / `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=48`, so it is the same source recipe as this direct MediaDive/JCM record rather than a distinct Peptone Corn Agar.

## Evidence

MediaDive J48 and the JCM GRMD 48 page support the target source identity, pH 7.2, and direct ingredients in the generated record.

TOGO M40 also traces to JCM GRMD 48 and supports the same formulation as the direct JCM/MediaDive record. Its maintained owner currently contributes the split generated sibling with a water row encoded as `1 G_PER_L`.

The ingredient ontology treatment in this generated record is mostly appropriate. `Agar` is source text without a commercial product qualifier in JCM 48 and can be grounded to `CHEBI:2509`; `NaCl`, `CaCl2 x 2 H2O`, and `Starch` are straightforward. Corn steep liquor and the Oxoid peptone are appropriately left ungrounded as undefined or commercial complex ingredients.

## Completeness

The generated direct record preserves the direct solid components, pH, source note, and source grounding, but it omits the 1 L distilled water row from JCM 48.

Completeness is also affected across the generated set because the same JCM 48 formulation appears twice: this direct MediaDive/JCM generated record without water, and the TOGO M40 generated sibling with water imported as `1 G_PER_L`.

## Findings

1. Needs curation: `data/normalized_yaml/bacterial/peptone_corn_agar.yaml` and this generated record omit the 1 L distilled water row from JCM 48.
2. Needs curation: the JCM 48 recipe is split across two generated records. `data/merge_yaml/merged/PEPTONE_CORN_AGAR.yaml` is the TOGO M40 copy of the same JCM GRMD 48 source recipe, but its maintained owner encodes the source's water as `1 G_PER_L`; that unit/scaling error prevents a clean source-duplicate merge with the direct JCM/MediaDive owner.

## Recommended Edits

1. Add the source 1 L distilled water component to `data/normalized_yaml/bacterial/peptone_corn_agar.yaml` with a volume unit rather than a grams-per-liter unit.
2. Repair `data/normalized_yaml/bacterial/TOGO_M40_Peptone_Corn_Agar.yaml` so `Distilled water` represents 1000 ml for the source recipe, not `1 G_PER_L`.
3. Regenerate merged YAML so the JCM/MediaDive J48 and TOGO M40 owners merge into one generated source-duplicate record.

## Follow-up Checks

1. Re-run open, strict, reference, and term validation on the repaired maintained owners and regenerated merged record.
2. Repeat an exact ignored-inclusive search for `mediadive.medium:J48`, `GRMD=48`, and `TOGO:M40` after regeneration to verify JCM 48 is represented once in `data/merge_yaml/merged/`.

## Additional Notes

The exact ignored-inclusive duplicate search covered `data`, `src`, and `scripts` for `mediadive.medium:J48`, `GRMD=48`, `CultureMech:002840`, and `TOGO_M40_Peptone_Corn_Agar`.

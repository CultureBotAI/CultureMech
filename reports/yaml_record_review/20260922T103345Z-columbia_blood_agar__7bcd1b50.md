# YAML Record Review: Columbia Blood Agar

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_blood_agar__7bcd1b50.yaml`
- Started UTC: `2026-09-22T10:31:15Z`
- Finished UTC: `2026-09-22T10:33:45Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:008948` for TOGO Medium `M2362`, `Columbia Blood Agar`, generated from `data/normalized_yaml/bacterial/TOGO_M2362_Columbia_Blood_Agar.yaml` on merge fingerprint `7bcd1b507f8bd3301688c1d0286cae84a094f3403ef47c73ea00ccf0c53ff295`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/columbia_blood_agar__7bcd1b50.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The source identity is correct: TOGO `M2362` points to DSMZ Medium 429, `COLUMBIA BLOOD AGAR`.

The generated record correctly preserves the source formulation boundary as Columbia agar base supplemented with horse blood. Keeping `Columbia agar base` unexpanded is appropriate because DSMZ 429 does not spell out that base composition in the 429 section.

An ignored-inclusive generated-record search found multiple related Columbia blood agar branches, including three `columbia_blood_agar__*.yaml` generated records and several blood-source variants. The search included ignored files.

## Evidence

The TOGO M2362 API and the DSMZ 429 PDF both support the same short formula: Columbia agar base supplemented with 4% horse blood. The DSMZ note about rehydrating freeze-dried pellets in media 545, 215, or 1 describes optional liquid rehydration media and is not part of the agar composition.

The generated branch encodes `4% horse blood` as an ingredient name with `VARIABLE` concentration, instead of using the TOGO `conc_value: 4` and `conc_unit: %` fields as a structured horse-blood supplement.

## Completeness

The generated record is stale relative to the maintained normalized input. `data/normalized_yaml/bacterial/TOGO_M2362_Columbia_Blood_Agar.yaml` now has `Columbia agar base`, `Defibrinated horse blood` at `4 PERCENT_V_V`, a mix preparation step, TOGO/DSMZ references, curation flags, and a source-duplicate relation to the direct MediaDive `columbia_blood_agar.yaml` parent.

No target organism or growth evidence is present. That is an empty optional area in this source-only branch.

## Findings

- Major: 4% horse blood is present only inside `preferred_term: 4% horse blood`; the structured concentration is still a schema-defaulted `VARIABLE`.
- Major: the generated record predates the repaired normalized input and is missing the source-duplicate parent link to the direct DSMZ/MediaDive Columbia blood agar branch.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/TOGO_M2362_Columbia_Blood_Agar.yaml` so the generated branch carries `Defibrinated horse blood` with `4 PERCENT_V_V`, explicit source references, the mix step, and the source-duplicate relation.
- Confirm the regeneration does not import DSMZ Medium 429's rehydration media 545, 215, or 1 as Columbia blood agar ingredients.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm the horse blood row has a structured `4 PERCENT_V_V` concentration and no percentage embedded only in the ingredient label.
- Confirm `Columbia agar base` remains unexpanded unless a source-specific base composition is added.
- Confirm the repaired branch links to the direct DSMZ/MediaDive Columbia blood agar parent as a source duplicate.

## Additional Notes

Empty optional fields are not defects.

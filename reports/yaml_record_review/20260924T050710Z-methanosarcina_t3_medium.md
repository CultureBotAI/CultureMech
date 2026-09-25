# YAML Record Review: methanosarcina_t3_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanosarcina_t3_medium.yaml
- Started UTC: 2026-09-24T05:07:10Z
- Finished UTC: 2026-09-24T05:07:10Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:015871` for JCM medium 1462, "METHANOSARCINA T3 MEDIUM".

## Validation

- LinkML open schema validation: Passed with "No issues found".
- Strict recipe validation: Passed; `/private/tmp/methanosarcina_t3_medium.strict.tsv` contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

- The record identity is correctly grounded to JCM GRMD 1462, and the live JCM page still serves "METHANOSARCINA T3 MEDIUM".
- The parent salts, 9.0 g NaCl value, solution-addition rows, post-autoclave addition rows, pH 6.5 preparation target, and reducing-agent rows match the JCM source.
- The local `Ni-Se-W solution (see below)` table from JCM 1462 is flattened into the parent ingredient list instead of remaining attached to the 10 ml stock addition.
- The JCM 151 and JCM 197 references are left as unlinked preferred-term text.

## Evidence

- JCM 1462 lists a parent recipe containing 10 ml Trace mineral solution from Medium 151, 10 ml Ni-Se-W solution defined later on the same page, 2 mg ferrous ammonium sulfate hexahydrate, 980 ml water, and the same main salts shown in the YAML.
- JCM 1462 lists post-autoclave additions of 10 ml Trace vitamins from Medium 197, 35 ml 2 M trimethylammonium chloride solution, 5 ml methanol, 10 ml 5% L-Cysteine HCl H2O solution, and 10 ml 5% Na2S x 9 H2O solution.
- The local Ni-Se-W stock table contains 30.0 mg NiCl2 x 6 H2O, 0.3 mg Na2SeO3 x 5 H2O, 0.4 mg Na2WO2 x 2 H2O, and 1.0 L distilled water; those four rows are present as parent ingredients after `5% Na2S x 9 H2O solution`.
- Medium 151 and Medium 197 pages still resolve and define reusable stock media, but the generated record only preserves their IDs inside free-text preferred terms.

## Completeness

- The main JCM 1462 formula is mostly present.
- The local Ni-Se-W stock boundary is missing.
- The Medium 151 and Medium 197 cross-references are not structured.
- The JCM default autoclave condition from the page header is not represented, though the record does preserve that the base is autoclaved before overnight standing.

## Findings

1. Major - The local Ni-Se-W stock is flattened into the parent ingredient list. JCM 1462 adds 10 ml/l of `Ni-Se-W solution (see below)`, but the generated record exposes nickel, selenite, tungsten, and the stock water as separate parent ingredients.
2. Major - The Ni-Se-W stock water row has a corrupted concentration. Source stock water is `1.0 L`; the generated row says `1.0 ML_PER_L` on the parent formula.
3. Major - Cross-medium stock references are unstructured. The 10 ml Medium 151 trace-mineral addition and 10 ml Medium 197 trace-vitamin addition remain as raw preferred-term strings and are not linked to the referenced JCM media or expanded as child stock recipes.
4. Minor - The generated `preparation_steps` conflate the post-autoclave additions with the final pH adjustment in one step and do not identify which listed solution rows are the "following solutions" referenced by the source.
5. Minor - The local tungsten row lacks a chemical grounding, leaving `Na2WO2 x 2 H2O` as ungrounded source text.

## Recommended Edits

- Move the Ni-Se-W composition and its 1 L water row under a child solution that is added to the parent at 10 ml/l.
- Resolve JCM Medium 151 and JCM Medium 197 references as structured stock links or curated child formulas.
- Keep the source's 10 ml/l, 35 ml/l, 5 ml/l, and 10 ml/l post-autoclave additions as milliliter stock additions, with flags or notes for the starred filter-sterilized rows if the schema can represent them.
- Split the final pH 7.0 adjustment from the prose that introduces the post-autoclave stock-addition table.
- Review whether the source `Na2WO2 x 2 H2O` row is a JCM typographical error or requires an ungrounded source-text exception.

## Follow-up Checks

- Re-run focused schema, strict, reference, and term validators on the regenerated merged YAML.
- Confirm that the regenerated parent ingredient list has no standalone Ni-Se-W stock solutes after the reducing-agent rows.
- Confirm that the source 1 L stock water row does not become a parent `ML_PER_L` ingredient.

## Additional Notes

This is the base recipe used by JCM 1463/MFA9. Fixing the Ni-Se-W structure here should be paired with the JCM 1463 derivative repair so the child stock structure can be inherited before the MFA9 NaCl substitution is applied.

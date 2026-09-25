# YAML Record Review: CLOSTRIDIUM (RB-9) MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_rb_9_medium.yaml`
- Started UTC: `2026-09-22T09:32:20Z`
- Finished UTC: `2026-09-22T09:32:32Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:001693` for MediaDive medium `558a`, DSMZ Medium 558a `CLOSTRIDIUM (RB-9) MEDIUM`. The generated record merges four MediaDive/KOMODO sources on merge fingerprint `38eb7f95424a87c108e267a88665ffc874ba207bc76150041943d7c2a8c137d9`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_rb_9_medium.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The canonical record identity is DSMZ Medium 558a, but the merged source set combines DSMZ Medium 558a `CLOSTRIDIUM (RB-9) MEDIUM`, DSMZ Medium 558 `CLOSTRIDIUM (RB-1) MEDIUM`, a KOMODO combined RB-1/RB-9 source, and a KOMODO source explicitly named `rb_1_rb_9_medium_replace_glucose_with_starch`.

RB-1 and RB-9 share the same printed ingredient list, but they do not have the same pH or gas-atmosphere instructions. DSMZ 558a adjusts the parent medium to pH 5-6 under 100% N2 and final pH 5.0-6.0, while DSMZ 558 adjusts pH to 3.5 under 80% N2 / 20% CO2 and final pH 3.5. The generated record keeps only the RB-9 values.

`Na2HPO4 x 12 H2O` is grounded to generic disodium hydrogenphosphate rather than a dodecahydrate-specific term, and `NiCl2 x 6 H2O` is grounded to generic nickel dichloride. `Calcium D-(+)-pantothenate` has no CHEBI-keyed MediaIngredientMech link.

## Evidence

The DSMZ Medium 558a PDF supports the generated base RB-9 pH range and main preparation paragraph. It also shows that Modified Wolin's mineral solution and Wolin's vitamin solution (10x) are one-liter stocks added to the final medium at only 10 ml/l and 1 ml/l, respectively.

The DSMZ Medium 558 PDF confirms that RB-1 has the same visible ingredient list as RB-9 but different preparation pH, gas mixture, and final pH.

The normalized `rb_1_rb_9_medium_replace_glucose_with_starch.yaml` source still contains `D-Glucose`, not starch, and was merged as a `SOURCE_DUPLICATE`; its starch replacement is only present in the source name.

## Completeness

The generated record preserves RB-9 pH and preparation prose, but it is incomplete structurally:

- Modified Wolin's mineral solution is not represented as a stock solution.
- Wolin's vitamin solution is not represented as a stock solution.
- RB-1 pH 3.5 and 80% N2 / 20% CO2 instructions are lost in the RB-1 synonym.
- The KOMODO starch-replacement variant is not represented as a variant or as a starch formula.

## Findings

- Modified Wolin mineral-stock internals are flattened into final `ingredients`: `Nitrilotriacetic acid` `1.5 G_PER_L`, `MgSO4 x 7 H2O` `3 G_PER_L`, `MnSO4 x H2O` `0.5 G_PER_L`, `NaCl` `1 G_PER_L`, `FeSO4 x 7 H2O` `0.1 G_PER_L`, `CoSO4 x 7 H2O` `0.18 G_PER_L`, `CaCl2 x 2 H2O` `0.1 G_PER_L`, and similar trace salts are stock-composition values for a stock used at 10 ml/l.
- Wolin vitamin-stock internals are flattened at full stock strength, including `Biotin` `0.02 G_PER_L`, `Pyridoxine hydrochloride` `0.1 G_PER_L`, `Vitamin B12` `0.001 G_PER_L`, and `p-Aminobenzoic acid` `0.05 G_PER_L`.
- DSMZ Medium 558 / RB-1 is merged as a source duplicate of DSMZ Medium 558a / RB-9 even though pH and gas composition differ.
- The KOMODO starch variant was merged without replacing glucose; the generated record still has only `D-Glucose` at `9.8912 G_PER_L`.
- The generated formula rescales the base ingredient amounts over an inferred final volume, but leaves the two nested one-liter stock recipes at stock strength. That creates mixed concentration semantics inside one flat `ingredients` list.

## Recommended Edits

- Fix the MediaDive/KOMODO normalized sources or stock import logic, then regenerate; `data/merge_yaml/merged/clostridium_rb_9_medium.yaml` is derived.
- Move Modified Wolin's mineral solution and Wolin's vitamin solution into structured stock `solutions` with 10 ml/l and 1 ml/l aliquots.
- Keep RB-1 and RB-9 preparation differences as variants or separate media records rather than collapsing pH 3.5 with pH 5.0-6.0.
- Correct the KOMODO starch replacement source so it actually contains starch or demote the misleading source if no evidence supports the substitution.
- Revisit the hydrate groundings for disodium hydrogen phosphate dodecahydrate and nickel chloride hexahydrate.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm no Modified Wolin or Wolin vitamin stock internal remains as a top-level final ingredient.
- Confirm DSMZ 558 and 558a no longer collapse into one record that hides their pH and gas differences.
- Confirm the starch-named variant either has starch in its ingredient signature or is no longer surfaced as a structured variant.

## Additional Notes

Empty optional fields are not defects. The formula-level blocker is loss of stock context; the identity-level blocker is merging records with different pH and atmosphere requirements under a single RB-9 identity.

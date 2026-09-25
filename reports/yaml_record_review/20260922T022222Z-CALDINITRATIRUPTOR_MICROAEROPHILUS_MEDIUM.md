# YAML Record Review: caldinitratiruptor_microaerophilus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml
- Started UTC: 2026-09-22T02:19:55Z
- Finished UTC: 2026-09-22T02:22:22Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:010224`, `caldinitratiruptor_microaerophilus_medium`, `Caldinitratiruptor Microaerophilus Medium`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium` on fingerprint `d64ef2829ef2a30e74df475c2fb4ed4cb7b57a888330a992fcb86f307bd8af71`.
- Authoritative owner: `data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml`.
- Claimed source identity: TOGO Medium M812, `Caldinitratiruptor Microaerophilus Medium`, wrapping JCM Medium 782.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- TOGO Medium M812 resolves to JCM `GRMD=782`, and the live JCM page is `CALDINITRATIRUPTOR MICROAEROPHILUS MEDIUM` with the same salts, 10 ml trace-minerals addition, 25 ml 8% sodium bicarbonate solution, and 20 ml 1 M glucose solution represented by the TOGO JSON.
- KH2PO4, K2HPO4, NH4Cl, KNO3, NaCl, KCl, calcium chloride dihydrate, magnesium chloride hexahydrate, KOH, carbon dioxide, and nitrogen are grounded to source-compatible identities where grounded.
- `KNO3` has a correct current primary potassium nitrate term but still carries a legacy `mediaingredientmech_term` field instead of a `mediaingredientmech_chebi_term` field.
- Yeast extract is intentionally ungrounded as an undefined biological mixture.

## Evidence

- JCM Medium 782 lists KH2PO4, K2HPO4, NH4Cl, KNO3, NaCl, KCl, calcium chloride dihydrate, magnesium chloride hexahydrate, 10 ml trace minerals, yeast extract, and 1 L distilled water in the autoclaved base.
- JCM instructs curators to adjust the base to pH 7.2 with KOH, distribute it under a 4:1 N2 / CO2 gas mixture, autoclave, and add 25 ml of 8% NaHCO3 solution plus 20 ml of 1 M glucose solution per liter from anaerobic stocks after cooling.
- The TOGO API preserves the 10 ml, 25 ml, and 20 ml solution volumes and distinguishes those from component masses.
- The generated record converted the 1 L water row to `1 G_PER_L` and moved the three solution additions into empty `Unknown solution` records with `G_PER_L` units.

## Completeness

- The final pH 7.2 is absent.
- The source preparation paragraph is absent from `preparation_steps`; KOH and the N2/CO2 atmosphere are present only as variable-concentration ingredient rows.
- The 10 ml trace-minerals cross-reference is present only as an empty solution shell.
- The source 25 ml bicarbonate and 20 ml glucose solution additions are present only as empty solution shells with the wrong unit.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the inspected TOGO/JCM sources support the formulation but do not add a strain-specific growth claim.

## Findings

- Major: the 1 L distilled-water row is represented as 1 g/L.
- Major: the 10 ml Trace minerals, 25 ml 8% NaHCO3, and 20 ml 1 M glucose additions are represented as empty `Unknown solution` records with `G_PER_L` units instead of as milliliter-per-liter solution additions.
- Major: JCM's pH, N2/CO2, autoclaving, and post-cooling stock-addition instructions are absent from `preparation_steps`.
- Major: KOH, carbon dioxide, and nitrogen are modeled as variable-concentration ingredients even though they are pH-adjustment and gas-atmosphere instructions in JCM.
- Major: the same JCM 782 source exists as a separate direct JCM generated record, `data/merge_yaml/merged/caldinitratiruptor_microaerophilus_medium__a882ad30.yaml`, instead of a `SOURCE_DUPLICATE` merge.
- Minor: `KNO3` still uses a legacy `mediaingredientmech_term` object despite the CHEBI-keying migration recorded in `curation_history`.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml`, not the generated merge.
- Convert the 1 L distilled-water row to the correct water representation.
- Model Trace minerals, 8% NaHCO3 solution, and 1 M Glucose solution as milliliter additions with retained stock identities; use the existing TOGO M142 or direct JCM Medium 151 cross-reference for the trace-minerals stock instead of leaving an empty `Unknown solution`.
- Move KOH and the N2/CO2 gas mixture into a preparation step with the JCM pH 7.2 adjustment, Hungate distribution, autoclaving, and post-cooling stock-addition instructions.
- Link or merge the TOGO M812 and direct JCM 782 records as source duplicates after both owners preserve equivalent solution semantics.
- Migrate the `KNO3` MediaIngredientMech link to the CHEBI-keyed field.
- Regenerate merged YAML and verify that only one generated record represents JCM 782.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized TOGO owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Re-run an ignored-inclusive exact search for `TOGO:M812`, `JCM_M782`, `GRMD=782`, and `mediadive.medium:J782` to confirm the TOGO and direct JCM imports are represented in one generated source-duplicate merge.
- Compare the regenerated merge against JCM 782 and TOGO M812, with special attention to water units, the 10 ml trace-minerals addition, the 25 ml bicarbonate and 20 ml glucose additions, pH 7.2, and the N2/CO2 autoclaving instructions.

## Additional Notes

- `find . -iname '*caldinitratiruptor*'` included ignored and hidden files and found the base Caldinitratiruptor DSMZ/KOMODO pair, this TOGO/JCM generated split, and their active normalized owners.
- A gitignore-independent search for TOGO M812, JCM 782, and Caldinitratiruptor microaerophilus identifiers found the active TOGO owner, the active direct JCM owner, their split generated merges, registry/catalog rows, current content review manifest rows, organism-candidate stubs keyed by the retired source filenames, and archived validation rows for both source paths.

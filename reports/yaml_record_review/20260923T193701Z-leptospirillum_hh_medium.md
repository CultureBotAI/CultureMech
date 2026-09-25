# YAML Record Review: LEPTOSPIRILLUM (HH) MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/leptospirillum_hh_medium.yaml
- Started UTC: 2026-09-23T19:35:29Z
- Finished UTC: 2026-09-23T19:37:01Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:006732 |
| Name | leptospirillum_hh_medium |
| Original name | LEPTOSPIRILLUM (HH) MEDIUM |
| Category | bacterial |
| Physical state | LIQUID |
| Media grounding | komodo.medium:882 |
| Source provenance | KOMODO 882 enriched with DSMZ Medium 882 |
| Generated file | data/merge_yaml/merged/leptospirillum_hh_medium.yaml |
| Maintained owners | data/normalized_yaml/bacterial/KOMODO_882_LEPTOSPIRILLUM_HH_MEDIUM.yaml; data/normalized_yaml/bacterial/leptospirillum_hh_medium.yaml |
| Merge fingerprint | 4c1c7b19de971a25725749df709e1942a9f23d60308151a10f8ca404a5034b77 |

The reviewed target is a generated two-source merge of KOMODO 882 and MediaDive DSMZ 882 owners. Future fixes belong in the maintained normalized owners or in the merge logic for nested stock solutions, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/leptospirillum_hh_medium.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/leptospirillum_hh_medium.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

MediaDive 882 and DSMZ Medium 882 identify the default Leptospirillum HH medium with final pH 2.3. The merged KOMODO record instead carries `ph_value: 1.8`; that pH is present in the related NBRC 1336 / Togo M2038 HH medium and is also mentioned by DSMZ only for a subset of strains, so it should be modeled as a strain-specific adjustment rather than silently replacing the DSMZ 2.3 default.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:006732`, `komodo.medium:882`, `mediadive.medium:882`, the shared slug, and the merge fingerprint found the merged generated record, both maintained owners merged into it, the related Togo M2038/NBRC 1336 sibling, a generated Togo sibling, source indexes, and archived validation rows.

## Evidence

Supported in the inspected DSMZ and MediaDive sources:

- DSMZ 882 is a nested formulation with 950 ml Solution A, 50 ml Solution B, and 1 ml Solution C for a final 1001 ml medium.
- Solution A contains milligram-scale ammonium sulfate, magnesium chloride hexahydrate, potassium dihydrogen phosphate, and calcium chloride dihydrate in 950 ml water, adjusted to pH 2.3 with 10 N H2SO4.
- Solution B contains 20 g FeSO4 x 7 H2O in 50 ml of 0.25 N H2SO4 and should have pH 1.2.
- Solution C contributes 1 ml of a trace-element stock containing mg/L MnCl2 x 4 H2O, ZnCl2, CoCl2 x 6 H2O, H3BO3, Na2MoO4, and CuCl2 x 2 H2O.
- DSMZ says to autoclave solutions A and C at 121 C for 20 min and solution B at 112 C for 30 min, then mix A and B and add the trace elements; the default final pH is 2.3.

Unsupported or incomplete in the generated record:

- The nested stock-solution structure is flattened into top-level ingredient concentrations, so solution B and trace-stock component concentrations are not represented as final-medium concentrations.
- H2SO4 is stored as `50 G_PER_L` even though the source lists 50 ml of 0.25 N H2SO4 in solution B, plus a separate 10 N H2SO4 pH adjustment for solution A.
- The generated merge keeps the KOMODO pH 1.8 value and discards the MediaDive DSMZ pH 2.3 default and pH-specific preparation context.
- The DSMZ autoclaving and static-incubation instructions are absent.
- The record has no structured reference to KOMODO, MediaDive 882, or the DSMZ PDF.

## Completeness

The record preserves the expected source identity and high-metal ingredients, but it is incomplete for solution hierarchy, final-medium concentration semantics, pH-variant context, preparation steps, sterilization, and structured references.

Empty optional organism, incubation, and storage fields are acceptable for this review because the inspected DSMZ and MediaDive entries do not provide those as structured target conditions.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Critical | DSMZ stock solutions were flattened into misleading top-level final concentrations. | DSMZ 882 uses 950 ml Solution A, 50 ml Solution B, and 1 ml Solution C, where Solution C is itself a trace-element stock; the generated record exposes the stock concentrations as if they were all final-medium g/L rows. | nested-solution import and merge logic |
| Critical | H2SO4 is represented with a mass unit and loses normality. | DSMZ 882 lists 50 ml of 0.25 N H2SO4 in Solution B and a 10 N H2SO4 pH adjustment for Solution A; the generated record stores `50 G_PER_L`. | `data/normalized_yaml/bacterial/KOMODO_882_LEPTOSPIRILLUM_HH_MEDIUM.yaml` or nested-solution import |
| Major | The pH 1.8 variant is merged without the DSMZ pH 2.3 default. | MediaDive DSMZ 882 has final pH 2.3, while the KOMODO owner and the generated merge store pH 1.8 without strain-specific context. | merge logic or `data/normalized_yaml/bacterial/KOMODO_882_LEPTOSPIRILLUM_HH_MEDIUM.yaml` |
| Major | DSMZ preparation and sterilization steps are missing after merge. | The MediaDive owner has the DSMZ 121 C and 112 C autoclaving instructions, solution mixing note, static-growth note, Solution A pH adjustment, and Solution B pH note; the generated merge has no `preparation_steps`. | merge logic |
| Minor | Structured references are missing. | The generated reference validator performed zero checks despite available KOMODO, MediaDive, and DSMZ source identifiers. | maintained owners |

## Recommended Edits

1. Preserve DSMZ 882 as a solution-level recipe with Solution A, Solution B, Solution C, and the trace-element stock rather than flattening every stock into final ingredients.
2. Represent sulfuric acid as 50 ml 0.25 N H2SO4 in Solution B and as a 10 N H2SO4 pH adjustment for Solution A, not as `50 G_PER_L`.
3. Model final pH 2.3 as the DSMZ 882 default and pH 1.8 as a strain-specific or NBRC 1336/Togo M2038 variant.
4. Preserve the DSMZ autoclaving and solution-mixing instructions from the MediaDive owner in the regenerated record.
5. Add structured references for KOMODO 882, MediaDive 882, and DSMZ Medium 882.
6. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated record against DSMZ 882 for 950 ml Solution A, 50 ml Solution B, 1 ml Solution C, final pH 2.3, and distinct 121 C / 112 C autoclaving steps.
- Re-run an ignored-inclusive exact search for `komodo.medium:882`, `mediadive.medium:882`, and `TOGO:M2038` to confirm that the DSMZ 882 default and NBRC pH-1.8 variant are linked without collapsing their pH and trace-element differences.

## Additional Notes

NBRC 1336 / Togo M2038 is a related Leptospirillum HH medium that uses pH 1.8 and a manganese chloride dihydrate trace-element row; keep it as a related variant rather than using it to overwrite the DSMZ 882 default.

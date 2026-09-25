# YAML Record Review: LB (Luria-Bertani) Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_luria_bertani_medium.yaml
- Started UTC: 2026-09-23T19:06:39Z
- Finished UTC: 2026-09-23T19:08:23Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009052 |
| Name | lb_luria_bertani_medium |
| Original name | LB (Luria-Bertani) Medium |
| Category | bacterial |
| Physical state | SOLID_AGAR |
| Media grounding | TOGO:M2476 |
| Source provenance | Togo Medium M2476 and Togo Medium M2619, both from DSMZ Medium 381 |
| Generated file | data/merge_yaml/merged/lb_luria_bertani_medium.yaml |
| Maintained owners | data/normalized_yaml/bacterial/TOGO_M2476_LB_Luria-Bertani_Medium.yaml; data/normalized_yaml/bacterial/TOGO_M2619_LB_Luria-Bertani_Medium.yaml |
| Merge fingerprint | d0614da0c4b18eca72d43c9cc409247cd2bab397907b6fc8269461ffd750ea4f |

The review target is a generated merged record made from two duplicate Togo imports. Future Togo-specific fixes belong in both maintained normalized owners, or in the Togo importer if this 1000 ml water conversion error is systemic, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lb_luria_bertani_medium.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/lb_luria_bertani_medium.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

Togo M2476, Togo M2619, MediaDive DSMZ Medium 381, and the DSMZ Medium 381 PDF all identify the same `LB (Luria-Bertani) Medium` formula. The ingredients and pH agree across the inspected sources: 10 g/L tryptone, 5 g/L yeast extract, 10 g/L NaCl, 20 g/L agar, 1000 ml distilled water per liter, and pH 7.0.

The two merged Togo sources are therefore true duplicate imports of the DSMZ 381 base LB agar recipe. The generated record's `TOGO:M2476` grounding is valid for one of the two imported Togo identities, but the record lacks structured source-duplicate information connecting it to Togo M2619 and to the direct DSMZ Medium 381 import at `data/normalized_yaml/bacterial/lb_luria_bertani_medium.yaml`.

An ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:009052`, `TOGO:M2476`, `TOGO:M2619`, `DSMZ_Medium381`, both Togo source slugs, and the merge fingerprint found the reviewed merge, both maintained Togo owners, the separate direct DSMZ 381 owner, and archived validation rows.

## Evidence

Supported in the inspected sources:

- Togo M2476 and Togo M2619 both point to DSMZ Medium 381 and reproduce its base LB agar formula.
- The DSMZ Medium 381 PDF and MediaDive 381 both support 10 g/L tryptone, 5 g/L yeast extract, 10 g/L NaCl, 20 g/L agar, 1000 ml distilled water in a 1 L main solution, and pH 7.0.
- The Togo roles and properties on water, yeast extract, NaCl, agar, and tryptone are supported by the two inspected Togo API records.
- The CHEBI mappings for water, sodium chloride, and agar match the inspected component identities.

Unsupported or incomplete relative to the inspected sources:

- `Distilled water` is represented as `1000 G_PER_L`; all inspected sources encode 1000 ml water, not 1000 g/L.
- The generated record omits pH 7.0 and the `Adjust pH to 7.0` preparation step.
- The generated record has no structured `references` collection and only carries the first merged Togo source URL in free-text notes.
- The DSMZ PDF includes a DSM 26804 instruction to add 100 g NaCl for 1000 ml medium. That addendum should remain a conditional strain-specific variant, not a change to this base LB recipe, but it is not represented as a note or variant relationship.

## Completeness

The generated record is complete enough for its base non-water ingredient identities and amounts, category, solid agar state, and duplicate Togo merge. It is materially incomplete for the source water unit, pH, pH-adjustment step, structured references, and source-duplicate cross-links to Togo M2619 and MediaDive DSMZ Medium 381.

Neither maintained Togo owner has been repaired, so the water-unit and pH omissions still originate in `data/normalized_yaml/bacterial/TOGO_M2476_LB_Luria-Bertani_Medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M2619_LB_Luria-Bertani_Medium.yaml`. The direct MediaDive DSMZ 381 owner preserves pH 7.0 and the adjustment step but also omits the 1000 ml water row from MediaDive's source recipe.

Empty optional organism, incubation, and storage fields are acceptable because the reviewed record is a base DSMZ formulation rather than the DSM 26804 high-salt variant or a growth-outcome assertion.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Both maintained Togo owners convert 1000 ml distilled water to `1000 G_PER_L`, and the generated merge carries the same unsupported mass concentration. | Togo M2476, Togo M2619, MediaDive 381, and the DSMZ 381 PDF all encode distilled water as 1000 ml for the 1 L medium. | `data/normalized_yaml/bacterial/TOGO_M2476_LB_Luria-Bertani_Medium.yaml`; `data/normalized_yaml/bacterial/TOGO_M2619_LB_Luria-Bertani_Medium.yaml`; or the Togo importer |
| Major | The maintained Togo owners and generated merge omit pH 7.0 and the pH-adjustment step. | Both inspected Togo API records carry pH 7.0 and the comment `Adjust pH to 7.0.`; MediaDive 381 and the DSMZ PDF carry the same condition. | `data/normalized_yaml/bacterial/TOGO_M2476_LB_Luria-Bertani_Medium.yaml`; `data/normalized_yaml/bacterial/TOGO_M2619_LB_Luria-Bertani_Medium.yaml` |
| Minor | The generated merge does not preserve all recoverable source identities as structured references or duplicate relationships. | The merge combines Togo M2476 and M2619, while MediaDive 381 imports the same DSMZ Medium 381 record directly; only the first Togo URL appears in generated free-text notes. | both Togo owners plus merge generation |
| Minor | The DSM 26804 high-salt addendum in DSMZ Medium 381 is not represented as a conditional variant note. | DSMZ Medium 381's PDF adds a DSM 26804-specific instruction to add 100 g NaCl per 1000 ml medium. | a new or existing strain-specific variant, not the base `TOGO:M2476` or `TOGO:M2619` formulation |

## Recommended Edits

1. Correct distilled water to `1000 ML_PER_L` in both maintained Togo owners, or fix the Togo importer to map 1000 ml/L water without converting it to grams per liter.
2. Add `ph_value: 7.0` or an equivalent 7.0 pH range, and add the source pH-adjustment preparation step to both maintained Togo owners.
3. Add structured references for Togo M2476, Togo M2619, and DSMZ Medium 381; preserve the direct DSMZ 381 MediaDive import as a source duplicate where the model can express it.
4. Curate the DSM 26804 high-salt addendum as a conditional variant only if DSM 26804-specific media records are in scope.
5. Regenerate `data/merge_yaml/merged/` and downstream products from the repaired normalized owners.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on `data/merge_yaml/merged/lb_luria_bertani_medium.yaml` after editing both Togo owners and regenerating.
- Manually compare the regenerated record against Togo M2476, Togo M2619, MediaDive 381, and DSMZ Medium 381 for 10 g/L tryptone, 5 g/L yeast extract, 10 g/L NaCl, 20 g/L agar, 1000 ml/L distilled water, and pH 7.0.
- Re-run an ignored-inclusive search for `TOGO:M2476`, `TOGO:M2619`, `DSMZ_Medium381`, and `mediadive.medium:381` to confirm that all source-duplicate paths are intentionally connected after curation.

## Additional Notes

The direct DSMZ Medium 381 import in `data/normalized_yaml/bacterial/lb_luria_bertani_medium.yaml` is a useful repaired reference for pH but is not a complete substitute for fixing the Togo owners because it still omits the 1000 ml distilled water source row.

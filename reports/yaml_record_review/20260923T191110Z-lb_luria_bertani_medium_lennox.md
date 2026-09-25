# YAML Record Review: LB (Luria-Bertani) Medium (Lennox)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_luria_bertani_medium_lennox.yaml
- Started UTC: 2026-09-23T19:09:13Z
- Finished UTC: 2026-09-23T19:11:10Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007866 |
| Name | lb_luria_bertani_medium_lennox |
| Original name | LB (Luria-Bertani) Medium (Lennox) |
| Category | bacterial |
| Physical state | SOLID_AGAR |
| Media grounding | TOGO:M1330 |
| Source provenance | Togo Medium M1330 imported from JCM_M1236-2 / GRMD=1236 |
| Generated file | data/merge_yaml/merged/lb_luria_bertani_medium_lennox.yaml |
| Maintained canonical owner | data/normalized_yaml/bacterial/TOGO_M1330_LB_Luria-Bertani_Medium_Lennox.yaml |
| Other merged owners | TOGO M1270, M1334, M443, and M878 normalized inputs |
| Merge fingerprint | 6b5c3f0cd2bf4f77ba7573f48673517e7df3e524e9ec217223a1704fff4f9927 |

The reviewed target is a generated merge of five source records. The canonical label and `media_term` point to Togo M1330 Lennox LB, but the merged ingredient set uses 50 g/L NaCl from a 5% NaCl source and its synonyms include several biologically distinct LB agar variants.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lb_luria_bertani_medium_lennox.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/lb_luria_bertani_medium_lennox.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The generated record's identity is internally inconsistent. Its canonical ID, label, and `TOGO:M1330` grounding denote `LB (Luria-Bertani) Medium (Lennox)`, whose inspected Togo and MediaDive J1236 sources contain 5 g/L NaCl, 10 g/L BD-Difco tryptone, 5 g/L BD-Difco yeast extract, 1000 ml/L water, and a pH 7.0 adjustment with 15 g/L agar for solid medium.

The generated ingredient set instead contains 50 g/L NaCl, which belongs to Togo M1270 `LB (Luria-Bertani) Agar With 5% NaCl (pH 9.0)` and Togo M1334 `LB (Luria-Bertani) Agar With 5% NaCl`. Its `merged_from` list also includes Togo M443 ordinary LB agar with 10 g/L NaCl and repaired Togo M878 one-third LB agar with 3.3 g/L tryptone and 1.7 g/L yeast extract. These five source records are related LB-family formulations, not duplicate identities.

An ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:007866`, the five Togo source IDs, the five maintained source slugs, and the merge fingerprint found exactly those maintained inputs, the reviewed generated merge, source indexes, and archived validation rows.

## Evidence

Supported in the inspected Togo or MediaDive sources:

- Togo M1330 and MediaDive J1236 support the Lennox source identity and 5 g/L NaCl recipe.
- Togo M1270 supports a distinct 5% NaCl, pH 9.0 LB agar formulation with a 10% Na2CO3 solution added after autoclaving to adjust pH.
- Togo M1334 supports a distinct 5% NaCl LB agar formulation at pH 7.0.
- Togo M443 supports a distinct ordinary LB agar formulation with 10 g/L NaCl at pH 7.0.
- Togo M878 supports a distinct `1/3 LB Agar` formulation with 3.3 g/L tryptone, 1.7 g/L yeast extract, 5 g/L NaCl, 15 g/L agar, and 1000 ml/L water.

Unsupported or incomplete in the generated record:

- The generated record has a Lennox identity but 50 g/L NaCl; Lennox LB is 5 g/L NaCl.
- `Distilled water` is represented as `1 G_PER_L`; all five inspected Togo sources encode 1 L water.
- The merge erases source pH values: pH 9.0 for M1270 and pH 7.0 for M1330, M1334, and M443.
- The merge drops M1270's 10% Na2CO3 solution and its post-autoclave pH adjustment.
- The merge promotes M1270, M1334, M443, and M878 to synonyms of M1330 even though their NaCl, pH, additive, or tryptone and yeast extract amounts differ.
- The generated copy is stale for M878, whose maintained owner was repaired in September 2026 to 3.3 g/L tryptone, 1.7 g/L yeast extract, 5 g/L NaCl, 1000 ml/L water, and structured references.

## Completeness

The generated record is not complete enough for safe use because it has the wrong formulation for its canonical Lennox identity and hides four non-duplicate source formulations behind synonym rows. It also omits pH and preparation details required to distinguish the pH 9.0 high-salt recipe from pH 7.0 high-salt or Lennox recipes.

Of the five normalized owners, only `data/normalized_yaml/bacterial/TOGO_M878_1_3_LB_Agar.yaml` has already been repaired. The four remaining owners still need water-unit repair, pH and preparation repair where the source supplies pH, structured references, and de-duplication metadata that prevents future cross-variant merging.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Blocker | The merge combines five LB-family variants that are not duplicate recipes, so the generated record denotes the wrong thing. | Togo M1330 is Lennox LB with 5 g/L NaCl, M1270 is 5% NaCl at pH 9.0 with Na2CO3 solution, M1334 is 5% NaCl at pH 7.0, M443 is 10 g/L NaCl ordinary LB agar, and M878 is one-third LB agar. The generated M1330 record carries 50 g/L NaCl and synonyms for all of them. | merge de-duplication logic plus the five maintained Togo owners |
| Major | The generated record and four unrepaired owners still convert 1 L water to `1 G_PER_L`. | Each inspected Togo source uses 1 L Distilled water; repaired M878 already represents this as 1000 ml/L. | TOGO M1270, M1330, M1334, and M443 maintained owners, or the Togo importer |
| Major | The generated record omits pH and pH-adjustment details that distinguish the variants. | M1270 requires post-autoclave adjustment to pH 9.0 with sterile 10% Na2CO3, while M1330, M1334, and M443 specify pH 7.0. | TOGO M1270, M1330, M1334, and M443 maintained owners |
| Minor | The generated record lacks structured references. | Its reference validator performed zero checks despite five Togo sources and multiple JCM original-source URLs in provenance notes. | the five maintained Togo owners and merge generation |

## Recommended Edits

1. Split the five maintained Togo inputs into separate generated records or merge only truly equivalent source formulations; do not keep M1270, M1334, M443, or M878 as synonyms of Lennox M1330.
2. Repair the four stale Togo owners by converting 1 L water to 1000 ml/L water and by adding structured source references.
3. Add pH and preparation semantics to M1270, M1330, M1334, and M443, including M1270's 10% Na2CO3 solution and post-autoclave pH 9.0 adjustment.
4. Regenerate `data/merge_yaml/merged/` and downstream pages after the maintained owners and merge discrimination logic are corrected.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on each regenerated LB-family output after the split.
- Manually confirm that the Lennox output has 5 g/L NaCl and no high-salt or one-third LB synonyms.
- Manually confirm that M1270 retains 50 g/L NaCl, 10% Na2CO3, and pH 9.0; M1334 retains 50 g/L NaCl and pH 7.0; M443 retains 10 g/L NaCl and pH 7.0; and M878 remains a one-third LB agar formulation.
- Re-run an ignored-inclusive search for `TOGO:M1270`, `TOGO:M1330`, `TOGO:M1334`, `TOGO:M443`, and `TOGO:M878` to confirm the variants are no longer emitted under one fingerprint.

## Additional Notes

The generated record is schema-valid because all cross-variant amounts are individually legal numbers. The defect is a semantic identity failure caused by merging source records whose old Togo imports looked more similar than their upstream formulas actually are.

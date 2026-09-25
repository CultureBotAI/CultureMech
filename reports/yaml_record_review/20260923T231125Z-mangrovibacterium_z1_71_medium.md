# YAML Record Review: mangrovibacterium_z1_71_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mangrovibacterium_z1_71_medium.yaml
- Started UTC: 2026-09-23T23:11:25Z
- Finished UTC: 2026-09-23T23:11:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:015857 |
| name | mangrovibacterium_z1_71_medium |
| original_name | MANGROVIBACTERIUM Z1-71 MEDIUM |
| category | bacterial |
| medium_type | COMPLEX |
| composition_type | UNDEFINED |
| physical_state | LIQUID |
| pH | 6.5 |
| source term | jcm.grmd:1412, MANGROVIBACTERIUM Z1-71 MEDIUM |
| generated path | data/merge_yaml/merged/mangrovibacterium_z1_71_medium.yaml |
| maintained owner | data/normalized_yaml/bacterial/JCM_J1412_MANGROVIBACTERIUM_Z1_71_MEDIUM.yaml |

The reviewed YAML is a derived merge artifact. Its `merged_from` value names the exact normalized owner `JCM_J1412_MANGROVIBACTERIUM_Z1_71_MEDIUM`, and the terminal curation event reports an August 2026 merge on fingerprint `ade8bcb32a287b024a102c5acba1c4d1e5d1b62e7d6cda175a9c6310b83091c2`.

An ignored-file-inclusive exact search under `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:015857`, `jcm.grmd:1412`, `GRMD=1412`, and `JCM_J1412_MANGROVIBACTERIUM_Z1_71_MEDIUM` found this normalized owner, this generated copy, and derived JSON indexes; no second YAML in those searched trees claimed the same exact CultureMech or JCM identifier.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mangrovibacterium_z1_71_medium.yaml` |
| Strict validator | Passed with 0 ERROR rows; `/private/tmp/mangrovibacterium_z1_71_medium.strict.tsv` had the header row only |
| Reference validator | Passed structurally: 1 file validated, 0 reference checks, 0 failures |
| Term validator | Passed |
| Embedded history validation | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` lists in merged media records |

The equivalent focused validators were run directly against the generated `MediaRecipe` because the project-level `just` wrappers currently resolve the default Python 3.13 project environment before running.

## Identity and Grounding

The generated record denotes JCM Medium 1412, `MANGROVIBACTERIUM Z1-71 MEDIUM`, and its category, source accession, pH, and liquid state agree with the inspected JCM GRMD page.

JCM GRMD 1412 supports these ingredient amounts:

| Ingredient group | Supported amounts |
|---|---|
| Base salts and nutrients | 0.5 g NH4Cl; 4.0 g MgSO4 x 7H2O; 0.14 g CaCl2 x 2H2O; 0.14 g K2HPO4; 0.1 g KCl; 10.0 g NaCl; 2.5 g NaHCO3; 1.0 g yeast extract |
| Indicator and water | 0.5 mg resazurin; 980.0 ml distilled water |
| Stock-solution additions | 10.0 ml Wolfe's mineral solution; 10.0 ml trace vitamins; 20.0 ml 1.0 M glucose solution; 10.0 ml 5% L-Cysteine x HCl x H2O solution; 10.0 ml 5% Na2S x 9H2O solution |

The CHEBI and MediaIngredientMech links on the directly grounded salts, resazurin, and water are label-consistent with the source strings. Undefined yeast extract and named stock solutions correctly remain ungrounded rather than being forced to a narrow CHEBI term.

## Evidence

The ingredient list and pH are source-supported. The record preserves the 980 ml base-water amount and the 20 ml plus 10 ml plus 10 ml post-autoclave stock amounts instead of folding the recipe into an unsupported 1 L water basis.

The preparation sequence is incomplete. JCM GRMD 1412 instructs curators to mix the first table except NaHCO3, adjust pH to 6.5, boil briefly, cool under N2-CO2, add NaHCO3, dispense under the same gas, seal with butyl stoppers, autoclave, stand overnight, and then aseptically and anaerobically add the glucose, cysteine hydrochloride, and sodium sulfide solutions that have been autoclaved and stored under N2. The record stops after the overnight standing step and never records the final stock additions or their stored-under-N2 condition.

JCM also states its default sterilization condition as autoclaving at 121 C for 15 min unless otherwise stated. The record's autoclave step lacks that temperature and duration.

## Completeness

Missing or incomplete:

- The three terminal stock additions are present as ingredients but have no preparation step saying they are added aseptically and anaerobically after autoclaving.
- The record does not state that the terminal glucose, cysteine hydrochloride, and sodium sulfide stock solutions are autoclaved and stored under N2 before addition.
- The autoclave step omits JCM's default 121 C, 15 min setting.
- The `Wolfe's mineral solution` and `Trace vitamins` rows cite JCM Medium Nos. 265 and 197 only in their labels. They are not structured solution references, so a consumer cannot follow those nested recipes without string parsing.

Complete enough:

- No target organism or growth evidence is needed for this JCM recipe import.
- No structured storage rule is needed beyond the JCM stock-solution storage condition noted above.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The post-autoclave stock-addition step is missing. | JCM says to add the 1.0 M glucose, 5% L-Cysteine x HCl x H2O, and 5% Na2S x 9H2O solutions aseptically and anaerobically after the overnight stand; the generated record lists those ingredients but its `preparation_steps` stop at `After autoclaving, stand the medium overnight.` | data/normalized_yaml/bacterial/JCM_J1412_MANGROVIBACTERIUM_Z1_71_MEDIUM.yaml |
| major | JCM stock solutions are unresolved literals. | The JCM rows for Wolfe's mineral solution and trace vitamins link to Medium Nos. 265 and 197. The record keeps those rows only as ingredient strings and has no structured solution references to the stock recipes. | data/normalized_yaml/bacterial/JCM_J1412_MANGROVIBACTERIUM_Z1_71_MEDIUM.yaml, or the JCM importer if it owns parsing of nested medium links |
| minor | The autoclave step loses the default JCM temperature and duration. | JCM GRMD pages state to autoclave at 121 C for 15 min unless otherwise stated; this recipe only says `Autoclave.` | data/normalized_yaml/bacterial/JCM_J1412_MANGROVIBACTERIUM_Z1_71_MEDIUM.yaml, or the JCM importer if it owns default autoclave handling |

## Recommended Edits

1. Add a post-autoclave preparation step to `data/normalized_yaml/bacterial/JCM_J1412_MANGROVIBACTERIUM_Z1_71_MEDIUM.yaml` that aseptically and anaerobically adds 20 ml 1.0 M glucose solution, 10 ml 5% L-Cysteine x HCl x H2O solution, and 10 ml 5% Na2S x 9H2O solution per liter after the overnight stand.
2. Record that those three stock solutions are autoclaved and stored under N2 before use, either in the post-autoclave step text or in structured solution metadata if available.
3. Replace the two plain `see Medium No.` stock rows with structured solution references to JCM Medium 265 and JCM Medium 197 when those solutions are represented in CultureMech.
4. Clarify the autoclave step with JCM's 121 C, 15 min default.

## Follow-up Checks

- Rerun open schema, strict, term, and reference validation on the normalized owner and the regenerated merged record.
- Rerun merge generation plus the focused merge-freshness check or `just verify-merges` for JCM J1412.
- Manually re-read JCM GRMD 1412 and verify the regenerated preparation steps keep NaHCO3 before autoclaving and the glucose, cysteine hydrochloride, and sodium sulfide solutions after autoclaving.
- If Medium Nos. 265 and 197 become structured solution references, validate that those references resolve and that no string-only `see Medium No.` dependency remains in this record.

## Additional Notes

None found.

# YAML Record Review: marichromatium_bheemlicum_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marichromatium_bheemlicum_medium__1721177e.yaml
- Started UTC: 2026-09-23T23:20:47Z
- Finished UTC: 2026-09-23T23:20:47Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002881 |
| name | marichromatium_bheemlicum_medium |
| original_name | MARICHROMATIUM BHEEMLICUM MEDIUM |
| category | bacterial |
| medium_type | COMPLEX |
| composition_type | SEMI_DEFINED |
| physical_state | LIQUID |
| pH | 7.2 |
| source term | mediadive.medium:J533, MARICHROMATIUM BHEEMLICUM MEDIUM |
| generated path | data/merge_yaml/merged/marichromatium_bheemlicum_medium__1721177e.yaml |
| maintained owner | data/normalized_yaml/bacterial/marichromatium_bheemlicum_medium.yaml |

The reviewed YAML is a derived merge artifact. Its `merged_from` value names the single normalized owner `marichromatium_bheemlicum_medium`, and the terminal curation event reports an August 2026 merge on fingerprint `1721177e97d7814ee2800bf36195816bca6210d0cbdcfe047059b092fdff590a`.

An ignored-file-inclusive exact search under `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:002881`, `mediadive.medium:J533`, `GRMD=533`, `JCM Medium J533`, and `MARICHROMATIUM BHEEMLICUM MEDIUM` found this normalized owner, this generated copy, derived JSON indexes, and a TOGO mirror that cites the same JCM GRMD 533 page by original URL.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marichromatium_bheemlicum_medium__1721177e.yaml` |
| Strict validator | Passed with 0 ERROR rows; `/private/tmp/marichromatium_bheemlicum_medium__1721177e.strict.tsv` had the header row only |
| Reference validator | Passed structurally: 1 file validated, 0 reference checks, 0 failures |
| Term validator | Passed |
| Embedded history validation | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` lists in merged media records |

The equivalent focused validators were run directly against the generated `MediaRecipe` because the project-level `just` wrappers currently resolve the default Python 3.13 project environment before running.

## Identity and Grounding

The record denotes JCM/MediaDive Medium J533, `MARICHROMATIUM BHEEMLICUM MEDIUM`, and preserves pH 7.2 and the liquid physical state from JCM.

JCM GRMD 533 and MediaDive both distinguish three kinds of inputs:

| Boundary | Source representation |
|---|---|
| Main salts and nutrients | Direct gram additions: KH2PO4, CaCl2 x 2H2O, MgSO4 x 7H2O, NH4Cl, NaCl, yeast extract, sodium pyruvate, plus 1 L distilled water |
| Stock additions | 1 ml Micronutrient solution SL7; 5 ml ferric citrate at 0.1% w/v; 1 ml vitamin B12 at 2 mg/ml; 1 mM final Na2S x 9H2O |
| SL7 stock recipe | 1 ml 25% HCl, 70 mg ZnCl2, 100 mg MnCl2 x 4H2O, 60 mg H3BO3, 200 mg CoCl2 x 6H2O, 20 mg CuCl2 x 2H2O, 20 mg NiCl2 x 6H2O, 40 mg Na2MoO4 x 2H2O, and 1 L distilled water |

The generated record flattens the SL7 stock components into the final medium and promotes the ferric-citrate and vitamin B12 stock volumes into gram concentrations. That changes the scientific formulation.

## Evidence

The direct main-medium salts, yeast extract, sodium pyruvate, pH 7.2, and the final 1 mM sodium sulfide nonahydrate amount are source-supported. MediaDive has normalized the main-medium gram additions over a 1007 ml final volume, which explains the slight reductions such as `0.496524 G_PER_L` KH2PO4 from a 0.5 g source amount.

Unsupported or over-scoped assertions:

- `Ferric citrate` is stored as `5 G_PER_L`, but the source says to add 5 ml of a 0.1% w/v solution.
- `Vitamin B12` is stored as `1 G_PER_L`, but the source says to add 1 ml of a 2 mg/ml solution.
- The SL7 components are stored as if their 1 L stock recipe amounts were final-medium amounts. JCM instead calls for 1 ml of the prepared SL7 stock per liter of main medium.
- `HCl (25%, v/v)` is an SL7 stock component, not a 1 G_PER_L final-medium HCl ingredient.
- `Distilled water` is present in both the main medium and SL7 stock recipe in JCM/MediaDive, but absent from the generated record.
- The source says `NiCl2 x 6H2O`; the record grounds that row to CHEBI:34887, `nickel dichloride`, which loses the hexahydrate identity.

## Completeness

Missing or incomplete:

- The 1 L main-medium water row is absent.
- Micronutrient solution SL7 is not represented as a stock solution or as a 1 ML_PER_L stock addition.
- The water row inside the SL7 stock recipe is absent.
- Ferric citrate and vitamin B12 should remain stock additions or be converted with their stated stock concentrations.
- The HCl and trace-metal rows need to be scoped to SL7, not to the final medium.

Complete enough:

- No target-organism evidence is required for this JCM recipe import.
- The pH 7.2 adjustment is represented.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | SL7 stock-solution contents were flattened into final-medium concentrations. | JCM and MediaDive call for 1 ml Micronutrient solution SL7 per liter and define SL7 as a separate 1 L stock. The generated record places HCl, ZnCl2, MnCl2 x 4H2O, H3BO3, CoCl2 x 6H2O, CuCl2 x 2H2O, NiCl2 x 6H2O, and Na2MoO4 x 2H2O directly in the final ingredient list at their stock concentrations. | data/normalized_yaml/bacterial/marichromatium_bheemlicum_medium.yaml; if this came from generic MediaDive flattening, the MediaDive importer |
| major | Two stock additions were converted to impossible gram concentrations. | JCM lists 5 ml ferric citrate at 0.1% w/v and 1 ml vitamin B12 at 2 mg/ml; the record stores them as `5 G_PER_L` and `1 G_PER_L`, respectively. | data/normalized_yaml/bacterial/marichromatium_bheemlicum_medium.yaml or the MediaDive importer |
| major | Water rows are missing from the main medium and SL7 stock. | JCM and MediaDive list 1 L distilled water for the main medium and 1 L distilled water for the SL7 stock recipe; neither appears in the generated record. | data/normalized_yaml/bacterial/marichromatium_bheemlicum_medium.yaml or the MediaDive importer |
| major | The nickel chloride hydrate identity is under-specified. | The source says `NiCl2 x 6H2O`; the record maps it to CHEBI:34887 labelled `nickel dichloride`, losing the hexahydrate form. | data/normalized_yaml/bacterial/marichromatium_bheemlicum_medium.yaml |
| minor | JCM's default autoclave setting is omitted. | JCM GRMD pages state 121 C for 15 min unless otherwise stated; this record has no autoclave step. | data/normalized_yaml/bacterial/marichromatium_bheemlicum_medium.yaml |

## Recommended Edits

1. Restore the SL7 stock boundary in `data/normalized_yaml/bacterial/marichromatium_bheemlicum_medium.yaml`: represent Micronutrient solution SL7 as a 1 ML_PER_L addition and keep the nine SL7 ingredients inside a stock-solution recipe or an equivalent nested representation.
2. Represent ferric citrate as 5 ml of a 0.1% w/v stock and vitamin B12 as 1 ml of a 2 mg/ml stock, or convert them explicitly to final amounts with notes preserving the source stock strengths.
3. Add the missing distilled-water row to both the main medium and the SL7 stock.
4. Correct the NiCl2 x 6H2O grounding so the hydrate form is not lost.
5. Add JCM's default 121 C, 15 min autoclave detail if the local JCM import policy records that default for simple media.

## Follow-up Checks

- Rerun open schema, strict, term, and reference validation on the normalized owner and regenerated merged record.
- Re-fetch JCM GRMD 533 and MediaDive J533 and verify that the regenerated record preserves one main medium plus one SL7 stock, not a single flattened final ingredient list.
- Validate that the final medium keeps 1 mM Na2S x 9H2O as a final concentration and does not accidentally move it into SL7.
- If the MediaDive importer is changed, add a regression test for a medium with one nested stock solution plus mL additions of concentrated reagents.

## Additional Notes

None found.

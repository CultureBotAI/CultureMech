# YAML Record Review: carboxydothermus_medium_heterotroph

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/carboxydothermus_medium_heterotroph.yaml
- Started UTC: 2026-09-22T03:58:05Z
- Finished UTC: 2026-09-22T04:02:47Z
- Verdict: needs curation

## Target

- Reviewed generated `MediaRecipe` `CultureMech:001642`, `carboxydothermus_medium_heterotroph`, in `data/merge_yaml/merged/carboxydothermus_medium_heterotroph.yaml`.
- The generated record is a canonical merge of `data/normalized_yaml/bacterial/carboxydothermus_medium_heterotroph.yaml` and `data/normalized_yaml/archaea/pyrodictium_abyssi_medium.yaml` on `merge_fingerprint: 5c969896fa86b8d084908dd278dbcd7f06f1d6cff1801ecf28b49f0ba260dd55`.
- The canonical source identity is DSMZ/MediaDive Medium 508, `mediadive.medium:508`, `CARBOXYDOTHERMUS MEDIUM (HETEROTROPH)`.
- The generated record carries 32 flattened direct ingredients, no `solutions`, pH range 6.8-7.0, two preparation steps, a `pyrodictium_abyssi_medium` synonym, and both `archaea` and `bacterial` categories.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/carboxydothermus_medium_heterotroph.yaml` | Passed: `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/carboxydothermus_medium_heterotroph.yaml --out /private/tmp/carboxydothermus_medium_heterotroph.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/carboxydothermus_medium_heterotroph.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file, 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/carboxydothermus_medium_heterotroph.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries. |

## Identity and Grounding

- DSMZ Medium 508 and MediaDive `mediadive.medium:508` identify the formula as `CARBOXYDOTHERMUS MEDIUM (HETEROTROPH)` at pH 6.8-7.0, which agrees with the canonical `CultureMech:001642` owner under `data/normalized_yaml/bacterial/`.
- `CultureMech:001642` resolves to `data/normalized_yaml/bacterial/carboxydothermus_medium_heterotroph.yaml`, while the second merged owner `CultureMech:005709` resolves to `data/normalized_yaml/archaea/pyrodictium_abyssi_medium.yaml`.
- A gitignore-independent `rg --no-ignore --hidden` search for `CultureMech:001642`, `CultureMech:005709`, `mediadive.medium:508`, `komodo.medium:508`, `pyrodictium_abyssi_medium`, and `carboxydothermus_medium_heterotroph` covered hidden and ignored files and found the two active normalized owners, the generated merge, the hashed Togo sibling, generated indexes/catalogs, and related reports/scripts.
- The source-duplicate relationship is not identity-safe as represented. The KOMODO owner is named `PYRODICTIUM ABYSSI medium`, has pH 5.5-6.0, and was made chemically identical by a `dsmz-resolver-v1.0` event that copied DSMZ Medium 508 solely by numeric source ID; that does not by itself prove that KOMODO Medium 508 denotes DSMZ Medium 508.
- The generated `parent_media.path` for `pyrodictium_abyssi_medium` is `data/normalized_yaml/bacterial/pyrodictium_abyssi_medium.yaml`, but a `find data/normalized_yaml -name pyrodictium_abyssi_medium.yaml` search found only `data/normalized_yaml/archaea/pyrodictium_abyssi_medium.yaml`.
- `NiCl2 x 6 H2O` is again grounded to anhydrous `CHEBI:34887` / `nickel dichloride`; the supplied compound is the hexahydrate.

## Evidence

- DSMZ and MediaDive 508 support the main direct formula: KCl 0.33 g, MgCl2 x 6 H2O 0.52 g, CaCl2 x 2 H2O 0.29 g, NH4Cl 0.33 g, KH2PO4 0.33 g, Sodium resazurin 0.5 ml of 0.1% w/v stock, Na2CO3 1 g, Na-pyruvate 2.5 g, Yeast extract 0.05 g, Na2S x 9 H2O 0.3 g, Distilled water 1000 ml, Trace element solution SL-4 10 ml, Seven vitamins solution 1 ml, and Wolin's vitamin solution (10x) 1 ml.
- The same source keeps Trace element solution SL-4, Seven vitamins solution, and Wolin's vitamin solution (10x) as three separate 1000 ml stock recipes. The generated record has no `solutions` block and instead stores those stock ingredients directly under final-medium `ingredients`.
- Both normalized owners already contain partial `solutions` blocks for Seven vitamins solution and Wolin's vitamin solution (10x), but the generated merge does not preserve those stock additions and neither owner has nested Trace element solution SL-4.
- DSMZ and MediaDive include two preparation scopes: the main anaerobic preparation and the SL-4 EDTA/pH preparation. The generated `preparation_steps` preserve this text, but the SL-4 stock preparation is attached to the root medium because there is no SL-4 `SolutionDescriptor`.

## Completeness

- The DSMZ/MediaDive 508 identity, pH range, main preparation text, and SL-4 preparation text are present.
- The generated formula is incomplete because all three stock boundaries are absent and the duplicate stock rows for p-aminobenzoic acid, pyridoxine, nicotinic acid, and Vitamin B12 were summed across two distinct vitamin stocks.
- The synonym/category merge with `PYRODICTIUM ABYSSI medium` is not supported by an inspected source and should not be published as a true source duplicate until KOMODO Medium 508 has been checked against its own formulation.
- Empty `target_organisms`, `growth_metrics`, and literature `references` are acceptable for this imported DSMZ recipe; the DSMZ PDF supports the recipe but does not report growth evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The generated Carboxydothermus record is conflated with a KOMODO Pyrodictium record. | `data/normalized_yaml/archaea/pyrodictium_abyssi_medium.yaml` asserts `KOMODO Medium 508`, `PYRODICTIUM ABYSSI medium`, and pH 5.5-6.0; its equality to DSMZ Medium 508 comes from an automated numeric-ID resolver, while the generated record publishes it as a source duplicate, synonym, and `archaea` category on the Carboxydothermus canonical record. | Both normalized owners and the duplicate-link/merge rule that accepted this source pair. |
| major | The source-duplicate path is broken. | The generated record and the bacterial owner point at `data/normalized_yaml/bacterial/pyrodictium_abyssi_medium.yaml`; exhaustive `find` under `data/normalized_yaml` found the owner only under `data/normalized_yaml/archaea/`. | `data/normalized_yaml/bacterial/carboxydothermus_medium_heterotroph.yaml`. |
| major | Trace element solution SL-4 is flattened into direct medium ingredients. | MediaDive 508 adds 10 ml SL-4 to the main solution; the generated record instead lists stock-strength `Na2-EDTA`, `FeSO4 x 7 H2O`, `ZnSO4 x 7 H2O`, `MnCl2 x 4 H2O`, `H3BO3`, `CoCl2 x 6 H2O`, `CuCl2 x 2 H2O`, `NiCl2 x 6 H2O`, and `Na2MoO4 x 2 H2O` as final direct rows. | `data/normalized_yaml/bacterial/carboxydothermus_medium_heterotroph.yaml`, `data/normalized_yaml/archaea/pyrodictium_abyssi_medium.yaml`, and/or merge regeneration logic. |
| major | Vitamin stocks are only partially nested and are re-flattened in the generated merge. | DSMZ/MediaDive 508 adds 1 ml Seven vitamins solution and 1 ml Wolin's vitamin solution (10x). The normalized owners moved only five rows into partial stock descriptors, and the generated record again has direct vitamin rows including summed rows such as `Vitamin B12 0.101 G_PER_L` from two distinct stock recipes. | Both normalized owners plus `merge_recipes.py` if it cannot preserve existing `solutions`. |
| minor | `NiCl2 x 6 H2O` is grounded to anhydrous nickel chloride. | The source label specifies the hexahydrate but the generated row uses `CHEBI:34887`; the packaged MIM snapshot contains a hydrate-specific `CHEBI:53542` mapping. | Both normalized owners, the SL-4 solution owner, or the upstream MediaDive compound resolver for compound 40. |
| minor | `Calcium D-(+)-pantothenate` lacks its CHEBI-keyed MIM mirror where it remains direct. | The direct Wolin row in the normalized and generated records has `term: CHEBI:31345` but no `mediaingredientmech_chebi_term`; the exact label maps to `CHEBI:31345` in `label_index.csv`. | Both normalized owners, or the MIM enrichment backfill. |

## Recommended Edits

1. Re-evaluate KOMODO Medium 508 from a KOMODO source before keeping `pyrodictium_abyssi_medium` linked to DSMZ/MediaDive 508; if the numeric-ID DSMZ copy was wrong, remove the Carboxydothermus formula, source-duplicate relationship, synonym, and `archaea` category from this merge group.
2. If the Pyrodictium relationship survives source verification, correct `parent_media.path` to `data/normalized_yaml/archaea/pyrodictium_abyssi_medium.yaml` and keep reciprocal links under the actual owner path.
3. In the DSMZ/MediaDive 508 owner, remove SL-4, Seven vitamins, and Wolin stock components from root `ingredients`; add `solutions` entries for `mediadive.solution:20` at 10 `ML_PER_L`, `mediadive.solution:1038` at 1 `ML_PER_L`, and `mediadive.solution:5980` at 1 `ML_PER_L`.
4. Preserve the SL-4 EDTA/pH preparation on the SL-4 stock descriptor or `mediadive_20_Trace_element_solution_SL-4.yaml`, not as a root medium step.
5. Change merge generation so regenerated `data/merge_yaml/merged/carboxydothermus_medium_heterotroph.yaml` preserves complete stock descriptors instead of flattening stocks back to stock-strength direct rows.
6. Repair `NiCl2 x 6 H2O` and `Calcium D-(+)-pantothenate` MIM/CHEBI mirrors where those rows remain after stock reconstruction, append focused curation events to changed owners, and regenerate merged products.

## Follow-up Checks

- Rerun focused open-schema, strict, reference, and term validators against each edited normalized owner and against the regenerated `data/merge_yaml/merged/carboxydothermus_medium_heterotroph.yaml`.
- Rerun `just verify-merges` or the narrowest documented merge-freshness check to prove the generated merge no longer re-flattens solution composition.
- Manually compare the regenerated Carboxydothermus owner and merge against DSMZ Medium 508 or `/download/medium/508/json`, checking all three stock additions and the two preparation scopes.
- If the Pyrodictium link is retained, inspect KOMODO Medium 508 directly and verify that its name, pH, DSMZ cross-reference, and ingredient rows really denote DSMZ Medium 508 before restoring a `SOURCE_DUPLICATE` relationship.

## Additional Notes

- The related Togo M2610 `Carboxydothermus Medium (Heterotroph)` record resolves to a separate generated sibling, `data/merge_yaml/merged/carboxydothermus_medium_heterotroph__1e220aac.yaml`; that record was not judged here.
- The existing `mediadive_20_Trace_element_solution_SL-4.yaml`, `mediadive_1038_Seven_vitamins_solution.yaml`, and `mediadive_5980_Wolin_s_vitamin_solution_10x.yaml` solution owners also preserve their `1000 ml` water rows as `PERCENT_V_V`, which should be repaired when the owning medium starts referencing them.

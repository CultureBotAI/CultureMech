# YAML Record Review: Archaeoglobus profundus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/archaeoglobus_profundus_medium__007ec71e.yaml
- Started UTC: 2026-09-21T14:13:40Z
- Finished UTC: 2026-09-21T14:15:39Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed record | `data/merge_yaml/merged/archaeoglobus_profundus_medium__007ec71e.yaml` |
| Authoritative owner | `data/normalized_yaml/archaea/TOGO_M1672_Archaeoglobus_profundus_Medium.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:008230` |
| Name | `archaeoglobus_profundus_medium` |
| Original name | `Archaeoglobus profundus Medium` |
| Category | `archaea` |
| Source | TOGO `M1672`, original NBRC medium `M877` |
| Generated state | Generated merge from one source recipe, fingerprint `007ec71ed2aa8cb1d7c7390f99611833571359335c7f0ee486b7447ef0816850` |

The target is the generated canonical merge for a single TOGO/NBRC source record. Future scientific fixes belong in `data/normalized_yaml/archaea/TOGO_M1672_Archaeoglobus_profundus_Medium.yaml`; the reviewed file should be regenerated, not edited directly.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/archaeoglobus_profundus_medium__007ec71e.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/archaeoglobus_profundus_medium__007ec71e.yaml --out /private/tmp/archaeoglobus_profundus_medium__007ec71e.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference snippets | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/archaeoglobus_profundus_medium__007ec71e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed, but vacuously: 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/archaeoglobus_profundus_medium__007ec71e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The only emitted warning was the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone records under `history/`. |
| `just` validator entrypoints | Not run | The repository `uv` environment currently fails before target-specific validation under Python 3.13 while building `llvmlite==0.46.0`, so the same LinkML/reference/term tools were run via an offline Python 3.11 no-project environment. |

## Identity and Grounding

The stable ID and source identity agree: `CultureMech:008230` is registered to `data/normalized_yaml/archaea/TOGO_M1672_Archaeoglobus_profundus_Medium.yaml`, the generated record is `merged_from: [TOGO_M1672_Archaeoglobus_profundus_Medium]`, and the record carries TOGO `M1672` / NBRC `M877` provenance for `Archaeoglobus profundus Medium`.

The inspected TOGO payload and NBRC page agree on the source formulation: KP buffer, `MgCl2.6H2O 0.75 g`, `CaCl2.2H2O 0.15 g`, `NH4Cl 0.54 g`, `NaCl 30 g`, `Na2SO4 2.4 g`, `Na2S2O3.5H2O 2.4 g`, sodium acetate `0.8 g`, sodium pyruvate `1.1 g`, Bacto Yeast Extract `0.5 g`, `Fe(NH4)2(SO4)2.7H2O 2 mg`, Trace elements solution `2 ml`, Vitamin solution `2 ml`, Resazurin `1 mg`, `Na2CO3 1 g`, `Na2S.9H2O 0.36 g`, and a 1 L final volume of distilled water.

Most exact hydrate-sensitive final-medium ingredients are grounded to matching CHEBI terms, including water, sodium chloride, calcium chloride dihydrate, magnesium dichloride hexahydrate, sodium sulfide nonahydrate, sodium thiosulfate pentahydrate, and ferrous ammonium sulfate heptahydrate. Three salt identities are too broad or adjacent:

- `CoCl2.6H2O` is grounded as generic cobalt dichloride (`CHEBI:35696`) rather than cobalt chloride hexahydrate.
- `NiCl2.6H2O` is grounded as generic nickel dichloride (`CHEBI:34887`) rather than nickel chloride hexahydrate.
- `Ca-pantothenate` is grounded as `(R)-pantothenate` (`CHEBI:29032`), which drops the calcium salt identity supplied by the NBRC vitamin stock.

## Evidence

Supported:

- Source identity is supported by both the TOGO `M1672` payload and the NBRC `NO=877` source page.
- The top-level medium label, category, physical state, and complex/undefined classification are consistent with an archaeal NBRC complex liquid medium.
- The source supports the three stock additions as stock volumes in the final liter: `5 ml` KP buffer, `2 ml` trace elements solution, and `2 ml` vitamin solution.
- The source supports an NBRC-local KP buffer made from `119 g KH2PO4`, `21 g K2HPO4`, and 1 L distilled water, autoclaved under `N2`.
- The source supports an NBRC-local trace elements solution made from NTA, `FeCl3.6H2O`, `MnCl2.4H2O`, `CoCl2.6H2O`, `CaCl2.2H2O`, `ZnCl2`, `CuCl2.2H2O`, `H3BO3`, `Na2MoO4.2H2O`, `NaCl`, `NiCl2.6H2O`, `Na2SeO4`, `Na2WO4`, and 1 L distilled water.
- The source supports an NBRC-local vitamin solution with milligram quantities of biotin, folic acid, pyridoxine-HCl, thiamine-HCl, riboflavin, nicotinic acid, Ca-pantothenate, p-aminobenzoic acid, vitamin B12, and 1 L distilled water.
- The normalized owner has current import-tracking rows for the unresolved summed `NaCl` and `CaCl2.2H2O` duplicates, and concentration-plausibility rows for the obviously stock-scale `FeCl3.6H2O` and vitamin concentrations.

Unsupported or over-scoped:

- The generated merge still reports `Distilled water` as `4.0 G_PER_L` with `[Merged 4 duplicates: 1.0, 1.0, 1.0, 1.0]`, even though the normalized owner was repaired on 2026-09-02 to collapse that row to `1.0 G_PER_L`.
- The normalized owner still models source liters of water as grams per liter, and it no longer represents the KP, trace-elements, and vitamin-stock water rows as distinct stock-solution solvent rows.
- The generated and normalized records flatten stock formulas into the top-level medium. As a result, `119 g/L` KH2PO4, `21 g/L` K2HPO4, the trace stock salts, and the vitamin-stock milligram values are presented as final-medium `G_PER_L` concentrations rather than stock composition.
- The `solutions` entries encode `5 ml`, `2 ml`, and `2 ml` source additions as `G_PER_L`. The KP entry has empty composition; the trace and vitamin entries point to generic MediaDive solutions that do not match NBRC M877's local stocks.
- Final-medium `NaCl` is stored as `31.0 G_PER_L`, a sum of source final-medium `30 g` plus trace-stock `1 g`. Final-medium `CaCl2.2H2O` is stored as `0.25 G_PER_L`, a sum of source final-medium `0.15 g` plus trace-stock `0.1 g`.
- `Fe(NH4)2(SO4)2.7H2O` and `Resazurin` are final-medium milligram ingredients in NBRC but appear as `2 G_PER_L` and `1 G_PER_L`.
- The NBRC procedure is almost entirely absent: the record does not retain pH unadjusted, exclusion of KP/vitamin/Na2CO3/Na2S during initial mixing, H2/CO2 dispense gas and butyl-rubber sealing, separate N2 autoclaving of KP and 5% Na2S, filter sterilization of vitamin and 10% Na2CO3 stocks, anaerobic post-sterilization addition, or 150 kPa H2/CO2 pressurization.

## Completeness

- The material composition is incomplete because the three NBRC-local stocks are not represented as bounded local solution recipes or nested stock compositions.
- Preparation is incomplete enough to make the encoded record non-reconstructive: a reader cannot recover the required anaerobic handling, sterilization split, post-autoclave additions, or final gas pressure from the YAML.
- Conditions are incomplete: `pH unadjusted` and `H2/CO2 (80/20)` pressure handling are source claims but only unscoped gas placeholders survive in the record.
- Growth evidence is not present. That is acceptable for this imported database recipe because neither the TOGO payload nor the NBRC page provides a strain-level growth experiment.
- Empty optional slots such as target organisms, growth metrics, and storage conditions were not treated as defects where the inspected sources did not assert a value.
- An ignored-inclusive search across `data/normalized_yaml`, `data/merge_yaml`, the stable-ID registry, recipe catalog, media-content manifest, and import-tracking reports found only the expected normalized owner, generated merge, registry/catalog/index rows, and existing import diagnostics for this record. It found no alternate maintained NBRC M877 record that already preserves the missing KP, trace, vitamin, and preparation hierarchy for `CultureMech:008230`.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated merge is stale and still exposes the pre-repair `Distilled water` duplicate sum. | `data/merge_yaml/merged/archaeoglobus_profundus_medium__007ec71e.yaml` reports `Distilled water` as `4.0 G_PER_L` with four merged `1.0` parts. The authoritative normalized record has `1.0 G_PER_L` and a 2026-09-02 `repair_merged_duplicates.py` curation event. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/archaea/TOGO_M1672_Archaeoglobus_profundus_Medium.yaml` after the normalized fixes. |
| Major | The three source stock solutions are flattened or linked to the wrong MediaDive stocks, so many stock concentrations are being asserted as final-medium concentrations. | NBRC M877 defines KP, trace-elements, and vitamin stocks local to this medium. The record keeps their components as top-level ingredients; leaves `KP buffer*` with `composition: []`; links Trace elements solution to `mediadive.solution:6129`, whose YAML contains ZnSO4, MnCl2, MoO3, CuSO4, and Co(NO3)2; and links Vitamin solution to `mediadive.solution:6241`, whose YAML contains cyanocobalamine, thiamine HCl, biotin, and 100 ml water rather than NBRC's 1 L nine-vitamin stock. | `data/normalized_yaml/archaea/TOGO_M1672_Archaeoglobus_profundus_Medium.yaml` |
| Major | Final-medium milligram and stock-addition volumes were imported as `G_PER_L`. | `Fe(NH4)2(SO4)2.7H2O 2 mg`, `Resazurin 1 mg`, and all NBRC vitamin-stock milligram quantities are stored with `unit: G_PER_L`; the `5 ml` KP, `2 ml` trace, and `2 ml` vitamin additions are also stored as `G_PER_L` solution concentrations. | `data/normalized_yaml/archaea/TOGO_M1672_Archaeoglobus_profundus_Medium.yaml` |
| Major | Duplicate cleanup summed chemically distinct final-medium and stock-solution rows. | Import tracking already flags `NaCl 31.0 G_PER_L` as `30.0;1.0` and `CaCl2.2H2O 0.25 G_PER_L` as `0.15;0.1`; NBRC shows the larger values in the final medium and the smaller values inside the trace-elements stock. | `data/normalized_yaml/archaea/TOGO_M1672_Archaeoglobus_profundus_Medium.yaml`; if multiple TOGO imports share the same pattern, the TOGO importer or duplicate-cleanup rule also needs a guarded stock-boundary fix. |
| Major | Required preparation and condition text was dropped. | The NBRC source instructs anaerobic dispensing under H2/CO2 (80/20), butyl-rubber sealing, separate N2 autoclaving of KP and Na2S, filter sterilization of vitamin and Na2CO3, anaerobic post-sterilization addition of four solutions, and pressurization to 150 kPa. None of those scoped steps are represented; `H2`, `CO2`, `N2`, and `NaOH` survive only as variable ingredients. | `data/normalized_yaml/archaea/TOGO_M1672_Archaeoglobus_profundus_Medium.yaml` |
| Major | Three exact supplied chemical forms have broader or adjacent ontology grounding. | `CoCl2.6H2O` is linked to cobalt dichloride, `NiCl2.6H2O` is linked to nickel dichloride, and `Ca-pantothenate` is linked to `(R)-pantothenate`, losing the source hydrate or calcium-salt identity. | `data/normalized_yaml/archaea/TOGO_M1672_Archaeoglobus_profundus_Medium.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/archaea/TOGO_M1672_Archaeoglobus_profundus_Medium.yaml`, move the KP buffer, trace-elements solution, and vitamin solution into NBRC-local `solutions` entries with their own nested compositions, 1 L water rows, and preparation notes. Do not reuse `mediadive.solution:6129` or `mediadive.solution:6241` for these local NBRC stock formulas.
2. Store the three stock additions as volumes from the final recipe, not as `G_PER_L`: `5 ml` KP buffer, `2 ml` trace elements solution, and `2 ml` vitamin solution per 1 L final medium.
3. Restore final-medium amounts from the NBRC source after separating stock rows: `NaCl 30 g`, `CaCl2.2H2O 0.15 g`, `Fe(NH4)2(SO4)2.7H2O 2 mg`, `Resazurin 1 mg`, and 1 L final distilled water.
4. Preserve the NBRC preparation and condition text as scoped preparation notes or structured condition fields, including `pH unadjusted`, the H2/CO2 (80/20) anaerobic stream, butyl-rubber sealing, separate sterilization of KP/Na2S/vitamin/Na2CO3, anaerobic post-sterilization addition, and 150 kPa H2/CO2 pressurization.
5. Re-ground `CoCl2.6H2O`, `NiCl2.6H2O`, and `Ca-pantothenate` to exact salt/hydrate terms if available in the packaged MIM/CHEBI label index; leave them unresolved rather than keeping broad salts if exact terms are unavailable.
6. Regenerate `data/merge_yaml/merged/archaeoglobus_profundus_medium__007ec71e.yaml` from the normalized owner so the reviewed generated record picks up the 2026-09-02 water repair and the new stock-boundary curation.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/archaea/TOGO_M1672_Archaeoglobus_profundus_Medium.yaml`.
- Run `just validate-strict data/normalized_yaml/archaea/TOGO_M1672_Archaeoglobus_profundus_Medium.yaml`.
- Run `just validate-terms data/normalized_yaml/archaea/TOGO_M1672_Archaeoglobus_profundus_Medium.yaml`.
- Run `just validate-references data/normalized_yaml/archaea/TOGO_M1672_Archaeoglobus_profundus_Medium.yaml` after adding any structured reference/evidence entries.
- Run `just review-media-content` and confirm no `DIFFERING_PARTS` duplicate remains for `CultureMech:008230`.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating the derived merge.
- Manually compare the regenerated record against the NBRC `NO=877` page and TOGO `gmdb_medium_by_gmid?gm_id=M1672` payload to confirm that final-medium ingredients, local stocks, and preparation text are no longer conflated.

## Additional Notes

- The ignored-inclusive pre-report search under `reports/yaml_record_review` found no prior report for `archaeoglobus_profundus_medium__007ec71e`, `CultureMech:008230`, or `TOGO_M1672_Archaeoglobus_profundus_Medium`.
- The generated record lacks the normalized owner's 2026-09-02 `REPAIRED_SUMMED_DUPLICATE_MERGE` history entry, which is another signal that the merge was generated before the latest normalized curation event.
- TOGO public `/medium/M1672` pages should not be treated as fetchable source text; the public page returns a JavaScript shell, while `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1672` returned the inspected structured payload for this review.

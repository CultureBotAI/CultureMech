# YAML Record Review: Archaeoglobus profundus medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/archaeoglobus_profundus_medium__ae83c6c3.yaml
- Started UTC: 2026-09-21T14:20:20Z
- Finished UTC: 2026-09-21T14:21:57Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed record | `data/merge_yaml/merged/archaeoglobus_profundus_medium__ae83c6c3.yaml` |
| Authoritative owner | `data/normalized_yaml/archaea/TOGO_M1585_Archaeoglobus_profundus_medium.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:008135` |
| Name | `archaeoglobus_profundus_medium` |
| Original name | `Archaeoglobus profundus medium` |
| Category | `archaea` |
| Source | TOGO `M1585`, original NBRC medium `M393` |
| Generated state | Generated merge from one source recipe, fingerprint `ae83c6c3c4d4ec2decb529b692fece1d486c927d3c45616e5e9ca5628baf0764` |

The target is the generated canonical merge for a single TOGO/NBRC source record. Future scientific fixes belong in `data/normalized_yaml/archaea/TOGO_M1585_Archaeoglobus_profundus_medium.yaml`; the reviewed merge should be regenerated, not edited directly.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/archaeoglobus_profundus_medium__ae83c6c3.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/archaeoglobus_profundus_medium__ae83c6c3.yaml --out /private/tmp/archaeoglobus_profundus_medium__ae83c6c3.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference snippets | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/archaeoglobus_profundus_medium__ae83c6c3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed, but vacuously: 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/archaeoglobus_profundus_medium__ae83c6c3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The only emitted warning was the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone records under `history/`. |
| `just` validator entrypoints | Not run | The repository `uv` environment currently fails before target-specific validation under Python 3.13 while building `llvmlite==0.46.0`, so the same LinkML/reference/term tools were run via an offline Python 3.11 no-project environment. |

## Identity and Grounding

The stable ID and source identity agree: `CultureMech:008135` is registered to `data/normalized_yaml/archaea/TOGO_M1585_Archaeoglobus_profundus_medium.yaml`, the generated record is merged from `TOGO_M1585_Archaeoglobus_profundus_medium`, and the source notes identify TOGO `M1585` / NBRC `M393`.

The inspected TOGO payload and NBRC page agree on the final-medium formula: KCl, MgCl2.6H2O, MgSO4.7H2O, NH4Cl, CaCl2.2H2O, K2HPO4, NaCl, NaHCO3, sodium acetate, Na2SO4, Bacto Yeast Extract, Fe(NH4)2(SO4)2.7H2O, 10 ml Trace element solution, Resazurin, Na2S.9H2O, and 1 L final distilled water.

Most hydrate-sensitive salts in the final medium and stock are grounded to matching terms, including MgCl2.6H2O, MgSO4.7H2O, CaCl2.2H2O, Na2S.9H2O, Fe(NH4)2(SO4)2.7H2O, FeSO4.7H2O, ZnSO4.7H2O, CuSO4.5H2O, KAl(SO4)2.12H2O, and MnSO4.2H2O. Two grounding issues remain:

- `NiCl2.6H2O` is grounded as generic nickel dichloride (`CHEBI:34887`), losing the hexahydrate identity.
- `CoSO4.7H2O` is grounded as cobalt(2+) sulfate heptahydrate; the heptahydrate formula should be verified because the CHEBI label is not exact in the same way as the other hydrate labels.

## Evidence

Supported:

- Source identity and the TOGO-to-NBRC provenance are supported by TOGO `M1585` and the original NBRC `NO=393` page.
- The final medium contains a 10 ml addition of a local `Trace element solution`, not a MediaDive global trace-element solution.
- The local trace stock contains NTA, MgSO4.7H2O, MnSO4.2H2O, NaCl, FeSO4.7H2O, CoSO4.7H2O, CaCl2.2H2O, ZnSO4.7H2O, CuSO4.5H2O, KAl(SO4)2.12H2O, H3BO3, Na2MoO4.2H2O, NiCl2.6H2O, Na2SeO3.5H2O, and 1 L distilled water.
- NBRC supports anaerobic preparation: dissolve without bicarbonate and sulfide, boil briefly, cool under H2/CO2, add bicarbonate, adjust pH to 6.5, dispense into serum bottles under H2/CO2, seal, autoclave, reduce with anaerobic sterile neutral sulfide stock before use, and pressurize to 2 bar.
- Existing import tracking flags the `MgSO4.7H2O` and `NaCl` rows as sums of differing duplicate parts, and flags `Resazurin 1 G_PER_L` as an indicator unit slip.

Unsupported or over-scoped:

- The generated merge still reports `Distilled water` as `2.0 G_PER_L`, even though the normalized owner was repaired on 2026-09-02 to collapse that row to `1.0 G_PER_L`.
- The normalized owner still models 1 L water as `1.0 G_PER_L` and lacks a separate water row inside a local trace-stock composition.
- `MgSO4.7H2O`, `NaCl`, and `CaCl2.2H2O` are sums of final-medium rows plus Trace element solution rows. NBRC lists `3.45 g`, `18 g`, and `0.14 g` in the final medium and `3 g`, `1 g`, and `0.1 g` in the stock.
- The trace stock is flattened into top-level ingredient rows, so stock-only NTA, FeSO4, CoSO4, KAl(SO4)2, H3BO3, Mo, Ni, Se, W, and other rows are presented as final-medium concentrations.
- `Fe(NH4)2(SO4)2.7H2O`, `Resazurin`, and trace-stock Na2SeO3.5H2O are milligram source quantities encoded as grams per liter.
- `Trace element solution*` is encoded as `10 G_PER_L` and linked to `mediadive.solution:6187`; that referenced solution uses Na2-EDTA, FeCl3.6H2O, MnCl2.4H2O, ZnCl2.6H2O, CoCl2.6H2O, and Na2MoO4.2H2O, which do not match the NBRC M393 local stock.
- The source preparation text is not represented; the record only keeps unscoped `sodium bicarbonate`, CO2, H2, and KOH variable ingredient rows.

## Completeness

- The composition is incomplete because the NBRC-local Trace element solution is not modeled as a local solution and its components have been lifted into the final medium.
- Preparation is incomplete: the YAML drops the boil, gas-cooling, bicarbonate addition, pH adjustment, serum bottle dispense, H2/CO2 atmosphere, autoclaving boundary, sulfide reduction, and 2 bar pressurization.
- Conditions are incomplete: pH 6.5 and the H2/CO2 atmosphere are represented only indirectly or as unscoped placeholders.
- Growth evidence is not present. That is acceptable for this imported database recipe because neither inspected source provides a strain-level growth experiment beyond the recipe name.
- Empty optional slots such as target organisms, growth metrics, and storage conditions were not treated as defects where the inspected sources did not assert a value.
- An ignored-inclusive search across `data/normalized_yaml`, `data/merge_yaml`, the stable-ID registry, recipe catalog, media-content manifest, and import-tracking reports found the expected normalized owner, generated merge, registry/catalog/index rows, and existing diagnostics for this record. It found no alternate maintained NBRC M393 record that already preserves the local Trace element solution hierarchy for `CultureMech:008135`.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated merge is stale and still exposes the pre-repair summed water row. | `data/merge_yaml/merged/archaeoglobus_profundus_medium__ae83c6c3.yaml` reports `Distilled water 2.0 G_PER_L`, while the authoritative normalized owner has `1.0 G_PER_L` plus a 2026-09-02 `repair_merged_duplicates.py` event. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/archaea/TOGO_M1585_Archaeoglobus_profundus_medium.yaml` after normalized fixes. |
| Major | The local NBRC trace stock is flattened and linked to the wrong stock recipe. | NBRC M393 defines a local 10 ml Trace element solution. The record places that stock's components at the top level and links the addition to `mediadive.solution:6187`, whose composition is an unrelated EDTA/FeCl3/MnCl2/ZnCl2/CoCl2/Mo stock. | `data/normalized_yaml/archaea/TOGO_M1585_Archaeoglobus_profundus_medium.yaml` |
| Major | Duplicate cleanup summed final-medium and stock-solution rows. | Existing import tracking flags `MgSO4.7H2O 6.45 G_PER_L` as `3.45;3.0` and `NaCl 19.0 G_PER_L` as `18.0;1.0`; `CaCl2.2H2O 0.24000000000000002 G_PER_L` has the same final-plus-stock pattern from `0.14;0.1`. | `data/normalized_yaml/archaea/TOGO_M1585_Archaeoglobus_profundus_medium.yaml`; if this pattern recurs in TOGO imports, the TOGO importer or duplicate-cleanup rule should preserve stock scope. |
| Major | Multiple milligram quantities were imported as `G_PER_L`. | NBRC lists final Fe(NH4)2(SO4)2.7H2O at 2 mg, final Resazurin at 1 mg, and stock Na2SeO3.5H2O at 0.3 mg; the YAML stores `2`, `1`, and `0.3` as `G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1585_Archaeoglobus_profundus_medium.yaml` |
| Major | Preparation and conditions were dropped. | The NBRC source gives an anaerobic H2/CO2 serum-bottle protocol with pH 6.5 and 2 bar overpressure, but the YAML has no preparation steps and only keeps variable CO2, H2, bicarbonate, and KOH placeholders. | `data/normalized_yaml/archaea/TOGO_M1585_Archaeoglobus_profundus_medium.yaml` |
| Minor | Two hydrate groundings need exact-form audit. | `NiCl2.6H2O` is grounded to generic nickel dichloride, and `CoSO4.7H2O` needs confirmation against an exact heptahydrate CHEBI term. | `data/normalized_yaml/archaea/TOGO_M1585_Archaeoglobus_profundus_medium.yaml` |

## Recommended Edits

1. Replace the `mediadive.solution:6187` link with an NBRC M393-local `Trace element solution` that contains exactly the stock components and stock concentrations printed by NBRC.
2. Store the trace addition as `10 ml` per final liter, not as `10 G_PER_L`.
3. Move trace-stock-only components under that local stock and split `MgSO4.7H2O`, `NaCl`, and `CaCl2.2H2O` back into source-supported final-medium rows and stock rows.
4. Correct milligram quantities for final Fe(NH4)2(SO4)2.7H2O, final Resazurin, and stock Na2SeO3.5H2O.
5. Restore source preparation text or structured steps for boiling, H2/CO2 cooling and dispensing, bicarbonate and sulfide timing, pH 6.5 adjustment, serum-bottle sealing, autoclaving, and 2 bar pressurization.
6. Remove unscoped variable ingredient placeholders that only came from preparation text once pH/gas/adjuster/reducer details are represented in the correct slots.
7. Re-ground or explicitly leave unresolved `NiCl2.6H2O` and audit `CoSO4.7H2O`.
8. Regenerate `data/merge_yaml/merged/archaeoglobus_profundus_medium__ae83c6c3.yaml` from the normalized owner.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/archaea/TOGO_M1585_Archaeoglobus_profundus_medium.yaml`.
- Run `just validate-strict data/normalized_yaml/archaea/TOGO_M1585_Archaeoglobus_profundus_medium.yaml`.
- Run `just validate-terms data/normalized_yaml/archaea/TOGO_M1585_Archaeoglobus_profundus_medium.yaml`.
- Run `just validate-references data/normalized_yaml/archaea/TOGO_M1585_Archaeoglobus_profundus_medium.yaml` after adding any structured source references.
- Run `just review-media-content` and confirm no duplicate-sum row remains for `CultureMech:008135`.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating the derived merge.
- Manually compare the regenerated record against the NBRC `NO=393` page and TOGO `gmdb_medium_by_gmid?gm_id=M1585` payload to confirm that final-medium rows, local stock rows, and preparation conditions are no longer conflated.

## Additional Notes

- The ignored-inclusive pre-report search under `reports/yaml_record_review` found no prior report for `archaeoglobus_profundus_medium__ae83c6c3`, `CultureMech:008135`, or `TOGO_M1585_Archaeoglobus_profundus_medium`.
- The generated record lacks the normalized owner's 2026-09-02 `REPAIRED_SUMMED_DUPLICATE_MERGE` history entry, which is another signal that the merge was generated before the latest normalized curation event.
- The media-content manifest correctly marks this record `NEEDS_REVIEW` for variable-concentration placeholders, but it does not flag the wrong `mediadive.solution:6187` link or the unflagged `CaCl2.2H2O` final-plus-stock sum.

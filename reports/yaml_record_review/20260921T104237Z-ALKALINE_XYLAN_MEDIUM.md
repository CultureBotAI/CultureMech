# YAML Record Review: Alkaline Xylan Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALKALINE_XYLAN_MEDIUM.yaml
- Started UTC: 2026-09-21T10:40:20Z
- Finished UTC: 2026-09-21T10:42:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/ALKALINE_XYLAN_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007758` |
| Name | `alkaline_xylan_medium` |
| Original name | `Alkaline Xylan Medium` |
| Category | `bacterial` |
| Generated status | Generated merge from one maintained normalized source |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M122_Alkaline_Xylan_Medium.yaml` |
| Upstream source | TOGO `M122`, imported from JCM `JCM_M130` / GRMD `130` |
| Merge fingerprint | `1a3f733c5d575cc42783fead0fc4003b1e3568eb33e6265c169f420095762de7` |

The generated record was reviewed read-only. Future fixes should land in the
normalized TOGO M122 source record or, if the milligram-to-gram and pH-adjuster
loss is import-owned, in the TOGO/JCM importer followed by regeneration of
`data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALKALINE_XYLAN_MEDIUM.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALKALINE_XYLAN_MEDIUM.yaml --out /private/tmp/ALKALINE_XYLAN_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALKALINE_XYLAN_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALKALINE_XYLAN_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils`/`pkg_resources` deprecation warning |
| Embedded curation history | Not checked | No focused validator is documented for embedded `MediaRecipe.curation_history`; `just validate-history` validates standalone files under `history/` |

The usual `just` wrappers were not rerun here because target-specific `just
validate-schema`, `just validate-strict`, and `just validate-terms` currently
fail before target validation while the project `uv` environment attempts to
build `llvmlite==0.46.0` under Python 3.13. The no-project validator commands
above use Python 3.11 and the cached validator packages instead.

## Identity and Grounding

The target identity is coherent: the merge record, its sole `merged_from`
entry, and the maintained normalized parent all identify TOGO Medium M122 /
JCM Medium 130, `Alkaline Xylan Medium`. The fetched TOGO API record for
`M122` reports `original_media_id: JCM_M130`, the JCM GRMD 130 URL, and
`ph: 10.0`; the fetched JCM GRMD 130 page is the same medium number and title.

The exact ignored-files-including search:

```bash
rg -n "M122|JCM_M130|ALKALINE_XYLAN_MEDIUM|Alkaline xylan medium|JCM 130|GRMD 130" data/normalized_yaml data/merge_yaml --glob '*.yaml' --no-ignore --hidden
```

found the intended parent
`data/normalized_yaml/bacterial/TOGO_M122_Alkaline_Xylan_Medium.yaml` and an
adjacent same-name TOGO `M2692` / ATCC-derived
`data/normalized_yaml/bacterial/TOGO_M2692_Alkaline_xylan_medium.yaml`. The
target is not conflated with the adjacent record: it keeps TOGO `M122`, JCM
`M130`, CultureMech `007758`, and only the TOGO M122 parent in `merged_from`.

Ingredient ontology grounding is mostly compatible with the source identities:
water, magnesium sulfate heptahydrate, calcium chloride dihydrate, dipotassium
hydrogen phosphate, resazurin, iron(2+) sulfate heptahydrate, manganese(II)
sulfate, and ammonium nitrate are plausible for the listed JCM/TOGO components.
The record does not ground xylan or Hipolypepton/Polypepton, which is acceptable
for supplier- or material-specific undefined components pending exact
publication-time resolution.

## Evidence

The fetched JCM GRMD 130 table supports these per-liter formulation rows:

| Component | Source amount | Generated amount |
|---|---:|---:|
| Distilled water | 1 L | `1 G_PER_L` |
| Xylan | 10 g | `10 G_PER_L` |
| K2HPO4 | 1 g | `1 G_PER_L` |
| NH4NO3 | 2 g | `2 G_PER_L` |
| MgSO4 x 7H2O | 200 mg | `200 G_PER_L` |
| MnSO4 x H2O | 5 mg | `5 G_PER_L` |
| FeSO4 x 7H2O | 5 mg | `5 G_PER_L` |
| CaCl2 x 2H2O | 100 mg | `100 G_PER_L` |
| Yeast extract | 3 g | `3 G_PER_L` |
| Hipolypepton | 300 mg | `300 G_PER_L` |
| Resazurin | 1 mg | `1 G_PER_L` |

The fetched TOGO M122 API record agrees with the JCM milligram values for
MgSO4 x 7H2O, CaCl2 x 2H2O, Resazurin, FeSO4 x 7H2O, MnSO4 x H2O, and
Polypepton. The generated CultureMech record kept the source numbers for those
six rows but changed their units from `mg` into `G_PER_L`, so the final-medium
values are 1000-fold too high.

Both inspected source records also support a pH adjustment to 10.0 using
filter-sterilized 10% sodium carbonate solution. The generated record has no
pH, no preparation step, and only an empty variable `NaCO3 solution` with no
composition or 10% concentration. The source supports a filter-sterilized
10% Na2CO3 pH adjuster, not a bare empty `NaCO3` stock recipe.

The JCM page carries a default instruction to autoclave at 121 C for 15 min
unless a medium states otherwise. The generated record has no sterilization
step for the basal medium and therefore cannot be followed as a complete
protocol.

No claim-level `evidence` objects or structured `references` are present. The
TOGO and JCM source URLs are retained only as free text in `notes`.

## Completeness

Consequential gaps:

- Correct milligram-to-gram conversion is missing for every milligram-scale row.
- The source water volume is present but unit-corrupted.
- The final pH and pH-adjustment step are missing.
- Filter sterilization of the 10% sodium carbonate solution is missing.
- Basal autoclaving at 121 C for 15 min is missing.
- TOGO/JCM provenance is not represented in structured `sources`, `source_data`,
  or `references`.

Empty optional slots that are not automatic defects:

- `target_organisms` and `growth_metrics` can remain empty. JCM GRMD 130 and
  TOGO M122 are formulation records, not strain growth reports.
- The supplier-specific xylan and Hipolypepton/Polypepton rows can remain
  ungrounded until the exact commercial material is resolved.

The prior-report search:

```bash
find reports/yaml_record_review -name '*ALKALINE_XYLAN_MEDIUM*' -print
```

included ignored report files and found no existing report for this exact
generated record before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Six milligram-scale rows are 1000-fold too concentrated. `MgSO4 x 7H2O`, `CaCl2 x 2H2O`, `Resazurin`, `FeSO4 x 7H2O`, `MnSO4 x H2O`, and Polypepton should be 0.2, 0.1, 0.001, 0.005, 0.005, and 0.3 g/L respectively for a 1 L recipe, not 200, 100, 1, 5, 5, and 300 g/L. This also makes `high_metal: true` suspect. | JCM GRMD 130 lists those rows in `mg`; TOGO M122 serializes the same rows with `unit: "mg"`. | `data/normalized_yaml/bacterial/TOGO_M122_Alkaline_Xylan_Medium.yaml`, or the TOGO importer if the unit conversion is generated |
| Major | Water is dimensionally wrong. The recipe says `1 G_PER_L`, but the source says 1 L distilled water for the 1 L recipe. | JCM GRMD 130 lists 1 L distilled water; TOGO M122 serializes the water row with `unit: "L"`. | `data/normalized_yaml/bacterial/TOGO_M122_Alkaline_Xylan_Medium.yaml`, or the TOGO importer |
| Major | The pH-adjustment stock was flattened into an empty `NaCO3 solution` and the actual condition/procedure was dropped. The record is missing final pH 10.0, filter sterilization, and the 10% Na2CO3 pH-adjustment boundary. | JCM GRMD 130 and TOGO M122 both instruct pH adjustment to 10.0 with filter-sterilized 10% sodium carbonate. | `data/normalized_yaml/bacterial/TOGO_M122_Alkaline_Xylan_Medium.yaml`, or the TOGO importer |
| Minor | Provenance is free-text only and source version drift is not recorded. TOGO keeps `Xylan (Tokyo Kasei or Sigma)` and `Polypepton (Nihon Pharm. Co.)`; current JCM GRMD 130 has `Xylan` and `Hipolypepton (FUJIFILM Wako)`. | The normalized and merged records preserve only the TOGO snapshot in `notes`, while the live JCM source has changed supplier labels. | `data/normalized_yaml/bacterial/TOGO_M122_Alkaline_Xylan_Medium.yaml` |

No blocker findings were found.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M122_Alkaline_Xylan_Medium.yaml`,
   convert JCM milligram rows to final g/L values: MgSO4 x 7H2O 0.2 g/L,
   CaCl2 x 2H2O 0.1 g/L, Resazurin 0.001 g/L, FeSO4 x 7H2O 0.005 g/L,
   MnSO4 x H2O 0.005 g/L, and Hipolypepton/Polypepton 0.3 g/L.
2. Replace distilled water `1 G_PER_L` with a volume representation equivalent
   to 1 L of final medium, matching the repository convention for water in
   repaired records.
3. Replace the empty `NaCO3 solution` with a 10% Na2CO3 pH-adjusting stock or
   procedural addition, preserve its filter sterilization, and record final
   pH 10.0.
4. Add the basal autoclave instruction scoped to the non-filter-sterilized
   medium portion, reflecting the JCM page default of 121 C for 15 min.
5. Recompute or remove `high_metal` after the milligram quantities are
   corrected.
6. Move TOGO M122 and JCM GRMD 130 provenance out of free-text-only `notes`
   into structured source/reference fields where the schema supports them, and
   record the TOGO-vs-live-JCM supplier-label drift in a bounded discussion or
   curation note.
7. Regenerate `data/merge_yaml/merged/ALKALINE_XYLAN_MEDIUM.yaml` and generated
   pages from the maintained source.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/TOGO_M122_Alkaline_Xylan_Medium.yaml`.
- Run `just validate-strict data/normalized_yaml/bacterial/TOGO_M122_Alkaline_Xylan_Medium.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/TOGO_M122_Alkaline_Xylan_Medium.yaml` to recheck the corrected ingredient labels and any structured stock composition.
- Run `just validate-references data/normalized_yaml/bacterial/TOGO_M122_Alkaline_Xylan_Medium.yaml` after adding structured TOGO/JCM references.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating merges.
- Manually compare the regenerated merge against fetched TOGO M122 and JCM GRMD 130 for the six milligram rows, water, pH 10.0, and filter-sterilized 10% Na2CO3 step.

## Additional Notes

- The neighboring generated record
  `data/merge_yaml/merged/alkaline_xylan_medium__40677796.yaml` is TOGO M2692
  from an ATCC recipe. Its same normalized name is a de-duplication hazard, but
  it is not the reviewed target.
- The generated target is schema-valid despite being scientifically unusable
  as written; a structural validator will not catch milligram-to-gram unit
  inflation or loss of a source pH adjustment.

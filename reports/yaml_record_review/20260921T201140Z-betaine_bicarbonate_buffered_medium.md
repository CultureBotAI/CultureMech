# YAML Record Review: Betaine+bicarbonate Buffered Medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/betaine_bicarbonate_buffered_medium.yaml`
- Started UTC: 2026-09-21T20:08:40Z
- Finished UTC: 2026-09-21T20:11:40Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Generated record | `data/merge_yaml/merged/betaine_bicarbonate_buffered_medium.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M798_Betaine_bicarbonate_Buffered_Medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:010208` |
| Name | `betaine_bicarbonate_buffered_medium` |
| Original name | `Betaine+bicarbonate Buffered Medium` |
| Source accession | `TOGO:M798`, original source `JCM_M770` |
| Merge fingerprint | `bed093bcc6ce08284705312d3f767b63ecab563259769f142b7c5e6db349b627` |
| Merge sources | `TOGO_M798_Betaine_bicarbonate_Buffered_Medium` |

The generated merge is a single-source projection of TOGO Medium M798. Per `CLAUDE.md`, `data/merge_yaml/merged/` is derived output; any future correction belongs in the normalized TOGO record or the TOGO import/nesting transform, followed by merge and page regeneration.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/betaine_bicarbonate_buffered_medium.yaml` | Passed, `No issues found` |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/betaine_bicarbonate_buffered_medium.yaml --out /private/tmp/betaine_bicarbonate_buffered_medium.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/betaine_bicarbonate_buffered_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/betaine_bicarbonate_buffered_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: this repository documents `just validate-history` for standalone records under `history/`; there is no focused embedded-`MediaRecipe.curation_history` validator for one generated merge record. |

Schema validation proves only that the YAML is structurally acceptable. It does not catch the stock-solution flattening, unit conversion, or missing preparation fields described below.

## Identity and Grounding

- **Medium identity:** supported. The record denotes TOGO Medium M798, "Betaine+bicarbonate Buffered Medium", imported from JCM GRMD 770.
- **Source identity:** supported. The TOGO API reports `gm = http://togomedium.org/medium/M798`, `name = Betaine+bicarbonate Buffered Medium`, `original_media_id = JCM_M770`, and `src_url = https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=770`; the live JCM page at GRMD 770 is headed `BETAINE+BICARBONATE BUFFERED MEDIUM`.
- **Generated-vs-maintained status:** supported. The generated merge was produced from `TOGO_M798_Betaine_bicarbonate_Buffered_Medium.yaml`; exhaustive `rg --no-ignore --hidden` searches for `CultureMech:010208`, `TOGO:M798`, `JCM_M770`, and `M798` across `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports/yaml_record_review` resolved the maintained TOGO owner and related cross-references.
- **Ingredient grounding:** partly unsupported. Exact TOGO/JCM hydrate forms are not preserved for at least `CoCl2*6H2O`, which is grounded as generic/anhydrous `CHEBI:35696` `cobalt dichloride`, and `NiCl2*H2O`, which is grounded as generic/anhydrous `CHEBI:34887` `nickel dichloride`. `DL--Calcium pantothenate` still has only a legacy `MediaIngredientMech:000926` link in this TOGO-derived record.

## Evidence

- The TOGO and JCM sources both support the M798 recipe identity and the seven named recipe boundaries: `Solution A`, `Solution B`, `Solution C`, `Phosphate solution`, `Trace metal solution`, `Mineral salt solution`, and `Vitamin solution`.
- The source formulation is nested, not a single flat list. JCM gives 915 ml of `Solution A`, 50 ml of `Solution B`, and 50 ml of `Solution C` for the final medium. Inside those solutions it gives 15 ml of `Phosphate solution`, 10 ml of `1.0 M Betaine solution`, 1 ml of `Trace metal solution`, 1 ml of `Vitamin solution`, and 12.5 ml of `Mineral salt solution`.
- The generated record correctly preserves the raw stock-component names and amounts from the TOGO API, but attaches them to the wrong level. For example, `Resazurin` and both tungsten/selenium salts are top-level ingredients at `0.5`, `0.3`, and `0.3` `G_PER_L`; in JCM they are `0.5 mg`, `0.3 mg`, and `0.3 mg` within `Solution A`, which is then added at 915 ml to the final mixture.
- The final solution volumes are also represented with concentration semantics. `Solution A`, `Solution B`, and `Solution C` are 915 ml, 50 ml, and 50 ml source additions, but the generated `solutions` array stores them as `915`, `50`, and `50` `G_PER_L`.
- The generated record loses the TOGO/JCM pH and preparation evidence. TOGO metadata reports pH `6.9-7.2`, and JCM says to autoclave `Solution A` under an 80:20 N2-CO2 mixture, filter-sterilize `Solution B` and `Solution C`, stock B and C under the same gas mixture, then combine A, B, and C aseptically and anaerobically and check the final pH.

## Completeness

- Consequential empty structures are not complete: the generated `Phosphate solution`, `1.0 M Betaine solution`, `Trace metal solution`, `Vitamin solution`, and `Mineral salt solution` entries all have `composition: []` or no parsed composition despite the TOGO/JCM sources carrying the nested contents.
- The generated record has no `ph_value` and no `preparation_steps`. A bounded `rg --no-ignore --hidden` search for `ph_value`, `preparation_steps`, `target_organisms`, and `growth` in the generated record and its normalized TOGO owner found no such slots.
- `target_organisms` and growth-evidence fields are optional and correctly empty for this source-only import; neither the TOGO M798 API payload nor the JCM GRMD 770 medium page made a strain-specific growth claim to carry into this generated record.
- `applications: [Microbial cultivation]`, `medium_type: COMPLEX`, `composition_type: UNDEFINED`, and `physical_state: LIQUID` are source-compatible high-level classifications for a JCM medium containing yeast extract.
- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -type f -name '*betaine_bicarbonate_buffered_medium.md'` found no pre-existing report for this generated record before this file was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The TOGO M798 import flattens every nested stock formulation into final-medium `ingredients`, leaving source-defined stocks empty or as unresolved placeholders. | The live TOGO payload and JCM GRMD 770 divide M798 into A/B/C plus phosphate, trace-metal, mineral-salt, and vitamin stocks. The generated record instead has all phosphate, trace-metal, mineral-salt, and vitamin components as top-level ingredients and has empty `composition: []` for several `solutions`. | `data/normalized_yaml/bacterial/TOGO_M798_Betaine_bicarbonate_Buffered_Medium.yaml` or the TOGO solution-nesting importer, then regenerate `data/merge_yaml/merged/`. |
| Major | Several source amounts are encoded with the wrong dimensional meaning. | Source ml additions for `Solution A`, `Solution B`, `Solution C`, and internal stocks are stored as `G_PER_L` concentrations, and source mass amounts from nested stock recipes are promoted as if they were final-medium g/L concentrations. | TOGO importer quantity mapping for referenced solutions and stock ingredients. |
| Major | Source pH and anaerobic preparation instructions are missing. | TOGO exposes pH `6.9-7.2`; JCM supplies autoclave/filter-sterilize/storage/final-assembly instructions under an 80:20 N2-CO2 gas mixture. The generated record has no `ph_value` and no `preparation_steps`. | TOGO importer preparation and pH mapping, or a maintained normalized patch if importer backfill is not yet available. |
| Major | At least two hydrate-specific salts are grounded to non-hydrated CHEBI terms. | The source names `CoCl2*6H2O` and `NiCl2*H2O`; the generated ingredients carry `cobalt dichloride` and `nickel dichloride`, losing the exact supplied hydrate form. | `data/normalized_yaml/bacterial/TOGO_M798_Betaine_bicarbonate_Buffered_Medium.yaml`, after exact CHEBI ID/label verification against the packaged ontology source. |
| Minor | `DL--Calcium pantothenate` remains unresolved to CHEBI in the generated TOGO record. | The item retains `MediaIngredientMech:000926` and has no primary `term`, while the repository's newer CHEBI-keyed convention expects exact CHEBI grounding or an explicit unresolved value. | Ingredient grounding for the normalized TOGO record. |

## Recommended Edits

1. Update the TOGO import/nesting path for M798 so that `Solution A`, `Solution B`, `Solution C`, `Phosphate solution`, `Trace metal solution`, `Mineral salt solution`, and `Vitamin solution` are modeled as solution records or nested `solutions` entries with their source components preserved under the right recipe boundary.
2. Preserve source volumes as volumes. The final medium should reference 915 ml A, 50 ml B, and 50 ml C; A should reference 15 ml phosphate stock; B should reference 10 ml 1.0 M betaine, 1 ml trace-metal stock, 1 ml vitamin stock, and 12.5 ml mineral-salt stock. Do not turn those ml additions into `G_PER_L`.
3. Keep stock recipe ingredient masses scoped to the stock solution that owns them, or compute supported final-medium concentrations only when the total final volume and stock volume are explicit and the unit conversion is dimensionally valid.
4. Backfill `ph_value` and `preparation_steps` from the TOGO/JCM source comments: autoclave A under 80:20 N2-CO2, filter-sterilize B and C, stock B and C under 80:20 N2-CO2, and combine A/B/C aseptically and anaerobically before checking final pH 6.9 to 7.2.
5. Re-ground `CoCl2*6H2O`, `NiCl2*H2O`, and `DL--Calcium pantothenate` against the current packaged ingredient ontology; leave any still-unresolved exact hydrate explicit rather than using a chemically broader anhydrous salt.
6. Regenerate `data/merge_yaml/merged/betaine_bicarbonate_buffered_medium.yaml` and the generated media pages after the normalized TOGO owner or import transform changes.

## Follow-up Checks

- Re-run the focused open-schema, strict-schema, reference, and term validators on the normalized TOGO owner and the regenerated merged M798 record.
- Manually diff the regenerated nested solution tree against both `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M798` and `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=770`.
- Verify no `Solution ... (see below)` entry in M798 is left with `composition: []` when TOGO/JCM provide its component table.
- Verify source ml additions are represented with volume units and that mg source entries are not silently scaled by 1000x through a `G_PER_L` default.
- Re-run the merge freshness/product checks documented in `CLAUDE.md` for merge-input edits once the maintained owner changes.

## Additional Notes

- The duplicate MediaDive/JCM normalized record `data/normalized_yaml/bacterial/betaine_bicarbonate_buffered_medium.yaml` (`CultureMech:003112`) references the same JCM GRMD 770 source and already nests a subset of trace-metal and vitamin stock ingredients. The generated TOGO merge reviewed here is not derived from that file, but it is useful as a comparison fixture because both records describe the same JCM medium.
- This report is read-only and intentionally did not edit `data/normalized_yaml/bacterial/TOGO_M798_Betaine_bicarbonate_Buffered_Medium.yaml`, `data/merge_yaml/merged/betaine_bicarbonate_buffered_medium.yaml`, generated pages, or GitHub state.

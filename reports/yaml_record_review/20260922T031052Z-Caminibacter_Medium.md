# YAML Record Review: Caminibacter Medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/Caminibacter_Medium.yaml`
- Started UTC: 2026-09-22T03:08:13Z
- Finished UTC: 2026-09-22T03:10:52Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/Caminibacter_Medium.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M361_Caminibacter_Medium.yaml` |
| ID | `CultureMech:009742` |
| Name | `caminibacter_medium` |
| Source accession | `TOGO:M361` |
| Original source | `JCM_M367` / JCM GRMD 367 |
| Category | `bacterial` |
| Medium/composition/state | `COMPLEX` / `SEMI_DEFINED` / `LIQUID` |
| Merge lineage | Single-source merge from `TOGO_M361_Caminibacter_Medium` on fingerprint `4f8c5ea29856005fe800c07d79ad1786a1ad245194ecc3a5ac27006cec387fb9` |

The reviewed YAML is a generated merge owned by the normalized TOGO M361 import. Fixes should land in `data/normalized_yaml/bacterial/TOGO_M361_Caminibacter_Medium.yaml` or in TOGO/JCM import logic, then this generated record should be regenerated.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Caminibacter_Medium.yaml` | Pass: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Caminibacter_Medium.yaml --out /private/tmp/Caminibacter_Medium.strict.tsv --workers 1 --quiet` | Pass: 1 file scanned; 0 files with errors; report at `/private/tmp/Caminibacter_Medium.strict.tsv`. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Caminibacter_Medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass: 1 file validated; 0 reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Caminibacter_Medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass. |
| Embedded curation history | `just validate-history ...` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` events. |

I used the offline, no-project `uv` validator form because the local project environment currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`.

## Identity and Grounding

- **Source identity:** TOGO M361 points to JCM GRMD 367 and its `Caminibacter Medium` page; the live JCM 367 page is reachable and says to use Medium No. 365 with modifications.
- **Category and class:** `bacterial`, `COMPLEX`, `SEMI_DEFINED`, and `LIQUID` are plausible because the JCM 367 formulation is a liquid inorganic medium with 0.2 g/L final yeast extract.
- **Cross-reference conflict:** The live JCM 365 base medium references trace minerals from JCM 151 and trace vitamins from JCM 197. TOGO M361 and the active CultureMech record instead point to TOGO M142 and M190. Those M142/M190 links resolve, but they are different media/stock accessions than the current JCM source states.
- **Active duplicate:** A gitignore-independent `find data/merge_yaml/merged data/normalized_yaml -iname '*caminibacter*' -print` found `data/normalized_yaml/bacterial/caminibacter_medium.yaml` (`CultureMech:002726`, `mediadive.medium:J367`) as a direct JCM duplicate. A gitignore-independent `rg --no-ignore --hidden` over normalized records, registries, catalogs, and import reports confirmed both `CultureMech:009742` and `CultureMech:002726` are active.
- **Ontology grounding:** The main salts that have `term` blocks pass LinkML term validation. The source's sulfur powder is grounded to `CHEBI:26833` `sulfur atom`; that is at best an adjacent elemental-sulfur grounding, not a powder identity.

## Evidence

| Claim | Support |
|---|---|
| Base recipe and JCM 367 modifications | Partially supported. TOGO M361 carries the right main salts from JCM 367/365 plus yeast extract, sulfur, Na2S, and 1 g/L NaHCO3, and it correctly omits sodium acetate. The direct JCM sibling does not: it copied sodium acetate from JCM 365 even though JCM 367 says to omit it. |
| Water amount | Unsupported. TOGO M361 reports `Distilled water` as `1 L`; the YAML imported that as `1 G_PER_L`, which represents a mass concentration rather than 1 L of solvent. |
| Trace stock additions | Unsupported. The source-level additions are 10 ml trace minerals and 10 ml trace vitamins. The YAML has two empty `Unknown solution` records at `10 G_PER_L`, and they point to M142/M190 rather than the live JCM 365 M151/M197 stock references. |
| Gas handling and preparation | Incomplete. JCM 365 gives pH 6.5, separate sterilization for CaCl2, MgCl2, sulfur, and Na2S, and anaerobic dispensing under N2; JCM 367 further instructs filter-sterilizing NaHCO3 as an 8% aqueous solution, omitting sodium acetate, filling inoculated bottles with H2-CO2 (4:1), and pressurizing to 100 kPa. The TOGO owner has no `preparation_steps` and models CO2 and N2 as variable ingredients. |
| NaHCO3 | Partially supported. JCM 367 supports 1.0 g/L final NaHCO3, but specifically as a filter-sterilized 8% aqueous solution added to the medium. The active record stores only a 1 g/L final chemical row. |

## Completeness

- Empty target-organism and growth-evidence fields were not treated as defects; JCM 367 is a formulation source.
- The record is incomplete for resolvable stock solutions. Live JCM 365 links trace minerals to JCM 151 and trace vitamins to JCM 197, and both JCM stock pages are reachable.
- The record is incomplete for preparation. JCM 367's H2-CO2 (4:1) headspace and 100 kPa overpressure are source-specific, not generic anaerobic boilerplate.
- The active direct JCM record is a useful comparison but not a correct replacement, because it copied JCM 365 sodium acetate even though JCM 367 omits it and it scaled several JCM 365 copied rows by `1000/1020`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The `Distilled water` row was imported as `1 G_PER_L` instead of a 1 L solvent volume. | TOGO M361's structured API says `Distilled water`, `volume: 1`, `unit: L`; the YAML stores `value: '1'`, `unit: G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M361_Caminibacter_Medium.yaml`; fix TOGO volume-unit handling. |
| Major | Trace minerals and trace vitamins are wrong empty G/L solution placeholders. | TOGO M361 says both are 10 ml stock additions; the YAML records two empty `Unknown solution` entries at `10 G_PER_L`. The original JCM source inherited through Medium 365 now points to JCM 151 and JCM 197, not M142 and M190. | Repair stock references in the TOGO owner or in TOGO-to-JCM cross-reference normalization. |
| Major | Source preparation and gas instructions are missing. | JCM 367 gives the 8% NaHCO3 filter-sterilization instruction and H2-CO2 (4:1) / 100 kPa post-inoculation headspace; JCM 365 gives the base sterilization sequence. The YAML has no `preparation_steps` and keeps CO2 and N2 as variable top-level ingredients. | Curate `preparation_steps` in the TOGO owner and move gas rows out of `ingredients`. |
| Major | There are two active records for JCM GRMD 367. | The ID registry and recipe catalog list `CultureMech:009742` at `TOGO_M361_Caminibacter_Medium.yaml` and `CultureMech:002726` at `caminibacter_medium.yaml`; both have `name: caminibacter_medium` and source JCM 367, directly or through TOGO. | Merge or source-link the TOGO and direct JCM records so only one canonical JCM 367 recipe reaches the generated corpus. |
| Minor | The sulfur grounding is adjacent rather than exact. | JCM/TOGO specify sulfur or sulfur powder, but the row is grounded to `CHEBI:26833` `sulfur atom`. | Re-ground elemental sulfur powder to an exact available material term or leave it unresolved explicitly. |

## Recommended Edits

1. Repair `data/normalized_yaml/bacterial/TOGO_M361_Caminibacter_Medium.yaml` so `Distilled water` remains a 1 L solvent volume instead of `1 G_PER_L`.
2. Replace the M142/M190 `G_PER_L` solution stubs with 10 ml trace-minerals and 10 ml trace-vitamins additions that match live JCM 365's JCM 151 and JCM 197 references, after verifying whether TOGO's M142/M190 mapping is a historical JCM version or an import error.
3. Add JCM-supported preparation steps for base-medium sterilization, separate Ca/Mg and sulfur/Na2S handling, 8% filter-sterilized NaHCO3, H2-CO2 (4:1), and 100 kPa overpressure.
4. Reconcile active records `CultureMech:009742` and `CultureMech:002726`; retain the JCM 367 modification that omits sodium acetate when copying any JCM 365 base ingredients.
5. Revisit the sulfur powder ontology grounding and the exact hydrate punctuation once the formulation is otherwise source-faithful.

## Follow-up Checks

- Rerun open schema, strict schema, term, and reference validation on `data/normalized_yaml/bacterial/TOGO_M361_Caminibacter_Medium.yaml`.
- Rerun the media-content manifest and confirm `VARIABLE_CONCENTRATION` no longer appears on top-level CO2/N2 ingredients for this record.
- Regenerate merges and confirm the TOGO M361 and direct JCM J367 records do not publish as two separate active Caminibacter Medium recipes.
- Re-open JCM 367, JCM 365, JCM 151, and JCM 197 during the curation edit to confirm the exact stock accessions and preparation text.

## Additional Notes

- Existing `reports/media_content_review_manifest.tsv` marks the TOGO M361 owner `NEEDS_REVIEW` because of variable CO2 and N2 ingredient concentrations.
- The direct JCM J367 owner is currently marked `PASS` in the media-content manifest despite retaining sodium acetate from the JCM 365 base medium.

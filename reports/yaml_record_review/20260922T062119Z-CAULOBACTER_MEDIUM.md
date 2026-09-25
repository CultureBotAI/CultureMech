# YAML Record Review: caulobacter_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml
- Started UTC: 2026-09-22T04:37:00Z
- Finished UTC: 2026-09-22T06:21:19Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| class | MediaRecipe |
| id | CultureMech:006076 |
| name | caulobacter_medium |
| category | bacterial |
| generated path | data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml |
| generated status | Derived canonical merge from `KOMODO_595_CAULOBACTER_medium`, `caulobacter_medium`, and `caulobacter_medium_add_agar` |
| media term | `komodo.medium:595`, KOMODO Medium 595 / CAULOBACTER medium |
| merge fingerprint | `2b077606c8185a27b0adfab542f97f8dc969e3cecc0d8876d3496d3fb351600e` |

The reviewed record is the generated duplicate collapse of:

| Source record | ID | Source term | Maintained path |
|---|---:|---|---|
| KOMODO Medium 595 | CultureMech:006076 | `komodo.medium:595` | `data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml` |
| DSMZ / MediaDive Medium 595 | CultureMech:001722 | `mediadive.medium:595` | `data/normalized_yaml/bacterial/caulobacter_medium.yaml` |
| TOGO M2356 | CultureMech:008941 | `TOGO:M2356` | `data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml` |

`find data -iname '*caulobacter*' -print` found only the Caulobacter, marine-Caulobacter, and Caulobacter PYE generated or normalized YAMLs under `data/merge_yaml/merged`, `data/normalized_yaml/bacterial`, and `data/normalized_yaml/specialized`. The search covered ignored files because `find` does not honor `.gitignore`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml --out /private/tmp/CAULOBACTER_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: exit 0; `/private/tmp/CAULOBACTER_MEDIUM.strict.tsv` contained only `file layer category detail path message`. |
| Reference integrity | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file, 0 checks, all validations passed. |
| Term labels | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only an `eutils` / `pkg_resources` deprecation warning was emitted. |
| Embedded history | Not checked | `just validate-history` validates standalone `history/*.yaml` files, not embedded `MediaRecipe.curation_history` blocks. |

## Identity and Grounding

The duplicate group is correctly about DSMZ Medium 595, CAULOBACTER MEDIUM:

- DSMZ Medium 595 lists Bacto peptone 2.0 g, Yeast extract 1.0 g, MgSO4 x 7 H2O 0.2 g, and Tap water 1000.0 ml, with the instruction to add 15.0 g/l agar for solid medium.
- MediaDive `/download/medium/595/json` reports id 595, name CAULOBACTER MEDIUM, source DSMZ, link `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf`, and the same ingredient amounts.
- TogoMedium M2356 reports `Caulobacter Medium (add agar)`, source URL `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf`, and the same five source components.
- The MgSO4 x 7 H2O, water, and agar CHEBI groundings on the generated target agree with the exact ingredients exposed by DSMZ and MediaDive.

The target retains the KOMODO source term because the KOMODO duplicate won the old canonical-selection rule. A gitignore-independent source search, `rg --no-ignore --hidden -n "CAULOBACTER|Caulobacter|595" data/raw/komodo data/raw/komodo_web`, found no local raw KOMODO payload beyond the README files found by `find data/raw/komodo data/raw/komodo_web -maxdepth 4 -type f -print`; the KOMODO-to-DSMZ identity was therefore checked through the maintained KOMODO note and its exact DSMZ 595 ingredient fingerprint, not through a raw KOMODO capture.

## Evidence

| Claim | Status |
|---|---|
| Source identity as DSMZ / MediaDive Medium 595 | Supported by the inspected DSMZ PDF and MediaDive JSON. |
| TOGO M2356 synonym as Caulobacter Medium with added agar from DSMZ Medium 595 | Supported by the inspected TogoMedium M2356 JSON, whose `src_url` points to the same DSMZ Medium 595 PDF. |
| Bacto peptone 2 g/L | Supported by DSMZ and MediaDive. |
| Yeast extract 1 g/L | Supported by DSMZ and MediaDive. |
| MgSO4 x 7 H2O 0.2 g/L | Supported by DSMZ and MediaDive; the CHEBI:31795 heptahydrate grounding is exact. |
| Agar 15 g/L for solid medium | Supported by the DSMZ preparation line and the MediaDive `Agar` row with `condition: for solid medium`. |
| Tap water 1000 G_PER_L | Unsupported. The DSMZ, MediaDive, and TogoMedium records all encode 1000 ml; MediaDive's composition endpoint leaves `g_l` null for Tap water. |
| Caulobacter sp. K31 cold-growth variant and 2400 min doubling time at 4 C | Present with PMID:25274120 evidence on `data/normalized_yaml/bacterial/caulobacter_medium.yaml`, but missing from this generated duplicate record. |

## Completeness

The base formula does not have pH, sterilization, incubation temperature, or atmosphere text in the inspected DSMZ Medium 595 PDF, so those empty slots are not defects in this generated record.

Two consequential fields from the maintained DSMZ parent are absent after generation:

- `preparation_steps`: the parent carries the DSMZ / MediaDive agar-addition instruction as `ADD_AGAR`; the generated KOMODO-derived canonical keeps only an agar ingredient note.
- Growth and variant evidence: the parent carries `organism_culture_type: isolate`, a `target_organisms` entry for Caulobacter sp. K31, and a `cold_growth_caulobacter_k31` variant. None were copied into `data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml`.

The generated record does not carry first-class `source_data` or source `references`; its media-term IDs and import history point back to KOMODO, MediaDive, and TOGO maintained records. That is enough to recover source identity, but not enough to recover the full MediaDive Yeast extract attribute `BD 212750`.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| major | Tap water is modeled as `1000 G_PER_L` even though the sources make it a 1000 ml solvent / final-volume row. | The generated `Tap water` ingredient has `value: '1000'` and `unit: G_PER_L`. DSMZ Medium 595 and Togo M2356 report `Tap water 1000.0 ml`; MediaDive `/download/medium/595/json` reports `amount: 1000, unit: ml`; and MediaDive `/download/composition/595/json` leaves `g_l` and `mmol_l` null for Tap water. The same bad water concentration is already flagged for all three duplicate owners in `data/import_tracking/reports/concentration_plausibility.tsv`. | Correct the maintained water row in `data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml`, `data/normalized_yaml/bacterial/caulobacter_medium.yaml`, and `data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml`, or fix the DSMZ, KOMODO, and TOGO import normalization that rewrites solvent ml rows as `G_PER_L`. Regenerate `data/merge_yaml/merged/`. |
| major | Duplicate merging drops scientifically curated DSMZ-parent growth and variant evidence. | `data/normalized_yaml/bacterial/caulobacter_medium.yaml` contains `organism_culture_type: isolate`, a `target_organisms` row for Caulobacter sp. K31 with `growth_metrics` doubling time 2400 min under 4 C temperature stress, and a `cold_growth_caulobacter_k31` inline variant, all absent from `data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml`. `src/culturemech/merge/merger.py` starts from a selected canonical recipe and only re-merges ingredients, synonyms, categories, `merged_from`, and curation history; source-only `target_organisms`, `variants`, and `organism_culture_type` cannot survive when another duplicate is selected. | Update `src/culturemech/merge/merger.py` to preserve compatible `target_organisms`, `variants`, and `organism_culture_type` from exact `SOURCE_DUPLICATE` inputs, or curate the duplicate group so the DSMZ parent that holds the extra evidence is the selected canonical. Then regenerate this merged record. |
| minor | The MediaDive yeast-extract supplier qualifier is not represented. | MediaDive Medium 595 records Yeast extract with `attribute: BD 212750`; the maintained DSMZ and generated YAML rows only keep `preferred_term: Yeast extract`, `value: '1'`, and `unit: G_PER_L`. | Add a note or source-data field for the `BD 212750` qualifier in `data/normalized_yaml/bacterial/caulobacter_medium.yaml` if importer output is expected to retain MediaDive attributes. |

## Recommended Edits

1. In each maintained duplicate owner, remodel `Tap water 1000 ml` as source volume / preparation context instead of `1000 G_PER_L`, and keep the final solid-medium ingredient signature as Bacto peptone 2 g/L, Yeast extract 1 g/L, MgSO4 x 7 H2O 0.2 g/L, and Agar 15 g/L.
2. Teach `RecipeMerger.merge_group` to reconcile `target_organisms`, inline `variants`, and `organism_culture_type` across records collapsed by an exact duplicate fingerprint, while avoiding live `variant_children` links that merely point to records collapsed into `merged_from`.
3. Preserve the MediaDive `BD 212750` qualifier for Yeast extract on the maintained DSMZ / MediaDive record if CultureMech intends to expose supplier attributes.
4. Regenerate `data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml` and the derived media pages after the maintained YAML and merge logic are fixed.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation against all three maintained duplicate records and the regenerated `data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml`.
- Re-run `just verify-merges` and confirm the Caulobacter duplicate group remains a three-record source duplicate with fingerprint `2b077606c8185a27b0adfab542f97f8dc969e3cecc0d8876d3496d3fb351600e` after the water-volume representation change.
- Inspect the regenerated YAML and confirm it contains no `Tap water` concentration in `G_PER_L`, still carries agar only for the solid form, and preserves the Caulobacter sp. K31 `target_organisms` evidence plus `cold_growth_caulobacter_k31` variant.
- Rebuild media pages and verify the public CAULOBACTER MEDIUM page no longer shows water as 1000 g/L.

## Additional Notes

- `rg --no-ignore --hidden -n "CAULOBACTER_MEDIUM|Caulobacter|caulobacter|KOMODO_595|Medium 595|M2356|CultureMech:006076|CultureMech:001722|2b077606c8185a27b0adfab542f97f8dc969e3cecc0d8876d3496d3fb351600e" data src scripts reports` covered ignored files while resolving related records and source-owner paths.
- `data/merge_yaml/merged/caulobacter_medium__d821176b.yaml` and `data/merge_yaml/merged/caulobacter_medium__b4d7b29d.yaml` are similarly named TOGO Caulobacter Medium records, but exhaustive local search showed they are M1545 and M2355, have different fingerprints, and are not part of this DSMZ 595 duplicate group.

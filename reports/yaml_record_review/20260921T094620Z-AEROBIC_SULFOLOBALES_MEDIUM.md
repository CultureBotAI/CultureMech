# YAML Record Review: Aerobic Sulfolobales Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml
- Started UTC: 2026-09-21T09:45:07Z
- Finished UTC: 2026-09-21T09:46:20Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:010118`
- Label: `aerobic_sulfolobales_medium`
- Original name: `Aerobic Sulfolobales Medium`
- Category: `archaea`
- Media term: `TOGO:M711`
- Generated status: generated single-source record from `data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml --out /private/tmp/aerobic_sulfolobales_medium.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The generated record is a direct copy of the local TOGO M711 import. Its `media_term` is `TOGO:M711` / `Aerobic Sulfolobales Medium`; the notes preserve the original JCM source, `JCM_M691`; the original URL points to JCM GRMD 691; and the live TOGO API for M711 still reports `original_media_id: JCM_M691` with source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691`.

That identity is correct, but several ingredient values are not faithful to the source. Live TOGO M711 and live JCM GRMD 691 agree that Aerobic Sulfolobales Medium consists of 1.0 g sulfur powder, 0.5 g yeast extract, and 1.0 L Salt base solution; the Salt base solution is 1 L water with MgSO4.7H2O 0.25 g, CaCl2.2H2O 0.07 g, KH2PO4 0.28 g, Na2MoO4.2H2O 0.03 mg, MnCl2.4H2O 1.8 mg, ZnSO4.7H2O 0.22 mg, CuCl2.2H2O 0.05 mg, (NH4)2SO4 1.3 g, CoSO4.7H2O 0.01 mg, VOSO4.xH2O 0.03 mg, Na2B4O7.10H2O 4.5 mg, and variable 10 N H2SO4 to adjust the pH to 2.5.

## Evidence

Supported:

- The target preserves the intended medium identity from the normalized TOGO M711 record.
- The gram-denominated source rows were imported at the expected final-recipe scale: sulfur powder 1 g/L, yeast extract 0.5 g/L, MgSO4.7H2O 0.25 g/L, CaCl2.2H2O 0.07 g/L, KH2PO4 0.28 g/L, and (NH4)2SO4 1.3 g/L.
- `H2SO4` correctly has `CHEBI:26836` / `sulfuric acid` and a variable concentration, matching its role as the pH-adjusting 10 N sulfuric-acid solution.

Unsupported or over-scoped:

- Seven source rows are in milligrams, but the generated record stores their milligram values as grams per liter: Na2MoO4.2H2O 0.03 g/L instead of 0.00003 g/L, MnCl2.4H2O 1.8 g/L instead of 0.0018 g/L, ZnSO4.7H2O 0.22 g/L instead of 0.00022 g/L, CuCl2.2H2O 0.05 g/L instead of 0.00005 g/L, CoSO4.7H2O 0.01 g/L instead of 0.00001 g/L, VOSO4.xH2O 0.03 g/L instead of 0.00003 g/L, and Na2B4O7.10H2O 4.5 g/L instead of 0.0045 g/L.
- The source says `Salt base solution (see below)` is a 1 L component of the main solution; the generated record converted that to a separate `solutions` item with `composition: []`, `name: Unknown solution`, and `concentration: 1 G_PER_L`.
- `Distilled water` is a 1 L volume inside the Salt base solution, not 1 g/L as currently represented in `ingredients`.
- The source pH of 2.5 and the two preparation comments, autoclaving salt base and yeast extract separately / steaming sulfur for 3 hr on 3 successive days and then adjusting with 10 N H2SO4, are absent.
- `Sulfur (powder)` still carries a deprecated `mediaingredientmech_term` link, `MediaIngredientMech:001072`, even though later rows were migrated to CHEBI-keyed `mediaingredientmech_chebi_term` fields.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*AEROBIC_SULFOLOBALES*' -print` searched the ignored timestamped-report directory and found no pre-existing AEROBIC SULFOLOBALES report.
- Exact `rg --no-ignore --hidden` searches for `TOGO:M711`, `TOGO:M713`, `mediadive.medium:J691`, `mediadive.medium:J693`, `AEROBIC SULFOLOBALES MEDIUM`, `Aerobic Sulfolobales Medium`, and `KOMODO_1189_AEROBIC_SULFOLOBALES` covered tracked and ignored files. They found the target generated TOGO M711 record, the normalized TOGO M711 source, the same JCM 691 record imported directly through MediaDive, the direct JCM/TOGO sulfur-free M693/M713 child records, the KOMODO sulfur-free child, and the adjacent generated records for the sulfur-free and anaerobic Sulfolobales media families.
- TOGO M711 and JCM GRMD 691 were fetched live and both preserve the milligram units, the pH 2.5, and the preparation text missing from this generated record.
- The direct normalized JCM M691 record, `data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml`, already has the milligram rows converted to correct g/L equivalents, has `ph_value: 2.5`, and preserves the source preparation comments. The TOGO M711 record did not merge with that direct JCM record because its unit, water, and solution-boundary mistakes changed the ingredient signature.
- The normalized TOGO M713 sulfur-free child record already cites TOGO M711/JCM 691 as its parent and omits elemental sulfur. That confirms TOGO M711 is the intended base record, but M711 itself was not corrected when M713 was repaired.

## Findings

### blocker: seven trace salts are 1000-fold too concentrated

Na2MoO4.2H2O, MnCl2.4H2O, ZnSO4.7H2O, CuCl2.2H2O, CoSO4.7H2O, VOSO4.xH2O, and Na2B4O7.10H2O were all imported as `G_PER_L` using the numeric values from TOGO/JCM milligram rows. These values must be divided by 1000 before the generated record can be treated as source-faithful.

### blocker: water and Salt base solution are represented with invalid concentration semantics

The source uses 1 L Salt base solution in the main formula and 1 L distilled water inside that stock-like Salt base solution. The generated YAML instead has `Distilled water` at `1 G_PER_L` and an empty `solutions` entry whose own 1 L volume has also become `1 G_PER_L`. That leaves the solution boundary unusable and assigns a mass concentration to both liter-denominated source rows.

### major: pH and preparation instructions were dropped

The live source gives pH 2.5 and requires autoclaving Salt base solution separately from the 10% yeast extract, steaming sulfur for three successive 3 hr treatments, and adjusting with 10 N H2SO4. None of those source facts are present in the TOGO M711 YAML.

### major: the same JCM 691 recipe is split into a duplicate generated family

The direct MediaDive/JCM import for `mediadive.medium:J691` already has the correct trace-salt concentrations and pH, but it did not merge with TOGO M711 because the TOGO import defects changed the fingerprint. After M711 is repaired, the curator should decide whether TOGO M711 and JCM M691 are source duplicates that should collapse into one generated record or whether their parent graph needs an explicit relationship.

### minor: one deprecated MediaIngredientMech identifier survived the migration

`Sulfur (powder)` still has `mediaingredientmech_term: MediaIngredientMech:001072`, a legacy identifier type that the June 2026 migration notes state was deprecated in favor of CHEBI-keyed `mediaingredientmech_chebi_term` links.

## Recommended Edits

1. Fix `data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml`, not the generated merge YAML.
2. Divide the seven milligram-denominated trace salts by 1000 when representing them as `G_PER_L`: Na2MoO4.2H2O `0.00003`, MnCl2.4H2O `0.0018`, ZnSO4.7H2O `0.00022`, CuCl2.2H2O `0.00005`, CoSO4.7H2O `0.00001`, VOSO4.xH2O `0.00003`, and Na2B4O7.10H2O `0.0045`.
3. Repair the Salt base solution representation so the 1 L `Salt base solution (see below)` row and 1 L `Distilled water` row are not emitted as `G_PER_L` ingredient concentrations or as an empty `Unknown solution`.
4. Restore `ph_value: 2.5` and preparation steps for the separate autoclaving, sulfur steaming, and 10 N H2SO4 pH adjustment described by TOGO M711/JCM 691.
5. Replace the stale `MediaIngredientMech:001072` field on `Sulfur (powder)` with a CHEBI-keyed mapping if a source-faithful elemental sulfur mapping is acceptable.
6. Regenerate the merge YAML and confirm TOGO M711 reconciles with the direct JCM M691 import instead of producing a separate generated medium for the same GRMD 691 source.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml`.
- Fetch live TOGO M711 and JCM GRMD 691 again, then compare every ingredient amount, `ph_value`, and preparation step in `data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml` against those sources.
- Search with `rg --no-ignore --hidden '0.03.*G_PER_L|1.8.*G_PER_L|4.5.*G_PER_L|1.*G_PER_L' data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml` and confirm the milligram rows and liter-denominated solution rows are no longer represented at the wrong scale.
- Search with `rg --no-ignore --hidden 'MediaIngredientMech:001072|mediaingredientmech_term' data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml` and confirm no deprecated MIM field remains.
- Re-run an ignored-file-inclusive exact search for `TOGO:M711` and `mediadive.medium:J691` to confirm the repaired source records now merge or carry an intentional curated relationship.

## Additional Notes

- `data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml` carries its own source duplication issue: the direct JCM M693 sulfur-free source still includes elemental sulfur and has the direct JCM M691 base marked as a `SOURCE_DUPLICATE` parent. That adjacent record should be reviewed separately.

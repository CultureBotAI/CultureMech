# YAML Record Review: glycerol_asparagine_agar_isp_medium_no_5

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glycerol_asparagine_agar_isp_medium_no_5.yaml
- Started UTC: 2026-09-23T06:59:36Z
- Finished UTC: 2026-09-23T07:03:38Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:008027` |
| Name | `glycerol_asparagine_agar_isp_medium_no_5` |
| Original name | `Glycerol-Asparagine Agar (ISP Medium No.5)` |
| Category | `bacterial` |
| Canonical media term | `TOGO:M1483` |
| Merged Togo sources | `TOGO:M1483`, `TOGO:M52`, `TOGO:M1642` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glycerol_asparagine_agar_isp_medium_no_5.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glycerol_asparagine_agar_isp_medium_no_5.yaml --out /private/tmp/glycerol_asparagine_agar_isp_medium_no_5.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glycerol_asparagine_agar_isp_medium_no_5.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glycerol_asparagine_agar_isp_medium_no_5.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

The generated record is canonicalized to Togo M1483 / NBRC Medium 265 but merges two additional Togo accessions: M52 / JCM Medium 60 and M1642 / NBRC Medium 845.

A gitignore-independent exact search for `TOGO:M1483`, `TOGO:M52`, `TOGO:M1642`, `NBRC_M265`, `Glycerol-Asparagine_Agar_ISP-5`, `acidic_glycerol_asparagine_agar_isp_medium_no_5`, and `glycerol_asparagine_agar_isp_medium_no_5` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found the expected three maintained parents, their generated indexes, this generated merge, and related JCM pH/salinity variant records for M422 and M408.

Grounding for K2HPO4, glycerol, L-asparagine, agar, FeSO4 x 7 H2O, MnCl2 x 4 H2O, and ZnSO4 x 7 H2O is narrow and matches the source salt hydration states. The problem is solution context, not ontology identity.

## Evidence

The three merged parents share the same basal non-agar masses and the same trace-salts stock formula, but they are not exact duplicates:

| Source | Label | Agar | pH |
|---|---|---:|---|
| Togo M52 / JCM 60 | Glycerol-Asparagine Agar (ISP-5) | 15 g | 7.4 |
| Togo M1483 / NBRC 265 | Glycerol-Asparagine Agar (ISP Medium No.5) | 20 g | 7.0-7.4 |
| Togo M1642 / NBRC 845 | Acidic Glycerol-Asparagine Agar (ISP medium No.5) | 20 g | 5.0 |

The generated record is internally inconsistent: it is identified as Togo M1483 but uses the 15 g agar value from Togo M52 instead of the 20 g value from Togo M1483 / NBRC 265, and it has no pH even though all three sources specify one.

Every source uses 1 ml Trace salts solution per final liter. The stock contains 0.1 g each FeSO4 x 7 H2O, MnCl2 x 4 H2O, and ZnSO4 x 7 H2O in 100 ml distilled water. The generated record flattens the three salts as 0.1 g/l final ingredients, represents the 1 ml stock addition as an empty `1 G_PER_L` solution, and sums main water plus stock water into one `101.0 G_PER_L` Distilled water row.

The Togo M52 maintained parent was repaired on September 6, 2026 to model the trace stock as `1 ML_PER_L`, retain the pH 7.4 step, and use a 1000 `ML_PER_L` water row. The generated merge predates that repair.

## Completeness

The generated record is not complete enough to use as any of the three source media because it conflates pH and agar variants and misrepresents the trace stock addition. Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects by themselves.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | Togo M52, M1483, and M1642 are not source duplicates and must not collapse to one generated formula. | JCM M60 is pH 7.4 with 15 g agar; NBRC 265 is pH 7.0-7.4 with 20 g agar; NBRC 845 is acidic at pH 5.0 with 20 g agar. | Duplicate grouping in `scripts/merge_recipes.py` or Togo merge overlays for these accessions. |
| Major | The generated canonical M1483 recipe has the wrong agar quantity and no pH. | NBRC 265 and Togo M1483 list 20 g agar and pH 7.0-7.4; the generated M1483 record has 15 g agar and no `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/glycerol_asparagine_agar_isp_medium_no_5.yaml` and merge regeneration after the split. |
| Major | The trace-salts stock was flattened and the 1 ml addition row has the wrong unit. | Togo M1483, M52, and M1642 add 1 ml of a 100 ml trace stock per final liter; the generated record has an empty `Trace salts solution*` entry at `1 G_PER_L` and top-level Fe/Mn/Zn rows at 0.1 g/l. | Togo solution migration for M1483/M1642 and regeneration from repaired M52. |
| Major | Water rows from separate scopes were summed and recoded as `101.0 G_PER_L`. | Togo M1483 and M1642 have 1 L main water plus 100 ml trace-stock water; the generated record has a single Distilled water row noting `[Merged 2 duplicates: 1.0, 100.0]`. | Togo importer / solution migrator for nested stocks. |
| Minor | M1483 and M1642 are still unresolved old Togo imports while M52 has already been curated. | The M52 parent has September 2026 repair history, structured trace-salts solution composition, pH, and references; M1483/M1642 still have empty `Unknown solution` rows and flattened trace salts. | `data/normalized_yaml/bacterial/glycerol_asparagine_agar_isp_medium_no_5.yaml` and `data/normalized_yaml/bacterial/acidic_glycerol_asparagine_agar_isp_medium_no_5.yaml`. |

## Recommended Edits

1. Split the Togo M52, M1483, and M1642 branches so agar and pH differences remain explicit instead of being merged as source duplicates.
2. Reuse the repaired M52 trace-salts representation as the model for NBRC M265 and M845: 1 ml trace stock per final liter, 0.1 g of each trace salt in 100 ml stock water, and a separate 1 L main-water row.
3. Add pH 7.0-7.4 to M1483 and pH 5.0 to M1642 from Togo/NBRC.
4. Regenerate merged records and confirm M52 no longer shares a fingerprint with the NBRC 20 g agar variants.
5. Preserve the existing JCM M408 and M422 variant links on the M52 family when splitting this over-merge.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on all regenerated records in this split cluster.
- Compare regenerated M1483 and M1642 against the NBRC 265 and 845 pages, and M52 against JCM `GRMD=60`.
- Re-run the exact gitignore-independent search for `TOGO:M1483`, `TOGO:M52`, `TOGO:M1642`, `NBRC_M265`, `Glycerol-Asparagine_Agar_ISP-5`, `acidic_glycerol_asparagine_agar_isp_medium_no_5`, and `glycerol_asparagine_agar_isp_medium_no_5` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify the final generated clusters are intentional.

## Additional Notes

The initial Togo and NBRC/JCM source fetches hit sandbox DNS failures; rerunning `curl -L` with network escalation recovered the source records. Togo M1642 also returned one transient upstream socket hang-up before succeeding on retry.

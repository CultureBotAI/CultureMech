# YAML Record Review: bacillus_schlegelii_heterotrophic_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
- Started UTC: 2026-09-21T17:59:00Z
- Finished UTC: 2026-09-21T18:02:07Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml` |
| Generated ID | `CultureMech:004664` |
| Label | `bacillus_schlegelii_heterotrophic_medium` |
| Source selected by merge | KOMODO Medium 260, `komodo.medium:260` |
| Duplicate parent | `data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml` / DSMZ Medium 260, `mediadive.medium:260` |
| Canonical normalized owner | `data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml` |
| Merge fingerprint | `7733280f38fd4ec7f923cd67245bd92a74a2cbfd80d35bb205d8c3a5b0109bbc` |

The merged artifact is a generated duplicate merge from the KOMODO-imported Medium 260 record and the DSMZ Medium 260 parent. Future corrections belong in the normalized KOMODO/DSMZ owners or in merge regeneration logic, not in `data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml` | Passed |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml --out /private/tmp/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with no reported broken references |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone `history/` files |

## Identity and Grounding

The generated record has the correct Medium 260 identity: DSMZ Medium 260 is `BACILLUS SCHLEGELII HETEROTROPHIC MEDIUM`, and the KOMODO owner explicitly records that it copied ingredients from DSMZ Medium 260. The source-duplicate link between the KOMODO owner and `data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml` is plausible because the names, pH 7.1, agar state, and copied DSMZ non-water ingredients match.

Most direct salts are grounded to the matching hydrated or named ChEBI form. The `NiCl2 x 6 H2O` row is over-broadened to anhydrous `CHEBI:34887` / nickel dichloride in the generated record and both normalized owners even though DSMZ Medium 27 prints the SL-6 ingredient as the hexahydrate. The local ChEBI structure index distinguishes `CHEBI:53542` / nickel chloride hexahydrate from `CHEBI:34887` / nickel dichloride, so the hydrate is identity-significant.

## Evidence

DSMZ Medium 260 supports the main Medium 260 identity, `DEFINED` liquid salts with optional agar, pH 7.1, 1 L distilled water, and the direct amounts for `Na2HPO4 x 2 H2O`, `KH2PO4`, `NH4Cl`, `MnSO4 x H2O`, `MgSO4 x 7 H2O`, `CaCl2 x 2 H2O`, ferric ammonium citrate, `Trace element solution SL-6`, and Na-pyruvate. It does not support seven separate top-level final-medium SL-6 salts at the stock g/L concentrations.

DSMZ Medium 27 supports the SL-6 stock recipe referenced by Medium 260: `ZnSO4 x 7 H2O` 0.10 g/L, `MnCl2 x 4 H2O` 0.03 g/L, `H3BO3` 0.30 g/L, `CoCl2 x 6 H2O` 0.20 g/L, `CuCl2 x 2 H2O` 0.01 g/L, `NiCl2 x 6 H2O` 0.02 g/L, `Na2MoO4 x 2 H2O` 0.03 g/L, and distilled water 1000 ml in the stock. Medium 260 adds 3 ml/L of that stock, so each flattened final-medium concentration would be three-thousandths of the SL-6 stock concentration.

The generated record retains pH 7.1 but omits the DSMZ preparation context: agar only if necessary at 15 g, dispensing 30-50 ml portions into Erlenmeyer flasks, sterilizing 15 minutes at 121 C, and incubating without agitation at 65 C. The DSMZ normalized parent already carries this prose in `preparation_steps`; the KOMODO normalized duplicate and generated merge do not.

## Completeness

Consequential gaps:

- Missing the main `Distilled water` row from DSMZ Medium 260.
- Missing the stock-solution boundary and 3 ml/L amount for `Trace element solution SL-6`.
- Missing SL-6 stock water if the stock composition is kept inline.
- Missing the DSMZ dispensing, sterilization, and incubation instructions from the generated record because the merge selected the KOMODO duplicate's sparse preparation payload.

Empty optional organism and growth-evidence fields are not themselves defects for a source recipe. The review did not inspect a primary Bacillus schlegelii growth publication; the DSMZ source is enough to verify the medium formulation but not to add growth outcome claims.

An ignored-file-inclusive prior-report search covered `reports/yaml_record_review` for `BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM`, `bacillus_schlegelii_heterotrophic_medium`, `CultureMech:004664`, and `CultureMech:001359`; it found no prior report for this record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The SL-6 stock has been flattened into final medium at stock strength. | DSMZ Medium 260 adds only 3.00 ml/L `Trace element solution SL-6`, while DSMZ Medium 27 prints the listed trace salts per liter of SL-6 stock. The generated record and both normalized Medium 260 owners carry the stock values directly as top-level `G_PER_L` medium ingredients. | `data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml`; `data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml` |
| Major | The final medium is missing distilled water. | DSMZ Medium 260 prints `Distilled water 1000.00 ml`; neither Medium 260 normalized owner nor the generated merge has a main water row. | `data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml`; `data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml` |
| Major | The generated merge loses the DSMZ preparation procedure. | The DSMZ parent says to adjust pH, use 15 g agar if necessary, distribute 30-50 ml in Erlenmeyer flasks, sterilize for 15 minutes at 121 C, and incubate without agitation at 65 C. `bacillus_schlegelii_heterotrophic_medium.yaml` has that in one `preparation_steps` entry, but the KOMODO duplicate and generated merge have no preparation steps. | `data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml` or `scripts/merge_recipes.py` |
| Major | `NiCl2 x 6 H2O` is grounded as anhydrous nickel dichloride. | DSMZ Medium 27 names the hexahydrate in SL-6. The generated record maps it to `CHEBI:34887` / nickel dichloride; the local structure index has a distinct `CHEBI:53542` / nickel chloride hexahydrate row. | `data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml`; `data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml`; the MIM label-index rule for `NiCl2 x 6 H2O` |

## Recommended Edits

1. In both Medium 260 normalized owners, replace the seven top-level SL-6 trace-salt rows with a `solutions` entry for `Trace element solution SL-6` at `3.00 ML_PER_L`; keep the DSMZ Medium 27 stock composition, including 1000.00 ml/L distilled water, nested under that solution or link to a corrected reusable SL-6 solution record.
2. Add the DSMZ Medium 260 main `Distilled water` component as 1000.00 ml/L to both normalized Medium 260 owners.
3. Preserve the DSMZ pH-adjustment, optional-agar, dispensing, autoclave, and 65 C incubation instruction in the KOMODO Medium 260 duplicate or update the merge code so a generated source-duplicate merge keeps the non-conflicting preparation step from the DSMZ parent.
4. Re-ground `NiCl2 x 6 H2O` to a hydrate-specific term through the packaged MIM label index or leave it explicitly unresolved; do not publish it as anhydrous `CHEBI:34887`.
5. Regenerate `data/merge_yaml/merged/` after the normalized owners or merge logic are fixed.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml`.
- Run `just validate data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating the merged artifact.
- Re-run the no-project open-schema, strict, reference, and term validators against the regenerated `data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml`.
- Manually compare the regenerated Medium 260 with DSMZ Medium 260 and DSMZ Medium 27 to confirm the main water, 3 ml/L SL-6 amount, preparation prose, and hydrated nickel chloride identity survived generation.

## Additional Notes

The reusable local solution record `data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml` contains the right SL-6 salt names and stock g/L values, but it still has a placeholder `ingredients` row and records stock water as `1000 PERCENT_V_V`. If a future curation change references that solution instead of inlining SL-6 under Medium 260, repair that solution record first or copy from the already reviewed inline SL-6 representation in the repaired DSMZ Medium 27 normalized records.

One exact `rg --no-ignore --hidden` search originally included the absent `data/raw_yaml` path and exited 2 after printing partial hits. The finding above about no prior YAML review is based on a separate ignored-file-inclusive search scoped to `reports/yaml_record_review`.

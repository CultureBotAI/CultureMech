# YAML Record Review: ferrous_iron_yeast_extract_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ferrous_iron_yeast_extract_medium__a821658e.yaml
- Started UTC: 2026-09-23T03:00:45Z
- Finished UTC: 2026-09-23T03:01:44Z
- Verdict: needs curation

## Target

CultureMech:010495 is the generated merged record for JCM Medium J1182, `FERROUS IRON YEAST EXTRACT MEDIUM`.

JCM 1182 defines a basal solution with MgSO4 x 7 H2O, ammonium sulfate, Na2SO4, KH2PO4, KCl, Ca(NO3)2 x 4 H2O, 1 ml Trace element solution, and 1 L distilled water. After pH adjustment to 2.0 and autoclaving, it adds 10 ml of 1 M FeSO4 solution at pH 2.0 and 20 ml of 1.0% Yeast extract solution.

## Validation

- LinkML open-schema validation: pass; `linkml-validate` reported `No issues found`.
- Strict schema validation: pass; `scripts/validate_strict.py` reported 0 files with errors and 0 total error rows.
- Reference validation: pass; the reference validator scanned the file and reported 0 checks.
- Term validation: pass; `linkml-term-validator` exited 0 and reported `Validation passed`.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded history entries in generated MediaRecipe YAML.

## Identity and Grounding

The CultureMech identifier, normalized name, fungal category, JCM J1182 medium term, and source URL identify the intended JCM recipe.

The simple basal salts are grounded to specific CHEBI terms. `Yeast extract` is an undefined component and appropriately lacks a single CHEBI term.

Several stock constituents are grounded, but they are not valid top-level final-medium ingredients at the generated concentrations.

## Evidence

The generated MgSO4 x 7 H2O, ammonium sulfate, Na2SO4, KH2PO4, KCl, and Ca(NO3)2 x 4 H2O rows match the MediaDive J1182 conversion of the basal solution to a 1031 ml final volume.

The generated stock rows do not preserve the source formula. The 1 ml Trace element solution is flattened at its full 1 L stock concentrations, producing 10 g/L ZnSO4 x 7 H2O, 1 g/L CuSO4 x 5 H2O, 1 g/L CoSO4 x 7 H2O, and related rows. The 10 ml 1 M FeSO4 solution is represented as 10 g/L FeSO4 instead of being kept as a volume addition of a 1 M stock. The 20 ml 1.0% Yeast extract solution is represented as 20 g/L yeast extract instead of 0.2 g/L final contribution. The 0.01 M H2SO4 solvent for the trace stock is represented as 1000 g/L sulfuric acid.

The generated preparation step preserves the source instruction to add the FeSO4 and yeast-extract stocks after autoclaving.

## Completeness

The generated record has all JCM 1182 basal ingredients and all trace-stock constituents, but it is not composition-complete because it discards the nested stock boundaries and overstates every trace-stock constituent.

The 1 M FeSO4 and 1.0% yeast-extract additions also need stock-aware representation or correct final concentrations.

## Findings

1. The 1 ml Trace element solution is flattened at full 1 L stock concentration.
2. The 10 ml 1 M FeSO4 solution and 20 ml 1.0% Yeast extract solution are recorded as 10 and 20 `G_PER_L` rows, respectively, rather than as stock additions or final scaled contributions.
3. H2SO4 from the 0.01 M trace-element stock solvent is misrepresented as `1000` `G_PER_L` sulfuric acid.
4. The generated record does not encode the pH 2.0 target as structured `ph_value` metadata.

## Recommended Edits

1. Recurate JCM J1182 with Trace element solution, 1 M FeSO4 solution, and 1.0% Yeast extract solution as stock additions.
2. If stock constituents must be expanded, scale the 1 ml, 10 ml, and 20 ml additions to final medium concentrations before merging them into the top-level recipe.
3. Remove H2SO4 as a 1000 g/L top-level solute; keep it as the trace-stock solvent and the pH-adjustment reagent.
4. Add `ph_value: 2.0` if the schema semantics permit capturing the JCM adjustment target.

## Follow-up Checks

- Re-run open-schema, strict-schema, reference, and term validation after recurating the stock additions.
- Confirm the post-fix record still resolves to `mediadive.medium:J1182`.
- Confirm `H2SO4` no longer appears with `1000` `G_PER_L` and the trace element rows are scaled or nested.

## Additional Notes

None found.

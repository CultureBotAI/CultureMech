# YAML Record Review: acidithiobacillus_ferrooxidans_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml
- Started UTC: 2026-09-21T09:23:09Z
- Finished UTC: 2026-09-21T09:24:26Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:008883`
- Label: `acidithiobacillus_ferrooxidans_medium`
- Original name: `Acidithiobacillus ferrooxidans Medium`
- Category: `bacterial`
- Media term: `TOGO:M2297` / `Acidithiobacillus ferrooxidans Medium`
- Generated status: generated singleton from `data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml --out /private/tmp/acidithiobacillus_ferrooxidans.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The TOGO identity and ATCC provenance are correct: `TOGO:M2297` is `Acidithiobacillus ferrooxidans Medium`, and its API payload cites ATCC Medium 2039 as the original source via `https://www.atcc.org/~/media/4C29EA2E2A0749BB9354D8AC64AA715B.ashx`.

The recipe body is not source-faithful. ATCC 2039 is a two-solution complete medium:

- 800 ml Solution A, containing 0.8 g `(NH4)2SO4`, 2.0 g `MgSO4 x 7H2O`, 0.4 g `K2HPO4`, 5 ml Wolfe's Mineral Solution, and 800 ml DI water
- Solution A adjusted to pH 2.3 with H2SO4 and filter-sterilized
- 200 ml Solution B, containing 20.0 g `FeSO4 x 7H2O` and 200 ml DI water
- Solution B stirred to dissolve and quickly filter-sterilized
- aseptic combination of Solutions A and B as the complete medium
- Wolfe's Mineral Solution prepared separately as a 1 L stock and added at 5 ml

The target instead sums components that live in separate scopes. It merges 2.0 g MgSO4 from Solution A with 3.0 g MgSO4 from the Wolfe stock, 20.0 g FeSO4 from Solution B with 0.1 g FeSO4 from the Wolfe stock, and 800/200/1000 ml water into one 2000.0 `G_PER_L` water row. It also places the Wolfe stock salts at top level as though they were final-medium gram-per-liter quantities.

## Evidence

Supported:

- The TOGO record correctly points at the ATCC 2039 PDF, and the TOGO component/comment extraction agrees with the PDF's Solution A, Solution B, Wolfe's Mineral Solution, pH-adjustment, filter-sterilization, and complete-medium assembly instructions.
- The target's top-level 0.8 g `(NH4)2SO4`, 0.4 g `K2HPO4`, variable H2SO4, and 20.0 g portion of `FeSO4 x 7 H2O` are visible in the ATCC source, but only inside their respective Solution A or Solution B scopes.
- The target's 1.5 g nitrilotriacetic acid, 3.0 g `MgSO4 x 7H2O`, 0.5 g `MnSO4 x H2O`, 1.0 g NaCl, 0.1 g `FeSO4 x 7H2O`, 0.1 g `CoCl2 x 6H2O`, 0.1 g CaCl2, 0.1 g `ZnSO4 x 7H2O`, 0.01 g `CuSO4 x 5H2O`, 0.01 g `AlK(SO4)2 x 12H2O`, 0.01 g H3BO3, and 0.01 g `Na2MoO4 x 2H2O` values are visible in the ATCC source, but only inside the separately prepared 1 L Wolfe's Mineral Solution stock.

Unsupported or over-scoped:

- `MgSO4 x 7 H2O` is `5.0 G_PER_L`; this is an arithmetic merger of the 2.0 g Solution A quantity and the 3.0 g Wolfe stock quantity.
- `FeSO4 x 7 H2O` is `20.1 G_PER_L`; this is an arithmetic merger of the 20.0 g Solution B quantity and the 0.1 g Wolfe stock quantity.
- `DI Water` is `2000.0 G_PER_L`; this is an arithmetic merger of 800 ml Solution A water, 200 ml Solution B water, and 1000 ml Wolfe stock water.
- The Wolfe stock salts are top-level ingredients even though only 5 ml of the Wolfe stock is added to 800 ml Solution A.
- `Solution A`, `Solution B`, `*Wolfe's Mineral Solution (see below)`, and `Potassium hydroxide solution` are preserved as `solutions` placeholders with empty or out-of-record compositions, so the record has neither faithful nested stock formulas nor faithful final-medium concentrations.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ACIDITHIOBACILLUS_FERROOXIDANS*' -print` searched the ignored timestamped-report directory and found no pre-existing ACIDITHIOBACILLUS FERROOXIDANS report.
- Exact `rg --no-ignore --hidden` searches for `TOGO:M2297`, `M2297`, `4C29EA2E2A0749BB9354D8AC64AA715B`, `NBRCMediumDetailServlet\?NO=1379`, and `nbrc\.medium:1379` covered tracked and ignored files. They found the expected TOGO target and scratch reports but no separate NBRC 1379 normalized import for this medium.
- The same-name DSMZ Medium 70 / KOMODO sibling in `data/merge_yaml/merged/acidithiobacillus_ferrooxidans_medium__fd9133ad.yaml` is a separate ferrooxidans medium with different provenance and should be reviewed independently rather than used to normalize TOGO M2297.
- Optional organism, growth metric, evidence, pH, and temperature arrays are absent on the source import; that is not a target-specific defect.

## Findings

### blocker: nested ATCC solution formulas were flattened into final ingredients

ATCC 2039 and the TOGO M2297 API both define a nested recipe: 800 ml Solution A plus 200 ml Solution B, with Solution A itself receiving 5 ml Wolfe's Mineral Solution. `data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml` flattens the sub-solution formulas into direct final-medium ingredient rows and then merges same-named components across scopes. The generated singleton inherits unsupported rows such as 5.0 g/L `MgSO4 x 7 H2O`, 20.1 g/L `FeSO4 x 7 H2O`, 2000 g/L `DI Water`, and stock-strength Wolfe mineral salts that should be at most nested stock ingredients.

### major: solution placeholders preserve neither composition nor addition semantics

The `solutions` array still lists Solution A, Solution B, Wolfe's Mineral Solution, and potassium hydroxide solution, but the migrated solution rows are empty placeholders. Solution A and Solution B contain only out-of-record MediaDive references plus `G_PER_L` concentrations copied from source volumes, Wolfe's Mineral Solution has an empty `composition: []`, and the record loses the instructions to pH-adjust Solution A to 2.3, filter-sterilize both Solution A and Solution B, quickly dissolve the FeSO4 solution, aseptically combine the complete medium, and bring the Wolfe stock to pH 6.5 with KOH before the other salts are added.

### minor: magnesium sulfate has stale MediaIngredientMech CHEBI grounding

The MgSO4 primary `term` was repaired to heptahydrate `CHEBI:31795`, but `mediaingredientmech_chebi_term` still points at generic magnesium sulfate `CHEBI:32599`. The record therefore carries internally inconsistent ontology links for the same ingredient row.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml`, restore the ATCC hierarchy instead of editing the generated `data/merge_yaml/merged/` singleton directly.
2. Model the complete medium as 800 ml Solution A plus 200 ml Solution B, nest the six Solution A rows and two Solution B rows in those stocks, and represent filter-sterilization and aseptic combination as preparation semantics.
3. Model Wolfe's Mineral Solution as its own 1 L stock whose 5 ml addition belongs inside Solution A; keep KOH as a Wolfe-stock pH adjustment to 6.5 rather than as a top-level complete-medium ingredient.
4. Re-ground the MgSO4 `mediaingredientmech_chebi_term` to match the heptahydrate primary term.
5. Regenerate `data/merge_yaml/merged/` with `just merge-recipes`.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml`.
- Re-fetch the TOGO M2297 API payload and ATCC Medium 2039 PDF, then confirm that Solution A, Solution B, Wolfe's Mineral Solution, both filter-sterilization instructions, and both pH-adjustment instructions survive regeneration.
- Search with `rg --no-ignore --hidden '20\\.1|2000\\.0|\\[Merged 2 duplicates: 2\\.0, 3\\.0\\]|\\[Merged 3 duplicates: 800\\.0, 200\\.0, 1000\\.0\\]' data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml` and confirm those scope-collapsing artifacts are gone.

## Additional Notes

- ATCC notes that its sterile ready-to-use Trace Mineral Supplement, catalog `MD-TMS`, can substitute for Wolfe's Mineral Solution; that statement is a substitution note, not a direct ingredient.
- The adjacent DSMZ/KOMODO `acidithiobacillus_ferrooxidans_medium` generated record was inspected only to distinguish provenance. It still needs a separate full review.

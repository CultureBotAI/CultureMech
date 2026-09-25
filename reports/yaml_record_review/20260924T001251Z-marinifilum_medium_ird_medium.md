# YAML Record Review: marinifilum_medium_ird_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marinifilum_medium_ird_medium.yaml
- Started UTC: 2026-09-24T00:11:57Z
- Finished UTC: 2026-09-24T00:12:52Z
- Verdict: needs curation

## Target

- Reviewed generated record: `data/merge_yaml/merged/marinifilum_medium_ird_medium.yaml`
- Maintained upstream owner: `data/normalized_yaml/bacterial/marinifilum_medium_ird_medium.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:001011`
- Source identity: `mediadive.medium:1533`
- Label: `MARINIFILUM MEDIUM (IRD MEDIUM)`
- Generated status: single-source merge of `marinifilum_medium_ird_medium.yaml`.

## Validation

| Check | Result |
|---|---|
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marinifilum_medium_ird_medium.yaml` | Passed; printed `No issues found`. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marinifilum_medium_ird_medium.yaml --out /private/tmp/marinifilum_medium_ird_medium.strict.tsv --workers 1 --quiet` | Passed; summary reported 1 scanned file, 0 files with errors, and 0 total error rows. The TSV had one header line only. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marinifilum_medium_ird_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 total reference checks. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marinifilum_medium_ird_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after a non-fatal `eutils`/`pkg_resources` deprecation warning. |
| Embedded `MediaRecipe.curation_history` validation | Not checked: the repository's `just validate-history` target validates standalone files under `history/`, not embedded recipe events. |

## Identity and Grounding

- MediaDive REST medium 1533 and the DSMZ Medium 1533 PDF verify the target as
  `MARINIFILUM MEDIUM (IRD MEDIUM)`, pH 7.0.
- The main DSMZ formulation is recognizable, but the trace-element stock was
  imported as root ingredients instead of as 1 ml/l of
  `Trace mineral element solution`.
- The term validator passed all stored CURIE/label pairs. That does not prove
  the `FeCl2 x 7 H2O` grounding: the record points the heptahydrate label at
  `CHEBI:30812`/iron dichloride, which is the anhydrous compound in the local
  CHEBI structure index.

## Evidence

- Supported:
  - DSMZ supports the root 0.3 g KH2PO4, 0.3 g K2HPO4, 1 g NH4Cl, 25 g NaCl,
    0.1 g KCl, 0.1 g CaCl2 x 2 H2O, 0.5 g cysteine HCl, 1 g yeast extract, 1
    ml of 0.1% resazurin, 1000 ml distilled water, pH 7.0, and the
    N2/CO2 anaerobic preparation.
  - DSMZ supports post-autoclave addition of 20 ml/l each of 150 g/l MgCl2 x 6
    H2O, 10% NaHCO3, 2% Na2S x 9 H2O, and 1 M glucose stock solutions. The
    reviewed record's final `G_PER_L` values match those stock dilutions.
- Unsupported or misrepresented:
  - DSMZ lists `Trace mineral element solution (see medium 941)` as a 1 ml
    addition. MediaDive REST expands that subsolution as `Trace element
    solution SL-7`, but the reviewed record places the SL-7 stock contents at
    the root with the stock solution's undiluted gram-per-liter values.
  - The post-autoclave MgCl2 x 6 H2O, NaHCO3, Na2S x 9 H2O, and glucose entries
    retain the correct final masses but lose the source stock strengths and
    stock-addition boundary.
  - `FeCl2 x 7 H2O` is exact source text in MediaDive's SL-7 expansion, but the
    record grounds it to anhydrous `CHEBI:30812`.

## Completeness

- Direct ingredient coverage is incomplete because nested SL-7 stock chemistry
  is represented as final-medium chemistry.
- Solution structure is incomplete: the record has no `solutions` block for the
  1 ml/l SL-7 addition or the four post-autoclave anaerobic stock additions.
- Preparation coverage is mostly present, but the generic `pH 7.0` and `Add
  after autoclave` fragments should be retained as conditions or notes on the
  appropriate additions rather than as standalone `MIX`/`AUTOCLAVE` steps.
- Empty target-organism and growth-metric slots are acceptable because DSMZ
  Medium 1533 is a source recipe, not a primary growth study.
- A gitignore-independent exact scan of the reviewed normalized and merged YAML
  files found no `sources`, `source_data`, `references`, `target_organisms`,
  `growth_metrics`, `parent_media`, `variant_children`, or
  `variant_relationship` fields in the current target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The 1 ml/l trace-element stock was flattened into full-strength root ingredients. | DSMZ Medium 1533 calls for 1 ml of Trace mineral element solution; MediaDive expands that stock as SL-7. The record instead lists HCl, FeCl2 x 7 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O at the SL-7 stock concentrations. | `data/normalized_yaml/bacterial/marinifilum_medium_ird_medium.yaml`; if recurring, fix `src/culturemech/import/mediadive_importer.py` handling for nested MediaDive solutions. |
| major | `FeCl2 x 7 H2O` is grounded to an anhydrous CHEBI term. | The source stock names `FeCl2 x 7 H2O`; `CHEBI:30812` is `iron dichloride` with formula `Cl2Fe` in the local structure index. | `data/normalized_yaml/bacterial/marinifilum_medium_ird_medium.yaml`. |
| minor | Source stock strengths for post-autoclave additions are not explicitly represented. | MgCl2 x 6 H2O, NaHCO3, Na2S x 9 H2O, and glucose have correct final masses, but the record does not preserve that they came from 150 g/l, 10%, 2%, and 1 M sterile anaerobic stocks. | `data/normalized_yaml/bacterial/marinifilum_medium_ird_medium.yaml`. |

## Recommended Edits

1. Replace the flattened SL-7 root ingredients with a 1 ml/l `Trace mineral
   element solution` entry, either linked to the maintained Medium 941 stock or
   represented as a nested solution.
2. De-ground `FeCl2 x 7 H2O` from `CHEBI:30812` unless an exact curated
   identifier for that hydrate is available.
3. Preserve the MgCl2 x 6 H2O, NaHCO3, Na2S x 9 H2O, and glucose additions as
   sterile anaerobic stock additions with their source stock strengths.
4. Fold the pH and add-after-autoclave fragments into the structured
   preparation/addition representation instead of retaining them as standalone
   generic steps.
5. Add a curation-history event explaining the stock-solution restructuring and
   FeCl2 x 7 H2O grounding decision.

## Follow-up Checks

- Re-run the focused LinkML, strict, term, and reference validators on the
  edited normalized record.
- Manually compare the edited record against the DSMZ Medium 1533 PDF and
  MediaDive REST 1533 payload for all root ingredients, SL-7 content, and
  post-autoclave stock additions.
- Re-run merge generation and verify `marinifilum_medium_ird_medium` still emits
  a single canonical merged record.

## Additional Notes

- The DSMZ PDF and MediaDive REST endpoint agreed on the Medium 1533 identity,
  pH, root ingredients, SL-7 reference, and post-autoclave additions.
- Chemical hydrates are rendered with ASCII `x` in this report.

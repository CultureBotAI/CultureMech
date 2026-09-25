# YAML Record Review: ANAEROBIC CHOLESTEROL MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROBIC_CHOLESTEROL_MEDIUM.yaml
- Started UTC: 2026-09-21T12:17:41Z
- Finished UTC: 2026-09-21T12:18:35Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/ANAEROBIC_CHOLESTEROL_MEDIUM.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:006675`
- Label: `ANAEROBIC CHOLESTEROL MEDIUM`
- Category: `bacterial`
- Source identity on canonical merge: KOMODO `858`, cross-linked to DSMZ/MediaDive medium `858`
- Generated status: generated merge record with fingerprint `762fff04d982bd4b67c732bf0ad88674d296c389d83436ef4867985a84a837c7`
- Merge lineage: two sources, `data/normalized_yaml/bacterial/anaerobic_cholesterol_medium.yaml` and `data/normalized_yaml/specialized/anaerobic_cholesterol_medium.yaml`
- Maintained owner for future record edits: both normalized records own their flattened DSMZ 858 contents; the KOMODO resolver and MediaDive importer own any general fixes for DSMZ stock topology

## Validation

- Open schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROBIC_CHOLESTEROL_MEDIUM.yaml`
  - Result: passed
- Strict schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROBIC_CHOLESTEROL_MEDIUM.yaml --out /private/tmp/ANAEROBIC_CHOLESTEROL_MEDIUM.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROBIC_CHOLESTEROL_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 total checks
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROBIC_CHOLESTEROL_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed
- Embedded curation history: Not checked. The documented `just validate-history` recipe validates standalone records under `history/`; I did not find a focused embedded `MediaRecipe.curation_history` validator for one merge file.

## Identity and Grounding

The KOMODO and MediaDive inputs are legitimate duplicate imports of DSMZ Medium 858. The inspected MediaDive payload reports `id: 858`, `ANAEROBIC CHOLESTEROL MEDIUM`, pH 6.8 to 7.2, source `DSMZ`, and the DSMZ Medium 858 PDF link; the inspected PDF has the same medium number and title.

The merged record still has unsupported provenance residue: `notes` says `Aerobic: Yes`, but DSMZ 858 explicitly distributes cholesterol and Solution A into anaerobic tubes, autoclaves under 80 percent N2 plus 20 percent CO2, and adds later stocks under anaerobic conditions.

Most primary ingredient terms are plausible for their literal labels, but `NiCl2 x 6 H2O` is grounded to `CHEBI:34887`/`nickel dichloride`, dropping the hexahydrate specified in SL-10, and `NaNO3` still has a legacy `mediaingredientmech_term` even though the curation history says all 27 legacy MIM links were replaced.

## Evidence

Supported:

- DSMZ 858 and MediaDive support Solution A as 0.10 g MgSO4.7H2O, 0.10 g NH4Cl, 0.02 g CaCl2, 0.16 g NaNO3, and 200 ml distilled water.
- DSMZ 858 and MediaDive support Solution B as 1.00 g KH2PO4 in 100 ml water and Solution F as 8.40 g NaHCO3 in 100 ml water.
- DSMZ 858 and MediaDive support adding 9 ml Solution A, 500 microliter Solution B, 25 microliter Solution C, 50 microliter Solution D, 25 microliter Solution E, and 500 microliter Solution F to assemble 10 ml of medium.
- MediaDive expands Solution C as trace elements SL-10, Solution D as the 1 L vitamin solution, and Solution E as the 1 L selenite-tungstate stock.

Unsupported or over-scoped:

- The source's cholesterol addition, for example 5 mg in 10 ml medium, is missing from `ingredients`.
- Solution A, B, and F components are represented at their stock concentrations rather than their 9 ml, 0.5 ml, and 0.5 ml final-medium contributions.
- The Solution C, D, and E stock recipes are flattened into top-level ingredients even though the final 10 ml medium uses only 25 microliter of C, 50 microliter of D, and 25 microliter of E.
- Multiple water rows are missing: Solution A 200 ml, Solution B 100 ml, Solution F 100 ml, the 1 L vitamin stock water, SL-10 water, and the 1 L selenite-tungstate stock water.
- The KOMODO `Aerobic: Yes` note conflicts with the anaerobic source preparation.
- DSMZ preparation details are preserved only as broad text, not as structured anaerobic assembly, autoclaving, and post-cooling stock-addition steps.

## Completeness

Consequential gaps:

- Cholesterol is absent even though it is the named substrate and the source explicitly gives an example amount.
- The 10 ml assembly and its six source solutions are not represented.
- Trace elements SL-10, vitamin solution, and selenite-tungstate stock boundaries are absent.
- Solution-specific sterilization is not structured: Solutions A, B, and F are autoclaved anaerobically under 80 percent N2 plus 20 percent CO2, while Solutions C, D, and E may be prepared aerobically.
- No structured `references` entry captures the DSMZ PDF, MediaDive source, or KOMODO source beyond prose `notes`.

Correctly empty or not scored:

- `target_organisms`, `growth_metrics`, and variant links are empty. DSMZ Medium 858 is a recipe source, not primary growth evidence.
- The merge of KOMODO 858 and MediaDive 858 itself appears appropriate because both owners resolve to the same DSMZ medium.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ANAEROBIC_CHOLESTEROL_MEDIUM.md' -print` found no prior report for this generated record before the report was written; `find` included ignored report files.
- `find data/normalized_yaml -type f -name 'anaerobic_cholesterol_medium.yaml' -print` found the two same-stem normalized owners under `bacterial` and `specialized`; `find` included ignored files.
- `rg --no-ignore --hidden -F 'mediadive.medium:858' data/normalized_yaml data/merge_yaml data/culturemech_recipe_catalog.tsv data/culturemech_id_registry.tsv` found the specialized MediaDive owner and the KOMODO owner reference to DSMZ 858.

## Findings

| ID | Severity | Finding | Maintained owner |
| --- | --- | --- | --- |
| F1 | major | Cholesterol is absent from the ingredient model even though DSMZ instructs distributing an appropriate amount of cholesterol, for example 5 mg for 10 ml medium. | Both normalized `anaerobic_cholesterol_medium.yaml` owners and the KOMODO/MediaDive importers |
| F2 | major | The six-solution 10 ml assembly is flattened into final top-level ingredient rows at stock concentrations instead of retaining 9 ml A, 500 microliter B, 25 microliter C, 50 microliter D, 25 microliter E, and 500 microliter F. | Both normalized owners and the importers |
| F3 | major | Trace element, vitamin, and selenite-tungstate stocks are flattened into top-level final-medium ingredients at full stock strength. | Both normalized owners and the importers |
| F4 | major | Source water rows are missing across Solution A, B, F, vitamin solution, SL-10, and selenite-tungstate stock, preventing volume and dilution checks. | Both normalized owners and the importers |
| F5 | major | Solution-specific anaerobic/aerobic preparation semantics are stored as broad text and the KOMODO `Aerobic: Yes` note directly conflicts with DSMZ anaerobic preparation. | Both normalized owners, especially `data/normalized_yaml/bacterial/anaerobic_cholesterol_medium.yaml` for the KOMODO note |
| F6 | major | `NiCl2 x 6 H2O` is grounded as anhydrous `CHEBI:34887` nickel dichloride rather than a hexahydrate-specific material. | Both normalized owners |
| F7 | minor | `NaNO3` still carries `mediaingredientmech_term: MediaIngredientMech:000171` instead of `mediaingredientmech_chebi_term` despite the migration history claiming all legacy links were replaced. | Both normalized owners or the MIM legacy migration |
| F8 | minor | DSMZ, MediaDive, and KOMODO sources are present only in `notes`/`curation_history`, with no structured `references` entry available for future evidence validation. | Both normalized owners |

## Recommended Edits

1. Add cholesterol as a source-supported substrate with an amount that preserves the DSMZ wording, at minimum the example 5 mg per 10 ml medium.
2. Restore the final 10 ml assembly with Solution A through F volume additions.
3. Keep trace elements SL-10, vitamin solution, and selenite-tungstate solution as nested stock additions rather than inlining their 1 L stock compositions.
4. Restore water rows in Solution A, Solution B, Solution F, the vitamin stock, SL-10, and the selenite-tungstate stock.
5. Replace the stale KOMODO `Aerobic: Yes` note with source-faithful anaerobic preparation metadata.
6. Correct `NiCl2 x 6 H2O` by either grounding it to a hydrate-specific term or leaving the unresolved source label ungrounded; do not keep the anhydrous nickel dichloride term.
7. Finish migrating `NaNO3` from `mediaingredientmech_term` to `mediaingredientmech_chebi_term`.
8. Add structured references for KOMODO 858, MediaDive 858, and DSMZ Medium 858.
9. Regenerate `data/merge_yaml/merged/ANAEROBIC_CHOLESTEROL_MEDIUM.yaml` from the corrected normalized owners.

## Follow-up Checks

- Re-run open schema, strict schema, reference validation, and term validation on both normalized `anaerobic_cholesterol_medium.yaml` owners.
- Re-run the same focused validators on regenerated `data/merge_yaml/merged/ANAEROBIC_CHOLESTEROL_MEDIUM.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration to prove both normalized owners merge cleanly into one source-faithful canonical record.
- Manually compare the regenerated record against MediaDive 858 and DSMZ Medium 858, checking cholesterol, all six solution volumes, nested stock boundaries, water rows, NiCl2 hexahydrate grounding, and anaerobic handling.

## Additional Notes

- Direct `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` were not used for this report because the project `uv` environment attempted to build `llvmlite==0.46.0` under Python 3.13 and failed before target-specific validation. The no-project Python 3.11 commands above were used as focused equivalents.
- The generated merge selects the KOMODO source ID and stable ID but also merges the direct MediaDive/DSMZ import; that duplicate merge is source-plausible even though both inputs need the same stock-topology repair.

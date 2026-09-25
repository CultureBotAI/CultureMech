# YAML Record Review: ATHALASSOTOGA_MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ATHALASSOTOGA_MEDIUM.yaml
- Started UTC: 2026-09-21T16:28:24Z
- Finished UTC: 2026-09-21T16:31:13Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ATHALASSOTOGA_MEDIUM.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:001085` |
| Label | `athalassotoga_medium` |
| Original label | `ATHALASSOTOGA MEDIUM` |
| Category | `bacterial` |
| Source identity | `mediadive.medium:1604`; DSMZ Medium 1604 |
| Source URL | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1604.pdf` |
| Generated status | Generated on 2026-08-06 from `data/normalized_yaml/bacterial/athalassotoga_medium.yaml` |
| Merge fingerprint | `046946d4fabb439224dbe0f9bdb8b8225284fec32b3ef64a7fa364ff96892220` |

`data/merge_yaml/merged/` is derived output. Future fixes belong in
`data/normalized_yaml/bacterial/athalassotoga_medium.yaml` or the MediaDive
DSMZ importer, then this generated file should be regenerated.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ATHALASSOTOGA_MEDIUM.yaml` | Pass. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ATHALASSOTOGA_MEDIUM.yaml --out /private/tmp/ATHALASSOTOGA_MEDIUM.strict.tsv --workers 1 --quiet` | Pass; 1 file scanned, 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ATHALASSOTOGA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 1 file validated, 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ATHALASSOTOGA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass. The only emitted message was the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked | No focused validator for embedded `MediaRecipe.curation_history` is documented for one merged recipe. `just validate-history` targets standalone records under `history/`. |

Direct `just` validation was not used because this checkout currently reaches a
project `uv` build of `llvmlite==0.46.0` under Python 3.13 before target-specific
validation and fails in `setuptools` with `TypeError: Popen.__init__() got an
unexpected keyword argument 'dry_run'`.

## Identity and Grounding

- The ID, label, bacterial category, and `mediadive.medium:1604` source
  accession identify DSMZ Medium 1604, `ATHALASSOTOGA MEDIUM`.
- The inspected two-page DSMZ PDF names the same medium, pH 6.0, and final
  volume 1011 ml.
- The record's first eight concentration values are mostly plausible
  final-volume normalizations from DSMZ gram amounts divided by 1.011 L.
- Allen's trace element solution and Wolin's vitamin solution are not direct
  Athalassotoga-medium rows, but their stock contents are flattened into the
  generated main ingredient list at stock strength.

## Evidence

| Claim in generated record | Review |
|---|---|
| Ferric citrate, ammonium sulfate, KH2PO4, MgSO4.7H2O, CaCl2.2H2O, Yeast extract, FeCl2.4H2O, and L-Cysteine HCl.H2O as direct g/L rows | Supported as direct medium ingredients after normalizing DSMZ's gram amounts to the stated 1011 ml final volume. |
| MnCl2.4H2O, Na2B4O7.10H2O, ZnSO4.7H2O, CuCl2.2H2O, Na2MoO4.2H2O, VOSO4.2H2O, and CoSO4.7H2O as direct g/L rows | Wrong boundary. DSMZ lists these in Allen's trace element solution and adds that stock at 10 ml per 1011 ml final medium. |
| Biotin, Folic acid, Pyridoxine hydrochloride, Thiamine HCl, Riboflavin, Nicotinic acid, Calcium D-(+)-pantothenate, Vitamin B12, p-Aminobenzoic acid, and alpha-Lipoic acid as direct g/L rows | Wrong boundary. DSMZ lists these in Wolin's vitamin solution (10x) and adds 1 ml of that stock. |
| Step 1 pH 6.0 / anoxic autoclave / sterile stock-addition text | Supported as main-medium preparation, although the stock additions are unstructured. |
| Step 2 pH 2 adjustment | Mis-scoped. DSMZ's pH 2 instruction applies to Allen's trace element solution, not to the final Athalassotoga medium. |

## Completeness

- `find data/normalized_yaml -name '*ATHALASSOTOGA*' -o -name
  '*athalassotoga*' -print` searched ignored files and found a single maintained
  owner, `data/normalized_yaml/bacterial/athalassotoga_medium.yaml`.
- An ignored-file-inclusive exact search for `CultureMech:001085`,
  `mediadive.medium:1604`, `DSMZ_Medium1604`, `athalassotoga_medium`, and
  `ATHALASSOTOGA MEDIUM` across `data`, `reports`, `history`, and `.claude`
  found the normalized owner, this generated merge, source-index rows,
  archived validation rows, and one concentration-plausibility finding.
- `find reports/yaml_record_review -maxdepth 1 -name
  '*ATHALASSOTOGA_MEDIUM.md'` searched the ignored report directory and found no
  prior review for this exact generated record stem before this report was
  written.
- The record is missing explicit solution boundaries for 10 ml Allen's trace
  element solution and 1 ml Wolin's vitamin solution (10x).
- Empty `target_organisms` and `growth_metrics` are acceptable for this
  source-formulation record.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| major | Allen's trace element solution is flattened into direct main-medium trace salts at stock strength. | DSMZ 1604 adds 10 ml Allen's trace element solution from Medium 88; the generated record lists the seven Allen salts directly at stock g/L values. | `data/normalized_yaml/bacterial/athalassotoga_medium.yaml` or the MediaDive DSMZ importer. |
| major | Wolin's vitamin solution (10x) is flattened into direct vitamin rows at stock strength. | DSMZ 1604 adds 1 ml Wolin's vitamin solution from Medium 120; the generated record lists all ten vitamins directly at their stock g/L values. | Same maintained owner or importer. |
| major | Allen's trace-stock pH step is attached to the final medium. | The source pH 2 instruction follows the Allen's stock composition; the generated record stores it as top-level Athalassotoga step 2. | Same maintained owner or importer. |

## Recommended Edits

1. Re-model Allen's trace element solution as a 10 ml stock addition with its
   composition and pH 2 instruction scoped to the stock.
2. Re-model Wolin's vitamin solution (10x) as a 1 ml stock addition with its
   composition scoped to the stock.
3. Keep ferric citrate dissolution, pH 6.0 adjustment, anoxic gas handling,
   autoclaving, and sterile FeCl2/vitamin/cysteine additions on the main medium.
4. Regenerate `data/merge_yaml/merged/ATHALASSOTOGA_MEDIUM.yaml` after the
   normalized owner or importer is repaired.

## Follow-up Checks

- Rerun open-schema, strict, term, and reference validation on the normalized
  Athalassotoga owner after correction.
- Verify the regenerated record has two stock-solution entries for Allen's
  trace element solution and Wolin's vitamin solution.
- Confirm the generated top-level preparation no longer instructs the final
  medium to pH-adjust to 2.
- Compare direct ingredient final concentrations against DSMZ's 1011 ml final
  volume after regeneration.

## Additional Notes

- `data/import_tracking/reports/concentration_plausibility.tsv` currently flags
  only `Pyridoxine hydrochloride` in this record, but all ten vitamin rows share
  the same stock-flattening boundary defect.

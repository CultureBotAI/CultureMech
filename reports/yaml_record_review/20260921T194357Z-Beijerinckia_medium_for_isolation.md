# YAML Record Review: Beijerinckia medium for isolation

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Beijerinckia_medium_for_isolation.yaml
- Started UTC: 2026-09-21T19:42:31Z
- Finished UTC: 2026-09-21T19:43:57Z
- Verdict: pass with minor issues

## Target

- Reviewed `data/merge_yaml/merged/Beijerinckia_medium_for_isolation.yaml`.
- Class: `MediaRecipe`.
- ID: `CultureMech:001269`.
- Name: `beijerinckia_medium_for_isolation`.
- Original name: `Beijerinckia medium for isolation`.
- Source identity: `mediadive.medium:1847`, label `Beijerinckia medium for isolation`, source DSMZ.
- Generated status: derived merge output under `data/merge_yaml/merged/`; the maintained owner is `data/normalized_yaml/bacterial/beijerinckia_medium_for_isolation.yaml`.
- Merge metadata: one source record, `beijerinckia_medium_for_isolation`, on fingerprint `e76a2e0f5c5722cf31e07300c7e8eb9f228fd8dec8140d5088514f628d1df993`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Beijerinckia_medium_for_isolation.yaml` via the no-project Python 3.11 workaround | Passed |
| Closed-schema strict validation, `scripts/validate_strict.py data/merge_yaml/merged/Beijerinckia_medium_for_isolation.yaml --out /private/tmp/Beijerinckia_medium_for_isolation.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/Beijerinckia_medium_for_isolation.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were applicable |
| `linkml-term-validator validate-data data/merge_yaml/merged/Beijerinckia_medium_for_isolation.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded `MediaRecipe.curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not a focused embedded-history validator for one merged record |

The documented `just` commands were not run directly because the project runtime currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` before target-specific validation.

## Identity and Grounding

- `CultureMech:001269` resolves in `data/culturemech_id_registry.tsv` to `data/normalized_yaml/bacterial/beijerinckia_medium_for_isolation.yaml`.
- MediaDive JSON and the rendered MediaDive page identify source medium 1847 as `Beijerinckia medium for isolation`, with source DSMZ and pH range 6.3 to 6.7.
- The recipe is correctly kept separate from DSMZ 111 `BEIJERINCKIA MEDIUM` and its LMG 18 sibling; DSMZ 1847 substitutes D-sucrose as the 20 g/L carbon source and lacks the trace transition-metal salts in DSMZ 111.
- The phosphate, magnesium sulfate, ferric chloride, sodium molybdate, and agar rows are grounded to exact or source-appropriate CHEBI terms. `D-Sucrose` remains ungrounded.

## Evidence

- MediaDive 1847 supports the seven ingredient rows in the current record: 0.8 g KH2PO4, 20 g D-sucrose, 0.2 g K2HPO4, 0.5 g MgSO4, 0.1 g FeCl3, 0.005 g Na2MoO4, and 15 g agar per 1000 ml.
- MediaDive 1847 supports the pH range 6.3 to 6.7.
- MediaDive 1847 supports the four preparation operations now present: make up to 1000 ml with distilled water, heat to boiling to dissolve the medium completely, autoclave at 121 C for 15 min, and cool to 45-50 C.
- A gitignore-independent search over `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` for `CultureMech:001269`, digit-bounded `mediadive.medium:1847`, digit-bounded `DSMZ Medium 1847`, `beijerinckia_medium_for_isolation`, and `Beijerinckia medium for isolation` found only the normalized owner, generated merge, generated indexes, one organism-review row, and import-priority reports. It did not find a repository-owned raw MediaDive capture for this record.

## Completeness

- No consequential ingredient, amount, pH, or sterilization gap was found against the inspected MediaDive source.
- Empty target-organism, growth-evidence, storage, and variant slots are acceptable here; MediaDive 1847 gives no strain-specific growth result, storage condition, or variant recipe in the inspected source.
- The source notes that Medium 1847 is available as `M708 HIMEDIA`; that commercial availability note is not represented in the record, but it is not part of the medium formulation.
- The old DSMZ PDF path for Medium 1847 returned a DSMZ 404 HTML page, and the MediaDive JSON for this medium does not expose a PDF `link`, so the PDF was not inspected.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Minor | `D-Sucrose` is the only source ingredient without an ontology or MIM grounding. | `data/normalized_yaml/bacterial/beijerinckia_medium_for_isolation.yaml` |
| Minor | Preparation step 1 still contains source HTML for the 1000 ml amount instead of plain text or structured amount fields. | `data/normalized_yaml/bacterial/beijerinckia_medium_for_isolation.yaml` |

## Recommended Edits

1. Verify whether `D-Sucrose` has an exact MIM/CHEBI grounding and add it only if an exact identity match is available.
2. Remove the embedded HTML from the make-up-to-1000-ml preparation step while preserving the exact source instruction.
3. Regenerate `data/merge_yaml/merged/Beijerinckia_medium_for_isolation.yaml` after the normalized owner is corrected.

## Follow-up Checks

- Rerun the open schema validator, `scripts/validate_strict.py`, `linkml-term-validator`, and `linkml-reference-validator` on the normalized owner and the regenerated merged record.
- Manually compare the regenerated record against the MediaDive 1847 JSON to verify all seven rows, pH 6.3 to 6.7, the make-up-to-1000-ml instruction, boiling, autoclaving, and 45-50 C cooling are preserved.

## Additional Notes

- The MediaDive JSON and MediaDive rendered page agreed for every inspected ingredient, amount, pH bound, and preparation step.
- Reports are read-only review artifacts; no normalized recipe, generated merge, page, history entry, or GitHub issue was edited for this review.

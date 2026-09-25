# YAML Record Review: Hylemonella Gracilis Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hylemonella_gracilis_medium__4b68fc6c.yaml
- Started UTC: 2026-09-23T13:53:40Z
- Finished UTC: 2026-09-23T13:55:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:002458 |
| Name | hylemonella_gracilis_medium |
| Original name | Hylemonella gracilis medium |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | SOLID_AGAR |
| pH | 7.2 |
| Source identity | MediaDive/JCM Medium J1296, Hylemonella gracilis medium |
| Generated path reviewed | data/merge_yaml/merged/hylemonella_gracilis_medium__4b68fc6c.yaml |
| Maintained owner | data/normalized_yaml/bacterial/hylemonella_gracilis_medium.yaml |

The reviewed file is generated from the maintained MediaDive/JCM import above.
Future fixes should update
`data/normalized_yaml/bacterial/hylemonella_gracilis_medium.yaml`, preserve the
JCM optional agar semantics, and regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hylemonella_gracilis_medium__4b68fc6c.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hylemonella_gracilis_medium__4b68fc6c.yaml --out /private/tmp/hylemonella_gracilis_medium__4b68fc6c.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hylemonella_gracilis_medium__4b68fc6c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hylemonella_gracilis_medium__4b68fc6c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is coherent: `CultureMech:002458`,
  `mediadive.medium:J1296`, the MediaDive REST record, and the live JCM 1296
  page all identify Hylemonella gracilis medium.
- A gitignore-independent exact search for `CultureMech:002458` over
  `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports` found this
  maintained record, generated indexes, generated merged YAML, archival
  reports, and the review manifest.
- A gitignore-independent exact search for `mediadive.medium:J1296` over
  `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports` found only
  this JCM 1296 record plus generated indexes and the review manifest.
- Tween 80, KH2PO4, and agar are grounded to exact enough ontology terms.
  Bacto peptone and yeast extract remain explicit unresolved complex
  ingredients, which is acceptable for a JCM complex medium.
- The `SOLID_AGAR` physical-state assertion is too narrow because the source
  marks agar as optional with an "if needed" note.

## Evidence

- The generated Bacto peptone, yeast extract, Tween 80, KH2PO4, agar, and pH
  7.2 values match the MediaDive parse of the JCM 1296 table.
- JCM 1296 lists tap water as 1.0 L; MediaDive represents the row as 1000 ml;
  the YAML imports it as `1000 G_PER_L`.
- JCM labels the 15 g agar row as optional in prose; the YAML makes agar a
  required top-level ingredient and classifies the entire recipe as
  `SOLID_AGAR`.
- The JCM page provides no record-specific sterilization sentence after pH
  adjustment, so the provider default applies: autoclave at 121 C for 15 min
  unless otherwise stated. The YAML only records the pH-adjustment step.

## Completeness

- The required JCM table rows are present.
- The tap-water volume needs dimensional repair.
- Agar optionality and the resulting broth-versus-agar state need to be
  preserved as a variant or optional addition.
- Empty optional fields for target organisms, synonyms, variants, direct
  publication references, discussions, and quality flags are acceptable for
  this provider import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The 1 L tap-water row is represented as a mass concentration. | JCM 1296 lists 1.0 L Tap water; the YAML records Tap water as `1000 G_PER_L`. | `data/normalized_yaml/bacterial/hylemonella_gracilis_medium.yaml`; MediaDive volume import. |
| Major | Agar optionality is lost. | The source row is `Agar (if needed)` at 15 g, but the YAML records agar as mandatory and sets `physical_state: SOLID_AGAR`. | `data/normalized_yaml/bacterial/hylemonella_gracilis_medium.yaml`; optional ingredient handling. |
| Major | The JCM default autoclave step is missing. | JCM gives no formula-specific sterilization override for Medium 1296, so its default autoclave instruction applies; the YAML only says to adjust pH to 7.2. | `data/normalized_yaml/bacterial/hylemonella_gracilis_medium.yaml`; JCM import should preserve default sterilization. |

## Recommended Edits

1. Represent the 1 L tap-water row as source volume rather than `1000 G_PER_L`.
2. Model the 15 g agar row as optional or as a solidifying variant and avoid
   making the base medium intrinsically `SOLID_AGAR`.
3. Add JCM's default autoclave instruction after the pH adjustment.
4. Regenerate `data/merge_yaml/merged/` from the corrected normalized record.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  JCM 1296 merged record.
- Manually compare the regenerated six-row formula against JCM 1296 and
  MediaDive J1296.
- Confirm agar optionality is visible and tap water is no longer represented as
  a gram-per-liter concentration.

## Additional Notes

- The inspected MediaDive J1296 REST record has a clean 1000 ml main solution;
  the water defect is confined to the volume-to-concentration import layer.

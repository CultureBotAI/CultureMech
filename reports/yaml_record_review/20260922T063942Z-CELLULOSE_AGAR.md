# YAML Record Review: cellulose_agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CELLULOSE_AGAR.yaml
- Started UTC: 2026-09-22T06:39:08Z
- Finished UTC: 2026-09-22T06:39:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009975 |
| Name | cellulose_agar |
| Original name | Cellulose Agar |
| Category | bacterial |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml |
| Generated record | data/merge_yaml/merged/CELLULOSE_AGAR.yaml |
| Merge fingerprint | cfaf3419995f48c33e95a015b112e8576156cd98ef75231bf77577c06e361cfc |
| Merged from | TOGO_M57_Cellulose_Agar |

The record is generated from one TOGO import of JCM Medium 65 through TOGO
medium M57. The live TOGO API reports `original_media_id: JCM_M65`, source URL
`https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=65`, and name
`Cellulose Agar`.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/CELLULOSE_AGAR.yaml` | Passed |
| strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/CELLULOSE_AGAR.yaml --out /private/tmp/CELLULOSE_AGAR.strict.tsv --workers 1 --quiet` | Passed with 0 errors |
| reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/CELLULOSE_AGAR.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/CELLULOSE_AGAR.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| embedded curation history | `just validate-history data/merge_yaml/merged/CELLULOSE_AGAR.yaml` | Not checked: `just validate-history` validates standalone `history/` records against `HistoryRecord`, not `MediaRecipe.curation_history` blocks |

`just`-based validators were not used because the local project environment
tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools.
The narrow validators above ran offline with Python 3.11.

## Identity and Grounding

The record identity is correct for TOGO M57 Cellulose Agar / JCM M65. The
ingredient identities are mostly correct, including MgSO4 x 7H2O, K2HPO4,
FeSO4 x 7H2O, CaCO3, NH4NO3, L-asparagine, agar, and urea.

`Cellulose powder` is ungrounded in the TOGO record although the source denotes
cellulose as the carbon source; that is less severe than the quantity defects
because the preferred term is still explicit.

## Evidence

The inspected TOGO M57 API supports 0.3 g MgSO4 x 7H2O, 0.2 g K2HPO4, 5 mg
FeSO4 x 7H2O, 0.2 g CaCO3, 0.2 g NH4NO3, 20 g cellulose powder, 0.2 g casein,
0.25 g L-asparagine, 15 g agar, 0.1 g BD-Difco yeast extract, 0.1 g urea,
0.1 g BD-Difco Casamino acids, 1 L distilled water, and the note that the pH is
unadjusted.

The generated record stores FeSO4 x 7H2O as `5 G_PER_L`, inflating the source
5 mg by 1000-fold. It also stores 1 L distilled water as `1 G_PER_L` and drops
the source's `pH unadjusted` preparation note.

The original JCM URL embedded in the record was fetched directly and currently
returns a JCM page for medium 65 with `Nothing found`; only the TOGO API cache
was able to recover the imported JCM 65 formulation during this review.

## Completeness

A gitignore-independent exact search over `data`, `.`, YAML, JSON, and archived
reports found the maintained TOGO M57 record plus a separate MediaDive J65
record at `data/normalized_yaml/bacterial/cellulose_agar.yaml` and
`data/merge_yaml/merged/cellulose_agar__f667ef58.yaml`. The MediaDive sibling
normalizes the same FeSO4 row to 0.005 g/L and keeps the `pH unadjusted`
preparation note, so the two same-source imports should converge after the TOGO
unit bug is fixed.

Empty optional organism and growth slots are acceptable for JCM 65 because the
source formula contains no strain-specific growth measurements.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `FeSO4 x 7H2O` is represented as `5 G_PER_L`; TOGO M57 lists `5 mg`, which should be `0.005 g/L` for this 1 L formula. | data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml; TOGO importer |
| Major | The same JCM 65 formula exists as a separate MediaDive-maintained and generated record with a different CultureMech ID and fingerprint. | data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml; data/normalized_yaml/bacterial/cellulose_agar.yaml; merge reconciliation |
| Minor | `Distilled water` is stored as `1 G_PER_L` even though the source lists `1 L`; this should be final volume context rather than one gram per liter of water. | data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml |
| Minor | The TOGO record drops the `pH unadjusted` note and points at a JCM `GRMD=65` URL that currently returns no medium formulation. | data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml |
| Minor | `Cellulose powder` is not grounded to a structured cellulose term. | data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml |
| Minor | The first TOGO import history note says `Source: JCM, ID: M57`; `M57` is the TOGO medium ID, while the original JCM ID is `JCM_M65` / `GRMD=65`. | data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml`, convert the
   FeSO4 x 7H2O row from `5 G_PER_L` to `0.005 G_PER_L`, preserving the source
   evidence that listed 5 mg in the 1 L formula.
2. Reconcile the TOGO M57 and MediaDive J65 maintained inputs so the merge emits
   one generated Cellulose Agar record for JCM 65.
3. Represent the 1 L water row as a final-volume/preparation fact rather than
   `1 G_PER_L`.
4. Preserve the source `pH unadjusted` note as preparation or condition
   metadata.
5. Ground cellulose powder to the appropriate cellulose term if the packaged
   ingredient resolver has an exact match for this supplied form.
6. Add a current accessible source URL if JCM `GRMD=65` remains unavailable, and
   add a clarifying history event distinguishing TOGO M57 from JCM 65 if older
   history cannot be corrected.

## Follow-up Checks

1. Rerun merge generation and verify that JCM 65 emits one generated record.
2. Rerun LinkML, strict, term, and reference validation for the regenerated
   Cellulose Agar record.
3. Compare the regenerated TOGO-owned record against the live TOGO M57 API and
   the MediaDive J65 sibling, confirming that FeSO4 is 0.005 g/L and that pH is
   explicitly unadjusted.
4. Re-fetch the JCM `GRMD=65` URL or a replacement canonical source to verify
   whether the original JCM page is still unavailable.

## Additional Notes

`Agar` correctly sets `physical_state: SOLID_AGAR`; its 15 g/L amount is
supported by TOGO M57.

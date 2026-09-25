# YAML Record Review: LACTOBACILLUS medium II

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lactobacillus_medium_ii__915ff5f7.yaml
- Started UTC: 2026-09-23T18:23:29Z
- Finished UTC: 2026-09-23T18:24:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/lactobacillus_medium_ii__915ff5f7.yaml` |
| Generated status | Generated canonical merge from `KOMODO_93_LACTOBACILLUS_medium_II.yaml` and `lactobacillus_medium_ii.yaml`; do not edit directly |
| Schema class | `MediaRecipe` |
| CultureMech ID | `CultureMech:006867` |
| Name | `lactobacillus_medium_ii` |
| Original name | `LACTOBACILLUS medium II` |
| Category | `bacterial` |
| Physical state | `SOLID_AGAR` |
| Source accessions | `komodo.medium:93`, `mediadive.medium:93` |
| Merge fingerprint | `915ff5f71df10a46a397e33e144ae22f00d697f9115a9c83a4d3f62948127358` |
| Maintained owners inspected | `data/normalized_yaml/bacterial/KOMODO_93_LACTOBACILLUS_medium_II.yaml`; `data/normalized_yaml/bacterial/lactobacillus_medium_ii.yaml` |

The generated target merges the KOMODO import for DSMZ Medium 93 with the
DSMZ/MediaDive import for the same medium. The duplicate relationship is
source-supported, but the generated record still omits source water, converts
milliliter additions to gram-per-liter concentrations, and loses the DSMZ
parent's pH-adjustment step when the KOMODO child is selected as canonical.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lactobacillus_medium_ii__915ff5f7.yaml` | Passed; no output |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/lactobacillus_medium_ii__915ff5f7.yaml --out /private/tmp/lactobacillus_medium_ii__915ff5f7.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/lactobacillus_medium_ii__915ff5f7.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/lactobacillus_medium_ii__915ff5f7.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded history | `just validate-history data/merge_yaml/merged/lactobacillus_medium_ii__915ff5f7.yaml` | Not checked: `just validate-history` validates standalone `history/` YAML records, not embedded `MediaRecipe.curation_history` lists |

The `just` validator entry points were not used because this checkout resolves
`llvmlite==0.46.0` under Python 3.13 and the build currently crashes in
`setuptools` before validators run. The focused Python 3.11 commands above
exercise the same record-level schema, strict, reference, and term validators.

## Identity and Grounding

- `CultureMech:006867` identifies the KOMODO source record for DSMZ Medium 93.
  Its `parent_media` points to the DSMZ/MediaDive source duplicate,
  `CultureMech:002115`.
- Live MediaDive `/rest/medium/93` resolves to `LACTOBACILLUS MEDIUM II`,
  source DSMZ, pH 5.2, and the DSMZ Medium 93 PDF URL.
- The DSMZ Medium 93 PDF matches the 14 non-water ingredients in the generated
  record and supplies the same pH 5.2.
- A separate JCM `J16` Lactobacillus Medium II record exists, but it is a
  different source recipe with a Salt solution R stock and pH 6.3; it should not
  be merged into this DSMZ 93 branch.
- The DL-mevalonic acid `term.label` is malformed as the folded scalar
  `mevalonic acid acid`; the record keeps the legacy
  `MediaIngredientMech:000769` DL-mevalonic-acid term, but the primary CHEBI
  label is not trustworthy as emitted.

An ignored-inclusive exact search covered `data/normalized_yaml`,
`data/merge_yaml`, and `reports/archive` for `CultureMech:006867`,
`CultureMech:002115`, digit-bounded `komodo.medium:93` and
`mediadive.medium:93`, the exact KOMODO filename, and the merge fingerprint. It
found the generated target, both normalized owners, normalized source indexes,
the archived DSMZ/KOMODO source-duplicate review, and old validation reports.
A previous looser label search had overmatched `LACTOBACILLUS medium III`; that
result was discarded.

## Evidence

Supported in inspected sources:

- DSMZ Medium 93 lists Casein peptone tryptic digest 10 g, Yeast extract 5 g,
  Meat extract 2 g, Glucose 20 g, KH2PO4 0.5 g, K2HPO4 0.5 g,
  FeSO4 x 7 H2O 10 mg, MgSO4 x 7 H2O 200 mg, MnSO4 x H2O 7.5 mg,
  Tween 80 1 ml, Ethanol 40 ml, Na-acetate 20 g, DL-mevalonic acid 30 mg,
  Agar 15 g, and Distilled water 1000 ml, followed by pH adjustment to 5.2.
- MediaDive `/rest/medium/93` reports the same compound list, pH 5.2, and 1000
  ml recipe volume.
- The KOMODO source record accurately links itself back to DSMZ Medium 93 as a
  source duplicate of the DSMZ/MediaDive owner.

Unsupported or stale in the generated target:

- The generated target omits the DSMZ/MediaDive `Distilled water` 1000 ml row.
- `Tween 80` and `Ethanol` are represented as `1 G_PER_L` and `40 G_PER_L`
  respectively, but both inspected sources give those rows in milliliters.
- The generated merge drops the pH-adjustment `preparation_steps` entry present
  on the DSMZ/MediaDive parent.
- The target has no `references` list even though the DSMZ PDF and MediaDive
  REST record were recoverable.

## Completeness

Consequential gaps:

- Distilled water is missing from the composition.
- Volume additions need volume-aware concentrations or source-quantity notes.
- DSMZ pH preparation and source references are absent from the merged output.
- The emitted DL-mevalonic-acid CHEBI label needs repair.

Empty or absent fields that are not defects for this generated DSMZ recipe:

- `target_organisms`, growth metrics, genome assembly, atmosphere, storage, and
  shelf-life fields can stay empty until source-specific evidence supports
  them.

## Findings

| Severity | Finding | Evidence | Maintained owner for fix |
|---|---|---|---|
| Major | DSMZ/MediaDive water is missing. | The DSMZ PDF and MediaDive medium 93 both include 1000 ml distilled water; neither normalized owner nor the generated merge includes water. | `data/normalized_yaml/bacterial/lactobacillus_medium_ii.yaml` and `data/normalized_yaml/bacterial/KOMODO_93_LACTOBACILLUS_medium_II.yaml`, or their DSMZ/KOMODO import path if this omission is systemic. |
| Major | Milliliter additions are represented as mass concentrations. | DSMZ and MediaDive report Tween 80 as 1 ml and Ethanol as 40 ml; the generated record stores `1 G_PER_L` and `40 G_PER_L`. | Both normalized owners. |
| Major | The merge drops the source pH-adjustment step. | DSMZ says to adjust pH to 5.2 and the DSMZ/MediaDive normalized owner has that `preparation_steps` entry; the generated KOMODO-canonical merge has no preparation steps. | Preserve parent preparation metadata in `src/culturemech/merge/merge_recipes.py` or copy the step into `KOMODO_93_LACTOBACILLUS_medium_II.yaml` before merging. |
| Major | Source references are absent from the generated and normalized records. | The record has only free-text `notes`; no `references` list points to the DSMZ Medium 93 PDF or MediaDive medium 93 endpoint. | Both normalized owners. |
| Minor | The DL-mevalonic-acid primary term label is malformed and overbroad. | The YAML folds the label as `mevalonic acid acid`; the source specifies DL-mevalonic acid. | Re-ground or de-ground `DL-mevalonic acid` in both normalized owners using the packaged MIM label index or a checked CHEBI lookup. |

## Recommended Edits

1. Add the 1000 ml distilled-water row to the DSMZ/MediaDive normalized owner
   and propagate the same source-corrected composition to the KOMODO duplicate.
2. Correct Tween 80 and Ethanol so their milliliter source amounts are not
   stored as `G_PER_L` mass concentrations.
3. Preserve the DSMZ pH 5.2 adjustment and add source references when the
   KOMODO duplicate is merged with its DSMZ/MediaDive parent.
4. Repair the malformed DL-mevalonic-acid grounding and label.
5. Regenerate `data/merge_yaml/merged/` and verify that
   `lactobacillus_medium_ii__915ff5f7.yaml` still merges only the KOMODO 93 and
   DSMZ 93 records, not the same-label JCM 16 recipe.

## Follow-up Checks

- Rerun the focused open, strict, reference, and term validators against both
  normalized owners after the water, unit, reference, and DL-mevalonic-acid
  edits.
- Re-query the DSMZ Medium 93 PDF and MediaDive `/rest/medium/93` to confirm all
  amounts, units, pH, and source identities.
- Run `just merge-recipes`, then rerun focused validators against
  `data/merge_yaml/merged/lactobacillus_medium_ii__915ff5f7.yaml`.
- Run `just audit-merge-freshness --json --list` and confirm this generated
  file is not drifted.
- Search with ignored files included for exact `komodo.medium:93` and
  `mediadive.medium:93` after curation to confirm the intended source-duplicate
  relationship remains.

## Additional Notes

- The review inspected `CLAUDE.md`, `justfile`, `project.justfile`, the local
  review and curation skills, the review checklist, the relevant MediaRecipe
  schema section, the generated target, both normalized owners, the same-label
  JCM J16 sibling, live MediaDive medium 93, and the DSMZ Medium 93 PDF.
- The same-label JCM J16 record is a real Lactobacillus Medium II recipe but has
  a different pH and different ingredient list; label-only duplicate detection
  must keep it separate from DSMZ 93.

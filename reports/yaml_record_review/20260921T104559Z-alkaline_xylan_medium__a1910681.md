# YAML Record Review: ALKALINE XYLAN MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/alkaline_xylan_medium__a1910681.yaml
- Started UTC: 2026-09-21T10:44:45Z
- Finished UTC: 2026-09-21T10:45:59Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/alkaline_xylan_medium__a1910681.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:002473` |
| Name | `alkaline_xylan_medium` |
| Original name | `ALKALINE XYLAN MEDIUM` |
| Category | `bacterial` |
| Generated status | Generated merge from one maintained normalized source |
| Maintained owner | `data/normalized_yaml/bacterial/alkaline_xylan_medium.yaml` |
| Upstream source | JCM GRMD `130` through the direct MediaDive/JCM import |
| Merge fingerprint | `a1910681947d198ee18feb79faf9de0b391c1f5a0fe04b0c1d49f46b292e5a00` |

This is the generated merge of the direct JCM/MediaDive source record for JCM
Medium 130. The generated merge should be regenerated after repairing
`data/normalized_yaml/bacterial/alkaline_xylan_medium.yaml` or the direct JCM
importer; the derived merge itself should remain read-only.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/alkaline_xylan_medium__a1910681.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/alkaline_xylan_medium__a1910681.yaml --out /private/tmp/alkaline_xylan_medium__a1910681.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/alkaline_xylan_medium__a1910681.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/alkaline_xylan_medium__a1910681.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils`/`pkg_resources` deprecation warning |
| Embedded curation history | Not checked | No focused validator is documented for embedded `MediaRecipe.curation_history`; `just validate-history` validates standalone files under `history/` |

The usual `just` wrappers were not rerun here because target-specific `just
validate-schema`, `just validate-strict`, and `just validate-terms` currently
fail before target validation while the project `uv` environment attempts to
build `llvmlite==0.46.0` under Python 3.13. The no-project validator commands
above use Python 3.11 and the cached validator packages instead.

## Identity and Grounding

The record identity is coherent for JCM Medium 130: the `media_term` is
`mediadive.medium:J130`, `notes` point to JCM GRMD 130, the source history
names `JCM` and `J130`, and the generated merge is from the single maintained
parent `alkaline_xylan_medium`.

The exact ignored-files-including search:

```bash
rg -n "a1910681947d198ee18feb79faf9de0b391c1f5a0fe04b0c1d49f46b292e5a00|CultureMech:002473|JCM Medium J130|mediadive.medium:J130|https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd\?GRMD=130" data/normalized_yaml/bacterial data/merge_yaml/merged/alkaline_xylan_medium__a1910681.yaml --glob '*.yaml' --no-ignore --hidden
```

found the intended maintained parent and this generated record. Other hits were
nearby JCM numbers such as J1300, J1301, and J1303, or the source-equivalent
TOGO M122 snapshot, not alternate parents for this merge.

Ingredient grounding agrees with most of the JCM GRMD 130 rows. The generic
`MnSO4 x n H2O` label is also compatible with the current JCM `xH2O` hydrate
form; the row is not overgrounded to a specific hydrate. Xylan and Polypeptone
remain undefined materials, which is acceptable because the current source
does not supply a ChEBI-level product identity.

## Evidence

The inspected JCM GRMD 130 page supports all non-water ingredient quantities:
Xylan 10 g/L, K2HPO4 1 g/L, NH4NO3 2 g/L, MgSO4 x 7H2O 0.2 g/L, MnSO4 x H2O
0.005 g/L, FeSO4 x 7H2O 0.005 g/L, CaCl2 x 2H2O 0.1 g/L, yeast extract 3 g/L,
Polypeptone/Hipolypepton 0.3 g/L, and resazurin 0.001 g/L. The generated
record preserves those numeric final concentrations.

The same JCM page lists 1 L distilled water. The generated record has no water
row, so the formulation has no explicit solvent/final-volume component.

The JCM page records pH 10.0 adjustment with filter-sterilized 10% sodium
carbonate. The generated record preserves `ph_value: 10.0` and a preparation
description for the adjustment, but the preparation action is
`FILTER_STERILIZE`; the step being performed is pH adjustment with a
filter-sterilized solution, not filtration of the whole medium.

JCM GRMD pages also state that media should be autoclaved at 121 C for 15 min
unless otherwise specified. Nothing in this recipe overrides that default, and
the generated record has no autoclaving step.

No claim-level `evidence` objects or structured `references` are present. The
JCM URL is retained only in free text under `notes`.

## Completeness

Consequential gaps:

- Distilled water, 1 L, is missing from a 1 L JCM recipe.
- Basal autoclaving at 121 C for 15 min is missing.
- The pH-adjustment step has the wrong action enum and no structured 10%
  Na2CO3 reagent.
- The JCM source is represented only as a free-text note.

Empty optional slots that are not automatic defects:

- `target_organisms` and `growth_metrics` can remain empty because JCM GRMD 130
  is a medium formulation, not a growth study.
- Xylan and Polypeptone/Hipolypepton can remain ungrounded until an exact
  material identity is verified.

The prior-report search:

```bash
find reports/yaml_record_review -name '*alkaline_xylan_medium__a1910681*' -print
```

included ignored report files and found no existing report for this exact
generated record before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The 1 L distilled-water row is missing. Without it, the recipe loses its solvent and final-volume basis. | JCM GRMD 130 lists 1 L distilled water. | `data/normalized_yaml/bacterial/alkaline_xylan_medium.yaml`, or the direct JCM/MediaDive importer |
| Major | Default autoclaving was dropped. The record captures only the pH adjustment and omits sterilization of the basal recipe. | The inspected JCM page says to autoclave media at 121 C for 15 min unless otherwise stated, and this medium gives no override. | `data/normalized_yaml/bacterial/alkaline_xylan_medium.yaml`, or the direct JCM/MediaDive importer |
| Minor | The pH-adjustment preparation step is typed as `FILTER_STERILIZE`, even though the source calls for pH adjustment with a filter-sterilized 10% Na2CO3 solution. | JCM GRMD 130 describes a pH adjustment to 10.0, not a filter-sterilization operation on the recipe. | `data/normalized_yaml/bacterial/alkaline_xylan_medium.yaml` |
| Minor | Provenance is free-text only, and live JCM supplier wording has drifted from the imported snapshot: the record says `Polypeptone`, while the current JCM page names `Hipolypepton (FUJIFILM Wako)`. | The only source link is in `notes`; the fetched JCM page carries the current supplier-specific name. | `data/normalized_yaml/bacterial/alkaline_xylan_medium.yaml` |

No blocker findings were found.

## Recommended Edits

1. Add 1 L distilled water to
   `data/normalized_yaml/bacterial/alkaline_xylan_medium.yaml`, using the
   repository's volume convention for water in a 1 L recipe.
2. Add a basal autoclaving preparation step for 121 C for 15 min.
3. Change the pH-adjustment step action from `FILTER_STERILIZE` to the closest
   pH-adjustment action available in the schema, and represent the 10% Na2CO3
   solution as a pH-adjusting reagent rather than implying the whole medium is
   filter-sterilized.
4. Move the JCM GRMD 130 URL into structured source/reference fields and record
   the Polypeptone-to-Hipolypepton source-version drift.
5. Regenerate `data/merge_yaml/merged/alkaline_xylan_medium__a1910681.yaml` and
   generated pages from the maintained source.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/alkaline_xylan_medium.yaml`.
- Run `just validate-strict data/normalized_yaml/bacterial/alkaline_xylan_medium.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/alkaline_xylan_medium.yaml` after adding water and any Na2CO3 reagent.
- Run `just validate-references data/normalized_yaml/bacterial/alkaline_xylan_medium.yaml` after adding structured JCM provenance.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating the merge.
- Manually compare the regenerated merge against JCM GRMD 130 for the retained g/L conversions, the restored 1 L water row, pH 10.0, and the default autoclaving step.

## Additional Notes

- The neighboring TOGO M122 record is a snapshot of the same JCM GRMD 130
  recipe, but this direct JCM import has a different stable ID and merge
  fingerprint. The missing-water defect is specific to this direct import; the
  TOGO snapshot preserved water but assigned it the wrong unit.
- This generated record is structurally valid and scientifically closer than
  the TOGO M122 import because it already converted JCM milligram quantities to
  g/L.

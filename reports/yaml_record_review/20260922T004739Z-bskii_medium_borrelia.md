# YAML Record Review: BSKII medium (Borrelia)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bskii_medium_borrelia.yaml
- Started UTC: 2026-09-22T00:47:39Z
- Finished UTC: 2026-09-22T00:47:39Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:001256 |
| Label | bskii_medium_borrelia |
| Original label | BSKII medium (Borrelia) |
| Category | bacterial |
| Source accession | mediadive.medium:1829 |
| Source | DSMZ Medium 1829 |
| Generated path | data/merge_yaml/merged/bskii_medium_borrelia.yaml |
| Maintained owner | data/normalized_yaml/bacterial/bskii_medium_borrelia.yaml |
| Merge fingerprint | 157a5167c9b8b7aa5fd3594b8d8ff02361bcadfc5b3d90c4dcdb1b472c99bf07 |

The reviewed target is a generated merge under `data/merge_yaml/merged`, derived
from the single normalized owner `bskii_medium_borrelia`. Future fixes belong in
that normalized file or in the LB-commercial-product enrichment path that added
unsupported LB rows.

## Validation

| Check | Result |
| --- | --- |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bskii_medium_borrelia.yaml` | Passed |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bskii_medium_borrelia.yaml --out /private/tmp/bskii_medium_borrelia.strict.tsv --workers 1 --quiet` | Passed |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bskii_medium_borrelia.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 structured URL checks |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bskii_medium_borrelia.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| `just validate-history data/merge_yaml/merged/bskii_medium_borrelia.yaml` | Not checked: `validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |

Direct `just validate-schema`, `just validate-strict`, `just validate-terms`, and
`just validate-references` were not rerun because the project uv environment tries
to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with
`TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The
equivalent no-project Python 3.11 validators above passed.

## Identity and Grounding

The generated target's ID, label, MediaDive accession, liquid physical state, and
pH 7.3 identify DSMZ Medium 1829, BSKII medium (Borrelia). The inspected DSMZ PDF
for Medium 1829 directly supports HEPES, trisodium citrate dihydrate, glucose,
pyruvate, N-acetylglucosamine, sodium bicarbonate, yeast extract, Bacto peptone,
rabbit serum, MEM alpha Modification, pH 7.3, and filter sterilization.

The CHEBI mappings for HEPES, citrate, glucose, pyruvate,
N-acetylglucosamine, and sodium bicarbonate are acceptable for the labels in the
DSMZ recipe. Rabbit serum, Bacto peptone, MEM alpha Modification, and bovine
serum albumin Fraction V are complex or commercial materials and need source
labels rather than small-molecule CHEBI substitutions.

## Evidence

Supported:

| Claim | Source support |
| --- | --- |
| DSMZ/MediaDive 1829 identity | The live DSMZ PDF is titled `1829: BSKII medium (Borrelia)` |
| pH 7.3 and liquid state | DSMZ reports final pH 7.3 and final volume 100 ml |
| HEPES, trisodium citrate dihydrate, glucose, pyruvate, N-acetylglucosamine, sodium bicarbonate, yeast extract, Bacto peptone, and MEM alpha Modification amounts | DSMZ lists the same amounts per 100 ml, matching the generated g/L conversions |
| `FILTER_STERILIZE` preparation | DSMZ says to combine all ingredients, adjust pH to 7.3 with 1 M NaOH, and filter-sterilize |

Unsupported or incomplete:

| Generated claim | Problem |
| --- | --- |
| Top-level LB Miller notes and `Tryptone 10.0 G_PER_L`, extra `Yeast extract 5.0 G_PER_L`, `Sodium chloride 10.0 G_PER_L` | DSMZ Medium 1829 does not cite LB Miller broth, Sigma L3522, BD 244520, laboratorynotes.com, or these three LB rows. |
| No bovine serum albumin | DSMZ lists bovine serum albumin Fraction V at 0.85 g per 100 ml, so the generated record is missing 8.5 g/L BSA. |
| `Rabbit serum`, `8.56 G_PER_L` | DSMZ lists rabbit serum as 8.56 ml per 100 ml; the record preserves the number but changes the volume to mass and loses the 10x g/L conversion context. |
| No deionized water row | DSMZ instructs to fill with deionized water to 100 ml. |
| No structured DSMZ reference | Source identity is only represented by a DSMZ label in `notes` and `mediadive.medium:1829`; no structured URL is available for reference validation. |

## Completeness

The record is materially incomplete and over-specified at the same time. It lacks
DSMZ's BSA and water rows, misstates rabbit serum, and adds an unrelated LB
Miller expansion. The LB block is not isolated to this record: a
gitignore-independent search for the `laboratorynotes.com` LB Miller text found
the same unsupported enrichment block in many normalized and generated records,
and earlier YAML review reports have already flagged it in other BSK and
Middlebrook records. That search included hidden and ignored files under
`data`, `scripts`, `.claude`, and `reports`.

A second gitignore-independent `rg --no-ignore --hidden --pcre2` search for
`CultureMech:001256`, `mediadive.medium:1829`, `DSMZ Medium 1829`,
`bskii_medium_borrelia`, and merge fingerprint `157a5167...` covered hidden and
ignored files under `data/normalized_yaml`, `data/merge_yaml/merged`, ID
registries, generated indexes, media reports, growth-review reports, archived
validation reports, and existing YAML review reports. It found only the active
normalized owner, this generated merge, expected indexes, and historical report
paths under the pre-rename `DSMZ_1829_BSKII_medium_Borrelia.yaml` filename. I
found no pre-existing `reports/yaml_record_review/*bskii_medium_borrelia.md`
report.

Empty target-organism and growth-evidence slots are not defects for this source
recipe. A prior growth-review pass found Borrelia BSK/modified-BSK cultivation
leads but no sufficiently supported strain/formulation candidates for this local
parent.

## Findings

| Severity | Finding | Maintained owner for a future fix |
| --- | --- | --- |
| Major | Three LB Miller ingredients and all LB Miller commercial-product metadata are unsupported in DSMZ Medium 1829. They add 10 g/L tryptone, 5 g/L yeast extract, and 10 g/L sodium chloride to BSKII medium even though the DSMZ formula contains none of those LB rows. | `data/normalized_yaml/bacterial/bskii_medium_borrelia.yaml` and the LB commercial-product enrichment rule |
| Major | Bovine serum albumin Fraction V is missing. DSMZ Medium 1829 lists 0.85 g per 100 ml, equivalent to 8.5 g/L. | `data/normalized_yaml/bacterial/bskii_medium_borrelia.yaml` |
| Major | Rabbit serum is unit-shifted. DSMZ lists 8.56 ml per 100 ml, but the record stores `8.56 G_PER_L` instead of a volume amount. | `data/normalized_yaml/bacterial/bskii_medium_borrelia.yaml` |
| Major | Deionized water to the 100 ml final volume is missing. | `data/normalized_yaml/bacterial/bskii_medium_borrelia.yaml` |
| Major | The record lacks a structured DSMZ/MediaDive reference, leaving reference validation with zero checks. | `data/normalized_yaml/bacterial/bskii_medium_borrelia.yaml` |

No blocker or minor findings found.

## Recommended Edits

1. Remove the unsupported LB Miller top-level note block and the extra Tryptone,
   LB Yeast extract, and Sodium chloride rows from
   `data/normalized_yaml/bacterial/bskii_medium_borrelia.yaml`.
2. Add Bovine serum albumin Fraction V at 8.5 g/L and deionized water to the
   final volume.
3. Correct rabbit serum to a source-preserving volume, either 8.56 ml per
   100 ml or the equivalent 85.6 ml/L.
4. Add a structured reference to DSMZ/MediaDive Medium 1829.
5. Regenerate `data/merge_yaml/merged/bskii_medium_borrelia.yaml`.

## Follow-up Checks

- Rerun focused schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/bskii_medium_borrelia.yaml`.
- Rerun `just verify-merges` after regeneration and inspect the generated BSKII
  diff to confirm only the DSMZ Medium 1829 rows remain.
- Manually compare the regenerated record against the DSMZ PDF to confirm all
  eleven DSMZ rows, pH 7.3, and filter sterilization survived curation.
- Rerun the exact hidden/ignored-file LB Miller search after the systemic
  enrichment fix to confirm this owner no longer carries
  `laboratorynotes.com` or `L3522` metadata.

## Additional Notes

- The MediaDive HTML page for `/medium/1829` loaded, but the official DSMZ
  one-page PDF was the concise inspected formulation source.

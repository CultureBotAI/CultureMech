# YAML Record Review: am3_nalidixic_acid_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/am3_nalidixic_acid_medium.yaml`
- Started UTC: 2026-09-21T11:16:31Z
- Finished UTC: 2026-09-21T11:17:24Z
- Verdict: needs curation

## Target

| Field | Observed value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:008610` |
| Name | `am3_nalidixic_acid_medium` |
| Original name | `AM3 + Nalidixic acid medium` |
| Source identity | TOGO Medium M2022, original source NBRC M1313 |
| Generated status | Generated 3-source merge |
| Generated path | `data/merge_yaml/merged/am3_nalidixic_acid_medium.yaml` |
| Maintained inputs | `data/normalized_yaml/bacterial/am3_medium.yaml`; `data/normalized_yaml/bacterial/am3_nalidixic_acid_medium.yaml`; `data/normalized_yaml/bacterial/am3_nalidixic_acid_kanamycin_medium.yaml` |

The generated record names the nalidixic-acid AM3 variant but is a stale merge of plain AM3, the nalidixic-acid AM3 variant, and the nalidixic-acid plus kanamycin AM3 variant.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/am3_nalidixic_acid_medium.yaml` | Passed; no issues found. |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/am3_nalidixic_acid_medium.yaml --out /private/tmp/am3_nalidixic_acid_medium.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 `ERROR` rows emitted. |
| Reference | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/am3_nalidixic_acid_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/am3_nalidixic_acid_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Documented focused validator | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints are unavailable in this checkout because project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before target-specific validation. The no-project commands above exercise the same schema and validation code with Python 3.11.

## Identity and Grounding

The top-level ID, label, and source fields point to TOGO M2022 / NBRC M1313:

- `id: CultureMech:008610`
- `name: am3_nalidixic_acid_medium`
- `media_term.term.id: TOGO:M2022`
- `notes: Original source: NBRC - NBRC_M1313`

That identity is corrupted by the generated merge metadata. The record was merged from:

- `am3_medium.yaml`: NBRC M1312 plain AM3, no antibiotic solution
- `am3_nalidixic_acid_medium.yaml`: NBRC M1313 AM3 plus 1 ml/L Nalidixic acid solution at 50 mg/ml
- `am3_nalidixic_acid_kanamycin_medium.yaml`: NBRC M1314 AM3 plus 1 ml/L Nalidixic acid solution at 100 mg/ml and 1 ml/L Kanamycin solution at 25 mg/ml

Those are supplemented variants, not source duplicates. The already-repaired M2023 owner now records `variant_relationship: SUPPLEMENTED_VARIANT` to AM3, but this generated record still lists it as a synonym and `merged_from` source for the M2022 canonical record.

The basal AM3 salts and glucose have exact ChEBI groundings. `Beef extract`, `Yeast extract`, `Peptone`, `Agar (if needed)`, and the nalidixic-acid stock are ungrounded or empty even though the curated M2023 sibling demonstrates accepted mappings for those AM3 and antibiotic rows.

## Evidence

Inspected source documents:

- NBRC Medium No. 1313 at `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1313`
- TOGO Medium M2022 API at `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2022`
- Normalized AM3 base and antibiotic sibling records under `data/normalized_yaml/bacterial/`

Supported claims:

- NBRC M1313 and TOGO M2022 both support the AM3 plus Nalidixic acid medium identity.
- NBRC M1313 supports the AM3 basal ingredient amounts: 1.5 g beef extract, 1.5 g yeast extract, 5 g peptone, 1 g glucose, 3.5 g NaCl, 3.68 g K2HPO4, 1.32 g KH2PO4, 15 g agar if needed, and 1 L distilled water per liter.
- NBRC M1313 supports 1 ml/L Nalidixic acid solution at 50 mg/ml, sterilized separately by filtration.
- NBRC M1313 supports the pH as unadjusted.

Unsupported or mismatched claims:

- The `SOURCE_DUPLICATE` relationship to plain AM3 is wrong because M2022 adds nalidixic acid.
- The merged synonym for `am3_nalidixic_acid_kanamycin_medium` is wrong because NBRC M1314 changes the nalidixic acid stock strength and adds kanamycin.
- `Nalidixic acid solution (50 mg/ml)*` is stored as an empty `Unknown solution` at `1 G_PER_L`, not as a 1 ml/L addition of a 50 mg/ml stock.
- The generated record omits NBRC's filtration instruction for the nalidixic-acid stock.
- The generated record stores the 1 L solvent row as `Distilled water` at `1 G_PER_L`.

## Completeness

Consequential gaps:

- Three distinct supplemented variants have been collapsed into one generated record.
- The nalidixic-acid solution composition, addition volume, grounding, and filter-sterilization procedure are absent.
- The pH-unadjusted source condition is absent.
- Several AM3 basal undefined ingredients and the agar row lack exact groundings.
- Target organisms are absent; no focused growth-evidence search was performed during this review.

Empty optional slots correctly left empty:

- No target organism was asserted, so there is no unsupported growth claim.
- No storage condition was asserted by NBRC M1313.

Bounded absence checks:

- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -type f -name '*am3_nalidixic_acid_medium.md'` search found no pre-existing report for this generated record before this report was written.
- A gitignore-independent `rg --no-ignore --hidden` search over `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for `am3_nalidixic_acid_medium`, `AM3 NALIDIXIC ACID MEDIUM`, `Nalidixic`, and `nalidixic` found the M2022 owner, the adjacent AM3/M2023 owners, the merged generated output, and repair scripts for related NBRC antibiotic media.

## Findings

### Blocker

1. **The generated record merges AM3 base medium and two different antibiotic-supplemented media as duplicates.**

   Evidence: `merged_from` contains `am3_medium`, `am3_nalidixic_acid_medium`, and `am3_nalidixic_acid_kanamycin_medium`. NBRC M1312 plain AM3 has no antibiotic solution, NBRC M1313 adds 1 ml/L Nalidixic acid solution at 50 mg/ml, and the curated M2023 / NBRC M1314 owner adds a 100 mg/ml nalidixic-acid stock plus a 25 mg/ml kanamycin stock. These source recipes do not denote the same medium.

   Owner: change the M2022 relationships in `data/normalized_yaml/bacterial/am3_nalidixic_acid_medium.yaml` and `data/normalized_yaml/bacterial/am3_medium.yaml` from `SOURCE_DUPLICATE` to `SUPPLEMENTED_VARIANT`, ensure merge generation includes `solutions` and variant relationships when fingerprinting, then regenerate `data/merge_yaml/merged/`.

### Major

1. **The NBRC M1313 nalidixic-acid solution is typed as 1 g/L with no composition.**

   Evidence: NBRC M1313 lists `Nalidixic acid solution (50 mg/ml)*` with a 1 ml amount, and the TOGO API represents that row with `volume: 1`, `unit: "ml"`. The record has one solution named `Unknown solution`, concentration `1 G_PER_L`, and an empty `composition`.

   Owner: model the stock in `data/normalized_yaml/bacterial/am3_nalidixic_acid_medium.yaml` as a 1 ml/L `Nalidixic acid solution (50 mg/ml)` whose nested composition is nalidixic acid at 50 mg/ml.

2. **The separate filtration requirement for nalidixic acid is missing.**

   Evidence: NBRC M1313 marks the nalidixic-acid stock with an asterisk and states that the marked stock is sterilized separately by filtration. The generated record has no `preparation_steps` or `sterilization` entry.

   Owner: add preparation and sterilization entries to the M2022 normalized owner that autoclave basal AM3 and separately filter-sterilize the nalidixic-acid solution before aseptic addition.

3. **The source pH condition is absent.**

   Evidence: NBRC M1313 states that pH is unadjusted, and TOGO M2022 carries `comment: "pH unadjusted"`. The generated M2022 record has no pH note.

   Owner: encode the pH-unadjusted condition in the maintained M2022 owner, using the same local pattern as the already-repaired M2023 record.

4. **NBRC M1313 distilled water is modeled as 1 g/L.**

   Evidence: both NBRC and TOGO list distilled water as 1 L. The generated CultureMech record stores it with `value: '1'` and `unit: G_PER_L`.

   Owner: convert the M2022 solvent row to `1000 ML_PER_L`, matching the repaired M2023 owner, or remove the solvent row if the importer treats 1 L water as recipe volume.

### Minor

1. **Several source-supported AM3 rows remain ungrounded.**

   Evidence: `Beef extract`, `Yeast extract`, `Peptone`, and `Agar (if needed)` lack exact ontology terms or mirrored MediaIngredientMech links, while `am3_nalidixic_acid_kanamycin_medium.yaml` already grounds the same AM3 rows in its repaired NBRC M1314 record.

   Owner: port the AM3 basal groundings from the repaired M2023 owner when repairing `data/normalized_yaml/bacterial/am3_nalidixic_acid_medium.yaml`.

## Recommended Edits

1. Repair M2022 as a supplemented variant of AM3, not a source duplicate, and update AM3's reciprocal `variant_children`.
2. Change the M2022 nalidixic-acid solution to a 1 ml/L, filter-sterilized, 50 mg/ml nalidixic-acid stock.
3. Add preparation steps and sterilization notes that preserve the NBRC asterisked filtration instruction.
4. Encode NBRC M1313's unadjusted pH condition.
5. Convert the 1 L distilled-water row to the same 1000 ml/L representation used in the curated M2023 sibling, or omit it as solvent volume.
6. Ground beef extract, yeast extract, peptone, agar, and nalidixic acid using the same accepted terms as the repaired M2023 and M2013 antibiotic records.
7. Regenerate generated merge records and rendered products.

## Follow-up Checks

- Rerun schema, strict, reference, and term validators on the corrected `am3_medium.yaml`, `am3_nalidixic_acid_medium.yaml`, and regenerated generated output.
- Rerun duplicate merging and verify plain AM3, AM3 plus nalidixic acid, and AM3 plus nalidixic acid plus kanamycin no longer merge to fingerprint `df2061b3dec4d0b73bfdda0556709810ad336ff389cde1a67e6de1a06cc6837e`.
- Manually compare the corrected M2022 owner against NBRC M1313 to confirm the 50 mg/ml nalidixic-acid stock and filtration instruction are preserved.
- Inspect the rendered pages to confirm AM3 links both M2022 and M2023 as supplemented variants.

## Additional Notes

- This review is read-only. It intentionally leaves `data/merge_yaml/merged/am3_nalidixic_acid_medium.yaml`, its normalized owners, and generated pages unchanged.
- Generated files under `data/merge_yaml/merged/` are derived artifacts. Corrections belong in `data/normalized_yaml/bacterial/am3_nalidixic_acid_medium.yaml`, reciprocal relationships in `data/normalized_yaml/bacterial/am3_medium.yaml`, and merge rules that currently ignore antibiotic `solutions`.

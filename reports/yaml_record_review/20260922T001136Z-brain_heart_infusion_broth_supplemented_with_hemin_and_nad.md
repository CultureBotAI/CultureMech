# YAML Record Review: brain-heart infusion broth (supplemented with hemin and beta-NAD)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_hemin_and_nad.yaml
- Started UTC: 2026-09-22T00:11:36Z
- Finished UTC: 2026-09-22T00:13:08Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009499 |
| Label | brain-heart infusion broth (supplemented with hemin and beta-NAD) |
| Source accession | TOGO:M2976 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_broth_supplemented_with_hemin_and_nad.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | 7f68ce53dd354b912d97a37359e1eb3a3675c36743eff3e38f95561679ed75d8 |

The reviewed file is the generated TOGO M2976 sBHI record. Future fixes belong
in the normalized owner named above or in the TOGO microgram/unit and gas import
paths that populated it.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_hemin_and_nad.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_hemin_and_nad.yaml --out /private/tmp/brain_heart_infusion_broth_supplemented_with_hemin_and_nad.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_hemin_and_nad.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_hemin_and_nad.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M2976` identifies Difco brain-heart infusion broth supplemented with
  hemin and beta-NAD for Haemophilus influenzae sBHI culture.
- TOGO M2976 lists 10 ug/ml hemin, 10 ug/ml beta-NAD, 1 L Difco BHI broth, and
  5% CO2 as a gas context.
- The NCBI PMC page behind the underlying Infection and Immunity paper gives
  DOI `10.1128/IAI.01540-05` and PMID 16714571 and contains the M2976 culture
  sentence.
- A gitignore-independent exact search for `TOGO:M2976`,
  `CultureMech:009499`, the merge fingerprint, and the normalized slug covered
  generated records, normalized records, local indexes, reports, source,
  scripts, `justfile`, and `.claude`; it found the single M2976 normalized
  owner and the single generated record.

The generated record identifies the TOGO M2976 source correctly, but the
supplement units are off by 1000-fold, the BHI volume unit is wrong, beta-NAD is
ungrounded, and conditional incubation CO2 is modeled as a top-level medium
ingredient.

## Evidence

TOGO M2976 supports 10 ug/ml hemin and 10 ug/ml beta-NAD. The record stores
both supplements as `10 G_PER_L`.

TOGO M2976 supports 1 L Difco brain-heart infusion broth as a prepared broth
base. The record preserves that row label but changes the volume to `1 G_PER_L`.

TOGO M2976 supports H. influenzae culture at 37 C in room air or 5% CO2, where
indicated. The record stores CO2 as a `VARIABLE` ingredient and does not
preserve the room-air alternative, the 5% condition, the 37 C incubation
temperature, or the H. influenzae growth scope.

## Completeness

- Consequential gap: source hemin and beta-NAD are 10 ug/ml supplements but are
  each stored as `10 G_PER_L`.
- Consequential gap: the 1 L BHI broth base is stored as `1 G_PER_L`.
- Consequential gap: CO2 is modeled as a medium ingredient instead of a
  conditional incubation atmosphere.
- Consequential gap: the record lacks H. influenzae growth scope and the source
  DOI/PMID.
- Consequential gap: beta-NAD is not grounded to a CHEBI term.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  the normalized slug and the M2976 merge fingerprint found no prior report for
  this target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Hemin and beta-NAD are imported with mass units that are 1000-fold too high. | TOGO M2976 lists hemin and beta-NAD at 10 ug/ml; the record stores each as `10 G_PER_L`. | `data/normalized_yaml/bacterial/brain_heart_infusion_broth_supplemented_with_hemin_and_nad.yaml`; likely also the TOGO microgram-per-milliliter unit importer |
| Major | The 1 L Difco BHI broth row has the wrong unit and value. | TOGO M2976 lists 1 L Difco brain-heart infusion broth; the record stores `1 G_PER_L`. | `data/normalized_yaml/bacterial/brain_heart_infusion_broth_supplemented_with_hemin_and_nad.yaml`; likely also the TOGO liter unit importer |
| Major | Conditional CO2 incubation context is modeled as an ingredient. | The source grew H. influenzae at 37 C in room air or 5% CO2 where indicated; the record stores a top-level `CO2` ingredient with `VARIABLE` concentration. | `data/normalized_yaml/bacterial/brain_heart_infusion_broth_supplemented_with_hemin_and_nad.yaml` |
| Major | Source organism, primary citation, and beta-NAD grounding are missing. | The M2976 source is an H. influenzae study with DOI `10.1128/IAI.01540-05` / PMID 16714571; the record has no target organism, no DOI/PMID reference, and no beta-NAD CHEBI grounding. | `data/normalized_yaml/bacterial/brain_heart_infusion_broth_supplemented_with_hemin_and_nad.yaml` |

## Recommended Edits

1. Correct hemin and beta-NAD to 10 ug/ml or the equivalent 10 mg/L.
2. Correct the Difco BHI broth base to a 1 L volume row.
3. Move CO2 out of ingredients and represent 37 C room-air or 5% CO2
   incubation as conditional growth context.
4. Add a CHEBI grounding for beta-NAD.
5. Add the underlying Infection and Immunity DOI/PMID and H. influenzae growth
   scope at the narrowest source-supported level.
6. Regenerate merged YAML after the normalized owner or importer is fixed.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on the corrected
  normalized M2976 owner.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Regenerate merges and verify the sBHI generated record has no top-level CO2
  ingredient and preserves 10 ug/ml supplement concentrations.
- Manually compare the regenerated record against the TOGO M2976 API payload.

## Additional Notes

- Chocolate agar with Isovitalex is an alternative plate medium in the source
  sentence and is outside this BHI broth record.

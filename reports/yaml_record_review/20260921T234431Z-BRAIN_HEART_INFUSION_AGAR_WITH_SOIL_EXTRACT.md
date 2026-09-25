# YAML Record Review: Brain Heart Infusion Agar With Soil Extract

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml
- Started UTC: 2026-09-21T23:44:31Z
- Finished UTC: 2026-09-21T23:47:45Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009715 |
| Label | Brain Heart Infusion Agar With Soil Extract |
| Source accession | TOGO:M337 / JCM_M342 |
| Generated status | Generated merge of six normalized owners |
| Merge fingerprint | a6b0678a3e68e60759e7d3c78e3f86ae7ab79094267d5658820bb396f7b6b3ae |

The reviewed file is a generated merge. Future corrections belong in the
normalized owners named under `merged_from` or in the merge rule that assigned a
shared fingerprint to unrelated BHI-agar recipes:

- `data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml`
- `data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml`
- `data/normalized_yaml/bacterial/bhi_glucose_medium.yaml`
- `data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml`
- `data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml`
- `data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml`

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml --out /private/tmp/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M337` is Brain Heart Infusion Agar With Soil Extract and wraps the
  source `JCM_M342`.
- Live JCM GRMD 342 lists only 37.0 g Brain heart infusion broth (BD-Difco),
  1.0 L Soil extract, and 15.0 g Agar for Medium 342.
- The TOGO M337 API payload agrees with the same JCM source and keeps the same
  three formula rows, but references `M94` for its soil extract row.
- `TOGO:M94` is the TOGO wrapper for `JCM_M102`, Nutrient Agar With 25% Soil
  Extract. Live JCM GRMD 102 defines the referenced soil extract as 400 g
  air-dried garden soil in 1.0 L tap water, autoclaved at 121 C for 1 hr and
  clarified after sedimentation and centrifugation.
- A gitignore-independent, source-ID-bounded exact search for `TOGO:M337`,
  `CultureMech:009715`, the merge fingerprint,
  `TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract`,
  `mediadive.medium:J342`, `CultureMech:002702`, `komodo.medium:82`,
  `mediadive.medium:82`, `CultureMech:001983`, `CultureMech:006566`,
  `mediadive.medium:J28`, `CultureMech:002647`, `mediadive.medium:J263`,
  `CultureMech:002621`, and `BHI-GLUCOSE` covered generated records,
  normalized records, local indexes, reports, source, scripts, `justfile`, and
  `.claude`; it found the six normalized owners that were merged into this
  target and their generated/index references.

The generated record keeps the TOGO M337 identity but combines it with the 5 g
glucose and 12 g agar signature from DSMZ/KOMODO Medium 82, plus synonym
metadata for plain JCM BHI agar and 2% NaCl JCM BHI agar. That fingerprint makes
the generated record denote more than one source formulation.

## Evidence

TOGO M337 and live JCM GRMD 342 support a final medium made from 37 g BHI broth,
1 L soil extract, and 15 g agar. They do not support an extra 5 g glucose row,
a 12 g agar amount, a 20 g NaCl sibling, or a plain-BHI source synonym in the
same record.

TOGO M94 and live JCM GRMD 102 support the soil-extract stock recipe referenced
by M337/J342: suspend 400 g air-dried garden soil in 1 L tap water, autoclave at
121 C for 1 hr, then use the clear supernatant after sedimentation and
centrifugation. The TOGO M337 normalized owner keeps that stock as an empty
`Unknown solution` at `1 G_PER_L`; the direct JCM J342 owner has the soil-extract
stock preparation as a final-medium preparation step but no 1 L soil-extract
ingredient row.

The opaque 37 g Brain heart infusion broth (BD-Difco) row is expanded to
calf-brain, beef-heart, proteose-peptone, dextrose, sodium-chloride, and
disodium-phosphate rows inferred from a MicrobeNotes page. The inspected JCM and
TOGO source text does not give that internal composition for BD-Difco BHI broth.

## Completeness

- Consequential gap: the target is a six-source chimera; its identity,
  ingredients, and synonyms cannot all be correct at once.
- Consequential gap: the 1 L soil-extract row from M337/J342 is represented as a
  solution with an empty composition and a mass unit.
- Consequential gap: the direct JCM J342 normalized owner lacks the 1 L
  soil-extract ingredient.
- Consequential gap: the soil-extract stock recipe from JCM 102 is not modeled
  as a structured stock/solution; its source text is only copied into the direct
  JCM J342 preparation step.
- Empty target-organism and growth-evidence slots are acceptable for these
  source-only medium formulations.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  `BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT`,
  `Brain Heart Infusion Agar With Soil Extract`, and the merge fingerprint found
  no prior report for this target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The generated record overmerges six recipes that denote different formulations. | M337/J342 is BHI broth plus 1 L soil extract plus 15 g agar; DSMZ/KOMODO 82 is BHI-glucose with 5 g glucose and 12 g agar; JCM J28 is plain BHI agar; JCM J263 is BHI agar with 2% NaCl. | Merge fingerprint/rule plus the six normalized owners |
| Major | The M337 soil-extract addition is represented as an empty `Unknown solution` at `1 G_PER_L` instead of 1 L of the JCM 102 soil-extract stock. | TOGO M337 lists `Soil extract (see Medium [M94])`, `reference_media_id: M94`, `volume: 1`, `unit: L`; TOGO M94 maps to `JCM_M102` and defines the soil extract from 400 g air-dried garden soil plus 1 L tap water. | `data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml` |
| Major | The direct JCM J342 owner omits the 1 L soil-extract ingredient and places the stock preparation on the final medium. | Live JCM GRMD 342 lists 1.0 L Soil extract as an ingredient; the normalized direct JCM owner has no soil-extract ingredient row and only stores the JCM 102 soil-extract stock procedure as its preparation step. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml` |
| Major | The M337 target inherits the BHI-glucose 5 g glucose and 12 g agar signature. | The generated target has a 5 g/L glucose row and 12 g/L agar row; M337/J342 has no standalone glucose row and lists 15 g agar. | Merge fingerprint/rule and `data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml` |
| Major | The opaque 37 g BD-Difco BHI broth row is expanded into inferred constituents. | M337/J342 and the direct JCM/DSMZ sibling sources cite a commercial BHI broth/base row; they do not directly assert the expanded tissue-infusion and buffer rows stored in the normalized owners. | The BHI premix import/enrichment path and affected normalized owners |

## Recommended Edits

1. Split fingerprint `a6b0678a3e68e60759e7d3c78e3f86ae7ab79094267d5658820bb396f7b6b3ae`
   so DSMZ/KOMODO 82, TOGO M337, direct JCM J342, JCM J28, and JCM J263 do not
   generate as one record.
2. In the TOGO M337 owner, remodel `Soil extract (see Medium [M94])` as 1 L of
   soil extract and link it to the TOGO M94 / JCM 102 stock recipe instead of
   an empty `Unknown solution` with `G_PER_L`.
3. In the direct JCM J342 owner, add the missing 1 L soil-extract row and attach
   the soil-preparation text to the referenced soil-extract stock rather than
   treating it as the only final-medium preparation step.
4. Restore BHI broth/base source rows as opaque 37 g commercial premix rows
   unless a BD-Difco primary specification is attached for the expanded
   formula.
5. Regenerate merged YAML and derived pages after the normalized records and
   merge rules are corrected.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on each corrected
  normalized owner.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Rerun `just verify-merges` and `just audit-merge-freshness`.
- Regenerate merged records and confirm M337/J342 no longer merges with DSMZ 82,
  KOMODO 82, JCM J28, or JCM J263.
- Check the regenerated TOGO M337 and direct JCM J342 records manually against
  live JCM GRMD 342, TOGO M337, and TOGO M94/JCM 102.

## Additional Notes

- TOGO `M94` and JCM Medium `102` are the same soil-extract source in different
  accession namespaces: TOGO M94 reports `original_media_id: JCM_M102` and its
  `src_url` points to GRMD 102.
- Optional empty growth-evidence slots were not treated as defects.

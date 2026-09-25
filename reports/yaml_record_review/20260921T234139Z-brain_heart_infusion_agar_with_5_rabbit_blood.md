# YAML Record Review: Brain Heart Infusion Agar With 5% Rabbit Blood

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_agar_with_5_rabbit_blood.yaml
- Started UTC: 2026-09-21T23:41:39Z
- Finished UTC: 2026-09-21T23:42:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:010365 |
| Label | Brain Heart Infusion Agar With 5% Rabbit Blood |
| Source accession | TOGO:M942, wrapping JCM_M901 |
| Merge source | data/normalized_yaml/bacterial/TOGO_M942_Brain_Heart_Infusion_Agar_With_5_Rabbit_Blood.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | acf29ce26a7fd67c4bc98c7ea7a8331a87c9df4c6ece8c3df7e9ed94e58bdfa4 |

The reviewed file is generated from a single TOGO normalized owner. That owner
and the generated merge agree on the scientific rows, so formulation fixes
belong in
`data/normalized_yaml/bacterial/TOGO_M942_Brain_Heart_Infusion_Agar_With_5_Rabbit_Blood.yaml`
or in the TOGO/BHI premix importer rule that populated it.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_agar_with_5_rabbit_blood.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_agar_with_5_rabbit_blood.yaml --out /private/tmp/brain_heart_infusion_agar_with_5_rabbit_blood.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_agar_with_5_rabbit_blood.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_agar_with_5_rabbit_blood.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- TOGO:M942 resolves to Brain Heart Infusion Agar With 5% Rabbit Blood and
  wraps JCM_M901.
- An exact gitignore-independent search for `TOGO:M942`,
  `CultureMech:010365`, the normalized TOGO filename, the merge fingerprint,
  `JCM_M901`, `CultureMech:003250`, and `mediadive.medium:J901` found a
  separate direct-JCM normalized owner for the same JCM medium:
  `data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_5_rabbit_blood.yaml`.
- The current JCM GRMD 901 URL returned a "Nothing found" HTML page during this
  review; the inspected TOGO payload and the direct JCM/MediaDive record both
  preserve the historical JCM M901 recipe text.
- The record's top-level identity is correct, but its water, rabbit blood, and
  BHI base rows are not represented with the source units and scope.

## Evidence

TOGO M942 lists 950 ml distilled water, 50 ml Rabbit blood, 15 g Agar, and 37 g
Brain heart infusion broth (BD-Difco). Its preparation comment says to mix all
ingredients except rabbit blood, autoclave, cool to about 50 C, then
aseptically add sterile defibrinated rabbit blood to 5% final before dispensing
into sterile petri dishes.

The reviewed record instead stores distilled water and rabbit blood as
gram-per-liter masses, expands the 37 g commercial BHI broth into inferred
constituents from a MicrobeNotes page, and omits the source preparation.

## Completeness

- Consequential gap: the 950 ml water and 50 ml rabbit blood volumes are not
  represented.
- Consequential gap: the post-autoclave rabbit-blood addition at about 50 C is
  absent.
- Consequential gap: the TOGO/JCM M901 recipe is duplicated by a direct
  JCM/MediaDive owner under `CultureMech:003250`.
- Empty target-organism and growth-evidence slots are acceptable for this
  source-only JCM/TOGO formulation.
- A target-specific `find` under `reports/yaml_record_review` found no prior
  non-suffixed `brain_heart_infusion_agar_with_5_rabbit_blood` report, so this
  report did not overwrite an earlier review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Distilled water and rabbit blood are modeled as masses. | TOGO M942 lists `Distilled water` as 950 ml and `Rabbit blood` as 50 ml. | `data/normalized_yaml/bacterial/TOGO_M942_Brain_Heart_Infusion_Agar_With_5_Rabbit_Blood.yaml` |
| Major | The basal `Brain heart infusion broth (BD-Difco)` row was replaced by inferred full-strength BHI constituents. | TOGO M942 lists one 37 g Bacto BHI row plus 15 g agar; it does not assert calf-brain, beef-heart, proteose-peptone, dextrose, sodium-chloride, or disodium-phosphate rows directly. | `data/normalized_yaml/bacterial/TOGO_M942_Brain_Heart_Infusion_Agar_With_5_Rabbit_Blood.yaml`; likely also the TOGO/BHI premix expansion importer |
| Major | The rabbit-blood handling instructions are missing. | TOGO M942 says to autoclave and cool the non-blood ingredients to about 50 C, then aseptically add 5% final sterile defibrinated rabbit blood and dispense into sterile petri dishes. | `data/normalized_yaml/bacterial/TOGO_M942_Brain_Heart_Infusion_Agar_With_5_Rabbit_Blood.yaml` |
| Major | The same JCM M901 formula is represented twice with different CultureMech IDs. | TOGO M942 wraps JCM_M901 under `CultureMech:010365`; `data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_5_rabbit_blood.yaml` represents mediadive.medium:J901 under `CultureMech:003250`. | Both normalized JCM/TOGO owners |
| Minor | Rabbit blood remains ungrounded. | TOGO supplies a rabbit-blood GMO row, but the normalized owner carries no ontology term for the complex blood ingredient. | `data/normalized_yaml/bacterial/TOGO_M942_Brain_Heart_Infusion_Agar_With_5_Rabbit_Blood.yaml` |

## Recommended Edits

1. Restore the TOGO M942 owner to 950 ml distilled water, 50 ml sterile
   defibrinated rabbit blood, 15 g agar, and 37 g Brain heart infusion broth
   (BD-Difco).
2. Keep rabbit blood out of the autoclaved fraction and add the post-autoclave,
   about-50 C aseptic blood-addition step.
3. Reconcile the duplicate JCM M901 representation in the TOGO owner and
   `data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_5_rabbit_blood.yaml`.
4. If the BHI broth premix is expanded, attach a source that supports the exact
   BD-Difco product formula; otherwise keep the premix opaque.
5. Regenerate merged records after the authoritative normalized records or the
   importer that populates them are corrected.

## Follow-up Checks

- Rerun `just validate` on the corrected TOGO and direct-JCM normalized owners.
- Regenerate merges and confirm JCM_M901 and TOGO:M942 are either represented
  once or explicitly cross-linked as source duplicates.
- Rerun `just verify-merges` and `just audit-merge-freshness`.
- Rerun focused LinkML, strict, reference, and term validation on the
  regenerated rabbit-blood BHI agar record or records.

## Additional Notes

- The current JCM website did not return GRMD 901; this review used the TOGO
  API payload and the parallel direct-JCM normalized record for source text.
- Optional empty growth-evidence slots were not treated as defects.

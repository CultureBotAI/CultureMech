# YAML Record Review: BRAIN HEART INFUSION AGAR WITH 5% RABBIT BLOOD

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_agar_with_5_rabbit_blood__490a0131.yaml
- Started UTC: 2026-09-21T23:43:37Z
- Finished UTC: 2026-09-21T23:43:57Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:003250 |
| Label | BRAIN HEART INFUSION AGAR WITH 5% RABBIT BLOOD |
| Source accession | mediadive.medium:J901 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_5_rabbit_blood.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | 490a0131420ecb03f8aacc773c60a827aa051d6e396bf157e57ba970768cb3e2 |

The reviewed file is the direct JCM/MediaDive import for JCM Medium J901. Its
single normalized owner agrees with the generated merge on the scientific rows,
so future fixes belong in
`data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_5_rabbit_blood.yaml`
or in the JCM/BHI premix importer path that populated it.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_agar_with_5_rabbit_blood__490a0131.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_agar_with_5_rabbit_blood__490a0131.yaml --out /private/tmp/brain_heart_infusion_agar_with_5_rabbit_blood__490a0131.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_agar_with_5_rabbit_blood__490a0131.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_agar_with_5_rabbit_blood__490a0131.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `mediadive.medium:J901` identifies JCM Medium J901, BRAIN HEART INFUSION
  AGAR WITH 5% RABBIT BLOOD.
- An exact gitignore-independent search for `mediadive.medium:J901`,
  `CultureMech:003250`, the merge fingerprint, the normalized slug, and
  `TOGO:M942` across `data`, `src`, `scripts`, `docs`, `.claude`, and
  `justfile` found this direct-JCM owner and a separate TOGO owner,
  `data/normalized_yaml/bacterial/TOGO_M942_Brain_Heart_Infusion_Agar_With_5_Rabbit_Blood.yaml`,
  wrapping the same JCM_M901 source under `CultureMech:010365`.
- The current JCM GRMD 901 URL returned a "Nothing found" HTML page during this
  review; the inspected TOGO M942 payload and this JCM/MediaDive record both
  preserve historical JCM M901 text.
- The record's top-level identity is correct, but its water, rabbit blood, and
  BHI base rows are not represented with the source units and scope.

## Evidence

TOGO M942 wraps the same JCM_M901 source and lists 950 ml distilled water,
50 ml Rabbit blood, 15 g Agar, and 37 g Brain heart infusion broth (BD-Difco).
Its preparation comment matches the preparation already present in this direct
JCM owner: autoclave the non-blood ingredients, cool to about 50 C, then
aseptically add sterile defibrinated rabbit blood to 5% final before dispensing
into sterile petri dishes.

The reviewed record retains the preparation and the 15 g agar row, but it omits
950 ml distilled water, stores 50 ml rabbit blood as `50 G_PER_L`, and expands
the 37 g Bacto BHI broth into inferred constituents from a MicrobeNotes page.

## Completeness

- Consequential gap: the 950 ml distilled water row is absent.
- Consequential gap: the 50 ml rabbit blood volume is represented as a mass.
- Consequential gap: the direct JCM/MediaDive record and the TOGO:M942 record
  represent the same JCM M901 source under different CultureMech IDs.
- Empty target-organism and growth-evidence slots are acceptable for this
  source-only JCM formulation.
- A target-specific `find` under `reports/yaml_record_review` found no prior
  `brain_heart_infusion_agar_with_5_rabbit_blood__490a0131` report, so this
  report did not overwrite an earlier review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The recipe is missing 950 ml distilled water. | TOGO M942, which wraps the same JCM M901 source, lists 950 ml distilled water. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_5_rabbit_blood.yaml` |
| Major | Rabbit blood is modeled as `50 G_PER_L` instead of a 50 ml, 5% final volume addition. | The source preparation says to add 5% final sterile defibrinated rabbit blood; TOGO M942 lists the rabbit blood row as 50 ml. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_5_rabbit_blood.yaml` |
| Major | The basal `Brain heart infusion broth (BD-Difco)` row was replaced by inferred full-strength BHI constituents. | TOGO M942 lists one 37 g Bacto BHI row plus 15 g agar; it does not assert calf-brain, beef-heart, proteose-peptone, dextrose, sodium-chloride, or disodium-phosphate rows directly. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_5_rabbit_blood.yaml`; likely also the JCM/BHI premix expansion importer |
| Major | The same JCM M901 formula is represented twice with different CultureMech IDs. | This direct-JCM record uses `CultureMech:003250`; TOGO M942 wraps JCM_M901 in `TOGO_M942_Brain_Heart_Infusion_Agar_With_5_Rabbit_Blood.yaml` under `CultureMech:010365`. | Both normalized JCM/TOGO owners |

## Recommended Edits

1. Add the missing 950 ml distilled water row.
2. Change rabbit blood from `50 G_PER_L` to a volume-aware 50 ml/L addition and
   keep the note that it is aseptically added after autoclaving to 5% final.
3. Restore the BHI base to an opaque 37 g Brain heart infusion broth (BD-Difco)
   row unless a BD-Difco specification is attached for the expanded formula.
4. Reconcile this direct JCM J901 owner with the TOGO M942 owner that wraps the
   same source.
5. Regenerate merged records after the authoritative normalized records or the
   importer that populates them are corrected.

## Follow-up Checks

- Rerun `just validate` on the corrected direct-JCM and TOGO normalized owners.
- Regenerate merges and confirm JCM_M901 and TOGO:M942 are either represented
  once or explicitly cross-linked as source duplicates.
- Rerun `just verify-merges` and `just audit-merge-freshness`.
- Rerun focused LinkML, strict, reference, and term validation on the
  regenerated rabbit-blood BHI agar record or records.

## Additional Notes

- The current JCM website did not return GRMD 901; this review used the TOGO
  API payload and the parallel TOGO normalized record for source context.
- Optional empty growth-evidence slots were not treated as defects.

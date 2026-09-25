# YAML Record Review: centenum_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CENTENUM_MEDIUM.yaml
- Started UTC: 2026-09-22T06:47:11Z
- Finished UTC: 2026-09-22T06:48:18Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:006227 |
| Name | centenum_medium |
| Original name | CENTENUM medium |
| Category | bacterial |
| Source | KOMODO Medium 650, copied from DSMZ Medium 650 |
| Generated status | Generated merged output |
| Maintained owners | data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml; data/normalized_yaml/bacterial/centenum_medium.yaml; data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml |

The reviewed file is a generated merge of two KOMODO Medium 650-derived
records and one DSMZ/MediaDive Medium 650 owner. Future fixes belong in the
normalized owners or in the merge logic that chooses which duplicate owner's
preparation steps survive, followed by merge/page regeneration.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/CENTENUM_MEDIUM.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/CENTENUM_MEDIUM.yaml --out /private/tmp/CENTENUM_MEDIUM.strict.tsv --workers 1 --quiet` | Passed with 0 errors; TSV written to `/private/tmp/CENTENUM_MEDIUM.strict.tsv`. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/CENTENUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/CENTENUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not checked | `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in the merged YAML. |

## Identity and Grounding

- The generated `KOMODO Medium 650` identity, DSMZ 650 provenance, duplicate
  `medium_650_modified_for_dsm_8319` synonym, and parent
  `mediadive.medium:650` owner all point to CENTENUM MEDIUM / DSMZ Medium 650.
- The duplicate relationship is coherent: `KOMODO_650_CENTENUM_medium.yaml`,
  `centenum_medium.yaml`, and `medium_650_modified_for_dsm_8319.yaml` have the
  same ingredient and concentration signature.
- The direct DSMZ Medium 650 PDF and the MediaDive Medium 650 JSON agree on
  the ingredient list, pH 7.0, nitrogen boil/autoclave step, and 20 mM pyruvate
  addition after autoclaving.

## Evidence

DSMZ Medium 650 specifies 1 g K2HPO4, 0.5 g MgSO4, 10 g yeast extract,
20 ug vitamin B12, and 1000 ml tap water; it then says to adjust pH to 7.0,
boil under nitrogen gas, autoclave at 121 C for 15 min, and add 20 mM pyruvate
after autoclaving.

The reviewed generated record preserves the ingredient amounts, the 1.741 g/L
pyruvate conversion for 20 mM pyruvate, and `ph_value: 7.0`. It does not
preserve the two DSMZ preparation steps that exist in the MediaDive normalized
owner:

| Source instruction | Present in generated record? |
|---|---|
| Adjust pH to 7.0 | No |
| Boil under nitrogen gas and autoclave at 121 C for 15 min | No |
| Add 20 mM pyruvate after autoclaving | No |

## Completeness

- Main formula completeness is good: the six source ingredients are present
  with the same amounts used by the MediaDive Medium 650 JSON.
- Procedural completeness is not sufficient because the generated merge drops
  anaerobic boiling, autoclaving, and pyruvate addition timing.
- Exact `rg --no-ignore --hidden` searches over YAML for the KOMODO 650,
  KOMODO 650_8319, MediaDive 650, CultureMech:006227, CultureMech:006226,
  CultureMech:001789, and exact `centenum_medium` identities included ignored
  and hidden files. They found the three merged normalized owners and the
  reviewed generated target; no additional normalized CENS/DSMZ 650 owners were
  found.
- Empty optional slots such as explicit organisms and incubation temperature
  were not treated as defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | DSMZ Medium 650 preparation steps were dropped from the generated merge. | The MediaDive owner and MediaDive JSON retain pH adjustment, boiling under nitrogen, autoclaving, and post-autoclave 20 mM pyruvate addition. The reviewed record has no `preparation_steps`, so it loses the anaerobic treatment and would let pyruvate be autoclaved with the base medium. | Merge logic or the KOMODO duplicate owners that become canonical |

## Recommended Edits

1. Preserve the DSMZ/MediaDive preparation steps when merging the KOMODO 650
   duplicates into the canonical CENTENUM record.
2. If the KOMODO duplicate records remain as maintained files, copy or
   re-import the DSMZ 650 preparation steps there so canonical-owner selection
   cannot drop them again.
3. Regenerate `data/merge_yaml/merged/CENTENUM_MEDIUM.yaml` and rendered pages
   after the maintained owner or merge rule is fixed.

## Follow-up Checks

- Re-run open-schema and strict validation on all three normalized owners and
  the regenerated `data/merge_yaml/merged/CENTENUM_MEDIUM.yaml`.
- Re-run a focused merge verification and confirm the regenerated canonical
  record still carries pH adjustment, nitrogen boiling/autoclaving, and
  post-autoclave pyruvate addition.
- Manually compare the regenerated YAML against the DSMZ Medium 650 PDF or
  MediaDive Medium 650 JSON.

## Additional Notes

- The direct DSMZ PDF was rendered with `mutool` because it is image-based and
  `pypdf` extraction returned no text.
- Shape validation passes because missing `preparation_steps` are optional at
  the schema layer.

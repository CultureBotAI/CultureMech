# YAML Record Review: chaetomium_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CHAETOMIUM_MEDIUM.yaml
- Started UTC: 2026-09-22T06:54:01Z
- Finished UTC: 2026-09-22T06:55:57Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:004212 |
| Name | chaetomium_medium |
| Original name | CHAETOMIUM medium |
| Category | bacterial |
| Source | KOMODO Medium 188, copied from DSMZ Medium 188 |
| Generated status | Generated merged output |
| Maintained owners | data/normalized_yaml/bacterial/KOMODO_188_CHAETOMIUM_medium.yaml; data/normalized_yaml/bacterial/chaetomium_medium.yaml |

The reviewed file is a generated merge of a KOMODO Medium 188 copy and the
DSMZ/MediaDive Medium 188 parent. Future fixes belong in those normalized
owners or in the MediaDive/KOMODO import and merge logic, followed by
regeneration of the merged YAML and rendered pages.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/CHAETOMIUM_MEDIUM.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/CHAETOMIUM_MEDIUM.yaml --out /private/tmp/CHAETOMIUM_MEDIUM.strict.tsv --workers 1 --quiet` | Passed with 0 errors; TSV written to `/private/tmp/CHAETOMIUM_MEDIUM.strict.tsv`. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/CHAETOMIUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/CHAETOMIUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not checked | `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in the merged YAML. |

## Identity and Grounding

- The generated `komodo.medium:188` identity, the DSMZ Medium 188 provenance
  note, and the `mediadive.medium:188` duplicate parent all identify
  CHAETOMIUM MEDIUM.
- The duplicate merge is justified at the formula level: the KOMODO and DSMZ
  owners have the same ingredient, concentration, pH, category, and physical
  state signature.
- The DSMZ PDF and MediaDive JSON agree on pH 7.2, 1000 ml distilled water, and
  the instruction to place a strip of sterile filter paper on cooled agar and
  inoculate on the filter strip.

## Evidence

The inspected DSMZ Medium 188 formula lists NaNO3, MgSO4 x 7 H2O, KCl,
Fe2(SO4)3 x H2O, KH2PO4, K2HPO4, agar, yeast extract, distilled water, and
Cellulose MN 300. The reviewed record preserves all of those ingredients except
the 1000 ml distilled water solvent.

The MediaDive owner imported one preparation step from DSMZ: adjust to pH 7.2,
place sterile filter paper on the cooled agar, and inoculate on the filter
strip. The generated record preserved only `ph_value: 7.2`; it dropped the
filter-paper handling instruction.

## Completeness

- Distilled water is absent even though DSMZ Medium 188 includes 1000 ml.
- The post-cooling filter-paper inoculation instruction is absent.
- Exact `rg --no-ignore --hidden` searches over YAML for
  `komodo.medium:188`, `mediadive.medium:188`, `CultureMech:004212`,
  `CultureMech:001280`, and exact `chaetomium_medium` identities included
  ignored and hidden files. They found the two merged normalized owners and the
  reviewed generated target; no additional CHAETOMIUM Medium normalized owner
  was found.
- Empty optional fields such as explicit organisms and target temperature were
  not treated as defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The final solvent is missing. | DSMZ 188 and MediaDive 188 list 1000 ml distilled water; neither normalized owner nor the generated merge has a distilled-water row. | `data/normalized_yaml/bacterial/chaetomium_medium.yaml`; `data/normalized_yaml/bacterial/KOMODO_188_CHAETOMIUM_medium.yaml`; MediaDive/KOMODO import transforms |
| Major | The generated merge lost the DSMZ preparation step. | The DSMZ/MediaDive owner retains a pH 7.2 and filter-paper inoculation step, but the KOMODO owner and generated canonical record have no `preparation_steps`. | Merge logic or the KOMODO duplicate owner |

## Recommended Edits

1. Restore the 1000 ml distilled-water ingredient from DSMZ Medium 188 in the
   DSMZ owner and propagate it to the KOMODO duplicate.
2. Preserve the DSMZ Medium 188 preparation step when merging the KOMODO
   duplicate with the DSMZ owner.
3. Regenerate `data/merge_yaml/merged/CHAETOMIUM_MEDIUM.yaml` and rendered
   pages after the maintained owners or merge rule are fixed.

## Follow-up Checks

- Re-run open-schema, strict, term, and reference validation on both normalized
  owners and the regenerated `data/merge_yaml/merged/CHAETOMIUM_MEDIUM.yaml`.
- Re-run a focused merge verification to confirm preparation steps survive
  when a KOMODO duplicate is canonical.
- Manually compare the regenerated record against the DSMZ Medium 188 PDF or
  MediaDive Medium 188 JSON for distilled water and the sterile filter-paper
  instruction.

## Additional Notes

- The DSMZ PDF was rendered with `mutool` because `pypdf` did not extract text.
- The unresolved `Fe2(SO4)3 x H2O` ontology grounding was not treated as a
  defect because it is retained explicitly and may not have a single exact
  CHEBI term.

# YAML Record Review: bhi_medium_for_strict_anaerobes

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml
- Started UTC: 2026-09-21T21:06:40Z
- Finished UTC: 2026-09-21T21:08:30Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001317 |
| Name | bhi_medium_for_strict_anaerobes |
| Original name | BHI MEDIUM FOR STRICT ANAEROBES |
| Category | bacterial |
| Source identity | DSMZ Medium 215c, `mediadive.medium:215c` |
| Reviewed artifact | `data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml` |
| Generated state | Derived single-source merge from `merged_from: [bhi_medium_for_strict_anaerobes]`, `merge_fingerprint: bc50d0b7f292df0e8d533ffc2710cdb64c4913457a0a9d8a8e5c040c1ce11c4c` |

`data/culturemech_id_registry.tsv` maps `CultureMech:001317` to
`data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml`.

The inspected MediaDive REST record for 215c and the inspected DSMZ Medium
215c PDF both define BHI Medium for Strict Anaerobes as 37 g/L Brain heart
infusion, 0.25 g/L L-Cysteine HCl x H2O, 0.25 g/L Na2S x 9 H2O, and 1000 ml
distilled water. MediaDive also reports `min_pH: 7.2` and `max_pH: 7.6`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml --out /private/tmp/BHI_MEDIUM_FOR_STRICT_ANAEROBES.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 ERROR rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file, 0 reference checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded-`MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone records under `history/` |

The direct `just validate-*` wrappers were not rerun for this record because
this checkout currently fails before target-specific validation while building
`llvmlite==0.46.0` under Python 3.13. The no-project commands above exercise
the same narrow validators under Python 3.11 from a cache outside the project
environment.

## Identity and Grounding

- **Record identity is coherent.** `mediadive.medium:215c`, the MediaDive REST
  payload, and the DSMZ PDF all identify BHI MEDIUM FOR STRICT ANAEROBES.
- **The generated merge is stale.** The generated file still has only the
  2026-08-06 merge event and contains the old MicrobeNotes decomposition of
  BHI. The normalized owner has a 2026-09-12
  `repair_komodo_215c_strict_anaerobes_score15.py` event that restores the
  DSMZ 215c aggregate recipe, water row, references, and source-scoped notes.
- **pH and reducing agents are supported.** MediaDive reports pH 7.2-7.6;
  MediaDive and DSMZ both list 0.25 g/L L-Cysteine HCl x H2O and 0.25 g/L
  Na2S x 9 H2O.
- **Brain Heart Infusion is missing as an aggregate in the reviewed merge.**
  The source lists 37 g/L Brain heart infusion; the generated YAML replaces it
  with six unsupported BHI subcomponents.

## Evidence

| Claim | Review |
|---|---|
| DSMZ 215c / BHI MEDIUM FOR STRICT ANAEROBES | Supported by MediaDive REST and the DSMZ PDF. |
| pH 7.2-7.6 | Supported by MediaDive REST. |
| L-Cysteine HCl x H2O and Na2S x 9 H2O | Supported by MediaDive REST and the DSMZ PDF. |
| Anoxic N2 preparation and post-autoclave reducing agents | Supported by MediaDive REST and the DSMZ PDF. |
| Six expanded BHI constituents | Unsupported and already repaired upstream. DSMZ 215c lists a 37 g/L Brain heart infusion aggregate. |

## Completeness

- The reviewed merge has the source pH, reducing-agent ingredients, and anoxic
  preparation statement.
- The reviewed merge is missing the normalized owner's 37 g/L Brain heart
  infusion aggregate, 1000 ml distilled water, and structured references.
- The DSMZ PDF also lists strain-specific supplements for DSM 10643, DSM
  19851, and DSM 108840. The normalized owner does not currently model those
  as variants or discussion entries.
- Empty organism and growth slots are acceptable because the inspected DSMZ
  and MediaDive recipe records do not assert growth outcomes.
- A gitignore-independent search with `rg --no-ignore --hidden` over `data`
  and `reports/yaml_record_review` for `CultureMech:001317`,
  `mediadive.medium:215c`, `bhi_medium_for_strict_anaerobes`, and the merge
  fingerprint found the expected normalized owner, generated merge, generated
  indexes, duplicate KOMODO 215c owner, and import-tracking references. A
  `find` search over the ignored `reports/yaml_record_review` directory found
  no pre-existing `*-BHI_MEDIUM_FOR_STRICT_ANAEROBES.md` report before this
  one was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated merge is stale and still carries the old unsupported BHI decomposition. | The generated merge was last emitted on 2026-08-06. `data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml` was repaired on 2026-09-12 and now matches DSMZ 215c with 37 g/L Brain heart infusion, reducing agents, distilled water, and structured DSMZ/MediaDive references. | Regenerate `data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml` from the normalized owner, then regenerate generated pages. |
| minor | DSMZ strain-specific supplement notes are not represented as variants. | The DSMZ 215c PDF lists glycerol for DSM 10643, haemin/vitamin K1 for DSM 19851, and rumen fluid for DSM 108840; the normalized owner currently records only the base medium. | `data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml` for future variant or discussion curation. |

## Recommended Edits

1. Regenerate this merge from the already-repaired
   `data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml`.
2. Regenerate generated pages from the fresh merge output.
3. In a later source-curation pass, either model the DSMZ 215c
   strain-specific supplements as variants or record why they are out of scope
   for the base medium.

## Follow-up Checks

- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  this merge.
- Rerun schema, strict, term, and reference validation on the regenerated
  merge and on `data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml`.
- Manually inspect the regenerated merge and confirm the unsupported Calf
  brains, Beef heart, Proteose peptone, Dextrose, Sodium chloride, and Disodium
  phosphate rows are gone.

## Additional Notes

None found.

# YAML Record Review: mms_medium_huber_et_al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mms_medium_huber_et_al.yaml
- Started UTC: 2026-09-24T09:33:00Z
- Finished UTC: 2026-09-24T09:35:03Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:007034 |
| Label | mms_medium_huber_et_al |
| Original label | Mms medium; huber et al |
| Source term | MEDIADB:144, Mms medium; huber et al |
| Maintained owner | data/normalized_yaml/bacterial/mms_medium_huber_et_al.yaml |
| Reviewed artifact | data/merge_yaml/merged/mms_medium_huber_et_al.yaml |
| Generated? | Yes. The `merge_recipes.py` history event reports a merge from `mms_medium_huber_et_al.yaml`; future edits should land in the normalized MediaDB record or the MediaDB importer and then regenerate this merged artifact. |

I searched for `CultureMech:007034`, `mms_medium_huber_et_al`, `Mms medium; huber et al`, and `Medium ID: 144` with `rg --no-ignore --hidden` under `data`, `src`, `scripts`, and `history`; the exact record ID maps to the normalized owner above, this merged file, generated indexes, import reports, and archived validation reports. The search included ignored files.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mms_medium_huber_et_al.yaml` | Passed with `No issues found`. |
| Strict validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mms_medium_huber_et_al.yaml --out /private/tmp/mms_medium_huber_et_al.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. `/private/tmp/mms_medium_huber_et_al.strict.tsv` has 1 line, so only the TSV header was emitted. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mms_medium_huber_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mms_medium_huber_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the expected `eutils/pkg_resources` warning. |
| Embedded history | `just validate-history` | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The CultureMech ID, slug, `media_term`, and maintained path all identify MediaDB medium 144, `Mms medium; huber et al`. The live MediaDB medium page for `/defined_media/media/144/` reports the same medium label, 22 compounds with mM amounts, one `Thermotoga maritima` growth data record, and source 46, `Huber et al, 1986`; `/defined_media/media_text/144/` reports the same 22 tab-delimited compound rows and the same concentrations.

The generated merge is stale relative to its owner. `data/normalized_yaml/bacterial/mms_medium_huber_et_al.yaml` was repaired on 2026-08-31 by `repair_mediadb_names.py` and now restores `Nickel(II) ammonium sulfate`, but this 2026-08-06 merge still contains only the parse fragment `'''Nickel(II` for the 0.00697114 mM ingredient.

The MediaDB source identity is not carried into structured record provenance. MediaDB source 46 identifies Huber et al. 1986 in Archives of Microbiology, and Crossref resolves that paper to DOI `10.1007/BF00409880`. The import history instead cites `Mazumdar et al. (2014) PLOS One`, which comes from the MediaDB importer hard-coded curation note rather than medium 144 or source 46.

## Evidence

Supported by the inspected MediaDB endpoints:

- The source medium is MediaDB 144 and is named `Mms medium; huber et al`.
- The ingredient list has the same 22 MediaDB compounds and the same mM values reported by `/defined_media/media_text/144/`.
- The medium page links MediaDB source 46, `Huber et al, 1986`.
- The medium page links growth data 292 for `Thermotoga maritima` on MediaDB 144.
- The growth-data page reports a growth rate of 0.555 1/h, pH 6.5, temperature 85.0, and the note `doubling time`.

Unsupported or over-scoped:

- The generated `'''Nickel(II` ingredient is not an ingredient label in the inspected MediaDB 144 output; the current normalized record has already restored it to `Nickel(II) ammonium sulfate`.
- The MediaDB page and tab-delimited export give no preparation protocol, so the generated dissolve, conditional pH-adjustment, and 0.22 um filter-sterilization steps are generic importer output, not source evidence for this medium.
- `Cultivation of genome-sequenced organisms`, `Metabolic modeling`, and `Systems biology research` are generic MediaDB importer applications. They are not stated on the inspected medium 144, source 46, organism 63, or growth-data 292 pages.
- The embedded January import event cites the wrong publication.

## Completeness

The core MediaDB 22-compound table is present and the molar amounts match `/defined_media/media_text/144/`.

Consequential gaps:

- The sole MediaDB growth-data row is absent from the record: no `target_organisms`, growth rate, pH 6.5, or 85.0 C condition was imported.
- No structured source, DOI, or MediaDB source ID captures the Huber et al. 1986 provenance for medium 144.
- The record has no explicit quality flag saying the MediaDB endpoint lacks preparation steps; it instead asserts a complete-looking but unsupported filter-sterilization protocol.

Empty optional fields that are not inherently defects:

- The record has no variants, parent recipe, or nested stock solutions, and the inspected MediaDB medium 144 page did not list variants or stock recipes.

I also searched for local raw MediaDB inputs with `find data -path '*mediadb*' -maxdepth 5 -type f`; no raw MediaDB files were present under `data` to depth 5. `find` is gitignore-independent, so ignored files were included. Live MediaDB pages were used as the source of truth for this review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | None found | The file is valid YAML, its ID and source term resolve to a single MediaDB medium, and schema, strict, reference, and term validation passed. | Not applicable |
| Major | The merged artifact is stale and still exposes the old MediaDB SQL parser truncation. | The generated record's 0.00697114 mM nickel ingredient has `preferred_term: '''Nickel(II`; MediaDB 144 and its text export call that row `Nickel(II) ammonium sulfate`; the normalized owner already has the repaired name and a 2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` event. | Regenerate `data/merge_yaml/merged/mms_medium_huber_et_al.yaml` from `data/normalized_yaml/bacterial/mms_medium_huber_et_al.yaml`; if regeneration reintroduces the fragment, fix `scripts/merge_recipes.py` or the MediaDB merge input path. |
| Major | The MediaDB growth condition is missing. | MediaDB growthdata 292 records `Thermotoga maritima` growing on MediaDB 144 with growth rate 0.555 1/h, pH 6.5, temperature 85.0, and note `doubling time`; the generated record has no `target_organisms` or scoped growth evidence. | Add MediaDB growth-data import support in `src/culturemech/import/mediadb_importer.py`, or curate `data/normalized_yaml/bacterial/mms_medium_huber_et_al.yaml` if the importer will not be rerun. |
| Major | Preparation steps are source-unsupported generic importer assertions. | MediaDB medium 144 only supplies a compound table and source/growth links. The three record steps were created by `MediaDBImporter._create_preparation_steps`, which unconditionally emits dissolve, adjust-pH, and filter-sterilize steps for MediaDB media. | Remove or qualify generated MediaDB preparation defaults in `src/culturemech/import/mediadb_importer.py`; update `data/normalized_yaml/bacterial/mms_medium_huber_et_al.yaml` to retain only source-backed preparation data or a discussion flag. |
| Major | Source provenance cites the wrong paper and omits the structured Huber et al. source. | MediaDB source 46 names Huber et al. 1986 and Crossref resolves DOI `10.1007/BF00409880`; the embedded import event cites `Mazumdar et al. (2014) PLOS One` because `_create_curation_history` hard-codes that reference. | Fix `src/culturemech/import/mediadb_importer.py` and repair the existing curation event/source metadata in `data/normalized_yaml/bacterial/mms_medium_huber_et_al.yaml`. |
| Minor | One deprecated MediaIngredientMech slot remains after migration. | `Sodium sulfide` still has `mediaingredientmech_term: MediaIngredientMech:000119` even though the June 2026 history event says legacy MediaIngredientMech IDs were replaced with CHEBI-keyed links where id-safe. | Re-run or patch the MediaIngredientMech migration for this ingredient in `data/normalized_yaml/bacterial/mms_medium_huber_et_al.yaml` if `CHEBI:76208` is an id-safe mapping. |
| Minor | Generic application tags are over-broad for this single source record. | The inspected MediaDB pages for medium 144 do not assert `Cultivation of genome-sequenced organisms`, `Metabolic modeling`, or `Systems biology research` as applications of Huber et al.'s Thermotoga medium. | Replace generic MediaDB application defaults with evidence-backed applications in `src/culturemech/import/mediadb_importer.py` or remove them from `data/normalized_yaml/bacterial/mms_medium_huber_et_al.yaml`. |

## Recommended Edits

1. Regenerate the merged YAML from the repaired normalized record so `Nickel(II) ammonium sulfate` replaces `'''Nickel(II` in `data/merge_yaml/merged/mms_medium_huber_et_al.yaml`.
2. Correct MediaDB importer source handling so it can attach source 46 / DOI `10.1007/BF00409880` and does not stamp every import with `Mazumdar et al. (2014) PLOS One`; repair this record's embedded import note in the normalized owner.
3. Import or curate growthdata 292 as a scoped `Thermotoga maritima` growth claim with pH 6.5, temperature 85.0 C, growth rate 0.555 1/h, and source 46 evidence.
4. Remove the unconditional MediaDB dissolve/adjust-pH/filter-sterilize block from this normalized record unless a primary Huber et al. protocol is inspected and supports those exact steps.
5. Drop the generic applications or tie them to source text that actually supports those claims for this medium.
6. Finish converting the leftover sodium sulfide `mediaingredientmech_term` if the current CHEBI mapping is id-safe.

## Follow-up Checks

- Rerun the focused schema, strict, reference, and term validators against both `data/normalized_yaml/bacterial/mms_medium_huber_et_al.yaml` and the regenerated `data/merge_yaml/merged/mms_medium_huber_et_al.yaml`.
- Re-open `/defined_media/media/144/`, `/defined_media/media_text/144/`, `/defined_media/sources/46/`, `/defined_media/organisms/63/`, and `/defined_media/growthdata/292/` and verify each curated source, organism, and growth datum against the live MediaDB pages.
- If the Huber et al. 1986 article is accessible, compare the MediaDB formulation against DOI `10.1007/BF00409880` before adding any preparation claims MediaDB itself does not expose.
- Run the merge verification gate after regeneration and confirm `merge_fingerprint` no longer corresponds to a pre-repair normalized input.
- Check `rg --no-ignore --hidden -n \"'''Nickel\\(II|Nickel\\(II\\) ammonium sulfate\" data/normalized_yaml/bacterial/mms_medium_huber_et_al.yaml data/merge_yaml/merged/mms_medium_huber_et_al.yaml` to prove the repaired ingredient name propagated and the truncation fragment disappeared from the target.

## Additional Notes

- The legacy `springerlink.com` article URL linked from MediaDB source 46 did not resolve, and the current Springer PDF endpoint redirected to an identity-provider HTML page. I did not inspect the original Huber et al. PDF.
- `Nickel(II) ammonium sulfate` remains chemically ungrounded in the normalized owner and generated record. That is preferable to assigning an adjacent unsupported ChEBI term, but it should remain visible as an unresolved exact-grounding task.
- No GitHub issue, PR, or comment was created or edited by this read-only review.

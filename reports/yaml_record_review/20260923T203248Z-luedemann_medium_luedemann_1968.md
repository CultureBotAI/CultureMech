# YAML Record Review: LUEDEMANN Medium (LUEDEMANN; 1968)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/luedemann_medium_luedemann_1968.yaml`
- Started UTC: `2026-09-23T20:31:29Z`
- Finished UTC: `2026-09-23T20:32:48Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:006714`
- `name`: `luedemann_medium_luedemann_1968`
- `original_name`: `LUEDEMANN medium (LUEDEMANN; 1968)`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `media_term`: `komodo.medium:877`
- `merge_fingerprint`: `e1bdcad19f48014b80bb0b1e7a33cd8d2b689ecddc1533504cbc4fc55e31a97d`
- `merged_from`: `KOMODO_877_LUEDEMANN_medium_LUEDEMANN_1968`, `luedemann_medium_luedemann_1968`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/luedemann_medium_luedemann_1968.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:006714`, `CultureMech:002035`, `komodo.medium:877`, `mediadive.medium:877`, `luedemann_medium_luedemann_1968`, `KOMODO_877_LUEDEMANN_medium_LUEDEMANN_1968`, and the merge fingerprint found the maintained KOMODO 877 owner, the maintained DSMZ 877 owner, this generated merged record, and an archived DSMZ/KOMODO source-duplicate review.
- The KOMODO owner states DSMZ Medium 877 provenance, and the DSMZ owner resolves to MediaDive / DSMZ medium 877.
- MediaDive REST and the DSMZ PDF both resolve medium 877 as `LUEDEMANN MEDIUM (LUEDEMANN; 1968)` with pH 8.6.
- The generated merge correctly links KOMODO 877 to the DSMZ owner as a `SOURCE_DUPLICATE`.

## Evidence

- The DSMZ PDF lists the source recipe per 100 ml: 0.5 g yeast extract, 1.5 g malt extract broth, 1.0 g soluble starch, 1.0 g glucose, 0.2 g CaCO3, 0.5 g NaCl, 1.5 g agar, and 100 ml distilled water.
- MediaDive REST exposes the same DSMZ source and the same normalized gram-per-liter values used by the generated record: 5 g/L yeast extract, 15 g/L malt extract broth, 10 g/L starch, 10 g/L glucose, 2 g/L CaCO3, 5 g/L NaCl, and 15 g/L agar.
- The DSMZ PDF instructs pH 8.6 and sterilization at 121 C for 15 min at 1 atm.
- The maintained DSMZ owner stores that pH and sterilization instruction as a `HEAT` preparation step, but the generated KOMODO-centered record has no `preparation_steps`.

## Completeness

- All seven non-water recipe rows match DSMZ 877 after converting the 100 ml PDF recipe to grams per liter.
- The generated `ph_value` preserves the DSMZ pH 8.6.
- The generated record omits the 100 ml / 1000 ml distilled-water row.
- The generated record omits the DSMZ sterilization step.
- The generated record has no structured DSMZ, MediaDive, or KOMODO reference.

## Findings

1. The DSMZ preparation step was dropped during the duplicate merge.
   - Evidence: the maintained DSMZ owner includes `pH 8.6. Sterilize at 121 C for 15 min at 1 atm.` as a `HEAT` step, while the generated record merged from the KOMODO and DSMZ owners contains no `preparation_steps`.
   - Impact: the generated solid-agar recipe omits required sterilization conditions from the underlying DSMZ source.

2. Structured source references are absent.
   - Evidence: the generated record identifies KOMODO 877 and DSMZ 877 only in `media_term`, `notes`, and source-duplicate metadata; it has no `references` block for KOMODO, MediaDive 877, or the DSMZ PDF.
   - Impact: reference validation has no source URLs to check, and downstream users cannot follow a structured citation to the authoritative PDF.

3. The embedded KOMODO import timestamp is malformed.
   - Evidence: `curation_history` stores `timestamp: 2026-01-27T01:15:03.fZ`.
   - Impact: consumers that parse embedded curation history as ISO datetimes will fail on the generated record even though the current validators do not inspect embedded history objects.

## Recommended Edits

1. Preserve the DSMZ pH and sterilization instruction when merging DSMZ 877 into the KOMODO 877 generated record.
2. Add structured references for the DSMZ Medium 877 PDF, MediaDive 877, and the KOMODO 877 import source.
3. Fix the malformed KOMODO import timestamp in the normalized owner before regenerating outputs.
4. Keep the KOMODO and DSMZ owners linked as `SOURCE_DUPLICATE`; the ingredient signatures agree with the authoritative DSMZ PDF.

## Follow-up Checks

- Re-fetch DSMZ Medium 877 and MediaDive 877, then confirm the regenerated record still has 5 g/L yeast extract, 15 g/L malt extract broth, 10 g/L soluble starch, 10 g/L glucose, 2 g/L CaCO3, 5 g/L NaCl, and 15 g/L agar.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt record.
- Run an ignored-inclusive exact search for `luedemann_medium_luedemann_1968`, `komodo.medium:877`, and `mediadive.medium:877` to confirm no additional DSMZ 877 duplicate remains.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.

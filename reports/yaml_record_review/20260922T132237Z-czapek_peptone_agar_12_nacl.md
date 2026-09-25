# YAML Record Review: czapek_peptone_agar_12_nacl

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/czapek_peptone_agar_12_nacl.yaml`
- Started UTC: 2026-09-22T13:20:00Z
- Finished UTC: 2026-09-22T13:22:37Z
- Verdict: pass with minor issues

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated ID | `CultureMech:010462` |
| Name | `czapek_peptone_agar_12_nacl` |
| Original name | `CZAPEK PEPTONE AGAR + 12% NACL` |
| Source term | DSMZ Medium 1857 / `mediadive.medium:1857` |
| Category | `fungal` |
| Generated from | `czapek_peptone_agar_12_nacl` |
| Merge fingerprint | `0a237347ee10b21d2038ca87bd997b780cfa1029a98cbc6e877e9799659115bc` |

The generated record is a one-source projection of
`data/normalized_yaml/fungal/czapek_peptone_agar_12_nacl.yaml`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/czapek_peptone_agar_12_nacl.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/czapek_peptone_agar_12_nacl.yaml --out /private/tmp/czapek_peptone_agar_12_nacl.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/czapek_peptone_agar_12_nacl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/czapek_peptone_agar_12_nacl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after a harmless `eutils`/`pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` equivalent for `curation_history` | Not checked: the repository history validator targets standalone `history/*.yaml` records, not embedded generated `MediaRecipe.curation_history` events. |

## Identity and Grounding

- The record identifies DSMZ/MediaDive 1857, `CZAPEK PEPTONE AGAR + 12% NACL`.
  The MediaDive 1857 REST payload resolves and returns that exact medium ID and
  title.
- MediaDive 1857 supports all ten generated ingredients and the `ph_range`
  7.0-7.3.
- The 120 g/L `NaCl` row is source-faithful: it encodes the `+ 12% NACL`
  component as 120 g in a 1000 ml main solution.
- Primary ChEBI terms are exact for sucrose, NaNO3, K2HPO4, MgSO4 x 7 H2O,
  KCl, Fe SO4 x 7 H2O, NaCl, and agar. Yeast extract and Proteose peptone no. 3
  are intentionally ungrounded complex ingredients.
- A gitignore-independent search with `rg --no-ignore --hidden` over
  `data/raw`, `data/normalized_yaml`, and `data/merge_yaml/merged` found no raw
  capture for `mediadive.medium:1857`; it found the maintained fungal source,
  generated record, and generated indexes for this source ID.

## Evidence

- Supported by MediaDive 1857: sucrose 30 g, NaNO3 3 g, K2HPO4 1 g,
  MgSO4 x 7 H2O 0.5 g, KCl 0.5 g, Fe SO4 x 7 H2O 0.01 g, yeast extract 2 g,
  Proteose peptone no. 3 5 g, NaCl 120 g, agar 20 g, and pH range 7.0-7.3 in a
  1000 ml main solution.
- Supported by the formula: `physical_state: SOLID_AGAR`, `medium_type:
  COMPLEX`, and `composition_type: UNDEFINED`.
- Not source-supported from the inspected MediaDive 1857 payload: any
  sterilization, incubation, storage, or target-organism assertion. The record
  correctly does not add those claims.

## Completeness

- Empty optional slots for target organisms, growth metrics, solutions, variant
  links, quality flags, and preparation steps are acceptable for the inspected
  MediaDive 1857 payload.
- No duplicate source records are merged into this generated file.
- The generated notes say only `Source: DSMZ`; the stable source CURIE is still
  recoverable from `media_term`, but a normalized `references` entry for the
  MediaDive REST source would make provenance easier to validate.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Minor | NaNO3 still carries a deprecated `mediaingredientmech_term` instead of the CHEBI-keyed secondary slot. | The ingredient has exact primary `term: CHEBI:63005` but still uses `mediaingredientmech_term: MediaIngredientMech:000171`; the June 2026 curation history says the MIM ID scheme is deprecated. | Refresh `NaNO3` in `data/normalized_yaml/fungal/czapek_peptone_agar_12_nacl.yaml` to `mediaingredientmech_chebi_term: CHEBI:63005`, then regenerate. |

## Recommended Edits

1. Replace the leftover NaNO3 `mediaingredientmech_term` with
   `mediaingredientmech_chebi_term: CHEBI:63005` in the maintained fungal
   source.
2. Optionally add a `references` entry for MediaDive/DSMZ 1857 so the reference
   validator can prove that source in future runs.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after the NaNO3
  secondary-grounding refresh.
- Regenerate `data/merge_yaml/merged/czapek_peptone_agar_12_nacl.yaml` and run
  `just verify-merges`.
- Manually compare the regenerated record against MediaDive 1857 to confirm all
  ten ingredient amounts and pH range 7.0-7.3 remain unchanged.

## Additional Notes

- A guessed DSMZ PDF URL for `DSMZ_Medium1857.pdf` returned a TYPO3 404 page;
  MediaDive's REST medium metadata for ID 1857 did not expose a PDF link.

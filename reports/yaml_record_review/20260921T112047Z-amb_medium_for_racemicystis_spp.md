# YAML Record Review: amb_medium_for_racemicystis_spp

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/amb_medium_for_racemicystis_spp.yaml`
- Started UTC: 2026-09-21T11:20:08Z
- Finished UTC: 2026-09-21T11:20:48Z
- Verdict: pass with minor issues

## Target

| Field | Observed value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:001095` |
| Name | `amb_medium_for_racemicystis_spp` |
| Original name | `AMB MEDIUM FOR RACEMICYSTIS SPP.` |
| Source identity | DSMZ Medium 1614, `mediadive.medium:1614` |
| Generated status | Generated one-source merge |
| Generated path | `data/merge_yaml/merged/amb_medium_for_racemicystis_spp.yaml` |
| Maintained input | `data/normalized_yaml/bacterial/amb_medium_for_racemicystis_spp.yaml` |

The generated record is a one-source merge and matches the normalized DSMZ owner.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/amb_medium_for_racemicystis_spp.yaml` | Passed; no issues found. |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/amb_medium_for_racemicystis_spp.yaml --out /private/tmp/amb_medium_for_racemicystis_spp.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 `ERROR` rows emitted. |
| Reference | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/amb_medium_for_racemicystis_spp.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/amb_medium_for_racemicystis_spp.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Documented focused validator | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints are unavailable in this checkout because project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before target-specific validation. The no-project commands above exercise the same schema and validation code with Python 3.11.

## Identity and Grounding

The record's ID, source accession, and label agree with DSMZ Medium 1614:

- `id: CultureMech:001095`
- `name: amb_medium_for_racemicystis_spp`
- `media_term.preferred_term: DSMZ Medium 1614`
- `media_term.term.id: mediadive.medium:1614`
- `notes: Source: DSMZ | Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1614.pdf`

The major ingredient amounts and pH agree with the DSMZ PDF. Grounding is exact for K2HPO4, MgSO4 x 7 H2O, and agar. The starch row is grounded to generic starch even though DSMZ specifies soluble starch, and Casitone remains ungrounded.

## Evidence

Inspected source documents:

- DSMZ Medium 1614 PDF, fetched from `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1614.pdf` and converted to text with `mutool draw -F txt`

Supported claims:

- DSMZ supports the AMB Medium for Racemicystis spp. identity and the DSMZ 1614 accession.
- DSMZ supports 5 g/L soluble starch, 2.5 g/L Casitone, 0.25 g/L K2HPO4, 0.5 g/L MgSO4 x 7 H2O, 14 g/L agar, 1000 ml distilled water, and pH 7.2.
- DSMZ supports the note that 10 mM HEPES may be added to keep the pH constant.

Unsupported or mismatched claims:

- `Starch` is slightly broader than the source label `Soluble starch`.
- `Casitone` is source-supported but ungrounded.
- The implicit 1000 ml distilled-water volume is not represented as a structured row; this is non-blocking because the remaining concentrations are already per liter.

## Completeness

Consequential gaps:

- No consequential formulation or preparation gaps found.
- Target organisms are absent; no focused growth-evidence search was performed during this review.

Empty optional slots correctly left empty:

- No target organism was asserted, so there is no unsupported growth claim.
- No storage condition or atmosphere was asserted by DSMZ.
- Distilled water is omitted as a solvent basis rather than imported as a false 1 g/L solute.

Bounded absence checks:

- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -type f -name '*amb_medium_for_racemicystis_spp.md'` search found no pre-existing report for this generated record before this report was written.
- A gitignore-independent `rg --no-ignore --hidden` search over `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for the AMB/Racemicystis slug and labels found no second normalized record for DSMZ Medium 1614. It did find a separate DSMZ/KOMODO AMB Medium cluster for DSMZ Medium 455; that source is not a duplicate of this Racemicystis spp. recipe.

## Findings

### Blocker

None found.

### Major

None found.

### Minor

1. **Soluble starch has been broadened to generic starch.**

   Evidence: DSMZ Medium 1614 lists soluble starch. The record stores `Starch` grounded to generic `CHEBI:28017`.

   Owner: use an exact soluble-starch label or leave the generic starch term only with a note that the DSMZ source specifies soluble starch.

2. **Casitone is ungrounded.**

   Evidence: DSMZ supports the 2.5 g/L Casitone row, but the row has no ontology term or MediaIngredientMech mirror.

   Owner: resolve Casitone to an exact medium-ingredient term if one exists in the local ingredient index; otherwise leave it unresolved with the source amount intact.

## Recommended Edits

1. Refine the starch label or note to preserve DSMZ's soluble-starch wording.
2. Resolve or explicitly leave unresolved the Casitone ingredient grounding.
3. Regenerate generated merge records and rendered products after the normalized owner changes.

## Follow-up Checks

- Rerun schema, strict, reference, and term validators on the corrected normalized owner and regenerated output.
- Manually compare the regenerated AMB/Racemicystis page to DSMZ Medium 1614 to confirm all five non-water ingredients and pH 7.2 remain unchanged.

## Additional Notes

- This review is read-only. It intentionally leaves `data/merge_yaml/merged/amb_medium_for_racemicystis_spp.yaml`, its normalized owner, and generated pages unchanged.
- Generated files under `data/merge_yaml/merged/` are derived artifacts. Minor corrections belong in `data/normalized_yaml/bacterial/amb_medium_for_racemicystis_spp.yaml`.

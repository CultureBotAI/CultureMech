# YAML Record Review: aurantimonas_manganoxydans_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AURANTIMONAS_MANGANOXYDANS_MEDIUM.yaml
- Started UTC: 2026-09-21T16:42:27Z
- Finished UTC: 2026-09-21T16:44:18Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/AURANTIMONAS_MANGANOXYDANS_MEDIUM.yaml`, a
generated `MediaRecipe` with stable ID `CultureMech:004082`, normalized name
`aurantimonas_manganoxydans_medium`, original name
`AURANTIMONAS MANGANOXYDANS medium`, category `bacterial`, `medium_type:
COMPLEX`, `composition_type: UNDEFINED`, `physical_state: SOLID_AGAR`,
`ph_value: 7.5`, media term `komodo.medium:1326`, and merge fingerprint
`ac1ad5e3c3259fa8960d5ab6bced703730044e0856bb72601a0660bff1506d9d`.

The generated merge combines two maintained sources,
`data/normalized_yaml/bacterial/KOMODO_1326_AURANTIMONAS_MANGANOXYDANS_medium.yaml`
and `data/normalized_yaml/bacterial/aurantimonas_manganoxydans_medium.yaml`.
Both are maintained inputs; future fixes should land there, or in merge rules,
then regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AURANTIMONAS_MANGANOXYDANS_MEDIUM.yaml` | Pass, `No issues found`. |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AURANTIMONAS_MANGANOXYDANS_MEDIUM.yaml --out /private/tmp/AURANTIMONAS_MANGANOXYDANS_MEDIUM.strict.tsv --workers 1 --quiet` | Pass: 1 file scanned, 0 files with errors, 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AURANTIMONAS_MANGANOXYDANS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass: 1 file validated, 0 reference checks emitted. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AURANTIMONAS_MANGANOXYDANS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass; the validator also emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused validator for `MediaRecipe.curation_history` in one generated merge record. |

The direct `just validate-schema`, `just validate-strict`, `just
validate-references`, and `just validate-terms` entrypoints were not used for
this target because this checkout currently reaches a project `uv` build of
`llvmlite==0.46.0` under Python 3.13 before target-specific validation and
crashes in setuptools with `TypeError: Popen.__init__() got an unexpected
keyword argument 'dry_run'`.

## Identity and Grounding

The generated identity is source-consistent: KOMODO 1326 explicitly cites DSMZ
Medium 1326, the local MediaDive/DSMZ owner has the same nine ingredients and
concentrations, and both normalized owners are already linked as
`SOURCE_DUPLICATE`. The generated record correctly carries the KOMODO owner as
canonical and the DSMZ/MediaDive owner as `parent_media`.

The source label `CaCl2 x 7 H2O` is grounded to `CHEBI:3312` calcium
dichloride. That anhydrous grounding does not exactly match the supplied
hydrate label. If no trusted CHEBI term exists for the stated hydrate, the row
should stay explicitly unresolved rather than point at anhydrous calcium
chloride.

A gitignore-independent exact search covered `data`, `reports`, `history`, and
`.claude` for `CultureMech:004082`, `CultureMech:000783`,
`komodo.medium:1326`, `mediadive.medium:1326`,
`KOMODO_1326_AURANTIMONAS_MANGANOXYDANS_medium`,
`aurantimonas_manganoxydans_medium`, and `AURANTIMONAS MANGANOXYDANS medium`.
It found only the two maintained normalized owners as current data owners, plus
generated indexes, archived pre-rename validation rows, and the archive that
recorded the DSMZ/KOMODO source-duplicate relationship. An exhaustive `find`
confirmed the two current owner paths.

## Evidence

The inspected DSMZ Medium 1326 PDF supports the base mixture as Yeast extract
0.5 g, Peptone 2.0 g, and 980 ml Artificial seawater. The artificial seawater
stock itself is 17.55 g NaCl, 0.75 g KCl, 12.35 g MgSO4 x 7 H2O, 1.46 g
CaCl2 x 7 H2O, and 1000 ml distilled water.

The generated target flattens Artificial seawater into final-medium NaCl, KCl,
MgSO4, and CaCl2 rows at the stock concentrations. That loses the source's
980 ml/L dilution and the stock boundary.

The DSMZ PDF also instructs adding 20 ml of 1 M HEPES sterile buffer at pH 7.8
and 0.1 ml of sterile 3 mg/ml ferric ammonium citrate after autoclaving. The
generated target stores HEPES as 4.766 g/L and ferric ammonium citrate as
0.1 g/L direct ingredients. The HEPES mass is consistent with a 20 mM final
amount, but the row loses the fact that it is an added sterile pH 7.8 buffer;
the ferric ammonium citrate row is quantitatively wrong because 0.1 ml of a
3 mg/ml stock contributes 0.3 mg, not 0.1 g.

The DSMZ/MediaDive owner has one `preparation_steps` item covering the
post-autoclave HEPES and ferric ammonium citrate additions, final pH 7.5, and
optional 15 g/L agar solidification. The generated canonical record selected
the KOMODO owner as primary and dropped that preparation step even though the
merged DSMZ duplicate contained it.

## Completeness

The missing target organism and growth-evidence fields are not findings in
this imported DSMZ/KOMODO recipe: the inspected medium recipe does not assert a
strain growth outcome.

The generated target is missing a consequential source-supported procedure from
one of its two duplicate inputs. Before writing this report,
`find reports/yaml_record_review -maxdepth 1 -name '*AURANTIMONAS_MANGANOXYDANS_MEDIUM.md' -print`
covered ignored and unignored files in the review-report directory and found no
prior exact report for this generated stem.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Artificial seawater was flattened into final-medium ingredients without preserving its 980 ml/L addition. | DSMZ lists Artificial seawater at 980 ml and defines a 1 L Artificial seawater stock; the target stores the stock NaCl, KCl, MgSO4, and CaCl2 values directly. | Both normalized AURANTIMONAS MANGANOXYDANS owners, or the DSMZ/KOMODO import rule that expands DSMZ stock solutions. |
| Major | Ferric ammonium citrate is off by more than two orders of magnitude. | DSMZ adds 0.1 ml of a 3 mg/ml sterile stock, which is 0.3 mg total; the target records `Ferric ammonium citrate` as `0.1 G_PER_L`. | Both normalized AURANTIMONAS MANGANOXYDANS owners. |
| Major | Post-autoclave addition context was dropped from the canonical merge. | The DSMZ/MediaDive normalized owner records the HEPES and ferric ammonium citrate post-autoclave instruction; the generated merge selected the KOMODO owner and contains no `preparation_steps`. | Merge rules for source duplicates, or the KOMODO duplicate owner if the canonical source remains KOMODO. |
| Major | `CaCl2 x 7 H2O` is grounded to an anhydrous calcium chloride term. | The source label explicitly includes seven waters of hydration, but the target uses `CHEBI:3312` calcium dichloride. | Both normalized owners and the ID-not-found fallback/regrounding path. |

No blockers or minor findings were found beyond those major curation issues.

## Recommended Edits

1. Represent DSMZ Artificial seawater as a 980 ml/L nested solution or
   explicitly calculate the 0.98-diluted final NaCl, KCl, MgSO4 x 7 H2O, and
   CaCl2 x 7 H2O concentrations with notes that preserve the stock arithmetic.
2. Replace `Ferric ammonium citrate 0.1 G_PER_L` with a representation of the
   sterile 3 mg/ml stock added at 0.1 ml/L, or with the correct final mass
   concentration and arithmetic notes.
3. Preserve the source's post-autoclave HEPES and ferric ammonium citrate
   addition step when the DSMZ and KOMODO source duplicates are merged.
4. Re-ground `CaCl2 x 7 H2O` to a verified exact hydrate term, or leave the row
   unresolved if CHEBI lacks that hydrate.

## Follow-up Checks

- Re-run open-schema LinkML, `scripts/validate_strict.py`, the reference
  validator, and the term validator against both edited normalized owners and
  the regenerated
  `data/merge_yaml/merged/AURANTIMONAS_MANGANOXYDANS_MEDIUM.yaml`.
- Manually compare the regenerated merge with DSMZ Medium 1326 to verify that
  the 980 ml Artificial seawater stock, 20 ml HEPES buffer, 0.1 ml ferric
  ammonium citrate stock, and optional 15 g/L agar are all correctly scoped.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  generated merges to ensure the source-duplicate merge stays fresh.

## Additional Notes

The DSMZ Medium 1326 PDF was fetched successfully. `pdftotext` was not
available in the local shell, so the source text above was extracted with the
cached Python `pypdf` package through `uv --no-project --offline`.

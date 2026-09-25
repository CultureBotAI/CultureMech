# YAML Record Review: ARTIFICIAL SEAWATER MEDIUM WITH PULLULAN

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/artificial_seawater_medium_with_pullulan__dbb4c222.yaml`
- Started UTC: 2026-09-21T15:25:10Z
- Finished UTC: 2026-09-21T15:25:33Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:003332` |
| Name | `artificial_seawater_medium_with_pullulan` |
| Original name | ARTIFICIAL SEAWATER MEDIUM WITH PULLULAN |
| Category | `bacterial` |
| Source identity | MediaDive/JCM `mediadive.medium:J983` |
| Generated status | Generated single-source merge of `data/normalized_yaml/bacterial/artificial_seawater_medium_with_pullulan.yaml` |

This is the MediaDive/JCM sibling of TOGO `M1036`. It should not be conflated
with the adjacent generated TOGO record,
`data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/artificial_seawater_medium_with_pullulan__dbb4c222.yaml` | Passed; no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/artificial_seawater_medium_with_pullulan__dbb4c222.yaml --out /private/tmp/artificial_seawater_medium_with_pullulan__dbb4c222.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/artificial_seawater_medium_with_pullulan__dbb4c222.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/artificial_seawater_medium_with_pullulan__dbb4c222.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record; `just validate-history` targets standalone records under `history/`. |

The documented `just` validators could not be used directly because project
`uv` still fails while building `llvmlite==0.46.0` under Python 3.13. The
no-project commands above ran the same validator families on the target record.

## Identity and Grounding

The source identity is valid: MediaDive resolves `J983` as `ARTIFICIAL SEAWATER
MEDIUM WITH PULLULAN`, marks it as a JCM medium, and links to the live JCM
`GRMD=983` page; JCM 983 carries the same title and formulation.

Ingredient grounding is mixed:

- Main-solution salts, pullulan, resazurin, most trace salts, and vitamins are
  chemically recognizable.
- `NiCl2 x 6 H2O` is grounded to `CHEBI:34887` / nickel dichloride, losing the
  hexahydrate identity.
- `HCl` is grounded to `CHEBI:17883` / hydrogen chloride, while the MediaDive
  FeCl2 stock row is explicitly 7.7 M, 25% hydrochloric acid.

## Evidence

MediaDive's medium JSON preserves a `Main sol. J983` solution with 1 ml FeCl2
solution, 1 ml trace element solution, 1 ml selenite-tungstate solution, 10 ml
trace vitamins, and 20/10/5/6 ml additions of the 5% Na2CO3, 1% NH4Cl, 1%
KH2PO4, and 5% Na2S x 9 H2O solutions. JCM 983 reports the same amounts and the
same preparation text.

The generated record has no `solutions` block. Several current direct
ingredients are stock-local or volume-addition rows, not final-medium direct
ingredients:

| Current ingredient rows | Source status |
|---|---|
| `HCl`, `FeCl2 x 4 H2O` | Components of MediaDive solution 3846 / FeCl2 solution, added to J983 at 1 ml. |
| `ZnCl2`, `MnCl2 x 4 H2O`, `H3BO3`, `CoCl2 x 6 H2O`, `CuCl2 x 2 H2O`, `NiCl2 x 6 H2O`, `Na2MoO4 x 2 H2O` | Components of MediaDive solution 3847 / Trace element solution, added to J983 at 1 ml. |
| `NaOH`, `Na2SeO3 x 5 H2O`, `Na2WO4 x 2 H2O` | Components of MediaDive solution 4172 / Selenite-tungstate solution, added to J983 at 1 ml. |
| All vitamin rows | Components of MediaDive solution 3861 / Trace vitamins, added to J983 at 10 ml. |
| `NH4Cl`, `KH2PO4`, `Na2CO3`, `Na2S x 9 H2O` | Source rows are volume additions of 1%, 1%, 5%, and 5% solutions, not 10/5/20/6 `G_PER_L` ingredient rows. |

The first six non-water main-solution ingredients have final-volume-adjusted
`g_l` values matching MediaDive's 1054 ml `Main sol. J983` export. Most
stock-local ingredients instead match the stock recipe's own `g_l` value, so
the record mixes final-medium concentrations and undiluted stock concentrations
in one flat ingredient list.

## Completeness

The record retains two important JCM preparation sentences and `ph_value: 7.3`.
Those are useful but incomplete:

- the JCM source gives a range of 7.2-7.5 and says to adjust with 5% Na2CO3 if
  necessary; the scalar `7.3` comes from MediaDive's min/max export rather than
  the source range;
- no source-linked solution additions remain, so the preparation text refers to
  "the following solutions" but the record has only direct ingredients; and
- the MediaDive stock solution IDs 3846, 3847, 4172, and 3861 are not preserved.

Optional target-organism and growth-evidence slots are empty. I did not flag
that as a defect because JCM and MediaDive identify the recipe rather than a
specific experiment or growth observation.

Before reporting raw-source absence, I searched for `CultureMech:003332`,
`mediadive.medium:J983`, `JCM Medium J983`, and `ARTIFICIAL SEAWATER MEDIUM
WITH PULLULAN` with `rg --no-ignore --hidden` across `data`, `scripts`,
`history`, `src`, `reports`, and `references_cache`. That gitignore-independent
search found the normalized owner, generated merge, indexes, and archived
reports, but no maintained raw YAML or source-specific importer file for J983.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | MediaDive solution structure has been flattened away, leaving stock-local ingredients as direct final-medium ingredients. | MediaDive JSON carries FeCl2, trace element, selenite-tungstate, and trace-vitamin solutions with their own solution IDs and 1/1/1/10 ml addition amounts; the CultureMech record lists all stock components directly and has no `solutions` block. | `data/normalized_yaml/bacterial/artificial_seawater_medium_with_pullulan.yaml` |
| major | Several post-autoclave additions have impossible final-medium amounts. | JCM/MediaDive use 10 ml of 1% NH4Cl, 5 ml of 1% KH2PO4, 20 ml of 5% Na2CO3, and 6 ml of 5% Na2S x 9 H2O; the record stores `10`, `5`, `20`, and `6` `G_PER_L` for those four chemicals. | `data/normalized_yaml/bacterial/artificial_seawater_medium_with_pullulan.yaml` |
| major | Final and stock concentration frames are mixed. | NaCl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, KCl, Resazurin, and Pullulan match MediaDive's final `Main sol. J983` values, but FeCl2, trace-solution solutes, selenite/tungstate solutes, and vitamins match the undiluted stock `g_l` values from MediaDive solutions 3846, 3847, 4172, and 3861. | `data/normalized_yaml/bacterial/artificial_seawater_medium_with_pullulan.yaml` |
| major | `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride. | The row denotes the hexahydrate but uses `CHEBI:34887` / nickel dichloride. | `data/normalized_yaml/bacterial/artificial_seawater_medium_with_pullulan.yaml` |
| minor | The JCM pH range is collapsed to a midpoint-like scalar. | JCM states pH 7.2-7.5 adjusted with 5% Na2CO3 if necessary; the record stores `ph_value: 7.3`. | `data/normalized_yaml/bacterial/artificial_seawater_medium_with_pullulan.yaml` |

## Recommended Edits

1. Rebuild the record from MediaDive's `medium/J983` hierarchy or JCM 983 so stock additions remain separate from final direct ingredients.
2. Preserve FeCl2 solution, trace element solution, selenite-tungstate solution, trace vitamins, 1% NH4Cl, 1% KH2PO4, 5% Na2CO3, and 5% Na2S x 9 H2O as volume-based post-autoclave additions.
3. Remove stock-local HCl, trace metals, selenite/tungstate salts, and vitamins from the direct final-medium ingredient list unless they are explicitly represented as calculated final concentrations with source and dilution provenance.
4. Re-ground `NiCl2 x 6 H2O` to an exact hydrate term, and treat `HCl` as 7.7 M, 25% hydrochloric acid if the FeCl2 stock is represented directly.
5. Preserve the source pH range or add a discussion noting why MediaDive's 7.3 scalar is retained instead of JCM's 7.2-7.5 range.
6. Regenerate `data/merge_yaml/merged/artificial_seawater_medium_with_pullulan__dbb4c222.yaml`.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/artificial_seawater_medium_with_pullulan.yaml`.
- Run `just validate-strict data/normalized_yaml/bacterial/artificial_seawater_medium_with_pullulan.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/artificial_seawater_medium_with_pullulan.yaml`.
- Run `just validate-references data/normalized_yaml/bacterial/artificial_seawater_medium_with_pullulan.yaml`.
- Run `just verify-merges` after regeneration.
- Manually compare the regenerated record with MediaDive `J983` and JCM `GRMD=983` to confirm the stock solution hierarchy, final 1054 ml volume arithmetic, pH range, and preparation steps agree.

## Additional Notes

None found.

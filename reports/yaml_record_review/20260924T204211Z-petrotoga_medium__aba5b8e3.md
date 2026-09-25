# YAML Record Review: PETROTOGA medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/petrotoga_medium__aba5b8e3.yaml
- Started UTC: 2026-09-24T20:42:11Z
- Finished UTC: 2026-09-24T20:42:11Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record path | `data/merge_yaml/merged/petrotoga_medium__aba5b8e3.yaml` |
| Canonical maintained owner | `data/normalized_yaml/bacterial/KOMODO_718_PETROTOGA_medium.yaml` |
| Other merged maintained owners | `data/normalized_yaml/bacterial/for_dsm_10674.yaml`, `data/normalized_yaml/bacterial/for_dsm_10691.yaml`, `data/normalized_yaml/bacterial/for_dsm_13782.yaml`, `data/normalized_yaml/bacterial/for_dsm_14811.yaml`, `data/normalized_yaml/bacterial/for_dsm_16923.yaml`, `data/normalized_yaml/bacterial/petrotoga_halophila_medium.yaml`, `data/normalized_yaml/bacterial/petrotoga_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:006360` |
| Name | `petrotoga_medium` |
| Original name | `PETROTOGA medium` |
| Media term | `komodo.medium:718` |
| Generated status | Generated merge output from 8 maintained normalized records |

The target resolves to the generated `aba5b8e3` merge whose canonical owner is
the KOMODO ModelSEED 718 import of DSMZ Medium 718. An ignored-inclusive search
over `data`, `src`, and `scripts` for `CultureMech:006360`, `aba5b8e3`,
`mediadive.medium:718a`, `DSMZ_Medium718a`, and the five
`komodo.medium:718.x` IDs found that the merge also pulled in DSMZ 718
strain-supplement rows and the separate DSMZ 718a Petrotoga halophila recipe.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/petrotoga_medium__aba5b8e3.yaml` | Passed; no issues found. |
| Strict repository validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/petrotoga_medium__aba5b8e3.yaml --out /private/tmp/petrotoga_medium__aba5b8e3.strict.tsv --workers 1 --quiet` | Passed; the TSV had only its header line, so 0 errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/petrotoga_medium__aba5b8e3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/petrotoga_medium__aba5b8e3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run. | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in one generated YAML file. |

## Identity and Grounding

The generated record no longer denotes one medium. The canonical source is
KOMODO 718 / DSMZ 718, but the merge set also includes five KOMODO 718.x
strain-supplement records and `petrotoga_halophila_medium`
(`mediadive.medium:718a`). DSMZ/MediaDive 718a is named PETROTOGA HALOPHILA
MEDIUM and is not the same source recipe as DSMZ 718 PETROTOGA MEDIUM.

This wrong merge materially changes the top-level formulation. DSMZ 718 has
18 g NaCl and 0.2 g yeast extract in the main solution. DSMZ 718a has 50 g NaCl
and 2 g yeast extract. The generated `petrotoga_medium__aba5b8e3.yaml` carries
NaCl `50.3583` g/L and yeast extract `1.97433` g/L, showing that the 718a
halophila values have been merged into a record whose media term still says
`komodo.medium:718`.

The top-level `composition_type: UNDEFINED` is also too weak. The relevant DSMZ
718 and 718a sources list defined salts and stock solutions plus yeast extract,
so each individual recipe is semi-defined and complex rather than undefined.

## Evidence

DSMZ/MediaDive 718 supports the base Petrotoga Medium recipe with 10 ml
Modified Wolin's mineral solution, 2 ml of 0.1% Fe(NH4)2(SO4)2 x 7 H2O,
0.5 ml of 0.1% sodium resazurin, 1 ml Wolin's vitamin solution (10x), and
1000 ml water in the main solution. Those two named stocks are 1000 ml
solutions with their own recipes.

DSMZ/MediaDive 718a supports a different top-level medium named PETROTOGA
HALOPHILA MEDIUM. Its stock solutions are the same, but its main solution has
50 g NaCl and 2 g yeast extract; those are deliberate differences from DSMZ
718's 18 g NaCl and 0.2 g yeast extract.

The DSMZ 718 `For DSM 10691`, `For DSM 13782`, `For DSM 14811`, and related
KOMODO 718.x owners are supplements or strain-specific changes to the base
medium, not alternate accessions for the same base recipe. Their source text
adds or removes ingredients such as Trypticase peptone, Na2S2O3 x 5 H2O, and
D-Glucose.

The generated record flattens stock recipes into final ingredients in the same
way as the direct DSMZ 718 and 718a normalized owners. MgSO4 x 7 H2O is
`6.40573` g/L from `[Merged 2 duplicates: 3.40573, 3.0]`, CaCl2 x 2 H2O is
`0.238203` g/L from `[Merged 2 duplicates: 0.138203, 0.1]`, and NaCl is
`50.3583` g/L from `[Merged 2 duplicates: 49.3583, 1.0]`; each sum crosses a
main-solution/stock-solution boundary that exists in the source.

The generated record has pH 6.5-6.7 but omits the DSMZ anaerobic preparation
steps for base 718 and 718a, including N2/CO2 sparging, anoxic dispensing,
autoclaving, post-autoclave addition of glucose, yeast extract, vitamins, and
sulfide from sterile stocks, vitamin filtration, and pH adjustment of the
complete medium. It also omits the Modified Wolin's mineral solution KOH
adjustment step.

## Completeness

The generated record lacks all nested `solutions:` data for Modified Wolin's
mineral solution and Wolin's vitamin solution (10x), and lacks the main and
stock water rows.

The generated record lacks preparation steps despite inheriting a pH range.

The generated merge omitted exact TOGO M2625, another DSMZ 718 derivative, but
incorrectly included DSMZ 718a and strain-specific 718.x supplements. That
combination shows that exact duplicates and biologically distinct variants are
both being mishandled for this family.

No empty optional field was material to this review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | The generated record conflates several non-identical Petrotoga recipes. | The `merged_from` list includes KOMODO 718, five KOMODO 718.x strain-supplement recipes, DSMZ 718a Petrotoga halophila Medium, and direct DSMZ 718; 718a is a different top-level medium with 50 g NaCl and 2 g yeast extract, and the KOMODO 718.x records encode source supplement instructions rather than exact accessions for base DSMZ 718. | Merge fingerprint/source-equivalence logic and the eight owners listed under `merged_from` |
| Major | Nested DSMZ stock solutions were flattened into the final ingredient list and stock concentrations were summed with main-solution concentrations. | DSMZ 718 and 718a both add 10 ml Modified Wolin's mineral solution and 1 ml Wolin's vitamin solution (10x); the generated record has no `solutions:` section and contains top-level stock ingredients plus summed duplicate salts. | `data/normalized_yaml/bacterial/KOMODO_718_PETROTOGA_medium.yaml`, `data/normalized_yaml/bacterial/petrotoga_medium.yaml`, and `data/normalized_yaml/bacterial/petrotoga_halophila_medium.yaml` |
| Major | The generated record omits DSMZ preparation requirements. | DSMZ 718 and 718a provide anaerobic N2/CO2, autoclaving, post-autoclave stock-addition, vitamin-filtration, final-pH, and mineral-stock pH steps, but the generated record has no `preparation_steps`. | The same three DSMZ/MediaDive owners and the KOMODO DSMZ enrichment path |
| Minor | The top-level composition type is too weak. | The merged source recipes are itemized and include yeast extract; each exact DSMZ recipe should be `SEMI_DEFINED`, not `UNDEFINED`. | Each owner in the `aba5b8e3` merge set |

## Recommended Edits

1. Tighten merge equivalence so exact DSMZ 718, DSMZ 718 strain supplements,
   and DSMZ 718a do not share the same fingerprint unless a variant-aware model
   can represent the supplement or halophila delta explicitly.
2. Split `data/merge_yaml/merged/petrotoga_medium__aba5b8e3.yaml` back into at
   least exact DSMZ 718, DSMZ 718a, and the individual strain-supplement
   outputs.
3. Merge TOGO M2625 into exact DSMZ 718 after preserving its source identity
   as another derivative of `mediadive.medium:718`.
4. Recurate the exact DSMZ 718 and 718a owners with explicit Modified Wolin's
   mineral solution and Wolin's vitamin solution (10x) stock scopes, including
   water rows and preparation steps.
5. Set `composition_type` to `SEMI_DEFINED` on each regenerated exact recipe.

## Follow-up Checks

1. Regenerate the merged YAML and rerun the open schema, strict, reference, and
   term validators on each regenerated Petrotoga output.
2. Use an ignored-inclusive exact search for `aba5b8e3`, `mediadive.medium:718`,
   `mediadive.medium:718a`, and `komodo.medium:718.` under `data`, `src`, and
   `scripts` to confirm that 718, 718a, and 718.x owners no longer collapse
   into one `merged_from` list.
3. Manually compare the regenerated DSMZ 718 and 718a outputs to their
   respective DSMZ/MediaDive sources and verify that NaCl, yeast extract,
   stock-solution aliquots, stock recipes, and preparation text are scoped to
   the correct recipe.

## Additional Notes

The exact TOGO M2625 split was reviewed separately in
`data/merge_yaml/merged/petrotoga_medium__0281b3a5.yaml`; this report focuses
on the direct DSMZ/KOMODO aggregate that should have received M2625 but instead
absorbed non-identical DSMZ 718 variants.

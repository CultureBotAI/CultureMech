# YAML Record Review: METHYLOMONAS MEDIUM (ELBE)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methylomonas_medium_elbe.yaml
- Started UTC: 2026-09-24T05:38:00Z
- Finished UTC: 2026-09-24T05:41:12Z
- Verdict: needs curation

## Target

- **Class**: MediaRecipe
- **ID**: CultureMech:001135
- **Name**: methylomonas_medium_elbe
- **Original name**: METHYLOMONAS MEDIUM (ELBE)
- **Generated status**: generated merge record under `data/merge_yaml/merged/`
- **Maintained owner**: `data/normalized_yaml/bacterial/methylomonas_medium_elbe.yaml`
- **Merge input**: `methylomonas_medium_elbe`
- **Merge fingerprint**: `9e1177243dfd46b1bfcc7c08d91c2d41aa4b3f4c0f49c2f89e957c456d1dcd4d`
- **Source identity**: DSMZ / MediaDive medium `1653`
- **Media term**: `mediadive.medium:1653` / DSMZ Medium 1653
- **Category**: bacterial
- **Composition and physical state**: `DEFINED`, `SOLID_AGAR`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methylomonas_medium_elbe.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/methylomonas_medium_elbe.yaml --out /private/tmp/methylomonas_medium_elbe.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file with 0 ERROR rows. The TSV contained the header only. |
| References, `linkml-reference-validator validate data data/merge_yaml/merged/methylomonas_medium_elbe.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Terms, `linkml-term-validator validate-data data/merge_yaml/merged/methylomonas_medium_elbe.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged recipe YAML. |

## Identity and Grounding

The record denotes the intended DSMZ/MediaDive source. The local `media_term`
identifier `mediadive.medium:1653`, label `METHYLOMONAS MEDIUM (ELBE)`, source
note URL, and the live MediaDive REST payload for medium 1653 all point to DSMZ
medium 1653. The current DSMZ PDF is also titled `1653. METHYLOMONAS MEDIUM
(ELBE)`.

The bacterial category and solid agar state are supported by the DSMZ recipe:
the main solution includes 20 g agar per liter, and the PDF notes that the DSM
strains only grow on agar-based media rather than in liquid medium.

An ignored-file-inclusive exact filename search under `data/` found
`data/normalized_yaml/bacterial/methylomonas_medium_elbe.yaml` and this
generated merge file. An ignored-file-inclusive exact ID search under
`data/raw/mediadive` and `data/raw/mediadive_api` found no checked-in raw
MediaDive JSON for medium 1653 or main solution 3427; only the source README
files are present in those raw directories.

## Evidence

The direct main-medium rows for `MgCl2 x 6 H2O`, `KCl`, `CaCl2 x 2 H2O`, and
agar match the DSMZ and MediaDive main solution amounts: 9.27 g, 10.00 g,
1.22 g, and 20.00 g per 1000 ml, respectively. The `HEPES buffer` row is also
dimensionally consistent with adding 10 ml of a 1 M HEPES buffer to a liter of
medium, which is 10 mmol/L HEPES or 2.383 g/L using the MediaDive equivalent.

The rest of the record flattens source stock recipes into final-medium
ingredients. DSMZ and MediaDive describe three nested solution additions in the
main medium: 1 ml Trace element solution SL-10, 3 ml PO4 buffer, and 5 ml
Vitamin solution per 1000 ml medium. The YAML drops those solution references
and serializes their undiluted recipes as final `ingredients`, for example:

| Source scope | Source row | YAML row |
|---|---|---|
| 3 ml PO4 buffer per 1000 ml final medium; the stock contains 0.90 g/L `Na2HPO4 x 2 H2O` and 0.30 g/L `KH2PO4` | `Na2HPO4 x 2 H2O` and `KH2PO4` are PO4 buffer components | `0.9 G_PER_L` and `0.3 G_PER_L` as final ingredients |
| 1 ml Trace element solution SL-10 per 1000 ml final medium; the stock contains 1.5 g/L `FeCl2 x 4 H2O` | `FeCl2 x 4 H2O` is a trace stock component | `1.5 G_PER_L` as a final ingredient |
| 5 ml Vitamin solution per 1000 ml final medium; the stock contains 100 mg/L nicotinic acid | `Nicotinic acid` is a vitamin stock component | `0.1 G_PER_L` as a final ingredient |

The standalone Vitamin B12 addition is also misserialized. DSMZ specifies
1.00 ml of a 50 mg/L Vitamin B12 stock; the YAML records Vitamin B12 at
`1 G_PER_L`, which treats the source volume as a gram-per-liter mass.

DSMZ gives one consequential cultivation condition, "The gas atmosphere is
air:methane 1:1." The YAML has no structured atmosphere, preparation step, or
condition preserving that requirement.

## Completeness

The record is complete enough for its DSMZ/MediaDive identity, direct
main-medium salts, and agar quantity, but it is incomplete as an executable
recipe because it omits the nested PO4 buffer, Trace element solution SL-10,
and Vitamin solution additions and lacks the air:methane 1:1 atmosphere.

Empty `target_organisms`, `growth_metrics`, and `references` are not defects
for this generated import by themselves. The current DSMZ PDF uses a placeholder
DSM strain token and does not name a strain or primary growth study.

The maintained normalized YAML has the same flattened ingredients as this merge
record, so the defect is already present before merge generation.

## Findings

### Blocker

None found.

### Major

1. **Nested stock recipes were flattened into final-medium ingredients.**
   DSMZ/MediaDive medium 1653 has a main solution plus three named subrecipes:
   PO4 buffer, Trace element solution SL-10, and Vitamin solution. The YAML has
   no `solutions` block and instead stores stock-strength PO4, trace-element,
   and vitamin entries as final `ingredients`. The concentration-plausibility
   report independently flags `Vitamin B12`, `FeCl2 x 4 H2O`, and `Nicotinic
   acid` in `bacterial/methylomonas_medium_elbe.yaml` as stock-strength or
   volume/unit anomalies. Future fixes belong in
   `data/normalized_yaml/bacterial/methylomonas_medium_elbe.yaml` or the
   MediaDive import/regeneration path that writes that normalized file; do not
   patch `data/merge_yaml/merged/methylomonas_medium_elbe.yaml` directly.

2. **The source atmosphere is absent from the structured recipe.** DSMZ
   specifies an air:methane 1:1 gas atmosphere. The record has no preparation or
   condition entry for that gas mix, so a downstream user could follow the YAML
   under ordinary air and materially diverge from the source protocol. The
   maintained owner is `data/normalized_yaml/bacterial/methylomonas_medium_elbe.yaml`.

### Minor

None found.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/methylomonas_medium_elbe.yaml`, replace
   the flattened PO4 buffer, Trace element solution SL-10, and Vitamin solution
   member ingredients with source-scoped solution additions:
   `mediadive.solution:3428` at 3 ml/L, `mediadive.solution:2243` at 1 ml/L,
   and `mediadive.solution:3430` at 5 ml/L.

2. Represent the Vitamin B12 addition as a 1 ml/L stock addition with its
   `50mg/l` source attribute rather than `1 G_PER_L` Vitamin B12.

3. Preserve the stock recipes for PO4 buffer, Trace element solution SL-10, and
   Vitamin solution as stock-solution records or as structured solution
   members tied to the source scopes; include stock water rows inside the stock
   recipes rather than as final-medium ingredients.

4. Add the DSMZ air:methane 1:1 gas atmosphere to the recipe's preparation or
   condition fields.

5. Regenerate `data/merge_yaml/merged/methylomonas_medium_elbe.yaml` from the
   normalized source and verify that the merge fingerprint changes only because
   of the reviewed stock and atmosphere corrections.

## Follow-up Checks

- Re-run focused open-schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/methylomonas_medium_elbe.yaml` and the
  regenerated `data/merge_yaml/merged/methylomonas_medium_elbe.yaml`.
- Manually compare the regenerated record against DSMZ Medium 1653 and the
  MediaDive REST `1653` payload to ensure all four source solution additions
  remain volume-scoped to the final medium.
- Re-run the concentration-plausibility report or its narrow equivalent and
  confirm `bacterial/methylomonas_medium_elbe.yaml` no longer carries the
  Vitamin B12, `FeCl2 x 4 H2O`, or nicotinic-acid anomaly rows.
- Re-run the merge freshness/audit check that covers normalized inputs and
  `data/merge_yaml/merged/`.

## Additional Notes

The current `src/culturemech/import/mediadive_importer.py` path already contains
logic to skip stock additions while parsing primary MediaDive recipes and to
preserve those stock additions in a `solutions` block. This record should be
checked during any MediaDive reimport to ensure the fixed path can reproduce
DSMZ 1653 from a MediaDive API cache.

The schema validators prove that the flattened record is well-formed YAML; they
do not check the dimensional error caused by turning stock-strength grams per
liter into final-medium concentrations.

# YAML Record Review: Halorhabdus Utahensis Medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/halorhabdus_utahensis_medium__f8de5621.yaml`
- Started UTC: 2026-09-23T11:18:37Z
- Finished UTC: 2026-09-23T11:19:12Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:008961` |
| Name | `halorhabdus_utahensis_medium` |
| Original name | `Halorhabdus Utahensis Medium` |
| Category | `archaea` |
| Physical state | `LIQUID` |
| Generated from | `data/normalized_yaml/archaea/TOGO_M2377_Halorhabdus_Utahensis_Medium.yaml` |
| Source accession | `TOGO:M2377` |
| Original source | DSMZ Medium 927 |
| Merge fingerprint | `f8de56215cc17baaeda4fb47edbf20ab4b88d4b48b609d05a7d50b0e05025b11` |

I reviewed the generated merged record, its normalized Togo owner, the Togo
`M2377` API payload, the DSMZ Medium 927 PDF named by Togo, and the MediaDive
927 REST payload.

I searched `data/normalized_yaml` and `data/merge_yaml` YAML files with
`rg --no-ignore --hidden` for `halorhabdus_utahensis_medium`,
`HALORHABDUS UTAHENSIS MEDIUM`, `mediadive.medium:927`, `DSMZ Medium 927`, and
`DSMZ_Medium927`. Ignored files were included. The search found the reviewed
Togo branch, direct MediaDive/DSMZ and KOMODO sibling branches for DSMZ 927,
and the generated outputs for each branch; only
`TOGO_M2377_Halorhabdus_Utahensis_Medium.yaml` feeds this reviewed
fingerprint.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halorhabdus_utahensis_medium__f8de5621.yaml` exited 0 with no diagnostics. |
| Strict schema | Passed: `python scripts/validate_strict.py data/merge_yaml/merged/halorhabdus_utahensis_medium__f8de5621.yaml --out /private/tmp/halorhabdus_utahensis_medium_f8de5621.strict.tsv --workers 1 --quiet` exited 0 and wrote a header-only TSV. |
| References | Passed with no checked references: `linkml-reference-validator validate data data/merge_yaml/merged/halorhabdus_utahensis_medium__f8de5621.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported `Total checks: 0`. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/halorhabdus_utahensis_medium__f8de5621.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries. |

The `just` validator entrypoints were not used because this checkout attempts
to resolve a Python 3.13 environment with `llvmlite==0.46.0`; the focused
validators above were run offline with Python 3.11 against the local uv cache.

## Identity and Grounding

The record is the Togo `M2377` branch for DSMZ Medium 927, Halorhabdus
utahensis medium. The main NaCl, NaBr, `MgSO4 x 7 H2O`, KCl, NH4Cl,
`Tris-HCl`, glucose, and yeast extract quantities match the Togo payload and
DSMZ 927.

One stale grounding remains: the primary `MgSO4 x 7 H2O` term was corrected to
`CHEBI:31795`, but `mediaingredientmech_chebi_term` still points to generic
`CHEBI:32599` / magnesium sulfate.

## Evidence

Togo `M2377` parses four water-bearing DSMZ paragraphs: the 1 L main medium,
the 1 L phosphate stock, the 1 L calcium chloride stock, and the 1 L Fe/Mn
stock. Those four distinct `Distilled water` rows were merged into one
`4000.0 G_PER_L` row in the generated record, losing both volume units and
stock boundaries.

Togo also parses the three post-autoclave solution additions as 2.5 ml
phosphate solution, 0.5 ml calcium chloride solution, and 0.25 ml Fe/Mn
solution. The generated `solutions` entries preserve those labels but have
`name: Unknown solution`, empty compositions for two of the three stocks, and
`G_PER_L` units for ml additions. The phosphate, calcium chloride, MnCl2, and
FeCl2 stock recipe rows remain in top-level `ingredients` at their stock
strengths instead of living inside those solution records.

Togo carries DSMZ's preparation comment saying to adjust to pH 7.6 with 5 M
NaOH, autoclave, cool, and then add the three stock solutions. The generated
record turns NaOH into a variable ingredient but has no `ph_value` and no
structured `preparation_steps`.

DSMZ 927 and MediaDive 927 include an additional conditional instruction,
`For DSM 27208 add 2ml/l trace elements SL-7`, followed by the SL-7 recipe.
Togo `M2377` omits that whole conditional section, so this branch cannot yet
encode the DSM 27208 exception present in the original source PDF.

## Completeness

The generated record is missing pH 7.6, the post-autoclave stock addition
amounts in their source ml units, the contents of each separate stock solution,
and the preparation sequence that scopes NaOH to pH adjustment.

The Togo API does not include target organisms, growth evidence, incubation
temperature, or atmosphere. Their absence in the generated record is not a
defect. The DSM 27208-only SL-7 condition is a real original-source gap, not a
generic empty optional slot.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Four water rows from separate Togo paragraphs were merged into one `4000.0 G_PER_L` ingredient. | Togo has four distinct `Distilled water`, `1000 ml` rows for the main medium and the phosphate, calcium chloride, and Fe/Mn stocks. | `data/normalized_yaml/archaea/TOGO_M2377_Halorhabdus_Utahensis_Medium.yaml`, duplicate-ingredient cleanup, or the Togo importer |
| Major | Phosphate, calcium chloride, and Fe/Mn stock recipes were left as top-level ingredients while the solution references became empty `Unknown solution` stubs. | Togo has 2.5 ml, 0.5 ml, and 0.25 ml solution additions plus separate KH2PO4, CaCl2, MnCl2, and FeCl2 stock recipes; the generated record stores the stock formulas at main-medium scope and gives two migrated solutions empty `composition` arrays. | `data/normalized_yaml/archaea/TOGO_M2377_Halorhabdus_Utahensis_Medium.yaml` or `solution-migrator-v1.0` |
| Major | pH/preparation context was lost. | Togo's comment says to adjust to pH 7.6 with 5 M NaOH, autoclave, cool, and add the three stock solutions. The generated record has NaOH as a variable ingredient but has no `ph_value` or `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M2377_Halorhabdus_Utahensis_Medium.yaml` or the Togo comment importer |
| Major | The DSM 27208-only SL-7 trace element addition from DSMZ Medium 927 is absent. | The DSMZ PDF and MediaDive 927 both include `For DSM 27208 add 2ml/l trace elements SL-7`; Togo `M2377` stops before that section. | Togo import source coverage, then `data/normalized_yaml/archaea/TOGO_M2377_Halorhabdus_Utahensis_Medium.yaml` |
| Minor | `MgSO4 x 7 H2O` has a stale `mediaingredientmech_chebi_term`. | The row's primary term is the heptahydrate `CHEBI:31795`, but its MIM/CHEBI key is still generic `CHEBI:32599`. | MIM link refresh logic or the normalized Togo record |

## Recommended Edits

1. Preserve the main medium, phosphate stock, calcium chloride stock, and
   Fe/Mn stock as separate scopes in the Togo import or normalized record.
2. Move `KH2PO4`, `CaCl2 x 6 H2O`, `MnCl2 x 4 H2O`, and `FeCl2 x 4 H2O`
   into stock-solution compositions and keep the main-medium references at
   2.5 ml, 0.5 ml, and 0.25 ml.
3. Restore each stock's own 1000 ml water row instead of merging all water into
   the main ingredient list.
4. Import the Togo preparation comment as pH 7.6 adjustment with 5 M NaOH,
   autoclaving, cooling, and post-autoclave stock addition steps.
5. Decide whether the Togo branch should be backfilled from DSMZ 927 for the
   DSM 27208-only SL-7 section or explicitly flagged as missing that original
   source paragraph.
6. Refresh `mediaingredientmech_chebi_term` for `MgSO4 x 7 H2O` after the
   heptahydrate grounding change.
7. Regenerate merged recipes from the corrected normalized owner; do not patch
   `data/merge_yaml/merged/halorhabdus_utahensis_medium__f8de5621.yaml`
   directly.

## Follow-up Checks

1. Run `just validate data/normalized_yaml/archaea/TOGO_M2377_Halorhabdus_Utahensis_Medium.yaml`
   after the normalized Togo record or importer is corrected.
2. Run `just validate-terms data/normalized_yaml/archaea/TOGO_M2377_Halorhabdus_Utahensis_Medium.yaml`
   to confirm exact hydrated-salt and refreshed MIM/CHEBI grounding.
3. Run `just validate-media-variant-links` if the DSM 27208-only SL-7 addition
   is modeled as a variant.
4. Run `just verify-merges` to prove the generated Togo M2377 branch
   regenerates from the corrected normalized source.
5. Manually compare the regenerated record against the Togo `M2377` API and
   DSMZ Medium 927 to confirm water rows, stock-solution boundaries, ml
   addition volumes, pH, and the DSM 27208 conditional are scoped correctly.

## Additional Notes

The direct MediaDive/DSMZ and KOMODO DSMZ 927 branches should stay separate
from Togo `M2377` until curation can preserve equivalent stock-solution
structure and DSM 27208 conditional semantics across all three source paths.

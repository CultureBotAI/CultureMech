# YAML Record Review: LB (LURIA-BERTANI) AGAR WITH KANAMYCIN AND RIFAMPICIN

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_luria_bertani_agar_with_kanamycin_and_rifampicin__0472ff8f.yaml
- Started UTC: 2026-09-23T19:02:34Z
- Finished UTC: 2026-09-23T19:03:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002340 |
| Name | lb_luria_bertani_agar_with_kanamycin_and_rifampicin |
| Original name | LB (LURIA-BERTANI) AGAR WITH KANAMYCIN AND RIFAMPICIN |
| Category | bacterial |
| Physical state | SOLID_AGAR |
| Media grounding | mediadive.medium:J1168 |
| Source provenance | MediaDive J1168, sourced from JCM |
| Generated file | data/merge_yaml/merged/lb_luria_bertani_agar_with_kanamycin_and_rifampicin__0472ff8f.yaml |
| Maintained owner | data/normalized_yaml/bacterial/lb_luria_bertani_agar_with_kanamycin_and_rifampicin.yaml |
| Merge fingerprint | 0472ff8f8a0355d722af4a1cfb2c7a7734526c17758375bb6525e03b5f9cf59d |

The reviewed file is a generated merged copy of a single MediaDive import. Future fixes belong in the maintained normalized owner and then require regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lb_luria_bertani_agar_with_kanamycin_and_rifampicin__0472ff8f.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/lb_luria_bertani_agar_with_kanamycin_and_rifampicin__0472ff8f.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

MediaDive J1168 identifies the intended JCM medium named `LB (LURIA-BERTANI) AGAR WITH KANAMYCIN AND RIFAMPICIN`, records pH 7.0, and preserves the JCM source URL for `GRMD=1168`. The generated `CultureMech:002340` file preserves that identity through its name, bacterial category, `SOLID_AGAR` physical state, and `mediadive.medium:J1168` media term.

An ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found this generated record, its maintained MediaDive owner, the related `Main sol. J1168` solution import, archived validation rows, and the Togo M1250 normalized sibling that represents the same JCM formula through Togo Medium. The duplicate Togo and MediaDive source lineages are distinct at import time, but both ultimately point at JCM medium 1168.

## Evidence

Supported in the inspected MediaDive J1168 source:

- The medium identity, `mediadive.medium:J1168` grounding, original JCM link, pH 7.0, complex-medium classification, and JCM source provenance are supported.
- The main gram-per-liter ingredient amounts in the record are supported: 10 g/L Tryptone, 5 g/L Yeast extract, 10 g/L NaCl, 15 g/L Agar, 0.05 g/L Kanamycin sulfate, and 0.025 g/L Rifampicin.
- The ChEBI mappings for NaCl, agar, kanamycin sulfate, and rifampicin match the inspected ingredient names.
- The preparation steps preserve the source's pH adjustment and post-autoclave aseptic addition of filter-sterilized antibiotics.

Unsupported or incomplete relative to the inspected MediaDive source:

- MediaDive J1168 includes 1000 ml distilled water in the 1 L main solution; this row is absent from the generated record and its maintained owner.
- MediaDive carries the BD-Difco attributes on Tryptone and Yeast extract, `dissolved in distilled water` on Kanamycin sulfate, and `dissolved in methanol` on Rifampicin. The generated record drops all four attributes, so the rifampicin solvent requirement is no longer visible.
- MediaDive exposes the source as structured JSON, but the record stores only free-text JCM provenance in `notes` and has no structured `references` entry for the MediaDive J1168 REST record.

The embedded JCM URL, `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1168`, currently returns `Nothing found`, so it cannot independently confirm the formula today.

## Completeness

The record is mostly complete for source identity, principal non-water amounts, pH, antimicrobial amounts, and preparation timing. It is incomplete for the MediaDive water component, the source-disclosed vendor or solvent attributes, and structured recoverable references.

The separate normalized `data/normalized_yaml/bacterial/TOGO_M1250_LB_Luria-Bertani_Agar_With_Kanamycin_And_Rifampicin.yaml` record has already been repaired to include 1000 ml/L water and the same source attributes as notes. This direct MediaDive owner has not received the equivalent repair, so the two source lineages still cannot merge to one CultureMech record for the same JCM formula.

Empty optional organism, incubation, storage, and discussion fields are acceptable here; the source record is a medium recipe and does not assert one tested organism or incubation protocol.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The MediaDive J1168 import omits the 1000 ml distilled water row from the 1 L main solution. | The inspected MediaDive REST payload lists `Distilled water`, amount 1000, unit `ml`, in the same `Main sol. J1168` recipe as the six imported non-water ingredients. | `data/normalized_yaml/bacterial/lb_luria_bertani_agar_with_kanamycin_and_rifampicin.yaml` or the MediaDive medium importer |
| Major | The import drops source attributes that distinguish BD-Difco tryptone and yeast extract and the antibiotic solvents. | MediaDive J1168 records `BD-Difco` attributes on Tryptone and Yeast extract, `dissolved in distilled water` on Kanamycin sulfate, and `dissolved in methanol` on Rifampicin; the maintained owner has only the bare ingredient names. | `data/normalized_yaml/bacterial/lb_luria_bertani_agar_with_kanamycin_and_rifampicin.yaml` or the MediaDive medium importer |
| Minor | The record has no structured `references` entry for the inspected MediaDive J1168 endpoint. | Source provenance appears only in `notes`, and reference validation performed zero checks for this record. | `data/normalized_yaml/bacterial/lb_luria_bertani_agar_with_kanamycin_and_rifampicin.yaml` |

## Recommended Edits

1. Add the missing 1000 ml/L distilled water component to the maintained MediaDive owner, or fix the MediaDive medium importer if water rows are being filtered unintentionally across imported recipes.
2. Preserve MediaDive `attribute` values in ingredient notes or preferred terms for BD-Difco Tryptone, BD-Difco Yeast extract, Kanamycin sulfate dissolved in distilled water, and Rifampicin dissolved in methanol.
3. Add a structured reference for `https://mediadive.dsmz.de/rest/medium/J1168`; keep the now-dead JCM GRMD URL as original-source provenance rather than the only recoverable formulation pointer.
4. After normalizing these details, check whether the direct MediaDive J1168 record and the repaired Togo M1250 import should now merge to a single generated CultureMech record for the JCM 1168 formula.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on `data/merge_yaml/merged/lb_luria_bertani_agar_with_kanamycin_and_rifampicin__0472ff8f.yaml` after editing the maintained MediaDive owner and regenerating merged YAML.
- Manually compare the regenerated ingredients against MediaDive J1168 and confirm that all seven MediaDive recipe rows and four `attribute` values are still represented.
- Re-run a gitignore-independent search for `mediadive.medium:J1168`, `TOGO:M1250`, and `JCM_M1168` after regeneration to confirm whether the duplicate JCM formula is still represented by two generated records or has merged.

## Additional Notes

MediaDive also generated `data/normalized_yaml/bacterial/mediadive_5278_Main_sol_J1168.yaml` for the underlying main solution. That solution record has additional issues, including `1000 PERCENT_V_V` for distilled water and a placeholder `ingredients` row, but it is a separate `SolutionRecipe` input and not the owner of this reviewed medium record.

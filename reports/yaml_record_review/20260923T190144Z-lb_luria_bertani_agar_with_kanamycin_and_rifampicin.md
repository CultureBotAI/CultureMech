# YAML Record Review: LB (Luria-Bertani) Agar With Kanamycin And Rifampicin

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_luria_bertani_agar_with_kanamycin_and_rifampicin.yaml
- Started UTC: 2026-09-23T18:59:20Z
- Finished UTC: 2026-09-23T19:01:44Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007781 |
| Name | lb_luria_bertani_agar_with_kanamycin_and_rifampicin |
| Original name | LB (Luria-Bertani) Agar With Kanamycin And Rifampicin |
| Category | bacterial |
| Physical state | SOLID_AGAR |
| Media grounding | TOGO:M1250 |
| Source provenance | Togo Medium M1250 imported from JCM_M1168 / GRMD=1168 |
| Generated file | data/merge_yaml/merged/lb_luria_bertani_agar_with_kanamycin_and_rifampicin.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M1250_LB_Luria-Bertani_Agar_With_Kanamycin_And_Rifampicin.yaml |
| Merge fingerprint | 9161f654e8d9c8431d424c4ce35c76ee7e654b3bbbc27cc46450b9c250445e5f |

The reviewed target is the generated merged copy. Future fixes belong in the maintained normalized Togo M1250 source above, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lb_luria_bertani_agar_with_kanamycin_and_rifampicin.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/lb_luria_bertani_agar_with_kanamycin_and_rifampicin.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

Togo Medium M1250 identifies `LB (Luria-Bertani) Agar With Kanamycin And Rifampicin`, gives the original media ID as `JCM_M1168`, records pH 7.0, and lists the expected LB agar base plus 50 mg kanamycin sulfate and 25 mg rifampicin in a second component group. MediaDive J1168 agrees on the JCM identity, medium name, pH 7.0, 1 L main solution, base ingredients, antibiotic identities, antibiotic amounts, and filter-sterilized aseptic post-autoclave antibiotic addition.

The `CultureMech:007781` identity, name, bacterial category, `SOLID_AGAR` state, and `TOGO:M1250` grounding therefore all point to the intended JCM-derived medium. No sibling or similarly named variant was conflated in the generated record; the sibling direct-JCM normalized import is a separate input with a generated sibling `lb_luria_bertani_agar_with_kanamycin_and_rifampicin__0472ff8f.yaml`.

## Evidence

Supported in the inspected Togo and MediaDive sources:

- The medium label and Togo grounding are supported by Togo M1250.
- The `JCM_M1168` provenance is supported by Togo M1250 and by MediaDive J1168's `J1168` record sourced from JCM.
- The LB agar base ingredients are supported by MediaDive J1168: 10 g/L Tryptone with the BD-Difco attribute, 5 g/L Yeast extract with the BD-Difco attribute, 10 g/L NaCl, 15 g/L Agar, and 1000 ml distilled water in a 1 L main solution.
- The antibiotic identities and source amounts are supported by Togo M1250 and MediaDive J1168: 50 mg kanamycin sulfate dissolved in distilled water and 25 mg rifampicin dissolved in methanol.
- The source pH and preparation boundary are supported by MediaDive J1168: adjust to pH 7.0, then after autoclaving aseptically add the filter-sterilized antibiotic stocks.

Unsupported or stale in the generated record:

- `Distilled water` is represented as `1 G_PER_L`, but the inspected sources encode a 1 L / 1000 ml water quantity, not 1 g of water per liter.
- `Kanamycin sulfate (dissolved in distilled water)` is represented as `50 G_PER_L`, but the sources encode 50 mg per liter, equivalent to 0.05 g/L.
- `Rifampicin (dissolved in methanol)` is represented as `25 G_PER_L`, but the sources encode 25 mg per liter, equivalent to 0.025 g/L.
- The generated record omits the pH 7.0 and the filter-sterilized post-autoclave antibiotic addition instructions, both of which are represented in MediaDive J1168 and already restored in the maintained normalized owner.

The record's embedded original JCM URL, `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1168`, was also inspected and currently returns `Nothing found`; the JCM identity is recoverable through Togo and MediaDive, but this direct source URL is no longer independently useful evidence.

## Completeness

The generated merged record is materially incomplete because it omits pH and preparation steps that a user needs to reproduce the source recipe. Its `references` collection is also absent, so the generated copy only carries source URLs as free-text `notes`.

The maintained normalized owner already contains the September 2026 repair for the large unit defects, pH 7.0, filter-sterilized post-autoclave antibiotic additions, ChEBI mappings for kanamycin sulfate and rifampicin, data quality flags, and Togo / MediaDive references. The generated review target was last merged in August 2026 and has not incorporated that maintained repair.

An ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:007781`, `TOGO:M1250`, `JCM_M1168`, `GRMD=1168`, the Togo M1250 slug, and the merge fingerprint found the generated target, its maintained Togo owner, the direct-JCM sibling import, index rows, and archived validation rows. No additional maintained overlay or unresolved duplicate owner for this exact `TOGO:M1250` record was found in those searched paths.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The generated record is stale and still carries three severe unit errors: water as `1 G_PER_L`, kanamycin sulfate as `50 G_PER_L`, and rifampicin as `25 G_PER_L`. | Togo M1250 encodes 1 L distilled water, 50 mg kanamycin sulfate, and 25 mg rifampicin. MediaDive J1168 encodes 1000 ml distilled water, 50 mg kanamycin sulfate with `g_l: 0.05`, and 25 mg rifampicin with `g_l: 0.025`. The maintained normalized owner has already converted these to `1000 ML_PER_L`, `0.05 G_PER_L`, and `0.025 G_PER_L`. | `data/merge_yaml/merged/` regeneration from `data/normalized_yaml/bacterial/TOGO_M1250_LB_Luria-Bertani_Agar_With_Kanamycin_And_Rifampicin.yaml` |
| Major | The generated record omits pH 7.0 and the aseptic, filter-sterilized, post-autoclave antibiotic addition step. | MediaDive J1168 records pH 7.0 and the post-autoclave filter-sterilized antibiotic addition. The maintained normalized owner already includes `ph_value: 7.0` and two preparation steps that preserve this preparation boundary. | `data/merge_yaml/merged/` regeneration from `data/normalized_yaml/bacterial/TOGO_M1250_LB_Luria-Bertani_Agar_With_Kanamycin_And_Rifampicin.yaml` |
| Minor | The maintained owner still stores the original JCM GRMD URL only in free-text notes, not as a structured reference. | The generated record's notes include the Togo and JCM URLs but have no structured `references`. The maintained owner adds Togo and MediaDive REST references but omits the direct JCM URL, which currently returns `Nothing found`. | `data/normalized_yaml/bacterial/TOGO_M1250_LB_Luria-Bertani_Agar_With_Kanamycin_And_Rifampicin.yaml` |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` from the maintained normalized corpus so `lb_luria_bertani_agar_with_kanamycin_and_rifampicin.yaml` receives the September 2026 Togo M1250 repair.
2. Regenerate downstream pages and indexes from the refreshed merged YAML so the stale `1 G_PER_L`, `50 G_PER_L`, and `25 G_PER_L` values are no longer published for CultureMech:007781.
3. Consider whether the original JCM GRMD URL should be retained as a structured historical reference, a source-data field, or just a note now that the URL returns no recipe.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on `data/merge_yaml/merged/lb_luria_bertani_agar_with_kanamycin_and_rifampicin.yaml` after regeneration.
- Manually inspect the regenerated YAML to confirm it contains `ph_value: 7.0`, 1000 ml/L water, 0.05 g/L kanamycin sulfate, 0.025 g/L rifampicin, Togo and MediaDive references, and the filter-sterilized post-autoclave antibiotic preparation step.
- Re-query Togo M1250 and MediaDive J1168 only if the maintained normalized repair is edited again; the current local owner already matches both inspected sources for the material recipe quantities.

## Additional Notes

The generated record passed all focused structural validators despite the source-level unit errors, because the bad values are syntactically and schema-valid. This review therefore depends on source inspection rather than validation alone.

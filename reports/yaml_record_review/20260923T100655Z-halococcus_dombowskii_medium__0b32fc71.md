# YAML Record Review: halococcus_dombowskii_medium__0b32fc71

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halococcus_dombowskii_medium__0b32fc71.yaml`
- Started UTC: 2026-09-23T10:06:55Z
- Finished UTC: 2026-09-23T10:08:42Z
- Verdict: needs curation

## Target

Generated merged YAML for the direct MediaDive/JCM `J402` import of `HALOCOCCUS DOMBOWSKII MEDIUM`, assigned `CultureMech:002758`.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed; `/private/tmp/halococcus_dombowskii_medium__0b32fc71.strict.tsv` contained only the header row.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches direct MediaDive medium `J402`, source `JCM`, and the JCM page for medium 402.
- A gitignore-independent exact search in `data/merge_yaml` and `data/normalized_yaml` found three sibling TOGO imports, `TOGO:M398`, `TOGO:M399`, and `TOGO:M400`, all pointing back to the same JCM 402 URL.
- The hydrated salts are grounded to the correct hydrate-sensitive CHEBI terms for magnesium dichloride hexahydrate and calcium chloride dihydrate.
- `Casamino acids` remains ungrounded, which is appropriate for a mixture with no single precise CHEBI identity.

## Evidence

- The generated concentrations for Casamino acids, Yeast extract, Tris base, KCl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, and NaCl match the JCM table and the MediaDive `J402` REST payload.
- The scalar pH value of 7.4 matches JCM and MediaDive.
- The generated preparation text matches MediaDive/JCM comments, but it flattens the conditional solid-medium and strain-specific sea-salt comments into ordinary `MIX` steps on a liquid recipe.

## Completeness

- Missing ingredient: distilled water is present in the source preparation instruction as the solvent brought to a final volume of 1.0 L, but the direct MediaDive record has no explicit water ingredient.
- Missing qualifier: JCM specifies `Casamino acids (BD-Difco)` and MediaDive carries `attribute: BD-Difco`; the generated ingredient is only `Casamino acids`.
- Missing variant structure: the JCM agar and sea-salt notes are represented by TOGO as M399 and M400 sibling variants, but the direct JCM import retains both as unscoped notes under the liquid base recipe instead of linking or modelling the variants.

## Findings

1. Conditional variant instructions are encoded as unconditional liquid-recipe preparation steps. The generated step 3 says to add 20.0 g/L agar for solid medium and step 4 says to supplement with 10.0 g/L sea salts for JCM 19729, even though the record is `LIQUID` and those are alternate solid or strain-specific variants rather than required base-medium operations.
2. The recipe omits distilled water. JCM instructs curators to add components to distilled water and bring volume to 1.0 L, and the TOGO base record parses that solvent explicitly; the generated direct JCM record only leaves it as prose.
3. The `Casamino acids` ingredient lost the BD-Difco product qualifier present in both the JCM ingredient text and MediaDive's `attribute`.

## Recommended Edits

- Keep this record as the JCM 402 liquid base recipe, but convert the agar and sea-salt comments into scoped variant relations or notes rather than unconditional `MIX` steps.
- Add explicit distilled water using the correct solvent/final-volume representation; do not copy TOGO's current `1 G_PER_L` water artifact literally.
- Restore the `BD-Difco` qualifier on Casamino acids.
- Reconcile the direct JCM liquid record with `TOGO:M398`, and connect the solid agar and sea-salt forms with `TOGO:M399` and `TOGO:M400` so one JCM page does not remain split across unrelated CultureMech records.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Verify that curated variant links preserve one base liquid form, one solid agar form with 20.0 g/L agar, and the JCM 19729 sea-salts variant without forcing either optional addition into every JCM 402 recipe.
- Re-run exact duplicate checks for `mediadive.medium:J402`, `TOGO:M398`, `TOGO:M399`, and `TOGO:M400`.

## Additional Notes

- Empty optional fields were not treated as defects.
- The sibling-record search used `rg --no-ignore --hidden`, so ignored files were included.

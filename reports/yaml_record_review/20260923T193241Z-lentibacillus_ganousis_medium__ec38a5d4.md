# YAML Record Review: Lentibacillus Ganousis Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lentibacillus_ganousis_medium__ec38a5d4.yaml
- Started UTC: 2026-09-23T19:31:24Z
- Finished UTC: 2026-09-23T19:32:41Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009831 |
| Name | lentibacillus_ganousis_medium |
| Original name | Lentibacillus Ganousis Medium |
| Category | bacterial |
| Physical state | SOLID_AGAR |
| Media grounding | TOGO:M445 |
| Source provenance | Togo M445 imported from JCM_M444-2 |
| Generated file | data/merge_yaml/merged/lentibacillus_ganousis_medium__ec38a5d4.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M445_Lentibacillus_Ganousis_Medium.yaml |
| Merge fingerprint | ec38a5d41c77bd7df05df85dbbef58750a710ea47a28cad82a52b4b33028410a |

The reviewed target is a generated one-source merge for Togo's solid-agar extraction of JCM 444. Future fixes belong in the maintained Togo M445 normalized owner, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lentibacillus_ganousis_medium__ec38a5d4.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/lentibacillus_ganousis_medium__ec38a5d4.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

Togo M445 is a solid-agar variant parsed from the JCM 444 Lentibacillus ganousis medium page. Its 20 g/L agar row and `SOLID_AGAR` physical state reflect the JCM instruction to add agar for solid medium.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:009831`, `TOGO:M445`, `JCM_M444-2`, `GRMD=444`, the maintained filename, the shared slug, and the merge fingerprint found this generated record, its maintained owner, the MediaDive J444 owner, the Togo M444 liquid owner, generated siblings for those liquid records, and source indexes. Togo M445 should stay distinct from the liquid J444/M444 recipe but should be explicitly linked as its solid variant.

## Evidence

Supported in the inspected JCM and Togo sources:

- The Togo M445 identity as an agar-containing variant of JCM 444 is supported.
- The solid variant contains the JCM 444 base salts and nutrients plus 20 g/L agar.
- The supported source quantities are 5 g/L proteose peptone no. 3, 10 g/L yeast extract, 1 g/L glucose, 100 g/L NaCl, 2 g/L KCl, 1 g/L MgSO4 x 7 H2O, 0.36 g/L CaCl2 x 2 H2O, 0.23 g/L NaBr, 0.06 g/L NaHCO3, 0.2 mg/L FeCl2 x 4 H2O, and 20 g/L agar.
- The liquid base is adjusted to pH 7.2 on the JCM page that supplies this solid-agar variant.

Unsupported or incomplete in the generated record:

- FeCl2 x 4 H2O is represented as `0.2 G_PER_L` even though JCM lists 0.2 mg/L.
- Distilled water is represented as `1 G_PER_L` instead of the one-liter solvent volume parsed by Togo.
- The JCM pH 7.2 endpoint and preparation text are absent.
- The record is not linked to the MediaDive J444 or Togo M444 liquid base record.
- The record has no structured references for Togo M445 or JCM 444.

## Completeness

The record preserves the solid-agar variant identity, the agar addition, and every base-formula component, but it is incomplete for water and trace-iron units, pH/preparation context, liquid-base variant linkage, and structured references.

Empty optional organism, incubation, storage, and sterilization fields are acceptable for this review because the inspected JCM and Togo entries do not provide those details.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Ferrous chloride tetrahydrate is off by a factor of 1000. | JCM 444 lists FeCl2 x 4 H2O as 0.2 mg; the Togo-derived YAML stores `0.2 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M445_Lentibacillus_Ganousis_Medium.yaml` or the Togo importer |
| Major | The solvent water row uses a mass unit. | Togo M445 parses distilled water as 1 L; the YAML stores `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M445_Lentibacillus_Ganousis_Medium.yaml` or the Togo importer |
| Major | pH and preparation context are missing. | JCM 444 specifies pH 7.2 and gives the same base-medium preparation text used by MediaDive J444, while the generated Togo M445 record has no `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M445_Lentibacillus_Ganousis_Medium.yaml` |
| Minor | The solid variant is not linked to its liquid base. | MediaDive J444 and Togo M444 represent the liquid base on the same JCM page; Togo M445 represents the 20 g/L agar variant but has no structured relation to them. | `data/normalized_yaml/bacterial/TOGO_M445_Lentibacillus_Ganousis_Medium.yaml` |
| Minor | Structured references are missing. | The generated reference validator performed zero checks despite available Togo and JCM source URLs. | `data/normalized_yaml/bacterial/TOGO_M445_Lentibacillus_Ganousis_Medium.yaml` |

## Recommended Edits

1. Correct FeCl2 x 4 H2O to 0.2 mg/L in the maintained Togo M445 owner.
2. Convert distilled water to a volume quantity or remove the solvent row if water is intentionally represented only in preparation text.
3. Add the pH 7.2 endpoint and the JCM preparation text.
4. Link Togo M445 as the solid-agar variant of the MediaDive J444 or Togo M444 liquid base.
5. Add structured references for Togo M445 and JCM 444.
6. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated formula against JCM 444 for 0.2 mg/L FeCl2 x 4 H2O, 20 g/L agar, and pH 7.2.
- Re-run an ignored-inclusive exact search for `TOGO:M445`, `TOGO:M444`, and `mediadive.medium:J444` to confirm that the agar variant is linked to the liquid base rather than collapsed into it.

## Additional Notes

The Togo M444 liquid import has the same water-unit and trace-iron scaling risks but lacks agar; it should be repaired or merged with the MediaDive J444 liquid recipe separately.

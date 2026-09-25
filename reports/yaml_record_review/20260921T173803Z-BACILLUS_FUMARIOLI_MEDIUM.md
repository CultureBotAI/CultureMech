# YAML Record Review: BACILLUS FUMARIOLI MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_FUMARIOLI_MEDIUM.yaml
- Started UTC: 2026-09-21T17:36:35Z
- Finished UTC: 2026-09-21T17:38:03Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:010022 |
| Generated record | data/merge_yaml/merged/BACILLUS_FUMARIOLI_MEDIUM.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M622_Bacillus_Fumarioli_Medium.yaml |
| Label | Bacillus Fumarioli Medium |
| Source identity | TOGO M622, imported from JCM_M614 |
| Merge state | Single-source merge from `TOGO_M622_Bacillus_Fumarioli_Medium` |

The generated target and normalized owner have the same scientific content, so
future formulation fixes belong in
`data/normalized_yaml/bacterial/TOGO_M622_Bacillus_Fumarioli_Medium.yaml` or
the TOGO import path before regenerating merge products.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_FUMARIOLI_MEDIUM.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_FUMARIOLI_MEDIUM.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails during
Python 3.13 dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **Medium identity is correct.** The record's label, `media_term`, TOGO M622
  accession, original source note, and JCM GRMD=614 URL all point to JCM 614
  BACILLUS FUMARIOLI MEDIUM.
- **The category and solid state are supported.** The record is a bacterial
  `MediaRecipe`, and the source contains 18 g agar in 1 L medium.
- **Most chemical groundings preserve the displayed ingredient identity.**
  MgSO4.7H2O, CaCl2.2H2O, KH2PO4, ammonium sulfate, agar, and water are
  grounded to compatible CHEBI terms. MnSO4.xH2O is grounded to anhydrous
  manganese(II) sulfate, which does not preserve the source's variable hydrate
  notation exactly.

## Evidence

- TOGO M622 resolves to Bacillus Fumarioli Medium, original media ID
  `JCM_M614`, and source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=614`.
  The original JCM page is also GRMD=614 / BACILLUS FUMARIOLI MEDIUM.
- TOGO M622 and JCM 614 list the same one-scope formulation: 1 L distilled
  water, yeast extract 4 g, ammonium sulfate 2.5 g, KH2PO4 3 g,
  MgSO4.7H2O 0.2 g, CaCl2.2H2O 0.25 g, MnSO4.xH2O 5 mg, and agar 18 g.
- The generated record keeps all gram-scale ingredients at the correct numeric
  values and uses `SOLID_AGAR`, but the MnSO4.xH2O row is `5 G_PER_L` instead
  of the source's 5 mg/L-equivalent row.
- TOGO M622 and JCM 614 both report pH 5.5. The generated record does not carry
  a structured pH or preparation note.

## Completeness

- The pH 5.5 adjustment is missing.
- The 5 mg manganese sulfate hydrate source amount was imported as 5 g/L.
- `target_organisms`, growth metrics, incubation temperature, salinity, and
  light are empty. The inspected TOGO and JCM sources do not supply those
  claims, so I did not count them as defects.
- A gitignore-independent search of `reports/yaml_record_review` for
  `BACILLUS_FUMARIOLI_MEDIUM` and `BACILLUS FUMARIOLI MEDIUM` found no prior
  report before this file was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | MnSO4.xH2O is 1000x too high because a milligram source row was normalized as grams per liter. | TOGO M622 and JCM 614 list `MnSO4.xH2O` as 5 mg in the 1 L medium; the record stores `5 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M622_Bacillus_Fumarioli_Medium.yaml`; TOGO unit conversion. |
| Major | pH 5.5 was dropped. | TOGO M622 has `ph: "5.5"` and the original JCM page instructs adjusting pH to 5.5, but the record has no pH or preparation field. | `data/normalized_yaml/bacterial/TOGO_M622_Bacillus_Fumarioli_Medium.yaml`; TOGO pH/comment import. |
| Minor | MnSO4.xH2O is grounded as anhydrous manganese(II) sulfate. | The source intentionally leaves hydration as `xH2O`; the record uses `CHEBI:86360`, whose label is manganese(II) sulfate. | `data/normalized_yaml/bacterial/TOGO_M622_Bacillus_Fumarioli_Medium.yaml`; MIM/CHEBI grounding. |
| Minor | Source evidence is encoded only as a note. | The TOGO and original JCM URLs appear in free text, but there is no structured reference or evidence tying ingredient rows to TOGO M622/JCM GRMD=614. | `data/normalized_yaml/bacterial/TOGO_M622_Bacillus_Fumarioli_Medium.yaml` or the TOGO importer. |

## Recommended Edits

1. Convert the TOGO `5 mg` MnSO4.xH2O row to `0.005 G_PER_L` or an equivalent
   milligram unit representation, not `5 G_PER_L`.
2. Preserve pH 5.5 from TOGO/JCM in the normalized owner.
3. Re-ground `MnSO4.xH2O` to an exact variable-hydrate term if one is available;
   otherwise remove the anhydrous manganese sulfate grounding until the hydrate
   scope can be represented.
4. Add structured source provenance for TOGO M622 and original JCM GRMD=614.
5. Regenerate merged products after the normalized owner is repaired.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the maintained TOGO
  owner after unit, pH, term, and provenance edits.
- Regenerate merges and verify the generated `BACILLUS_FUMARIOLI_MEDIUM.yaml`
  carries `0.005 G_PER_L` or a semantically equivalent value for MnSO4.xH2O and
  no longer drops pH 5.5.
- Compare the regenerated record manually against JCM GRMD=614, focusing on
  the MnSO4.xH2O `mg` unit and pH line.

## Additional Notes

- The exact prior-report searches used `find` and `rg --no-ignore --hidden`, so
  ignored review reports were included.

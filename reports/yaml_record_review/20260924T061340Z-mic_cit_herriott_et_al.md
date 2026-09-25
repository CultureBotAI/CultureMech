# YAML Record Review: Mic-Cit; Herriott et al

- Repository: CultureMech
- Record: `data/merge_yaml/merged/mic_cit_herriott_et_al.yaml`
- Started UTC: 2026-09-24T06:13:40Z
- Finished UTC: 2026-09-24T06:13:40Z
- Verdict: needs curation

## Target

- Reviewed merged record `data/merge_yaml/merged/mic_cit_herriott_et_al.yaml`.
- Editable normalized source: `data/normalized_yaml/bacterial/mic_cit_herriott_et_al.yaml`.
- MediaDB medium: `MEDIADB:282`, Mic-Cit; Herriott et al.
- MediaDB source page: Herriott et al., 1969, Journal Of Bacteriology.

## Validation

- LinkML open-schema validation: passed; exited 0 with no diagnostics.
- Strict validation: passed with 0 errors; `validate_strict.py` scanned 1 file and produced only the TSV header.
- Reference validation: passed; 1 file, 0 checks.
- Term validation: passed.
- Embedded history: Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The MediaDB identity is coherent: MediaDB medium 282 is `Mic-cit; herriott et al`, has 29 compounds, links source 94, and reports one growth-data record for *Haemophilus influenzae* Rd.
- MediaDB source 94 resolves to Herriott et al. 1969, Journal Of Bacteriology, `Defined nongrowth media for stage ii development of competence in haemophilus influenzae`, PubMed 5308771.
- The generated record's first ingredient has `preferred_term: ''` and no term, although MediaDB row 1 is `NAD+` at 0.00603 mM with KEGG `C00003` and CHEBI `15846`.
- The normalized source already fixes the blank first ingredient as `NAD+`, `CHEBI:15846`, with notes explaining restoration from MediaDB compound row `C00003`. It also grounds `L-Aspartate` to `CHEBI:29991`, while the generated YAML still has that ingredient ungrounded.

## Evidence

- The MediaDB tab-delimited export lists the same 29 compound amounts as the generated record, including `L-Glutamate` 8.83572 mM, glycerol 32.5768 mM, sodium chloride 99.2471 mM, sodium L-lactate 7.13903 mM, and hemin 0.01534 mM.
- The MediaDB HTML page lists the same 29 compounds and links the formulation to `Herriott et al, 1969`.
- The normalized source contains an August 2026 `fix_mediadb_leading_compounds.py` curation event restoring the MediaDB leading compound to `NAD+`; that event is absent from the generated merged record.

## Completeness

- Ingredient coverage is complete relative to MediaDB medium 282 after the normalized `NAD+` repair.
- Growth organism and literature provenance are only free-text/import-history context in the YAML; the medium page explicitly links *Haemophilus influenzae* Rd and Herriott et al. 1969.
- The three preparation steps in the YAML are generic MediaDB defaults. MediaDB does not provide these steps on the medium page or tab-delimited composition page.

## Findings

- The generated file is stale relative to `data/normalized_yaml/bacterial/mic_cit_herriott_et_al.yaml` and still publishes the former empty first ingredient instead of `NAD+`.
- The generated file is missing the normalized source's repaired `L-Aspartate` term.
- MediaDB provenance is under-specified. `notes` point only to the MediaDB landing page, and the YAML does not carry the exact medium, tab-delimited export, source 94, or PubMed 5308771 URLs as structured references.
- The generic dissolve, optional pH-adjustment, and 0.22 um filter-sterilization steps are not directly evidenced by the MediaDB entry.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/mic_cit_herriott_et_al.yaml` from `data/normalized_yaml/bacterial/mic_cit_herriott_et_al.yaml`.
- Confirm regeneration restores `NAD+` as the first ingredient and applies the `L-Aspartate` grounding.
- Add exact MediaDB medium/source/PubMed references to the normalized source if structured references are expected for MediaDB imports.
- Revisit the generic preparation defaults and either source them to an external protocol or remove them from MediaDB-only records where MediaDB provides composition but no recipe instructions.

## Follow-up Checks

- Re-run focused open-schema, strict, reference, and term validators for `data/merge_yaml/merged/mic_cit_herriott_et_al.yaml`.
- Compare the regenerated ingredient list against `https://mediadb.systemsbiology.net/defined_media/media_text/282/` and verify all 29 row labels are non-empty.
- Verify the first generated ingredient is `NAD+` at 0.00603 mM with `CHEBI:15846`.

## Additional Notes

- Empty optional fields were not treated as defects.

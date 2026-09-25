# YAML Record Review: modified_vogel_medium_maltose
- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_vogel_medium_maltose.yaml
- Started UTC: 2026-09-24T13:40:24Z
- Finished UTC: 2026-09-24T13:41:48Z
- Verdict: needs curation

## Target
Generated merged YAML for `modified_vogel_medium_maltose`, CultureMech ID `CultureMech:007245`.

- Reviewed generated record: `data/merge_yaml/merged/modified_vogel_medium_maltose.yaml`
- Reviewed normalized source: `data/normalized_yaml/bacterial/modified_vogel_medium_maltose.yaml`
- Media term: `MEDIADB:344`, `Modified Vogel Medium (maltose)`
- Source: MediaDB medium `344`
- Merge fingerprint: `c3aad0e3dd54874f784642cd86278df7861e563b1966d74fda90bae608c76115`
- `merged_from`: `modified_vogel_medium_maltose`

## Validation
- Open LinkML validation: Passed, `No issues found`.
- Strict validation: Passed with 0 error rows across 1 file. The strict TSV had 1 line, the header only.
- LinkML reference validation: Passed; 1 file validated, 0 checks, all validations passed.
- LinkML term validation: Passed; emitted the known `eutils`/`pkg_resources` deprecation warning and exited 0.
- Embedded `curation_history`: Not checked; the available history validator targets standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding
Live MediaDB medium `344` is `Modified vogel medium (maltose)` and lists the same 14 compounds and millimolar concentrations as the generated YAML. The chemical formula itself is therefore source-faithful at the MediaDB level.

The category is not source-faithful. MediaDB links this formula to `Aspergillus niger AB1.13`, so a `bacterial` category is wrong for this fungal growth record.

Grounding is partial. Seven ingredients have `mediaingredientmech_chebi_term` links; several have only `term` mappings; `Ferrous ammonium sulfate` is ungrounded.

## Evidence
Live MediaDB medium `344` resolves, labels the medium `Modified vogel medium (maltose)`, marks it as minimal, lists exactly 14 compounds, and links one organism: `Aspergillus niger AB1.13`.

The MediaDB 344 page links one literature source: source `119`, `Lu x et al, 2010`. That MediaDB source page identifies the title `The intra- and extracellular proteome of Aspergillus niger growing on defined medium with xylose or maltose as carbon substrate.`, journal `Microbial Cell Factories`, year 2010, and PubMed ID `20406453`.

The normalized owner was repaired on 2026-08-31 to restore `Modified Vogel Medium (maltose)` after a MediaDB SQL parse bug truncated names at parentheses. The reviewed generated artifact was emitted on 2026-08-06 and still has `'''Modified Vogel Medium (maltose` in `original_name` and `media_term.term.label`.

## Completeness
The compound table is complete for MediaDB 344. Target organism and source-specific literature provenance are not.

The generated preparation steps are generic importer guesses. MediaDB 344 exposes concentrations, organism, source, and growth-data links but does not support `Adjust pH if specified in original formulation` or `Sterilize by filtration (0.22 um) to preserve heat-sensitive components`.

## Findings
1. Needs curation - `category: bacterial` conflicts with the live MediaDB organism, `Aspergillus niger AB1.13`. The record should be fungal or otherwise aligned with the Aspergillus target.

2. Needs curation - the generated artifact is stale relative to the 2026-08-31 normalized repair. `original_name` and `media_term.term.label` still contain the parenthesis-truncated MediaDB import string.

3. Minor - source provenance points at the MediaDB root and the generic Mazumdar et al. MediaDB paper, not MediaDB medium 344 and source 119, Lu X et al. 2010.

4. Minor - preparation steps 2 and 3 are unsupported generic text. No pH value or filter-sterilization instruction is exposed on the MediaDB 344 page.

5. Minor - `Ferrous ammonium sulfate` has no structured ontology grounding.

## Recommended Edits
- Move the normalized record out of `data/normalized_yaml/bacterial` or set its category to fungal in whatever owner file is correct for `Aspergillus niger AB1.13`.
- Regenerate the merged artifact so the repaired `Modified Vogel Medium (maltose)` label is emitted.
- Add source-specific MediaDB references for medium `344`, source `119`, and PubMed `20406453`; keep Mazumdar et al. only as database provenance if desired.
- Remove unsupported generic pH-adjustment and filter-sterilization steps unless Lu X et al. 2010 explicitly supports them.
- Ground `Ferrous ammonium sulfate` or leave an explicit curation note that the source salt hydration or oxidation state is unresolved.

## Follow-up Checks
- Re-fetch MediaDB medium `344` and source `119` and confirm the regenerated record still has all 14 concentrations unchanged.
- Confirm that `category` and any path/index updates no longer classify this Aspergillus medium as bacterial.
- Revalidate the regenerated YAML with open LinkML, strict schema, reference, and term validators.

## Additional Notes
An exact local search including ignored files found an existing manifest entry that already carries the repaired `Modified Vogel Medium (maltose)` label, confirming that the generated YAML is older than the local name repair.

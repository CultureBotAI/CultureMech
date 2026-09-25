# YAML Record Review: deferrated_synbase_simpson_et_al

- Repository: CultureMech
- Record: data/merge_yaml/merged/deferrated_synbase_simpson_et_al.yaml
- Started UTC: 2026-09-22T13:58:17Z
- Finished UTC: 2026-09-22T14:01:44Z
- Verdict: needs curation

## Target

Reviewed generated record `data/merge_yaml/merged/deferrated_synbase_simpson_et_al.yaml` with generated identifier `CultureMech:007064`, media term `MEDIADB:173`, original name `Deferrated synbase; simpson et al`, category `bacterial`, and one merged source, `deferrated_synbase_simpson_et_al`.

## Validation

- LinkML open-schema validation: passed.
- Strict validation: passed with 0 error rows in `/private/tmp/deferrated_synbase_simpson_et_al.strict.tsv`.
- Reference validation: passed with 0 references checked.
- Term validation: passed.
- Embedded curation history: not checked; `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` blocks.

## Identity and Grounding

MediaDB medium 173 is `Deferrated synbase; simpson et al` and lists the same ten millimolar compound rows as the generated YAML: ammonium chloride, Cl-, dibasic sodium phosphate, Fe3+, glycerol, magnesium chloride, manganese chloride, potassium dibasic phosphate, sodium succinate, and sodium sulfate.

The per-medium MediaDB page links the formulation to organism `Vibrio vulnificus C7184`, source 65 `Simpson et al, 1983`, and growth data 358. The source page identifies the source article as `Siderophore production by vibrio vulnificus` in *Infection And Immunity* and links PMID 6223882; the growth-data page reports growth rate 0.142541 1/h at 37.0 C.

An exact gitignore-independent search for `MEDIADB:173`, `deferrated_synbase_simpson_et_al`, and `Deferrated synbase; simpson et al` across normalized YAML, merged YAML, and prior YAML record reviews found only the maintained source and this generated target for MediaDB medium 173.

## Evidence

The MediaDB tab-delimited export for medium 173 exactly supports the generated numeric amounts and MediaDB compound names. It also shows source-specific chemical cross-references: for example, magnesium chloride is MediaDB compound 6286 with KEGG `C07755`, PubChem `5360315`, and CHEBI `6636`.

## Completeness

The generated record is complete for the ten mM concentration rows exported by MediaDB 173. It is incomplete for MediaDB provenance and growth context: it has no source-specific MediaDB URL, source 65 URL, PubMed reference, organism, 37 C temperature, or 0.142541 1/h growth rate, and the only bibliographic provenance is the generic MediaDB database article named in the import history.

## Findings

1. **Source-specific MediaDB context is absent.** The YAML cites only the MediaDB homepage in `notes` and names Mazumdar et al. 2014 in import history. It does not preserve `/defined_media/media/173/`, `/defined_media/sources/65/`, `/defined_media/growthdata/358/`, or PMID 6223882.

2. **Growth evidence is dropped.** MediaDB 173 is tied to `Vibrio vulnificus C7184` and growth-data record 358, which reports growth rate 0.142541 1/h at 37.0 C. The generated record has no `target_organisms`, growth metric, or temperature.

3. **Preparation steps are generic and unsupported.** MediaDB 173 provides a compound table, not instructions to adjust pH or filter-sterilize through a 0.22 um filter. The generated `preparation_steps` therefore look like an importer template rather than source evidence.

4. **Magnesium chloride is probably over-specified as the hexahydrate.** The source row is `Magnesium chloride`, and the MediaDB export carries KEGG `C07755`, PubChem `5360315`, and CHEBI `6636`; the generated record grounds the ingredient to `CHEBI:86345` / magnesium dichloride hexahydrate.

## Recommended Edits

- Add source-specific references for MediaDB medium 173, MediaDB source 65, MediaDB growth data 358, and PMID 6223882.
- Capture `Vibrio vulnificus C7184`, temperature 37.0 C, and growth rate 0.142541 1/h from growth-data record 358.
- Remove or qualify the generic pH-adjustment and 0.22 um filter-sterilization steps unless a primary source confirms them.
- Recheck the magnesium chloride CHEBI mapping against MediaDB compound 6286 and use the correct non-hydrate-specific term if the source does not specify a hydrate.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after curation.
- Review the next record, `deferrated_synbase_with_ferric_ammonium_citrate_simpson.yaml`, together with this one because MediaDB source 65 links both Simpson deferrated SynBase variants.

## Additional Notes

The review used gitignore-independent `rg --no-ignore --hidden` searches for `MEDIADB:173`, `deferrated_synbase_simpson_et_al`, and `Deferrated synbase; simpson et al`, so ignored files were included in the duplicate/source scan.

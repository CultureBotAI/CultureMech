# YAML Record Review: deferrated_synbase_with_ferric_ammonium_citrate_simpson

- Repository: CultureMech
- Record: data/merge_yaml/merged/deferrated_synbase_with_ferric_ammonium_citrate_simpson.yaml
- Started UTC: 2026-09-22T14:01:44Z
- Finished UTC: 2026-09-22T14:03:57Z
- Verdict: needs curation

## Target

Reviewed generated record `data/merge_yaml/merged/deferrated_synbase_with_ferric_ammonium_citrate_simpson.yaml` with generated identifier `CultureMech:007065`, media term `MEDIADB:174`, original name `Deferrated synbase with ferric ammonium citrate; simpson`, category `bacterial`, and one merged source, `deferrated_synbase_with_ferric_ammonium_citrate_simpson`.

## Validation

- LinkML open-schema validation: passed.
- Strict validation: passed with 0 error rows in `/private/tmp/deferrated_synbase_with_ferric_ammonium_citrate_simpson.strict.tsv`.
- Reference validation: passed with 0 references checked.
- Term validation: passed.
- Embedded curation history: not checked; `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` blocks.

## Identity and Grounding

MediaDB medium 174 is `Deferrated synbase with ferric ammonium citrate; simpson`. It has the same Simpson deferrated SynBase backbone as MediaDB medium 173, but uses 1.432 mM ferric ammonium citrate rather than the 0.0006 mM Fe3+ row.

The per-medium MediaDB page links the formulation to organism `Vibrio vulnificus C7184`, source 65 `Simpson et al, 1983`, and growth data 359. The source page identifies the source article as `Siderophore production by vibrio vulnificus` in *Infection And Immunity* and links PMID 6223882; the growth-data page reports growth rate 0.921034 1/h at 37.0 C.

An exact gitignore-independent search for `MEDIADB:174`, `deferrated_synbase_with_ferric_ammonium_citrate_simpson`, and `Deferrated synbase with ferric ammonium citrate; simpson` across normalized YAML, merged YAML, and prior YAML record reviews found only the maintained source and this generated target for MediaDB medium 174, plus the previous local review that intentionally mentioned this paired record.

## Evidence

The MediaDB tab-delimited export for medium 174 exactly supports the generated numeric amounts and names for all ten exported rows: glycerol, Cl-, magnesium chloride, potassium dibasic phosphate, sodium sulfate, dibasic sodium phosphate, ammonium chloride, manganese chloride, sodium succinate, and ferric ammonium citrate.

## Completeness

The generated record is complete for the ten MediaDB concentration rows. It is incomplete for provenance and growth context: it lacks MediaDB medium/source/growth-data URLs, PMID 6223882, `Vibrio vulnificus C7184`, 37 C incubation temperature, and the 0.921034 1/h growth rate reported on MediaDB growth-data record 359.

## Findings

1. **Source-specific MediaDB context is absent.** The YAML cites only the MediaDB homepage in `notes` and names Mazumdar et al. 2014 in import history. It does not preserve `/defined_media/media/174/`, `/defined_media/sources/65/`, `/defined_media/growthdata/359/`, or PMID 6223882.

2. **Growth evidence is dropped.** MediaDB 174 is tied to `Vibrio vulnificus C7184` and growth-data record 359, which reports growth rate 0.921034 1/h at 37.0 C. The generated record has no `target_organisms`, growth metric, or temperature.

3. **Preparation steps are generic and unsupported.** MediaDB 174 supplies a compound table, not pH-adjustment or 0.22 um filter-sterilization instructions. The generated `preparation_steps` therefore look like an importer template.

4. **Magnesium chloride is probably over-specified as the hexahydrate.** The source row is `Magnesium chloride`, and the MediaDB export carries the same KEGG and PubChem cross-references as MediaDB 173; the generated record grounds the ingredient to `CHEBI:86345` / magnesium dichloride hexahydrate.

## Recommended Edits

- Add source-specific references for MediaDB medium 174, MediaDB source 65, MediaDB growth data 359, and PMID 6223882.
- Capture `Vibrio vulnificus C7184`, temperature 37.0 C, and growth rate 0.921034 1/h from growth-data record 359.
- Remove or qualify the generic pH-adjustment and 0.22 um filter-sterilization steps unless a primary source confirms them.
- Recheck the magnesium chloride CHEBI mapping against MediaDB compound 6286 and use the correct non-hydrate-specific term if the source does not specify a hydrate.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after curation.
- Re-review this record alongside `deferrated_synbase_simpson_et_al.yaml` to keep the shared Simpson source provenance and the variant-specific growth rates consistent.

## Additional Notes

The review used gitignore-independent `rg --no-ignore --hidden` searches for `MEDIADB:174`, `deferrated_synbase_with_ferric_ammonium_citrate_simpson`, and `Deferrated synbase with ferric ammonium citrate; simpson`, so ignored files were included in the duplicate/source scan.

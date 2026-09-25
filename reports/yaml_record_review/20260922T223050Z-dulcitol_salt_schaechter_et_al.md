# YAML Record Review: Dulcitol salt; schaechter et al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/dulcitol_salt_schaechter_et_al.yaml
- Started UTC: 2026-09-22T22:28:39Z
- Finished UTC: 2026-09-22T22:30:50Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:007127` at `data/merge_yaml/merged/dulcitol_salt_schaechter_et_al.yaml`.

- Label: `dulcitol_salt_schaechter_et_al`; original name: `Dulcitol salt; schaechter et al`.
- Generated status: generated merge output with `merge_fingerprint` `064e049414ba771cf1b6d2f006f12a1bccdfe8b6652ec019f75afa3a91f393c3`.
- Maintained owner for direct record repair: `data/normalized_yaml/bacterial/dulcitol_salt_schaechter_et_al.yaml`.
- Merge lineage: one source record, `dulcitol_salt_schaechter_et_al`.
- Declared external source: `MEDIADB:231`.
- Current external cross-reference: `kg_microbe_match: mediadive.medium:J526`.

## Validation

Focused validation on `data/merge_yaml/merged/dulcitol_salt_schaechter_et_al.yaml`:

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/dulcitol_salt_schaechter_et_al.yaml` | Passed; `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/dulcitol_salt_schaechter_et_al.yaml --out /private/tmp/dulcitol_salt_schaechter_et_al.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/dulcitol_salt_schaechter_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 checks, all validations passed. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/dulcitol_salt_schaechter_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the expected `eutils` / `pkg_resources` warning. |
| Embedded curation history | `just validate-history` | Not checked: the available history gate validates standalone `history/` files, not embedded `MediaRecipe.curation_history` in one merged YAML. |

The validators do not check that generic preparation text came from MediaDB or that `kg_microbe_match` points at a compatible medium.

## Identity and Grounding

The MediaDB identity is correct:

- `MEDIADB:231` resolves at `https://mediadb.systemsbiology.net/defined_media/media/231/`.
- The page label is `Dulcitol salt; schaechter et al`.
- The tab-delimited MediaDB export for record 231 lists exactly the six compounds and mM values represented by this record.

Ingredient grounding is mostly supportable from the MediaDB export:

- MediaDB exports KEGG `C01697`, BiGG `galt`, ModelSEED `cpd01171`, PubChem `11850`, and ChEBI `16813` for galactitol. The maintained normalized record now contains `CHEBI:16813`; this generated merge is stale and still omits that term.
- MediaDB has no ChEBI cross-reference for sodium ammonium phosphate, so the unresolved term is appropriate until a curator resolves the supplied compound.

The external `kg_microbe_match` is wrong. `mediadive.medium:J526` is JCM Medium 526, `NORRIS FERROPLASMA MEDIUM`, a complex pH 1.2 medium with ferrous sulfate and yeast extract; it is not the Schaechter Dulcitol salt formulation.

## Evidence

Supported against inspected MediaDB pages:

- Medium 231 supports citrate `5.20497 mM`, dibasic sodium phosphate `28.0899 mM`, galactitol `2.74469 mM`, magnesium sulfate `0.405729 mM`, potassium chloride `9.92605 mM`, and sodium ammonium phosphate `8.32187 mM`.
- MediaDB source 84 supports `Schaechter et al, 1958` as the medium source, with title `Dependency on medium and temperature of cell size and chemical composition during balanced growth of salmonella typhimurium`, journal `J. Gen. Microbiol.`, and PMID `13611202`.
- NCBI ESummary for PMID `13611202` resolves the Schaechter, Maaloe, and Kjeldgaard paper and DOI `10.1099/00221287-19-3-592`.
- MediaDB medium 231 links organism `Salmonella enterica Typhimurium LT2` and growth-data record `455` for that organism on this medium.

Unsupported in the generated record:

- The three `preparation_steps` are generic import text. MediaDB medium 231 exposes compound concentrations, source, organism, and growth-data links, but no pH, no distilled-water volume, and no filtration instruction.
- The `kg_microbe_match` value is unrelated to the MediaDB medium.
- The record's source note cites only the MediaDB home page and the import history cites `Mazumdar et al. (2014) PLOS One`; the inspected MediaDB page names Schaechter et al. 1958 as the formulation source.

## Completeness

Consequential gaps:

- Primary-source provenance should be captured from MediaDB source 84, including PMID `13611202` and DOI `10.1099/00221287-19-3-592`.
- The Salmonella Typhimurium LT2 growth-data relationship in MediaDB is not represented as a target organism or growth-evidence claim.
- The maintained normalized record has an August 20, 2026 galactitol grounding that the August 6, 2026 generated merge does not include, so this generated record is stale relative to its owner.

Empty pH is not itself a defect; MediaDB medium 231 did not provide pH in the inspected web or tab-delimited views.

An ignored-inclusive `find data -iname '*dulcitol*' -o -iname '*schaechter*'` search found the generated Dulcitol Salt record, seven sibling Schaechter salt records, and their normalized upstreams. An ignored-inclusive `rg --no-ignore --hidden` search for the slug, label, `MEDIADB:231`, `Medium ID: 231`, `CultureMech:007127`, the merge fingerprint, and `mediadive.medium:J526` across `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and the CultureMech registries found the active normalized record, active generated record, MediaDB index entries, and unrelated Norris Ferroplasma / sibling Schaechter matches for the bad `J526` cross-reference; it did not find another active `MEDIADB:231` record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The record contains unsupported generic preparation steps. | MediaDB medium 231 and its tab-delimited export list only compounds and mM amounts, plus source, organism, and growth-data links. They do not state distilled-water volume, pH adjustment, or 0.22 um filter sterilization. | `data/normalized_yaml/bacterial/dulcitol_salt_schaechter_et_al.yaml`; the MediaDB importer if these generic steps are injected systemically. |
| major | `kg_microbe_match` points at the wrong medium. | `mediadive.medium:J526` resolves to JCM 526 `NORRIS FERROPLASMA MEDIUM`, not MediaDB Dulcitol salt. | `data/normalized_yaml/bacterial/dulcitol_salt_schaechter_et_al.yaml`; any KG Microbe matching overlay that assigned `J526` to this and sibling Schaechter MediaDB records. |
| major | MediaDB's organism and growth-data claim were dropped. | MediaDB medium 231 links `Salmonella enterica Typhimurium LT2` and growth-data record `455`; the generated record has only generic applications. | `data/normalized_yaml/bacterial/dulcitol_salt_schaechter_et_al.yaml`. |
| minor | Primary source provenance is weaker than the inspected source. | The record cites the MediaDB home page and mentions Mazumdar et al. 2014 in import history, while MediaDB record 231 points to Schaechter et al. 1958 / PMID `13611202` as the formulation source. | `data/normalized_yaml/bacterial/dulcitol_salt_schaechter_et_al.yaml`. |
| minor | The generated merge is stale relative to its normalized owner. | `data/normalized_yaml/bacterial/dulcitol_salt_schaechter_et_al.yaml` now grounds Galactitol to `CHEBI:16813`; the generated record was last merged on August 6, 2026 and omits that term. | Regenerate `data/merge_yaml/merged/dulcitol_salt_schaechter_et_al.yaml` after normalized repairs. |

No blocker findings were found: the MediaDB identity and the six core mM amounts are correct.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/dulcitol_salt_schaechter_et_al.yaml`, remove the generic preparation steps unless the Schaechter primary paper supports them.
2. Remove or correct `kg_microbe_match: mediadive.medium:J526`; J526 is Norris Ferroplasma Medium.
3. Add source provenance for MediaDB source 84 and PMID `13611202`, and make the current MediaDB medium 231 URL recoverable.
4. Add the MediaDB `Salmonella enterica Typhimurium LT2` / growth-data 455 assertion if the schema has a supported target-organism or growth-evidence slot for MediaDB growth data.
5. Rerun merge generation so the generated record carries the maintained Galactitol `CHEBI:16813` grounding.

## Follow-up Checks

- Re-run the focused LinkML, strict, reference, and term validators on the repaired normalized record and regenerated merged record.
- Re-fetch `https://mediadb.systemsbiology.net/defined_media/media/231/` and `https://mediadb.systemsbiology.net/defined_media/media_text/231/` to confirm all six mM amounts still match.
- Check every sibling `*_schaechter_et_al.yaml` record with `kg_microbe_match: mediadive.medium:J526` and remove the bad MediaDive cross-reference where it is not independently supported.
- Confirm the regenerated merged YAML includes `CHEBI:16813` for Galactitol and no longer carries the stale August 6 view of the normalized source.

## Additional Notes

MediaDive JCM `J526` and the live JCM `GRMD=526` page agree with each other that medium 526 is Norris Ferroplasma Medium. They were inspected only to verify that the `kg_microbe_match` cross-reference in this MediaDB record is a false match.

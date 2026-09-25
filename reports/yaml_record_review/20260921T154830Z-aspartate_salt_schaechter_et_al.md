# YAML Record Review: Aspartate salt; schaechter et al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/aspartate_salt_schaechter_et_al.yaml
- Started UTC: 2026-09-21T15:46:40Z
- Finished UTC: 2026-09-21T15:48:31Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/aspartate_salt_schaechter_et_al.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:007128` |
| Label | `Aspartate salt; schaechter et al` |
| Normalized owner | `data/normalized_yaml/bacterial/aspartate_salt_schaechter_et_al.yaml` |
| Source | MediaDB `MEDIADB:232` |
| Generated status | Generated one-input merge of `aspartate_salt_schaechter_et_al.yaml`; future fixes belong in the normalized owner and should be propagated by regenerating merges/pages. |

## Validation

| Check | Result |
|---|---|
| Open-schema LinkML validation | Passed: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/aspartate_salt_schaechter_et_al.yaml` reported `No issues found`. |
| Strict validation | Passed: the no-project Python 3.11 invocation of `scripts/validate_strict.py data/merge_yaml/merged/aspartate_salt_schaechter_et_al.yaml --out /private/tmp/aspartate_salt_schaechter_et_al.strict.tsv --workers 1 --quiet` scanned 1 file and wrote 0 error rows. |
| Reference validation | Passed: `linkml-reference-validator validate data data/merge_yaml/merged/aspartate_salt_schaechter_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` validated 1 file, ran 0 snippet checks, and reported all validations passed. |
| Term validation | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/aspartate_salt_schaechter_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` reported validation passed after the known `eutils/pkg_resources` warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone records under `history/`, not a focused embedded-`MediaRecipe.curation_history` validator for one generated merge record. |

The documented `just` entry points remain blocked by the project-level Python
3.13 `llvmlite==0.46.0` build failure, so the focused no-project Python 3.11
validator invocations above were used for this one record.

## Identity and Grounding

The MediaDB identity is coherent. `CultureMech:007128` is registered to
`data/normalized_yaml/bacterial/aspartate_salt_schaechter_et_al.yaml`, the
generated target has the same ID, and MediaDB serves Medium 232 as `Aspartate
salt; schaechter et al`.

The `kg_microbe_match` is not coherent. The record asserts
`mediadive.medium:J526`, but MediaDive `J526` is `NORRIS FERROPLASMA MEDIUM`,
a JCM acidic archaea medium with yeast extract, ammonium sulfate, potassium
dihydrogen phosphate, magnesium sulfate heptahydrate, ferrous sulfate
heptahydrate, and pH 1.2. That is not equivalent to this six-component
Salmonella aspartate salt recipe.

## Evidence

The generated record has no structured `references` or snippet-level
`evidence`, but the MediaDB page and its tab-delimited export support the
source identity and six mM concentrations.

Supported claims:

- MediaDB Medium 232 is named `Aspartate salt; schaechter et al`.
- MediaDB lists six compounds, and the YAML preserves all six amounts: citrate
  5.20497 mM, D-Aspartate 0.901578 mM, dibasic sodium phosphate 28.0899 mM,
  potassium chloride 9.92605 mM, magnesium sulfate 0.405729 mM, and sodium
  ammonium phosphate 8.32187 mM.

Unsupported or over-scoped assertions:

| Record assertion | Problem |
|---|---|
| `kg_microbe_match: mediadive.medium:J526` | MediaDive `J526` is Norris Ferroplasma Medium and does not share this recipe's source, organism, ingredient set, or pH. |
| The medium should be dissolved in distilled water, pH-adjusted if specified, and filter-sterilized through 0.22 um. | The inspected MediaDB Medium 232 page and tab-delimited export list compounds, amounts, organism, source, and a growth-data link, but no pH or sterilization protocol. |

## Completeness

- The source MediaDB page lists one organism association, `Salmonella enterica
  Typhimurium LT2`, one source, `Schaechter et al, 1958`, and one growth-data
  record for that organism on this medium. None of those are represented as
  structured `target_organisms`, `references`, or `growth_metrics`.
- MediaDB source 84 links the Schaechter source to PubMed ID `13611202`, so the
  record's generic Mazumdar/MediaDB curation note can be narrowed to a primary
  source in a later curation pass.
- `D-Aspartate` lacks a term even though the tab-delimited MediaDB export
  carries KEGG `C00402`, BiGG `asp-D`, SEED `cpd00320`, PubChem `83887`, and
  CHEBI `17364` for this compound.
- `find data/normalized_yaml -name 'aspartate_salt_schaechter_et_al.yaml'`
  found exactly one normalized owner.
- A gitignore-independent exact search for
  `CultureMech:007128|MEDIADB:232|mediadive.medium:J526|Aspartate salt; schaechter et al`
  under `data`, `scripts`, `history`, `src`, `reports`, and
  `references_cache` found the normalized owner, the generated target, sibling
  Schaechter salt records with the same `J526` cross-match, the real J526
  normalized record, indexes, and reports.
- `find reports/yaml_record_review -maxdepth 1 -name '*aspartate_salt_schaechter_et_al.md'`
  found no prior report for this generated record.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The `kg_microbe_match` points to an unrelated JCM medium. | MediaDB 232 is Aspartate salt for Salmonella enterica Typhimurium LT2. MediaDive J526 is Norris Ferroplasma Medium for a different source and formulation. | `data/normalized_yaml/bacterial/aspartate_salt_schaechter_et_al.yaml` |
| Major | Generic preparation steps assert unsupported protocol details. | The YAML says to dissolve in distilled water, adjust pH if specified, and filter-sterilize by 0.22 um. MediaDB Medium 232 provides no pH, water, or sterilization instruction. | `data/normalized_yaml/bacterial/aspartate_salt_schaechter_et_al.yaml`, or the MediaDB importer/defaulting rule that added generic defined-medium preparation. |
| Minor | Source, organism, and growth association are not represented structurally. | MediaDB Medium 232 lists Schaechter et al. 1958, Salmonella enterica Typhimurium LT2, and a Medium 232 growth-data row, while the YAML only has a generic MediaDB root URL and no target organism. | `data/normalized_yaml/bacterial/aspartate_salt_schaechter_et_al.yaml` |
| Minor | `D-Aspartate` is left ungrounded despite source database cross-references. | The MediaDB tab-delimited export includes KEGG, BiGG, SEED, PubChem, and CHEBI IDs for the D-Aspartate source compound. | `data/normalized_yaml/bacterial/aspartate_salt_schaechter_et_al.yaml` |

## Recommended Edits

1. Remove `kg_microbe_match: mediadive.medium:J526` from
   `data/normalized_yaml/bacterial/aspartate_salt_schaechter_et_al.yaml`. Audit
   the sibling MediaDB Schaechter salt records that carry the same match before
   bulk-removing it there.
2. Remove or replace the generic preparation steps unless the primary
   Schaechter et al. 1958 article supplies pH, water, and sterilization
   instructions.
3. Add a structured reference for PMID `13611202` after checking the paper
   text, and scope it to the source MediaDB formulation.
4. Add a `Salmonella enterica`/Typhimurium LT2 target-organism claim only if
   MediaDB's organism and growth-data rows or the Schaechter paper support the
   exact strain and growth outcome represented by CultureMech.
5. Re-check the D-Aspartate CHEBI mapping before grounding it to CHEBI `17364`.

## Follow-up Checks

- Re-run focused schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/aspartate_salt_schaechter_et_al.yaml`.
- Re-run `just verify-merges` and `just audit-merge-freshness` after
  regenerating `data/merge_yaml/merged/aspartate_salt_schaechter_et_al.yaml`.
- Re-fetch `https://mediadb.systemsbiology.net/defined_media/media_text/232/`
  and compare all six mM amounts to the YAML after curation.
- Re-run an exact search for `mediadive.medium:J526` to find the sibling
  Schaechter salt records still needing the same cross-match audit.

## Additional Notes

- The unrelated local J526 owner is
  `data/normalized_yaml/archaea/norris_ferroplasma_medium.yaml`; editing that
  record would not correct this Aspartate salt mismatch.

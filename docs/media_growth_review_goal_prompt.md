# Media Growth Review Goal Prompt

```text
/goal Review the CultureMech media YAML record list as the target media corpus and produce evidence-backed reports identifying organisms that grow on each medium or its variants, including strain identifiers and genome IDs where available, and modeling media variations as variant records under a shared parent medium.
```

```text
Review this repo's CultureMech media records, especially `data/normalized_yaml/**/*.yaml`, with schema guidance from `docs/schema/MediaRecipe.md` and `docs/schema/MediaVariant.md`.

Task:
Use the repo's media YAML records themselves as the target media list. Research and report evidence for organisms that grow on each target medium or a close formulation variant. This is an open-ended medium-centered search across the YAML corpus, not a predeclared organism/media pair list. The organism list should be discovered from evidence for each YAML medium. The research question for each YAML record is: which specific organisms, strains, isolates, or genomes are documented to grow on this medium or a justified variant of it? Prefer evidence with strain identifiers, NCBI Taxonomy IDs, genome assembly accessions, BioSample IDs, or other genome identifiers. Use primary literature, culture collection pages, MediaDive/DSMZ/JCM/ATCC-style sources, and NCBI records where relevant.

Targets:
- Primary target corpus: every media recipe YAML record under `data/normalized_yaml/**/*.yaml`; this list of YAML records is the target media list.
- Include these directories: `data/normalized_yaml/algae`, `data/normalized_yaml/archaea`, `data/normalized_yaml/bacterial`, `data/normalized_yaml/fungal`, and `data/normalized_yaml/specialized`.
- Treat `data/normalized_yaml/solutions` as supporting stock-solution records, not primary growth-media targets, unless a solution record is clearly used as a growable medium or is needed to model a parent medium or variant.
- Process the corpus in explicit batches when needed. Each batch report must state the exact YAML paths reviewed.

Search strategy:
- First inventory the target YAML records and group likely duplicates/variants by exact name, original name, synonym, source database ID, common spelling variants, and formulation similarity.
- For each parent-medium group, choose the best canonical parent `MediaRecipe` record and note the member YAML paths.
- Identify existing records that are likely variants of the same parent medium.
- Search external sources for organisms/strains cultivated on the parent medium name and recognizable formulation variants.
- For each hit, compare the reported formulation and culture conditions to the CultureMech parent medium to decide whether it is an exact match, an existing variant, or a new variant proposal.

For each supported organism-medium relationship, report:
- Organism name, strain, and identifiers
- Genome assembly ID and/or BioSample/RefSeq/GenBank accession when available
- Existing CultureMech media YAML record path
- Exact medium name and source name
- Whether the source formulation matches the parent medium or requires a variant
- Growth evidence: growth/no growth, OD, doubling time, colony formation, yield, qualitative growth, or stated cultivation success
- Culture conditions: temperature, atmosphere, pH, salinity, carbon/nitrogen source, supplements, antibiotics, light, vessel, incubation time
- Source citations with PMID/DOI/URL and short evidence snippets

Media variation modeling rule:
Do not create unrelated duplicate media records for small formulation or condition changes. Treat similar formulations as one parent `MediaRecipe` with `variants` entries when they share a recognizable base medium. Use the parent record for the canonical/base formulation, and model organism- or study-specific changes as `MediaVariant` entries with:
- `name`
- `description`
- `modifications`
- `purpose`
- `evidence`

Create or propose a new parent media record only when the formulation is not reasonably a variant of an existing medium.

Deliverables:
1. A Markdown report under `reports/` summarizing the reviewed YAML batch, parent-medium grouping, discovered organisms/strains, sources, confidence, and unresolved gaps.
2. A table of organism growth evidence grouped by parent medium and variant, including organism/strain, genome or BioSample identifiers, evidence type, culture conditions, and citation.
3. A table of proposed YAML changes, including parent medium path, variant name, affected organism/strain, evidence source, and whether the change should be applied.
4. A machine-readable manifest under `reports/` or `workspace/reports/` recording reviewed YAML paths, search terms used, source URLs/PMIDs checked, match status, and proposed parent/variant grouping.
5. If making edits, keep them scoped to the relevant YAML records and validate with the repo's available commands, such as `just validate <file>` and any growth-evidence validation commands that apply.

Useful local commands:
- `python3 scripts/build_media_growth_review_manifest.py`
- `just propose-growth --category <dir> --offset <n> --limit <n> --retmax 3 --apply --write-empty`
- `just fetch-pubmed`
- `just validate-growth`

Evidence standards:
- Do not infer growth from taxonomy alone.
- Do not claim strain-specific growth unless the source names the strain or unambiguously links the isolate/genome to the experiment.
- Mark uncertain matches explicitly.
- Prefer exact medium formulation matches; otherwise explain the variant-level difference.
- Report negative searches too: if no strong organism-level evidence is found for a target medium, state the search terms and sources checked.
- Because this is a large corpus, never imply the full repo has been reviewed unless the manifest covers every target YAML path.
```

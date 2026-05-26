# CultureMech Per-Organism Recipe Extraction Template

This is the **phase-2** deep-research prompt: a follow-up to the
medium-level literature search (templates/media_growth_research.md).
The phase-1 search returned a list of candidate organisms reported to
grow on this medium; this template drills into *one* organism at a
time and tries to extract the actual recipe + metadata that the cited
publication used.

## Parent Medium (context only — do NOT re-research)

- **Record path:** {record_path}
- **CultureMech ID:** {media_id}
- **Name:** {media_name}
- **Original/source name:** {original_name}
- **Category:** {category}
- **Medium type:** {medium_type}
- **Physical state:** {physical_state}
- **Media term:** {media_term}
- **Parent ingredients (for diff/variant detection):** {ingredients}
- **Parent conditions:** {conditions}
- **Notes/provenance:** {notes}

## Target Organism

- **Organism name:** {organism_name}
- **Strain (if known):** {organism_strain}
- **Reported NCBI Taxonomy / GTDB / BioSample / assembly IDs:** {organism_identifiers}
- **Citation hint (PMID, DOI, or URL from phase 1):** {citation_hint}
- **Phase-1 evidence snippet:** {phase1_snippet}

## Research Objective

Find the primary publication(s) that report **{organism_name}**
(strain `{organism_strain}` if specified) growing on **{media_name}**
or a recognizable formulation variant of it. Extract everything that
would let a curator either:

1. add a `target_organisms` entry to `{record_path}`, OR
2. propose a `MediaVariant` under that record, OR
3. flag a brand-new media record if the formulation is genuinely
   distinct.

Do **not** infer growth from taxonomy alone. Do **not** claim
strain-specific growth unless the source names the strain or
unambiguously links the isolate/genome to the experiment.

## What to Extract per Source

For each primary publication that supports the organism-medium claim,
report:

### Citation & provenance
- PMID and/or DOI (required if available)
- Title, first author, year, journal
- Section / page / figure / table where the recipe is described
- A short exact-substring quote (snippet) — used as an EvidenceItem
  snippet, must be verbatim text from the paper

### Organism / strain identifiers
- Full strain designation as printed
- NCBI Taxonomy ID
- GTDB genome/lineage ID (if used)
- Genome assembly accession (GCF_/GCA_/SAMN)
- Culture collection IDs (DSM, ATCC, JCM, NBRC, CCAP, NCMA, etc.)
- BioSample / BioProject accessions

### Medium formulation reported in the paper
- Full ingredient list with concentrations and units, exactly as
  printed
- Any solutions / stock components referenced
- pH (value or range)
- Sterilization (method, temperature, duration)
- Preparation steps and order-of-addition if non-trivial
- Atmosphere / gas phase (anaerobic, aerobic, headspace composition)

### Diff vs. the parent medium
- Which ingredients match the parent (qualitatively, ignoring
  concentration noise)
- Which ingredients differ (added, omitted, substituted, or
  concentration shifted by >2× or to a different chemical form)
- Whether the paper's medium is most plausibly:
  - the **parent** itself (no meaningful difference),
  - a **MediaVariant** (small, named or unnamed deviation), or
  - a **distinct medium** (different identity entirely)
- Suggested `MediaVariantRelationshipEnum` value if a variant is
  proposed

### Culture conditions
- Temperature (value or range, in °C)
- Light intensity, light cycle, light quality (if photosynthetic)
- Salinity
- Aeration / shaking
- Inoculum size / source

### Growth metrics (if reported)
- Max OD, doubling time, growth rate, biomass yield
- Growth phase observed
- Lag time
- Whether values are mean ± SD, n replicates

### Perturbations / strain modifications (if reported)
- Knockouts, plasmids, evolved lineages
- Distinguish strain-level (carries across observations) from
  per-observation perturbations

### Confidence assessment
- `HIGH` — strain named, recipe printed in full, growth measured
- `MEDIUM` — strain named, recipe partially specified or cited
  to another paper
- `LOW` — organism named at species level only, or recipe inferred
- `UNCERTAIN` — record/medium match itself is uncertain; flag for
  curator review

## Output Format

Return Markdown with these sections, in order:

### 1. Summary
One paragraph: does the literature support **{organism_name}** on
**{media_name}**? Strongest single citation. Most likely
parent-vs-variant verdict.

### 2. Sources
A numbered list of primary publications used, each with:
- PMID / DOI / URL
- Citation in `Author Year Journal` form
- One-sentence relevance note

### 3. Recipe extraction table
A Markdown table with columns:

| Source # | Component | Concentration | Unit | Notes / CHEBI hint |

One row per ingredient. Include solutions / stocks. Mark
unspecified-but-implied components explicitly (e.g.
`(not in paper; inherited from parent)`).

### 4. Conditions & growth
A Markdown table with columns:

| Source # | Field | Value | Notes |

Rows for pH, temperature, atmosphere, light, salinity, inoculum,
growth metrics, etc.

### 5. Proposed YAML changes
For each proposed change, give:
- **Target file:** `{record_path}` (or a new path if a brand-new
  record is needed)
- **Change type:** `add_target_organism` | `add_media_variant` |
  `propose_new_record` | `add_evidence_only`
- **YAML fragment** (under a ```yaml``` block) ready to paste into
  the record, including:
  - `preferred_term`, `term` (with NCBITaxon `id` + `label`),
    `strain`, `genome_assembly_id` for organisms
  - `evidence` list with at least one `EvidenceItem`
    (`reference: PMID:xxx` or `doi:...`, `supports:` value,
    `snippet:` verbatim quote, `explanation:`)
  - For variants: `name`, `description`, `modifications`,
    `purpose`, `relationship`, `evidence`

### 6. Identifier resolution status
For each organism/strain/genome ID reported, mark whether it was
verified against the source vs. asserted by the paper without a
deposit. Note any ID conflicts (e.g. paper says DSM-XXX but
NCBITaxon disagrees).

### 7. Unresolved gaps & warnings
- Claims that should NOT yet be curated and why
- Recipes that are paywalled or only cited transitively
- Strain names that could not be resolved to NCBI/GTDB
- Conflicting recipes across multiple papers

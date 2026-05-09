# CultureMech Media Growth Evidence Research Template

## Target Medium
- **Record path:** {record_path}
- **CultureMech ID:** {media_id}
- **Name:** {media_name}
- **Original/source name:** {original_name}
- **Category:** {category}
- **Medium type:** {medium_type}
- **Physical state:** {physical_state}
- **Media term:** {media_term}
- **Conditions:** {conditions}
- **Applications:** {applications}
- **Synonyms:** {synonyms}
- **Ingredients:** {ingredients}
- **Solutions:** {solutions}
- **Existing target organisms:** {target_organisms}
- **Existing variants:** {variants}
- **Existing evidence:** {evidence}
- **Notes/provenance:** {notes}

## Research Objective

Research organisms reported to grow on **{media_name}** or a recognizable formulation
variant of this medium. Focus on exact organism-medium relationships that can support
CultureMech curation under `{record_path}`.

## Evidence Requirements

- Prefer strain-specific evidence and include strain identifiers when available.
- Include NCBI Taxonomy IDs, genome assembly accessions, BioSample IDs, RefSeq/GenBank
  accessions, culture collection identifiers, or other stable genome/isolate identifiers.
- Use primary literature, culture collection pages, MediaDive/DSMZ/JCM/ATCC-style
  sources, and NCBI records where relevant.
- Do not infer growth from taxonomy alone.
- Do not claim strain-specific growth unless the source names the strain or
  unambiguously links the isolate/genome to the experiment.
- Mark uncertain record, medium, strain, or formulation matches explicitly.

## Media Variation Modeling

Do not propose unrelated duplicate media records for small formulation or condition
changes. Treat similar formulations as variants under this parent `MediaRecipe` when
they share the same recognizable base medium.

For each organism-medium relationship, decide whether the evidence matches the parent
medium formulation or requires a `MediaVariant`. If a variant is needed, propose:
- `name`
- `description`
- `modifications`
- `purpose`
- `evidence`

Create or propose a new parent medium only when the source formulation is not
reasonably a variant of this record.

## Output Format

Return a curation-focused Markdown report with:
- A short summary of the strongest supported organism-medium relationships.
- A table with organism, strain, identifiers, genome/BioSample IDs, source medium name,
  growth evidence, culture conditions, citation, and confidence.
- A table of proposed YAML changes with parent medium path, variant name if needed,
  affected organism/strain, evidence source, and whether the change should be applied.
- Short evidence snippets for each source, with PMID/DOI/URL.
- Unresolved gaps and warnings for claims that should not yet be curated.

# CultureMech Medium Axis Classification Template

Classify one growth medium along the two composition axes that #148 introduced and
that the corpus does not yet populate: **nutritional class** and **functional
role**. The third axis, `composition_type`, is already derived from the ingredient
list and is NOT in scope here — it is given below as context only.

## Target Medium
- **Record path:** {record_path}
- **CultureMech ID:** {media_id}
- **Name:** {media_name}
- **Original/source name:** {original_name}
- **Category:** {category}
- **Composition type (already determined):** {medium_type}
- **Physical state:** {physical_state}
- **Media term:** {media_term}
- **Conditions:** {conditions}
- **Applications:** {applications}
- **Synonyms:** {synonyms}
- **Ingredients:** {ingredients}
- **Solutions:** {solutions}
- **Existing target organisms:** {target_organisms}
- **Notes/provenance:** {notes}

## What to determine

### 1. `nutritional_class` — how nutrient-rich the medium is (single-valued)

- `MINIMAL` — only the minimal nutrients required for growth: typically a defined
  medium with a single carbon/energy source plus essential salts (e.g. M9).
- `RICH` — nutrients in excess: abundant amino acids, peptides, vitamins and
  carbon sources, supporting rapid growth of fastidious or general organisms
  (e.g. LB, TSB, BHI).
- `GENERAL_PURPOSE` — standard nutrient level for routine cultivation, neither
  deliberately minimal nor deliberately enriched.

`GENERAL_PURPOSE` is the residual category. Do **not** use it as a default when
the evidence is simply absent — say so instead. An unclassified medium is more
useful than a wrongly-confident one, because a wrong value here is invisible
downstream.

### 2. `functional_role` — what the medium is designed to do (MULTIVALUED)

- `GENERAL_PURPOSE` — non-selective, non-differential, for routine growth of a
  broad range of organisms.
- `SELECTIVE` — suppresses unwanted organisms via antibiotics, dyes, bile salts,
  high NaCl, pH, or similar, to favour a target group.
- `DIFFERENTIAL` — distinguishes organism types by a visible biochemical reaction
  (fermentation colour change, haemolysis) without necessarily inhibiting growth.
- `ENRICHMENT` — promotes a target organism to detectable numbers from a mixed
  population, typically before isolation.

A medium can be several of these at once — MacConkey agar is both `SELECTIVE`
(bile salts and crystal violet suppress Gram-positives) and `DIFFERENTIAL`
(lactose plus neutral red distinguishes fermenters). Return every role that
applies.

## Evidence rules

- Ground the classification in the **named source medium** (DSMZ / JCM / ATCC /
  MediaDive catalogue entry, or the primary publication), not in the record's
  filename.
- Cite a specific ingredient or documented purpose for `SELECTIVE`,
  `DIFFERENTIAL` and `ENRICHMENT`. Naming the selective agent or the indicator dye
  is the evidence; "it is used for X" is not.
- Do **not** infer a functional role from the organism list alone. A medium used
  to grow one genus is not thereby selective — selectivity is a property of the
  formulation, not of who happens to be cultured on it.
- If the medium is a dilution or modification of a well-known base (½ TSB,
  1/10 LB), classify the medium as formulated here, and say how the dilution
  affects the nutritional class.
- Where the evidence does not support a confident call, return `null` for that
  axis with a short reason. Partial answers are expected and wanted.

## Output Format

Return a curation-focused Markdown report containing, in this order:

1. A one-paragraph summary of what this medium is and what it is for.
2. A table of the evidence consulted: source, what it established, and a
   PMID/DOI/URL.
3. **A single fenced YAML block, last in the document**, in exactly this shape:

```yaml
axis_classification:
  medium: "{media_name}"
  culturemech_id: "{media_id}"
  nutritional_class:
    value: RICH            # or MINIMAL / GENERAL_PURPOSE / null
    confidence: 0.9        # 0.0-1.0
    evidence: "Tryptone 10 g/L plus yeast extract 5 g/L supply amino acids and
               vitamins in excess; standard rich medium per Bertani 1951."
    reference: "doi:10.1128/JB.62.3.293-300.1951"
  functional_role:
    - value: GENERAL_PURPOSE
      confidence: 0.9
      evidence: "No selective agent, indicator dye, or enrichment step in the
                 formulation."
      reference: "https://mediadive.dsmz.de/medium/381"
  warnings:
    - "Free-text notes for a curator. These are human-only and are never applied."
```

Rules for the YAML block:

- Emit it **once**, as the last fenced block in the document. An extractor takes
  the last matching block, so an illustrative earlier copy will be ignored.
- `nutritional_class.value` must be one of `MINIMAL`, `RICH`, `GENERAL_PURPOSE`,
  or `null`. `functional_role` is a list; use `[]` if no role is supported.
- Never invent a `reference`. If a claim has no citable source, put it in
  `warnings` and set the value to `null`.
- `confidence` should reflect the source, not your fluency: a DSMZ catalogue entry
  naming the selective agent is high confidence; reasoning from the ingredient
  list alone is not.

---
name: match-kg-microbe
description: Identify and populate the kg_microbe_match field for CultureMech media records by finding exact ingredient matches in the KG-Microbe mediadive graph
category: enrichment
requires_database: false
requires_internet: false
version: 1.0.0
tags: [kg-microbe, matching, enrichment, ontology, mediadive]
---

# Match KG-Microbe Skill

## Overview

**Purpose**: For each CultureMech media record, find the corresponding `mediadive.medium:XXX` node in the KG-Microbe knowledge graph by comparing CHEBI ingredient sets (concentrations ignored), and populate the `kg_microbe_match` field.

**Why**: Enables direct traceability between CultureMech recipes and the KG-Microbe graph, supporting cross-database queries, validation against authoritative DSMZ formulations, and knowledge graph integration.

**Schema field**: `kg_microbe_match` (pattern: `^mediadive\.medium:[0-9a-zA-Z_-]+$`)  
**Match logic**: Exact CHEBI ingredient set equality via the `medium → solution → CHEBI` graph path in `edges.tsv`.

## When to Use This Skill

- After adding ontology term IDs (`term.id: CHEBI:XXXXX`) to media ingredients
- After a new batch of FEBA or other media is imported with CHEBI annotations
- After the KG-Microbe graph is updated with new mediadive data
- To check which media are already linked to the KG

## Approach

### Option A — Full repo scan (recommended, uses culturebotai-claw script)

Scans all 15,000+ CultureMech YAML files at once. Builds an in-memory CHEBI-set → mediadive.medium index from `edges.tsv`, then matches every CultureMech record.

```bash
# From the culturebotai-claw repo (dry run first)
python ../culturebotai-claw/scripts/match_culturemech_to_kg.py \
    --culturemech . \
    --kg-microbe ~/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe \
    --dry-run

# Apply
python ../culturebotai-claw/scripts/match_culturemech_to_kg.py \
    --culturemech . \
    --kg-microbe ~/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
```

Or via the justfile in culturebotai-claw:
```bash
cd ~/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
just match-culturemech-dry   # preview
just match-culturemech       # apply
```

### Option B — Single category (uses CultureMech's built-in module)

Uses `src/culturemech/match/kg_media_matcher.py` and the `enrich_with_kg_microbe_matches.py` script. Processes one category directory at a time.

```bash
# From within CultureMech repo (activate venv first)
source .venv/bin/activate

# Dry run on one category
python scripts/enrich_with_kg_microbe_matches.py \
    --kg-microbe-dir ~/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe \
    --recipe-dir data/normalized_yaml/bacterial \
    --dry-run

# Apply to one category
python scripts/enrich_with_kg_microbe_matches.py \
    --kg-microbe-dir ~/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe \
    --recipe-dir data/normalized_yaml/bacterial

# All categories (loop)
for cat in bacterial algae archaea fungal specialized; do
  python scripts/enrich_with_kg_microbe_matches.py \
    --kg-microbe-dir ~/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe \
    --recipe-dir data/normalized_yaml/$cat
done
```

### Option C — Single recipe (interactive check)

To check whether one specific recipe has a KG match:

```bash
source .venv/bin/activate
python - <<'EOF'
from pathlib import Path
from culturemech.match import KGMediaMatcher
import yaml

kg_dir = Path.home() / "Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe"
matcher = KGMediaMatcher(kg_dir)

recipe = yaml.safe_load(Path("data/normalized_yaml/bacterial/lb_agar.yaml").read_text())
match = matcher.find_exact_match(recipe)
print(f"Match: {match}")
EOF
```

## Prerequisites

- KG-Microbe data at `~/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed_last9/mediadive/`
  - `edges.tsv` — medium→solution→CHEBI relationships
  - `nodes.tsv` — medium node names and IDs
- Ingredients must have `term.id: CHEBI:XXXXX` populated for matching to work
- Media without any CHEBI-annotated ingredients cannot be matched

## Coverage Expectations

As of 2026-04-09 (last full run):
- **15,827** total CultureMech media files
- **10,207** have at least one CHEBI-annotated ingredient
- **489** exactly matched to KG-Microbe media nodes
- **9,718** have CHEBI annotations but no exact KG match (subset overlap, different formulation, or not yet in KG)
- **5,620** have no CHEBI annotations (cannot match without ontology enrichment)

To increase coverage: run FEBA ontology enrichment (`just feba-enrich-ontology` in culturebotai-claw) to add more CHEBI IDs, then re-run this skill.

## Workflow

```
1. Check current coverage
   grep -rl "kg_microbe_match" data/normalized_yaml/ | wc -l

2. Run dry-run to see what would be matched
   python ../culturebotai-claw/scripts/match_culturemech_to_kg.py \
     --culturemech . --kg-microbe ~/Documents/.../kg-microbe --dry-run

3. Apply matches
   python ../culturebotai-claw/scripts/match_culturemech_to_kg.py \
     --culturemech . --kg-microbe ~/Documents/.../kg-microbe

4. Verify a sample
   grep "kg_microbe_match" data/normalized_yaml/bacterial/lb_agar.yaml

5. Commit
   git add data/normalized_yaml/
   git commit -m "Add kg_microbe_match for N media matched to KG-Microbe nodes"
```

## Output Format

A matched media file gets one new field, e.g.:

```yaml
id: CultureMech:009373
name: lb_agar
kg_microbe_match: mediadive.medium:74
...
```

The value is always a `mediadive.medium:XXX` node ID. When multiple KG-Microbe media have identical CHEBI ingredient sets, the one with the lowest numeric ID is used.

## Troubleshooting

**No matches found**: Check that `term.id` fields are populated in the media's ingredients. Unmapped ingredients cannot contribute to matching.

**KG-Microbe path not found**: Verify the `--kg-microbe` path points to the repo root containing `data/transformed_last9/mediadive/edges.tsv`.

**Match seems wrong**: Use Option C to inspect the specific recipe. The match is purely by CHEBI set equality — verify both the CultureMech and KG-Microbe recipes actually represent the same medium.

**Many media unmatched**: The KG-Microbe mediadive graph contains ~3,317 media (DSMZ-derived). CultureMech has 15,827. Most CultureMech media are not in the KG; low match rate is expected.

## Related

- **Script (full repo)**: `../culturebotai-claw/scripts/match_culturemech_to_kg.py`
- **Script (per category)**: `scripts/enrich_with_kg_microbe_matches.py`
- **Matcher module**: `src/culturemech/match/kg_media_matcher.py`
- **Schema field**: `src/culturemech/schema/culturemech.yaml` → `kg_microbe_match`
- **MIM counterpart skill**: `match-kg-microbe` in MediaIngredientMech (uses `kg_microbe_node_id` field)
- **Implementation notes**: `docs/archive/KG_MICROBE_MATCHER_IMPLEMENTATION.md`
- **Ontology enrichment**: `just feba-enrich-ontology` in culturebotai-claw (adds CHEBI IDs to expand matchable media)

---
description: Deep-research the ungrounded growth-condition terms in the media recipes (atmosphere, pH, temperature, salinity, aeration, light); ground to METPO first (else PATO/ENVO/UO), and where no good term exists, draft a METPO proposal. METPO-maximizing, not METPO-forcing.
argument-hint: "[atmosphere|ph|temperature|salinity|aeration|light|all] [min-freq N | label \"...\"]  (default: all, min-freq 2)"
---

# Ground-or-propose residual growth-condition terms (METPO-first)

Goal: shrink the ungrounded residual of **growth-condition** terms across the current media corpus
recipes. These fields are free-text/enum strings today — `incubation_atmosphere`,
`ph_value`/`ph_range`, `temperature_value`/`temperature_range`, `salinity`, `aeration`,
`light_intensity`/`light_cycle`/`light_quality`, `culture_vessel` — and are exactly the
trait/phenotype layer METPO covers (oxygen relation, pH/temperature/salinity preference).
For **each recurring condition term**, either (a) ground it to an existing ontology term —
**METPO first**, then PATO/ENVO/UO — or (b) draft a **METPO proposal** when nothing fits.

> **Scope guardrail — this command is conditions only.** Ingredient/compound grounding is
> *not* in scope: it already has a pipeline (`scripts/aggregate_unmapped_ingredients.py` →
> `output/unmapped_ingredients.sssom.tsv`, the `match-kg-microbe` skill) and MIM is the
> ingredient source of truth. Do not re-ground ingredients here.

`$ARGUMENTS` selects which condition family to work (default: `all`, only values with count
≥ 2). Examples: `/ground-or-propose-metpo atmosphere` ·
`/ground-or-propose-metpo temperature min-freq 5`.

## The residual surface (re-scan each run — there is no standing report yet)
Scan `data/normalized_yaml/**/*.yaml` for the condition fields above, normalize each value to
its underlying *capability/quality* concept, and rank by frequency. Examples of the lift:
- `incubation_atmosphere: AEROBIC | ANAEROBIC | MICROAEROPHILIC` → oxygen-relation trait.
- `temperature_range: "20-25°C"` → mesophile preference (+ a UO-typed numeric quality).
- `ph_value: 9.5` → alkaliphile preference; `salinity: "3% NaCl"` → halophile preference.

Emit the worklist as `output/ungrounded_conditions.tsv`
(cols: `field, raw_value, normalized_concept, count, example_media, routing_hint`) so the run
is reproducible and the coverage delta is measurable. Group the numeric ranges into the
standard phenotype bins (psychro-/meso-/thermo-/hyperthermophile; acido-/neutro-/alkaliphile;
non-/slight-/moderate-/extreme-halophile) — don't ground every distinct "37°C" string.

## Inputs (read these)
- **Recipes:** `data/normalized_yaml/{bacterial,algae,fungal,specialized,archaea,solutions}/*.yaml`.
- **Schema:** `src/culturemech/schema/culturemech.yaml` — the condition slots and their enums.
- **Existing METPO usage:** `src/culturemech/export/kgx_export.py` already emits
  `METPO:2000517` ("grows in") for the organism→medium edge — the only METPO touchpoint today;
  the condition groundings below extend it.
- **METPO term inventory (search FIRST):** the latest release `https://w3id.org/metpo/metpo.owl`
  (BioPortal "METPO") — oxygen-preference, temperature-preference, pH-preference, salinity
  classes already exist there; reuse them.
- **Where groundings/proposals go:** new groundings → `output/condition_grounding.sssom.tsv`
  (create if absent); a proposal cohort under `proposals/` if anything has to be minted.
- **Conventions:** the `manage-identifiers` skill (ID reservation). CultureMech has no
  `metpo-proposal` skill of its own — for the proposal format, follow CommunityMech's
  `metpo-proposal` skill (ROBOT-template TSVs) and reserve IDs in the KG-Microbe range.

## Procedure

### 1. Build + cluster the worklist
Load the residual for the requested condition family, normalize, and **deduplicate by the
underlying concept** — "AEROBIC", "aerobic", "Aerobic, shaking" all ground to the same
oxygen-relation trait. Cluster the numeric ranges into phenotype bins (above). One decision
per concept covers all surface forms. Drop non-ontological narrative (free-text vessel
descriptions, supplier notes) as `skipped: non-ontological`.

### 2. Tier-0 bulk grounding — no research needed (do this first)
Most of the head is mechanical. Ground these directly:
| condition family | concept | search first | then |
|---|---|---|---|
| atmosphere / O₂ relation (aerobic, anaerobic, microaerophilic, facultative) | oxygen-preference trait | **METPO** | PATO, ENVO |
| temperature (psychro/meso/thermo/hyperthermo bin) | temperature-preference trait | **METPO** | PATO |
| pH (acido/neutro/alkali bin) | pH-preference trait | **METPO** | PATO |
| salinity (non/slight/moderate/extreme halophile) | salinity-preference trait | **METPO** | PATO, ENVO |
| light quality/cycle (phototroph context) | light/quality | PATO | ENVO |
| numeric value + unit (°C, %, lux) | unit-typed quantity | UO (unit) + PATO (quality) | — |
The categorical oxygen/temperature/pH/salinity preferences are METPO's home turf — ground
them there. Raw numeric magnitudes are UO/PATO, **not** METPO; don't force "37" into METPO.

### 3. Deep-research the ambiguous remainder
For each *cluster* that survives Tier-0 (e.g. an unusual atmosphere mix, a borderline
temperature bin), invoke the `deep-research-medium` skill with a tightly-scoped query:

> Deep-research the microbial growth-condition concept **"<term>"** (a culture-medium
> <atmosphere | temperature | pH | salinity | light> condition; context: <one line from the
> medium YAML>).
> 1. Does **METPO** (https://w3id.org/metpo/metpo.owl, BioPortal "METPO") contain a trait
>    class for this preference? Give the exact `METPO:` CURIE + label and the match strength.
> 2. If METPO has none, is there a standard PATO/ENVO/UO term? Give the CURIE + match strength.
> 3. If neither fits, propose a one-line Aristotelian definition + the most likely METPO
>    parent class for a new term.
> Cite OLS/BioPortal/OBO; be decisive about match strength.

### 4. Decide per concept (priority order)
1. **Strong METPO match** (exact/close) → ground to the `METPO:` CURIE. *Maximize this.*
2. **No METPO, strong PATO/ENVO/UO match** → ground to that CURIE. Reuse before minting.
3. **No good existing term anywhere**, but the concept is **generic + recurring + reusable** → **METPO proposal**.
4. **Vague / idiosyncratic / one-off** → leave residual.

Verify every chosen CURIE resolves to that label; the `id-label-correspondence` gate
(`validate-products`) re-checks OAK-resolvable prefixes, but not METPO.

### 5. Apply
- **Groundings** → append rows to `output/condition_grounding.sssom.tsv` (create with SSSOM
  header if absent): `subject_id` = `culturemech.condition:<field>=<normalized_value>`,
  `subject_label`, `predicate_id` (`skos:exactMatch`/`closeMatch`/`broadMatch`), `object_id`,
  `object_label`, `mapping_justification`, `source`, `confidence`, `comment`. The condition
  fields are free-text strings with no ontology slot in the schema today — record the grounding
  in the SSSOM and wire it into `kgx_export.py` (organism/medium → condition-trait edges) as the
  consumption point; note any schema-slot addition as a follow-up rather than inventing one here.
- **Proposals** → only if a real, recurring preference has no METPO/PATO term. Write a cohort
  `proposals/metpo_culturemech_v1/` in the `metpo-proposal` ROBOT-template format (see
  CommunityMech's skill), `definition_source` = `CultureMech:data/normalized_yaml/<…>` (citations
  only), placeholder IDs reserved via `manage-identifiers` in the KG-Microbe METPO block,
  collision-free against the latest release. Ground the motivating media to the placeholder CURIE.

### 6. Verify + report
`just validate-products` (id↔label gate clean) · `just validate-all` (schema) ·
`just qc` (composite). For a proposal cohort, run the `metpo-proposal` column-count/parent checks.

Report, against the prior coverage (conditions are ungrounded today — baseline ≈ 0%):
- new % of each condition family grounded, and the delta;
- counts: grounded-to-METPO vs grounded-to-PATO/ENVO/UO vs proposed vs skipped-non-ontological;
- the Tier-0 bulk share vs the deep-researched share;
- the new proposal cohort summary (if any).

## Guardrails
- **METPO-maximizing, not METPO-forcing:** never ground to a METPO CURIE whose meaning doesn't
  match just to raise METPO %. A wrong grounding is worse than a residual.
- **Right layer:** categorical oxygen/temperature/pH/salinity *preferences* → METPO; raw
  numeric magnitudes and units → UO/PATO; habitats → ENVO.
- **Conditions only:** never touch ingredient/compound grounding here (that's
  `aggregate_unmapped_ingredients` + `match-kg-microbe`, MIM as source of truth).
- **Conservative proposals:** propose only genuinely reusable preference concepts; one-off
  free-text conditions are not ontology terms.
- **Don't over-research:** Tier-0 the categorical head; spend `/deep-research-medium` only on the
  ambiguous middle. Work in batches, commit per condition family, keep the diff reviewable.

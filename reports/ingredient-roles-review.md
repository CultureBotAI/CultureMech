# Ingredient roles — schema and controlled-vocabulary review

**Date:** 2026-07-19
**Reviewer:** Codex (OpenAI) via `codex:codex-rescue`
**Codex session:** `019f7cbf-0497-7301-a2a7-d2cb975c2154`
**Task specification:** `scripts/codex_prompts/review-ingredient-roles.md`
**Gold-example benchmark:** `scripts/codex_prompts/review-ingredient-roles-gold-examples.md`
**Status:** Review only — no schema edits applied.

---

## Executive summary

- The current CultureMech `IngredientRoleEnum` (14 values, flat) mixes three orthogonal axes (nutritional element supply, physicochemical function, cell-level metabolic fate) into one vocabulary. Recommend splitting into three faceted enums.
- Three vocabularies exist for the same concept and have drifted:
  - CultureMech `IngredientRoleEnum` (14 values, no `meaning:` slots)
  - MediaIngredientMech `IngredientRoleEnum` (20 values; adds 6 physicochemical/indicator terms)
  - MediaIngredientMech Python `VALID_MEDIA_ROLES` (20 values; matches MIM LinkML but drifted from CultureMech despite comment claiming sync)
- CultureMech `NutrientRoleEnum` (8 values in file; prompt miscounted as 9) covers experiment-level nutrient overrides and adds SULFUR_SOURCE, PHOSPHATE_SOURCE, LIGHT_SOURCE, OTHER not present in `IngredientRoleEnum`.
- **Actual data-corpus usage: 15,878 YAML files, 171,458 `IngredientDescriptor` records, 0 ingredient-level `role:` assignments.** The vocabulary is completely unused. Redesign has essentially no migration cost for existing data — the whole corpus will be backfilled from a blank slate.
- Recommended redesign: three orthogonal facet enums owned canonically by MIM (which owns ingredient identity + the SSSOM), imported by CultureMech. All 12 asserted ChEBI role CURIEs verified as legitimate role terms (subclasses of CHEBI:50906) via OAK against sqlite:obo:chebi.
- The existing MIM/CultureMech `CellularRoleEnum` is misnamed — its values (PRIMARY_DEGRADER, SYNERGIST, COMMENSAL, COMPETITOR…) describe organisms in a community, not ingredients. Rename to `CommunityOrganismRoleEnum` to avoid conflation with the new `CellularMetabolicRoleEnum`.
- Backfill strategy: SSSOM → CHEBI → OAK-driven role inference → diff-only proposals → curator review. Do not batch-commit.

---

## Status audit

### Inventory

| Enum / constant | File | Line | Values | Ontology mappings today |
|---|---|---|---|---|
| CultureMech `IngredientRoleEnum` | `src/culturemech/schema/culturemech.yaml` | ~2218 | 14 | None |
| CultureMech `NutrientRoleEnum` | `src/culturemech/schema/culturemech.yaml` | ~2477 | 8 | None |
| CultureMech `CellularRoleEnum` | `src/culturemech/schema/culturemech.yaml` | ~2264 | 10 | None |
| CultureMech `CofactorCategoryEnum` | `src/culturemech/schema/culturemech.yaml` | ~2250 | 5 | None |
| MIM `IngredientRoleEnum` | `MIM/src/mediaingredientmech/schema/mediaingredientmech.yaml` | ~817 | 20 | None |
| MIM `CellularRoleEnum` | `MIM/src/mediaingredientmech/schema/mediaingredientmech.yaml` | ~861 | 10 | None |
| MIM Python `VALID_MEDIA_ROLES` | `MIM/src/mediaingredientmech/curation/ingredient_curator.py` | 48 | 20 | N/A |
| MIM Python `VALID_CELLULAR_ROLES` | `MIM/src/mediaingredientmech/curation/ingredient_curator.py` | 73 | 10 | N/A |

Slot bindings:
- `IngredientDescriptor.role` — `culturemech.yaml:824`, `multivalued: true`, `recommended: true`, range `IngredientRoleEnum`.
- `NutrientOverride.role` — `culturemech.yaml:1374`, range `NutrientRoleEnum`.
- MIM `IngredientRecord.media_roles` — `mediaingredientmech.yaml:118`, range `MediaRoleAssignment`.
- MIM `IngredientRecord.cellular_roles` — `mediaingredientmech.yaml:123`, range `CellularRoleAssignment`.

### Drift matrix (ingredient / media-role vocabularies)

Legend: ✓ present, — absent.

| Token | CultureMech `IngredientRoleEnum` | CultureMech `NutrientRoleEnum` | MIM `IngredientRoleEnum` | MIM Python `VALID_MEDIA_ROLES` |
|---|---|---|---|---|
| CARBON_SOURCE | ✓ | ✓ | ✓ | ✓ |
| NITROGEN_SOURCE | ✓ | ✓ | ✓ | ✓ |
| SULFUR_SOURCE | — | ✓ | — | — |
| PHOSPHATE_SOURCE | — | ✓ | — | — |
| ENERGY_SOURCE | ✓ | — | ✓ | ✓ |
| ELECTRON_DONOR | ✓ | ✓ | ✓ | ✓ |
| ELECTRON_ACCEPTOR | ✓ | ✓ | ✓ | ✓ |
| LIGHT_SOURCE | — | ✓ | — | — |
| MINERAL | ✓ | — | ✓ | ✓ |
| TRACE_ELEMENT | ✓ | — | ✓ | ✓ |
| BUFFER | ✓ | — | ✓ | ✓ |
| VITAMIN_SOURCE | ✓ | — | ✓ | ✓ |
| SALT | ✓ | — | ✓ | ✓ |
| PROTEIN_SOURCE | ✓ | — | ✓ | ✓ |
| AMINO_ACID_SOURCE | ✓ | — | ✓ | ✓ |
| SOLIDIFYING_AGENT | ✓ | — | ✓ | ✓ |
| COFACTOR_PROVIDER | ✓ | — | ✓ | ✓ |
| REDOX_INDICATOR | — | — | ✓ | ✓ |
| PH_INDICATOR | — | — | ✓ | ✓ |
| SELECTIVE_AGENT | — | — | ✓ | ✓ |
| SURFACTANT | — | — | ✓ | ✓ |
| REDUCING_AGENT | — | — | ✓ | ✓ |
| CHELATOR | — | — | ✓ | ✓ |
| OTHER | — | ✓ | — | — |

**Findings:**
- 6 values in MIM that CultureMech `IngredientRoleEnum` lacks: `REDOX_INDICATOR`, `PH_INDICATOR`, `SELECTIVE_AGENT`, `SURFACTANT`, `REDUCING_AGENT`, `CHELATOR` (the physicochemical / indicator cluster).
- 3 element-supply values in `NutrientRoleEnum` missing from `IngredientRoleEnum`: `SULFUR_SOURCE`, `PHOSPHATE_SOURCE`, `LIGHT_SOURCE`.
- MIM Python constant exactly matches MIM LinkML (no drift within MIM), but has drifted from CultureMech.
- CARBON_SOURCE / ENERGY_SOURCE overlap is a real semantic issue the schema already admits; the faceted redesign keeps both because heterotrophic sugars legitimately carry both simultaneously.

### Corpus usage

`data/normalized_yaml/**/*.yaml`:

- 15,878 YAML files
- 171,458 ingredient descriptors
- **0 ingredient-level `role:` assignments**

The initial hand-grep that found "2 assignments" hit `role:` tokens elsewhere in the corpus (e.g. `role:` on `NutrientOverride`, comments), not on `IngredientDescriptor`. **Every ingredient in the corpus is currently role-blank.** Migration cost for existing data ≈ zero. Backfill from scratch.

### Representative-ingredient anchor rows (from MIM SSSOM)

SSSOM file: `MediaIngredientMech/mappings/ingredient_mappings.sssom.tsv` (note: not `MIM/mappings/...` — my prompt had a stale path).

| # | Ingredient | MIM subject | Predicate | Object | Object label |
|---|---|---|---|---|---|
| 1 | Glucose | `MIM:Glucose` | `skos:exactMatch` | `CHEBI:17234` | glucose |
| 2 | Agar | `MIM:Agar` | `skos:exactMatch` | `CHEBI:2509` | agar |
| 3 | Resazurin | `MIM:Resazurin` | `skos:exactMatch` | `CHEBI:8806` | Resazurin |
| 4 | EDTA | `MIM:Edta` | `skos:exactMatch` | `CHEBI:64755` | EDTA(2-) |
| 5 | L-cysteine | `MIM:L-cysteine` | `skos:exactMatch` | `CHEBI:17561` | L-cysteine |
| 6 | Ammonium chloride | `MIM:Ammonium_Chloride_Nitrogen_Source` | `skos:exactMatch` | `CHEBI:31206` | ammonium chloride |
| 7 | K2HPO4 | `MIM:K2hpo4` | `skos:exactMatch` | `CHEBI:131527` | dipotassium hydrogen phosphate |
| 8 | Thiamine PP | `MIM:02_Thiamine_Pyrophosphate` | `skos:exactMatch` | `CHEBI:9532` | thiamine(1+) diphosphate |
| 9 | Sodium sulfide | `MIM:Na2s` | `skos:closeMatch` | `CHEBI:76208` | sodium sulfide (anhydrous) |
| 10 | Methanol | `MIM:Methanol` | `skos:exactMatch` | `CHEBI:17790` | methanol |

Every default backfill assignment must be traceable through one of these SSSOM anchors + a ChEBI axiom.

### Semantic / boundary observations

- The current flat `IngredientRoleEnum` mixes: element supply (CARBON_SOURCE, NITROGEN_SOURCE), vitamin/cofactor supply (VITAMIN_SOURCE, COFACTOR_PROVIDER), physicochemical function (BUFFER, SOLIDIFYING_AGENT — also REDUCING_AGENT, CHELATOR, SURFACTANT in MIM), indicators (PH_INDICATOR, REDOX_INDICATOR in MIM), selective/antimicrobial (SELECTIVE_AGENT in MIM), and metabolic-role-in-cell (ELECTRON_DONOR, ELECTRON_ACCEPTOR). These are four different axes and should be separately assignable.
- ELECTRON_DONOR / ELECTRON_ACCEPTOR are the strongest evidence for splitting: Na₂S is a reducing agent + sulfur source in *every* anaerobic medium, but only an electron donor for the *organism* if that organism is a sulfide oxidiser. Whether a compound is an electron donor is a fact about the organism, not the medium.
- `CellularRoleEnum` (both repos, 10 values: PRIMARY_DEGRADER, REDUCTIVE_DEGRADER, OXIDATIVE_DEGRADER, BIOTRANSFORMER, SYNERGIST, BRIDGE_ORGANISM, ELECTRON_SHUTTLE, DETOXIFIER, COMMENSAL, COMPETITOR) describes an organism's role in a community, not a cell-level attribute and not an ingredient attribute. Recommend renaming to `CommunityOrganismRoleEnum`.
- `CofactorCategoryEnum` is a taxonomy of cofactor *types* (VITAMINS, METALS, NUCLEOTIDES, ENERGY_TRANSFER, OTHER_SPECIALIZED), not a role facet — keep it distinct.

---

## Proposed vocabulary

Three orthogonal facet enums. All 12 asserted CHEBI CURIEs verified against `sqlite:obo:chebi` via `runoak` — all are legitimate role terms under `CHEBI:50906`.

### `NutritionalRoleEnum` — element / macronutrient supply

```yaml
NutritionalRoleEnum:
  description: What element or macronutrient the ingredient supplies to the medium.
  permissible_values:
    CARBON_SOURCE:      {meaning: TBD, mappings: [METPO:2000006]}
    NITROGEN_SOURCE:    {meaning: TBD, mappings: [METPO:2000014]}
    SULFUR_SOURCE:      {meaning: TBD, mappings: [METPO:2000020]}
    PHOSPHATE_SOURCE:   {meaning: TBD}
    IRON_SOURCE:        {meaning: TBD}
    TRACE_ELEMENT:      {meaning: TBD}
    VITAMIN_SOURCE:     {meaning: CHEBI:33229}   # vitamin (role)
    AMINO_ACID_SOURCE:  {meaning: TBD, mappings: [CHEBI:33709]}
    PROTEIN_SOURCE:     {meaning: TBD, mappings: [CHEBI:36080]}
    COFACTOR_PROVIDER:  {meaning: TBD, mappings: [CHEBI:23357]}
    ENERGY_SOURCE:      {meaning: TBD, mappings: [METPO:2000010]}
    LIGHT_SOURCE:       {meaning: TBD, mappings: [METPO:1000656]}
```

Notes: ChEBI does not carry clean "X source" role terms for elemental supply (CARBON_SOURCE, NITROGEN_SOURCE, etc.) — these are pragmatic curation categories. METPO candidates are marked as secondary `mappings:`; where METPO is a good fit, promote to `meaning:` after review. Element-supply terms with neither ChEBI nor METPO candidates (PHOSPHATE_SOURCE, IRON_SOURCE, TRACE_ELEMENT) are METPO-proposal candidates.

### `PhysicochemicalRoleEnum` — chemical / physical job in the recipe

```yaml
PhysicochemicalRoleEnum:
  description: >-
    Chemical or physical function the ingredient performs in the medium,
    independent of what element it supplies.
  permissible_values:
    BUFFER:                  {meaning: CHEBI:35225}   # buffer
    SOLIDIFYING_AGENT:       {meaning: TBD}
    CHELATOR:                {meaning: CHEBI:38161}   # chelator
    SURFACTANT:              {meaning: CHEBI:35195, mappings: [CHEBI:63046]}   # surfactant
    REDUCING_AGENT:          {meaning: CHEBI:63247}   # reducing agent
    OXIDIZING_AGENT:         {meaning: CHEBI:63248}   # oxidising agent
    PH_INDICATOR:            {meaning: CHEBI:50407}   # acid-base indicator
    REDOX_INDICATOR:         {meaning: TBD, mappings: [CHEBI:47867]}
    SELECTIVE_AGENT:         {meaning: TBD, mappings: [CHEBI:33281, CHEBI:33282, CHEBI:35718]}
    ANTIFOAM:                {meaning: CHEBI:77973}   # antifoaming agent
    OSMOTIC_AGENT:           {meaning: TBD, mappings: [CHEBI:25728]}
    PRECIPITATION_INHIBITOR: {meaning: TBD}
```

Notes: 8 of 12 values have a verified ChEBI role term. `SOLIDIFYING_AGENT` is a persistent gap — ChEBI has no "solidifying agent" role, this is a media-specific curation term.

### `CellularMetabolicRoleEnum` — role of the ingredient in / on the cultured microbe

```yaml
CellularMetabolicRoleEnum:
  description: >-
    What the ingredient does inside or to the cultured microbe(s) — its
    metabolic fate or biochemical function at the cell level.
    Values in this facet are often organism-conditional (e.g. ELECTRON_DONOR
    applies only for organisms that oxidise the compound for energy).
  permissible_values:
    SUBSTRATE:                  {meaning: TBD}
    ELECTRON_DONOR:             {meaning: CHEBI:15022}   # electron donor
    ELECTRON_ACCEPTOR:          {meaning: CHEBI:17654}   # electron acceptor
    COFACTOR:                   {meaning: CHEBI:23357}   # cofactor
    PROSTHETIC_GROUP_PRECURSOR: {meaning: TBD, mappings: [CHEBI:26348]}
    MEMBRANE_COMPONENT:         {meaning: TBD}
    OSMOPROTECTANT:             {meaning: TBD, mappings: [CHEBI:25728]}
    INDUCER:                    {meaning: TBD}
    INHIBITOR:                  {meaning: CHEBI:35222}   # inhibitor
    QUENCHER:                   {meaning: TBD}
    NONE:                       {meaning: TBD}
```

Notes: 4 of 11 have verified ChEBI role terms. `SUBSTRATE`, `MEMBRANE_COMPONENT`, `INDUCER`, `QUENCHER`, `NONE` are pragmatic curation categories without clean ChEBI equivalents.

### Rename recommendation

`CellularRoleEnum` → `CommunityOrganismRoleEnum` (or `EcologicalRoleEnum`). Keep its 10 permissible values; only the class name changes. Reason: current name conflicts with `CellularMetabolicRoleEnum` and is misleading (values describe organisms in communities, not cells).

### `NutrientRoleEnum` reconciliation

Merge overlapping values into `NutritionalRoleEnum`. If the experiment-level nutrient-override concept is genuinely distinct from ingredient-level nutritional supply, keep `NutrientRoleEnum` narrowed to just that role but populate it from `NutritionalRoleEnum` (import). Otherwise, retire.

### Gold-example expressibility check

All 10 gold examples from the benchmark file are expressible under the three-facet redesign:

| # | Ingredient | Nutritional | Physicochemical | Cellular-metabolic |
|---|---|---|---|---|
| 1 | Glucose | CARBON_SOURCE, ENERGY_SOURCE | — | SUBSTRATE |
| 2 | Agar | — | SOLIDIFYING_AGENT | NONE |
| 3 | Resazurin | — | REDOX_INDICATOR | NONE |
| 4 | EDTA | — | CHELATOR | NONE *(INHIBITOR conditional)* |
| 5 | L-cysteine | AMINO_ACID_SOURCE, SULFUR_SOURCE | REDUCING_AGENT | SUBSTRATE |
| 6 | NH₄Cl | NITROGEN_SOURCE | — | SUBSTRATE |
| 7 | K₂HPO₄ | PHOSPHATE_SOURCE | BUFFER *(paired)* | SUBSTRATE |
| 8 | Thiamine PP | VITAMIN_SOURCE, COFACTOR_PROVIDER | — | COFACTOR |
| 9 | Na₂S | SULFUR_SOURCE | REDUCING_AGENT | SUBSTRATE + ELECTRON_DONOR *(conditional: sulfide oxidisers)* |
| 10 | Methanol | CARBON_SOURCE, ENERGY_SOURCE | — | SUBSTRATE, ELECTRON_DONOR *(methylotrophs)* |

The redesign satisfies all six scoring criteria in the benchmark file: every gold value is expressible; multi-facet ingredients (cysteine, K₂HPO₄, TPP) resolve across all three enums simultaneously; organism-conditional cellular-metabolic roles are on their own facet; inert ingredients (agar, resazurin, EDTA) carry no nutritional defaults; recipe-conditional roles (K₂HPO₄ BUFFER, NH₄Cl SALT) stay on the CultureMech recipe-override layer.

### Model shape

- Keep LinkML `permissible_values` with `meaning:` slots. Rationale: preserves IDE support, documentation, and validator ergonomics; enum drift is manageable across three enums with one canonical owner.
- Add companion `role_curie` slot on `IngredientDescriptor` (typed `uriorcurie`) as an escape hatch for outside-vocabulary role terms, with a validator rule requiring the CURIE resolve within ChEBI role subtree or an accepted fallback namespace (METPO, ENVO, GO, PATO, NCIT, CHMO).
- MIM `MediaRoleAssignment` class extends analogously to per-facet subclasses (`NutritionalRoleAssignment`, `PhysicochemicalRoleAssignment`, `CellularMetabolicRoleAssignment`) each carrying role + confidence + evidence.

### Layering — MIM default vs CultureMech override

- **MIM ingredient records** carry canonical / default role assignments that apply to the compound whenever it appears in a medium (glucose is always `[CARBON_SOURCE, ENERGY_SOURCE]` + `[SUBSTRATE]`).
- **CultureMech `IngredientDescriptor`** carries recipe-specific overrides or additions. Resolution rule: inherit MIM defaults unless the recipe explicitly overrides on a given facet.

---

## Migration plan

1. **Land the three facet enums in MIM.** File: `MIM/src/mediaingredientmech/schema/mediaingredientmech.yaml`. Add `NutritionalRoleEnum`, `PhysicochemicalRoleEnum`, `CellularMetabolicRoleEnum` with `meaning:` values verified above. Add `NutritionalRoleAssignment`, `PhysicochemicalRoleAssignment`, `CellularMetabolicRoleAssignment` classes and matching slots (`nutritional_roles`, `physicochemical_roles`, `cellular_metabolic_roles`) on `IngredientRecord`. Regenerate MIM's derived Python.
2. **Delete manual `VALID_MEDIA_ROLES` set.** File: `MIM/src/mediaingredientmech/curation/ingredient_curator.py:48`. Replace with a constant derived from the LinkML enum (import `PermissibleValue`s at module load). Update `add_media_role(...)` → three new methods `add_nutritional_role`, `add_physicochemical_role`, `add_cellular_metabolic_role` with per-facet validation.
3. **Rename `CellularRoleEnum` → `CommunityOrganismRoleEnum`.** Files: MIM and CultureMech schemas, MIM curator Python constant `VALID_CELLULAR_ROLES`. Small standalone PR, safe to land before the facet split.
4. **Import MIM enums into CultureMech.** File: `src/culturemech/schema/culturemech.yaml`. Add `imports:` entry for MIM. Replace `IngredientDescriptor.role` (line 824) with three faceted slots + `role_curie` escape hatch. Reconcile or retire `NutrientRoleEnum` (my recommendation: merge overlapping values into `NutritionalRoleEnum`).
5. **Add validator rule.** New rule in the `audit-schema-gaps` harness: flag any `IngredientDescriptor` with a MIM SSSOM mapping (resolvable via `ingredient_mappings.sssom.tsv`) but no `nutritional_roles` or `cellular_metabolic_roles` assignment.
6. **Author backfill script.** New file under `scripts/`. Reads MIM SSSOM → resolves each ingredient to CHEBI → applies OAK-driven ChEBI hierarchy + `has_role` axioms to seed facet defaults → emits a diff of proposed assignments per record. Diff-only; commit nothing without curator review.
7. **Update developer docs.** Describe the faceted role model, MIM SSSOM as ingredient-identity anchor, and MIM-default vs CultureMech-override resolution rule.

---

## Open questions / risks

- **Enum ownership.** Recommendation: MIM owns. Alternative: CultureMech owns and MIM imports. Deciding factor is which repo more actively evolves the vocabulary — MIM has more values today (20 vs 14) and owns the ingredient identity layer, so MIM-owns is the natural choice. Confirm before step 1.
- **`NutrientRoleEnum` fate.** Merge into `NutritionalRoleEnum` (simpler) vs. keep as a narrowed experiment-override facet (preserves the distinction between "supplied in the recipe" and "designated experimental variable"). No usage data in the corpus to inform this — decide from curation intent.
- **`CofactorCategoryEnum`.** Keep as a compound taxonomy (VITAMINS, METALS, NUCLEOTIDES, ENERGY_TRANSFER, OTHER_SPECIALIZED); do not fold into role facets.
- **`SALT` disposition.** Currently in both `IngredientRoleEnum` and MIM's `IngredientRoleEnum`. Under the faceted split, is it nutritional (ionic contribution to biomass) or physicochemical (osmotic contribution)? Recommend physicochemical (`OSMOTIC_AGENT`) with a `NutritionalRoleEnum` element assignment when the salt's cation or anion is nutritionally relevant (NH₄Cl → NITROGEN_SOURCE + optionally OSMOTIC_AGENT at high concentration; NaCl → OSMOTIC_AGENT only at typical concentrations).
- **`MINERAL` disposition.** Retire and replace with specific element-source values (PHOSPHATE_SOURCE + IRON_SOURCE + explicit trace elements). Verify no curator relies on MINERAL as a catch-all.
- **CHEBI `has_role` axiom coverage.** ChEBI carries structural is-a hierarchies well, but `has_role` axioms are patchier. Backfill rule set will need per-compound review for cases the ontology does not cover (e.g. no ChEBI has-role axiom links resazurin → redox indicator explicitly; may need to key off ChEBI:47867 subclass check).
- **METPO submissions.** All `meaning: TBD` values in `NutritionalRoleEnum` (element-source roles) and several physicochemical / cellular-metabolic values are METPO-proposal candidates. Recommend batching a METPO submission after the initial schema lands, to fill in the TBDs.

---

## Appendix — CHEBI CURIE verification

Verified with `runoak -i sqlite:obo:chebi`; `is role?` means ancestors include `CHEBI:50906`. All 12 asserted CURIEs confirmed as legitimate role terms.

| CURIE | Asserted use | Actual ChEBI label | Is role? | Notes |
|---|---|---|---|---|
| CHEBI:63247 | REDUCING_AGENT | reducing agent | Yes | Correct. |
| CHEBI:63248 | OXIDIZING_AGENT | oxidising agent | Yes | Correct. Original review prompt suggested this for reducing agent — the prompt was wrong. |
| CHEBI:15022 | ELECTRON_DONOR | electron donor | Yes | Correct; not magnesium(2+) as I initially suspected. |
| CHEBI:17654 | ELECTRON_ACCEPTOR | electron acceptor | Yes | Correct; not 5'-deoxyadenosine as I initially suspected. |
| CHEBI:33229 | VITAMIN_SOURCE | vitamin (role) | Yes | Semantic caveat — role is "vitamin", not "vitamin source". |
| CHEBI:35225 | BUFFER | buffer | Yes | Correct. |
| CHEBI:38161 | CHELATOR | chelator | Yes | Correct. |
| CHEBI:35195 | SURFACTANT | surfactant | Yes | Correct. |
| CHEBI:50407 | PH_INDICATOR | acid-base indicator | Yes | Correct. |
| CHEBI:77973 | ANTIFOAM | antifoaming agent | Yes | Correct. |
| CHEBI:23357 | COFACTOR / COFACTOR_PROVIDER | cofactor | Yes | Exact match for cellular COFACTOR; only related for medium-side COFACTOR_PROVIDER (which is a "provider of…" concept ChEBI does not carry). |
| CHEBI:35222 | INHIBITOR | inhibitor | Yes | Correct. |

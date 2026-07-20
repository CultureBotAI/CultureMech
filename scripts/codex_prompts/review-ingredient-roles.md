<role>
You are Codex performing a schema / controlled-vocabulary review for the CultureMech project (LinkML-based growth-media curation feeding KG-Microbe).
Your job is to audit the current representation of *ingredient roles* — covering BOTH the ingredient's role in the growth medium (formulation-side) AND its role in / on the cultured microbe(s) (metabolic-side) — catch drift and gaps, and propose a re-representation with an ontology-grounded controlled vocabulary.
The primary source of ontology identity for ingredients is the MediaIngredientMech SSSOM (`MIM/mappings/ingredient_mappings.sssom.tsv`), which resolves MIM ingredient records to CHEBI/FOODON/ENVO/NCIT/MICRO/UBERON/CAS. All role mappings must anchor off that SSSOM: an ingredient's role candidates are derived from its mapped ontology ID (usually CHEBI) via the ontology's own role hierarchy and structural taxonomy.
Bias toward evidence-based recommendations grounded in the actual files and enum values, not general opinion about ontologies.
</role>

<task>
Deliver an actionable review + redesign for how ingredient roles are modelled across the CultureMech ecosystem. The output must include:
1. A status audit of the current role vocabularies (what exists, where, and how consistently).
2. A proposed re-representation as a **faceted** controlled vocabulary:
   - `NutritionalRoleEnum` (medium-side, elemental / macronutrient supply — CARBON_SOURCE, NITROGEN_SOURCE, PHOSPHATE_SOURCE, ...)
   - `PhysicochemicalRoleEnum` (medium-side, functional / chemical job — BUFFER, CHELATOR, SURFACTANT, REDOX_INDICATOR, ...)
   - `CellularMetabolicRoleEnum` (organism-side, what the ingredient does *in / on* the cultured microbe — SUBSTRATE, COFACTOR, ELECTRON_DONOR, ELECTRON_ACCEPTOR, OSMOPROTECTANT, INDUCER, INHIBITOR, MEMBRANE_COMPONENT, ...)
   Every value carries a `meaning:` CURIE and, where useful, secondary `mappings:`. ChEBI-first (its `role` branch under CHEBI:50906 is the primary target); METPO / ENVO / GO / PATO / NCIT / CHMO as fallbacks.
3. A concrete migration path for schema, curator code, and existing YAML instances that references the MIM SSSOM as the ingredient-identity source of truth.
</task>

<naming_note>
The existing enum `CellularRoleEnum` (MIM `src/mediaingredientmech/schema/mediaingredientmech.yaml:861`, mirrored in `CultureMech/src/culturemech/schema/culturemech.yaml:2264`) is **misnamed**: its permissible values (PRIMARY_DEGRADER, SYNERGIST, COMMENSAL, COMPETITOR, BRIDGE_ORGANISM, ELECTRON_SHUTTLE, DETOXIFIER, …) describe the role of an *organism within a microbial community* — not a role of an ingredient at the cell level, and not a role of an organism as a single cell in isolation. Treat it as a **community-level organism role** enum and call it out for renaming (`CommunityOrganismRoleEnum` or `EcologicalRoleEnum`). This review does NOT overhaul that enum, but must:
- Recommend the rename, so it does not get conflated with the new `CellularMetabolicRoleEnum`.
- Make crystal clear the axis distinction: `CellularMetabolicRoleEnum` is a facet of *ingredient*, describing its metabolic fate in / effect on cells; the misnamed `CellularRoleEnum` is a facet of *organism* in a community.
</naming_note>

<scope_and_files>
Primary artifacts to read (repo roots on disk):
- CultureMech: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech`
- MediaIngredientMech (MIM): `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MediaIngredientMech`

Files to open and cite by file:line:

CultureMech schema:
- `src/culturemech/schema/culturemech.yaml`
  - `IngredientRoleEnum` at ~line 2218 (14 values; no `meaning:` slots) — attached to `IngredientDescriptor.role` at ~line 824 (`multivalued: true`, `recommended: true`).
  - `NutrientRoleEnum` at ~line 2477 (9 values, adds SULFUR_SOURCE, PHOSPHATE_SOURCE, LIGHT_SOURCE, OTHER) — attached to `NutrientOverride.role` at ~line 1374.
  - `CellularRoleEnum` at ~line 2264 (community-level; see naming note).
  - `CofactorCategoryEnum` at ~line 2250 — evaluate whether it duplicates a role facet or is a genuinely distinct compound taxonomy.
- `src/culturemech/schema/mapped_ingredients_schema.yaml`, `unmapped_ingredients_schema.yaml` — confirm no role field exists here (grep found none, but verify).

MIM schema + curator:
- `src/mediaingredientmech/schema/mediaingredientmech.yaml`
  - `IngredientRoleEnum` at ~line 817 (**20 values** — 6 more than CultureMech: REDOX_INDICATOR, PH_INDICATOR, SELECTIVE_AGENT, SURFACTANT, REDUCING_AGENT, CHELATOR).
  - `CellularRoleEnum` at ~line 861 (community organism roles, as above).
  - `media_roles` slot on ingredient record at ~line 118; `cellular_roles` at ~line 123.
  - `role_inheritance` slot at ~line 198 (parent/child ingredient variants inherit media roles) — the review must preserve this semantics.
  - `MediaRoleAssignment` class at ~line 482 (role + confidence + evidence); `CellularRoleAssignment` at ~line 500.
- `src/mediaingredientmech/curation/ingredient_curator.py`
  - `VALID_MEDIA_ROLES` at line 48 (20 values, comment at line 63 claims sync with LinkML — verify it matches MIM's LinkML but has **drifted from CultureMech's LinkML**).
  - `VALID_CELLULAR_ROLES` at line 73.
  - `add_media_role(...)` at line 447, `add_cellular_role(...)` at line 537.

**Primary ontology source — MIM SSSOM:**
- `MIM/mappings/ingredient_mappings.sssom.tsv` (~2200 rows). Columns: `subject_id` (MIM:*) → `object_id` (CHEBI / FOODON / ENVO / NCIT / MICRO / UBERON / CAS / mesh) via `predicate_id` (mostly `skos:exactMatch`, some narrow/broad/closeMatch). Ontology distribution to expect: ~1457 CHEBI, 248 CAS, 202 kgmicrobe.compound, 86 mesh, 64 NCIT, 50 MICRO, 43 FOODON, 32 kgmicrobe.ingredient, 15 ENVO, 2 UBERON.
- Treat this SSSOM as the **canonical ingredient identity resolver**. When Codex proposes role mappings for individual example ingredients (glucose, agar, resazurin, EDTA, cysteine, NH4Cl, K2HPO4, thiamine PP), it must trace each ingredient to its MIM ID via this SSSOM, take the resolved CHEBI (or FOODON) CURIE from the SSSOM, and then derive candidate role terms from that resolved ontology entry — not from ad-hoc guesses.

CultureMech data corpus:
- `data/normalized_yaml/**/*.yaml` — grep for `role:` under ingredient blocks. Report actual usage counts. (Initial grep finds only ~2 explicit assignments across the corpus, so usage is near-zero; confirm.)
</scope_and_files>

<status_audit>
Produce a structured status audit answering:

1. **Inventory.** Every role-related enum / constant in CultureMech and MIM, with exact file:line, count of values, and whether it carries `meaning:` / `mappings:` slots today. Explicitly note that no `meaning:` slots appear on any of these role enums, unless you find otherwise.

2. **Drift matrix.** A table of role tokens × columns:
   - CultureMech `IngredientRoleEnum`
   - CultureMech `NutrientRoleEnum`
   - MIM `IngredientRoleEnum`
   - MIM `VALID_MEDIA_ROLES` (Python)
   Mark each cell present / absent / renamed. Explicitly call out:
   - The 6 values in MIM but not CultureMech (REDOX_INDICATOR, PH_INDICATOR, SELECTIVE_AGENT, SURFACTANT, REDUCING_AGENT, CHELATOR).
   - The 3 element/energy values in `NutrientRoleEnum` missing from `IngredientRoleEnum` (SULFUR_SOURCE, PHOSPHATE_SOURCE, LIGHT_SOURCE).
   - The CARBON_SOURCE / ENERGY_SOURCE conceptual overlap already flagged in the schema.
   - Whether MIM `VALID_MEDIA_ROLES` matches MIM's own LinkML `IngredientRoleEnum` (should — but verify).

3. **Usage.** In `data/normalized_yaml/**`, how many `IngredientDescriptor` records actually carry a `role:` value? Top-N distribution? Fraction of ingredients with zero role assignments? Any free-text or lower-case role values escaping the enum? Report absolute numbers.

4. **Semantic coherence.** Point out where a single ingredient legitimately has multiple simultaneous roles (glucose = CARBON_SOURCE + ENERGY_SOURCE; NH4Cl = NITROGEN_SOURCE + SALT; EDTA = CHELATOR + potentially TRACE_METAL_CONTROL; cysteine = REDUCING_AGENT + AMINO_ACID_SOURCE + SULFUR_SOURCE). Confirm the CultureMech slot supports `multivalued: true` (it does at line 827). Note where the current flat enum forces a curator to pick one when multiple apply.

5. **Boundary confusions / mixed axes.** Flag values that mix orthogonal facets:
   - Element supply (CARBON_SOURCE, NITROGEN_SOURCE, SULFUR_SOURCE, PHOSPHATE_SOURCE)
   - Vitamin / cofactor supply (VITAMIN_SOURCE, COFACTOR_PROVIDER)
   - Physicochemical function (BUFFER, SOLIDIFYING_AGENT, REDUCING_AGENT, CHELATOR, SURFACTANT)
   - Indicator (PH_INDICATOR, REDOX_INDICATOR)
   - Selective / antimicrobial (SELECTIVE_AGENT)
   - Metabolic role in cell (ELECTRON_DONOR, ELECTRON_ACCEPTOR — currently in `IngredientRoleEnum`, but arguably belongs on the *cellular-metabolic* facet)
   The last bullet is the strongest evidence that a facet split is warranted.

6. **Anchor to MIM SSSOM.** Pick 5-10 representative ingredients (glucose, agar, resazurin, EDTA, cysteine, NH4Cl, K2HPO4, thiamine pyrophosphate, sodium sulfide, methanol). For each, look up the row in `MIM/mappings/ingredient_mappings.sssom.tsv`, cite `subject_id → predicate_id → object_id (object_label)`, and show which of the current CultureMech / MIM enum values *should* apply. This grounds the redesign in real data.
</status_audit>

<re_representation_proposal>
Propose a concrete redesign with these constraints:

1. **Single source of truth per facet.** For each new facet enum, exactly one canonical LinkML definition (living in CultureMech schema, imported by MIM — or vice versa). No duplicated Python set: the MIM curator's `VALID_MEDIA_ROLES` disappears in favour of a constant generated from the LinkML enum. Show how (LinkML `PermissibleValue` iteration; or a tiny helper that reads the schema at import time).

2. **Faceted vocabulary** — three enums, orthogonal:
   - **`NutritionalRoleEnum`** (facet: element / macronutrient supply the ingredient contributes to the medium):
     `CARBON_SOURCE, NITROGEN_SOURCE, SULFUR_SOURCE, PHOSPHATE_SOURCE, IRON_SOURCE, TRACE_ELEMENT, VITAMIN_SOURCE, AMINO_ACID_SOURCE, PROTEIN_SOURCE, COFACTOR_PROVIDER, ENERGY_SOURCE, LIGHT_SOURCE`
     (ENERGY_SOURCE and CARBON_SOURCE stay separate; document that heterotrophic sugars will typically carry both.)
   - **`PhysicochemicalRoleEnum`** (facet: chemical / physical job the ingredient does in the recipe, independent of what element it supplies):
     `BUFFER, SOLIDIFYING_AGENT, CHELATOR, SURFACTANT, REDUCING_AGENT, OXIDIZING_AGENT, PH_INDICATOR, REDOX_INDICATOR, SELECTIVE_AGENT, ANTIFOAM, OSMOTIC_AGENT, PRECIPITATION_INHIBITOR`
   - **`CellularMetabolicRoleEnum`** (facet: what the ingredient does *in* or *to* the cultured microbe(s) — its metabolic fate / biochemical function inside the cell). Draft values:
     `SUBSTRATE` (metabolized carbon or electron substrate consumed by the cell),
     `ELECTRON_DONOR`, `ELECTRON_ACCEPTOR` (in the organism's energy metabolism — note these move here off `IngredientRoleEnum`),
     `COFACTOR` (used by cellular enzymes; distinct from COFACTOR_PROVIDER which is a medium-side supply role),
     `PROSTHETIC_GROUP_PRECURSOR`,
     `MEMBRANE_COMPONENT` (lipid / lipopolysaccharide precursor incorporated into cell envelope),
     `OSMOPROTECTANT`,
     `SIGNALING_MOLECULE` / `INDUCER`,
     `INHIBITOR` (e.g. antibiotics used as selective agents that also act on the cell),
     `QUENCHER` (for reactive species),
     `NONE` (present in medium but not metabolized or interacting — inert osmotic filler).

3. **Community organism role — rename existing `CellularRoleEnum`.** Recommend renaming it (e.g. `CommunityOrganismRoleEnum`) and note that it stays a separate concern — it describes organisms, not ingredients. Do not fold it into the ingredient facets.

4. **Ontology grounding — MIM SSSOM anchor, ChEBI role branch primary.**
   For every proposed permissible value, provide a candidate `meaning:` CURIE, drawn from ChEBI's role hierarchy under **CHEBI:50906 (role)**:
   - `CHEBI:24432` biological role (parent for cofactor, electron donor/acceptor, vitamin, growth substrate, …)
   - `CHEBI:33232` application (parent for buffer, culture medium component, …)
   - Chemical role subtree of CHEBI:50906
   Candidate targets to *verify* before asserting (Codex must confirm each ID exists and its label matches, else write `TBD`):
     - buffer → CHEBI:35225
     - electron donor → CHEBI:17499
     - electron acceptor → CHEBI:15339
     - cofactor → CHEBI:23357
     - chelator → CHEBI:38161
     - surfactant → CHEBI:35195
     - reducing agent → CHEBI:63248 *(verify)*
     - pH indicator → CHEBI:75220 *(verify)*
     - redox indicator → check ChEBI
     - antioxidant → CHEBI:22586
     - osmolyte / osmoprotectant → check ChEBI
   For element-source roles (CARBON_SOURCE, NITROGEN_SOURCE, SULFUR_SOURCE, PHOSPHATE_SOURCE, IRON_SOURCE) ChEBI generally has *no* clean "X source" role term — these are pragmatic curation categories. Codex should:
     - Check whether MCO / MICRO / METPO / ENVO has an "X source" or "nutrient of type X" concept.
     - If none, keep the value in the enum but mark `meaning: TBD` and log an ontology-request candidate (METPO submission target). Do not force-fit.

   For every representative ingredient chosen in status audit §6, produce a concrete mapping table row of the form:
     `MIM:<subject_id> (label) → CHEBI:<id> (from SSSOM) → proposed roles: [NutritionalRoleEnum:CARBON_SOURCE (meaning=TBD), CellularMetabolicRoleEnum:SUBSTRATE (meaning=CHEBI:...)]`

5. **Model shape.** Recommend a specific shape (do not present a menu):
   - Keep LinkML `permissible_values` with `meaning:` slots on each facet enum. Rationale: keeps documentation, IDE support, and validator ergonomics; enum drift is manageable at three enums.
   - Add a companion `role_curie` free slot on `IngredientDescriptor` typed as CURIE (a genuinely-outside-the-vocabulary escape hatch), with a validator rule: `role_curie` should resolve within the ChEBI role subtree or an accepted fallback ontology namespace.

6. **Ingredient-level (MIM) vs recipe-level (CultureMech) role assignment.** Clarify the layering:
   - **MIM ingredient records** carry *default / canonical* roles that apply to the compound whenever it appears in a medium (glucose is always CARBON_SOURCE + ENERGY_SOURCE + SUBSTRATE).
   - **CultureMech `IngredientDescriptor.role`** carries *recipe-specific* overrides or additions (e.g. glucose used at 0.1% in a selective medium may not be the primary carbon source; NH4Cl in a high-salt buffer variant may functionally act as SALT + BUFFER even if its default is NITROGEN_SOURCE).
   Provide a resolution rule (inherit MIM defaults unless recipe explicitly overrides).

7. **Multi-role guidance.** Short curator rule: "assign every applicable value from every facet. Glucose gets `NutritionalRoleEnum: [CARBON_SOURCE, ENERGY_SOURCE]` and `CellularMetabolicRoleEnum: [SUBSTRATE]`. Cysteine gets `NutritionalRoleEnum: [AMINO_ACID_SOURCE, SULFUR_SOURCE]` + `PhysicochemicalRoleEnum: [REDUCING_AGENT]`."

8. **Backfill strategy.** Given that only ~2 records currently carry a role:
   - Pass 1: MIM SSSOM → CHEBI → ChEBI-hierarchy rule to seed defaults on MIM ingredient records (`is-a CHEBI:33917 aldohexose` → `NutritionalRoleEnum: [CARBON_SOURCE]`).
   - Pass 2: CHEBI `has_role` axioms harvested via OAK to seed physicochemical roles (e.g. resazurin `has_role` redox indicator).
   - Pass 3: LLM-assisted for residuals, curator-in-the-loop review — never batch-committed without human sign-off.
   - CultureMech `IngredientDescriptor.role` is populated only when the recipe overrides / augments the MIM default.
</re_representation_proposal>

<migration_plan>
Concrete, ordered steps. Every step names the owning file.

1. Draft the three new enums with `meaning:` mappings in **MIM** `src/mediaingredientmech/schema/mediaingredientmech.yaml`, since MIM owns the ingredient records and the MIM SSSOM already anchors identity there. Regenerate MIM's derived Python.
2. Delete `VALID_MEDIA_ROLES` from `MediaIngredientMech/src/mediaingredientmech/curation/ingredient_curator.py:48`; drive validation off the LinkML enums instead. Update `add_media_role(...)` and add analogous `add_nutritional_role`, `add_physicochemical_role`, `add_cellular_metabolic_role`.
3. In **CultureMech** `src/culturemech/schema/culturemech.yaml`: import (`imports:`) the MIM enums, replace `IngredientRoleEnum` on `IngredientDescriptor.role` with the three faceted slots (`nutritional_roles`, `physicochemical_roles`, `cellular_metabolic_roles`) plus the `role_curie` escape hatch. Reconcile `NutrientRoleEnum` — merge overlapping values into `NutritionalRoleEnum` and either delete `NutrientRoleEnum` or narrow it to a genuinely distinct concept (experiment-level nutrient override). Rename `CellularRoleEnum` to `CommunityOrganismRoleEnum` per naming note.
4. Add a lightweight validator step (linkml-validate + a custom rule) that flags any `IngredientDescriptor` with a resolved MIM CHEBI mapping (via SSSOM lookup) but no `nutritional_roles` / `cellular_metabolic_roles` assignment. Wire it into the CultureMech `audit-schema-gaps` harness.
5. Author a backfill script under `CultureMech/scripts/` that: reads MIM SSSOM → resolves each ingredient to CHEBI → applies the ChEBI hierarchy rules → emits a diff of proposed facet assignments per file. Diff-only; do not commit backfilled data as part of this review.
6. Update the developer-facing schema doc (or CLAUDE.md if that is where such docs live) to describe the faceted role model, the MIM SSSOM as identity anchor, and the resolution rule for MIM default vs. CultureMech recipe override.
</migration_plan>

<deliverable_format>
Produce:
1. **Executive summary** — 5-10 bullets, ship/no-ship style: what's broken now, what the three-facet redesign gives, what it costs.
2. **Status audit** — inventory + drift matrix + usage numbers + representative-ingredient table anchored to MIM SSSOM.
3. **Proposed vocabulary** — one YAML block per facet enum, with `permissible_values:` entries carrying `meaning:` (or `TBD` when no defensible CURIE exists) and secondary `mappings:` where useful.
4. **Migration plan** — as above.
5. **Open questions / risks** — decisions to escalate to maintainers (e.g. do we import MIM enums into CultureMech or duplicate; do we retire `NutrientRoleEnum`; how strict is the SSSOM-anchored validator).

Do not write PR-ready code. Draft schema (YAML) + narrative descriptions of edits are sufficient. Applying edits is out of scope for this review.
</deliverable_format>

<grounding_rules>
Every claim about the current state must be tied to a file:line the reviewer can open.
Every proposed ontology mapping must be defensible from the ontology's own definitions — no invented CURIEs. If uncertain, write `TBD (verify against ChEBI/METPO/ENVO)` and note what to search for.
Every representative-ingredient row in the audit must cite the corresponding MIM SSSOM row (subject_id → predicate_id → object_id).
Where existing enum values are already reasonable, say so — do not redesign for its own sake.
</grounding_rules>

<final_check>
Before finalizing:
- Confirm the drift matrix reconciles all four vocabularies (CultureMech `IngredientRoleEnum`, CultureMech `NutrientRoleEnum`, MIM `IngredientRoleEnum`, MIM `VALID_MEDIA_ROLES`).
- Confirm the review explicitly separates the three ingredient-role facets (nutritional / physicochemical / cellular-metabolic) from the community-organism role concept, and recommends renaming the misnamed `CellularRoleEnum`.
- Confirm every proposed enum value has either a real CURIE or an explicit `TBD`, and every representative ingredient anchors to the MIM SSSOM.
- Confirm the migration plan has one owner-file per step.
- Confirm the review makes a clear recommendation, not a menu of options.
</final_check>

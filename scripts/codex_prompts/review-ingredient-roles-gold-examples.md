# Gold-example ingredient role assignments

Hand-curated benchmark for the ingredient-roles review (`review-ingredient-roles.md`).
Purpose: (1) score whatever Codex proposes against known-good assignments; (2) seed
the backfill rule set with worked examples across the three facets.

Every row anchors to the MediaIngredientMech SSSOM
(`MIM/mappings/ingredient_mappings.sssom.tsv`) as the identity source. `object_id`
below is quoted verbatim from that SSSOM.

The three facets referenced (per `review-ingredient-roles.md`):

- **Nutritional** = element / macronutrient supply the ingredient contributes to
  the medium.
- **Physicochemical** = chemical / physical job the ingredient does in the recipe,
  independent of what element it supplies.
- **Cellular-metabolic** = what the ingredient does *in / on* the cultured
  microbe(s) — metabolic fate or biochemical function inside the cell. This facet
  is organism-conditional: a value marked `(conditional: <group>)` applies only
  for the named metabolic group.

Conventions:

- Roles listed in `[brackets]` are the expected assignments.
- `—` means the facet has no applicable value for this ingredient in typical use.
- Multi-role entries are the norm, not the exception.

---

## 1. Glucose

- **MIM subject**: `MIM:Glucose` — "Glucose"
- **SSSOM row**: `skos:exactMatch → CHEBI:17234 "glucose"`
- **Nutritional**: [CARBON_SOURCE, ENERGY_SOURCE]
- **Physicochemical**: —
- **Cellular-metabolic**: [SUBSTRATE]; ELECTRON_DONOR *(conditional: chemoheterotrophic respiration — do not assign by default; implied by SUBSTRATE otherwise)*
- **Reasoning**: canonical fermentable hexose. Provides both the carbon skeleton
  for biosynthesis and the reducing equivalents / ATP via glycolysis. Do NOT
  auto-assign ELECTRON_DONOR unless the organism uses glucose as its named
  respiratory substrate — the default is that SUBSTRATE covers the metabolic
  fate.

## 2. Agar

- **MIM subject**: `MIM:Agar` — "Agar"
- **SSSOM row**: `skos:exactMatch → CHEBI:2509 "agar"`
- **Nutritional**: —
- **Physicochemical**: [SOLIDIFYING_AGENT]
- **Cellular-metabolic**: [NONE]
- **Reasoning**: sulfated galactan gelling polymer. Not metabolized by the vast
  majority of target microbes. Agarolytic marine strains are a real but narrow
  exception; the *default* role assignment is inert solidifier. If Codex proposes
  CARBON_SOURCE for agar, that's a scoring failure.

## 3. Resazurin

- **MIM subject**: `MIM:Resazurin` — "Resazurin"
- **SSSOM row**: `skos:exactMatch → CHEBI:8806 "Resazurin"`
- **Nutritional**: —
- **Physicochemical**: [REDOX_INDICATOR]
- **Cellular-metabolic**: [NONE]
- **Reasoning**: canonical anaerobic-conditions indicator dye; oxidised = pink,
  reduced = colourless. Present at micromolar concentrations, no metabolic role.

## 4. EDTA

- **MIM subject**: `MIM:Edta` — "EDTA"
- **SSSOM row**: `skos:exactMatch → CHEBI:64755 "EDTA(2-)"`
- **Nutritional**: —
- **Physicochemical**: [CHELATOR]
- **Cellular-metabolic**: [NONE] by default; INHIBITOR *(conditional: high
  concentration or Gram-negative outer membrane destabilisation)*
- **Reasoning**: chelates divalent cations to buffer trace-metal availability in
  defined media and to solubilise iron in trace-metal stocks. At physiological
  concentrations (~10-100 µM) it is not inhibitory; at millimolar concentrations
  in some assays it destabilises the outer membrane — call that INHIBITOR
  *conditional*, not default.

## 5. L-Cysteine

- **MIM subject**: `MIM:L-cysteine` — "L-Cysteine"
- **SSSOM row**: `skos:exactMatch → CHEBI:17561 "L-cysteine"`
- **Nutritional**: [AMINO_ACID_SOURCE, SULFUR_SOURCE]
- **Physicochemical**: [REDUCING_AGENT] *(when supplied at ≥ ~0.5 g/L, as is
  standard for anaerobic media)*
- **Cellular-metabolic**: [SUBSTRATE]
- **Reasoning**: the archetypal dual-facet example. As a proteinogenic amino acid
  it is a nutritional source of both organic N (implied — not an enum value here)
  and sulfur. Its thiol side chain also poises the redox potential of anaerobic
  media, so it doubles as a physicochemical reducing agent at the concentrations
  used in Hungate-style media. If Codex's redesign cannot express both facets on
  a single ingredient, that is a design failure.

## 6. Ammonium chloride (NH₄Cl)

- **MIM subject**: `MIM:Ammonium_Chloride_Nitrogen_Source` — "Ammonium chloride
  (nitrogen source)"
- **SSSOM row**: `skos:exactMatch → CHEBI:31206 "ammonium chloride"`
- **Nutritional**: [NITROGEN_SOURCE]
- **Physicochemical**: — *(SALT is defensible at ≥50 mM as osmotic contribution,
  but that is recipe-dependent; do not auto-assign at the ingredient level)*
- **Cellular-metabolic**: [SUBSTRATE] *(assimilated as NH₄⁺ via glutamine
  synthetase / GDH)*
- **Reasoning**: dominant use is nitrogen supply — MIM even encodes this into the
  subject_id. Chloride contribution to osmolarity / ionic strength is recipe-
  scale, not compound-scale, so `SALT` belongs on the CultureMech recipe override,
  not the MIM default.

## 7. K₂HPO₄

- **MIM subject**: `MIM:K2hpo4` — "K2HPO4"
- **SSSOM row**: `skos:exactMatch → CHEBI:131527 "dipotassium hydrogen phosphate"`
- **Nutritional**: [PHOSPHATE_SOURCE]
- **Physicochemical**: [BUFFER] *(conditional: paired with KH₂PO₄ or an acidic
  species in the same recipe to establish a phosphate buffer at pH ~6.5-7.5)*
- **Cellular-metabolic**: [SUBSTRATE] *(P assimilation for nucleic acids,
  phospholipids, ATP)*
- **Reasoning**: dual role again — the dibasic phosphate is both a phosphorus
  nutrient and, when paired with the monobasic form KH₂PO₄, the physiological
  pH buffer of choice. Whether BUFFER applies is *recipe-conditional*: single-
  salt supplementation ≠ buffer system. Codex should propose logic that reads the
  paired salt from the recipe before assigning BUFFER.

## 8. Thiamine pyrophosphate (TPP)

- **MIM subject**: `MIM:02_Thiamine_Pyrophosphate` — "0.2% Thiamine pyrophosphate"
- **SSSOM row**: `skos:exactMatch → CHEBI:9532 "thiamine(1+) diphosphate"`
- **Nutritional**: [VITAMIN_SOURCE, COFACTOR_PROVIDER]
- **Physicochemical**: —
- **Cellular-metabolic**: [COFACTOR]
- **Reasoning**: TPP is the active cofactor form of vitamin B₁; supplied to
  auxotrophs at trace concentrations. Distinguishes the medium-side role
  `COFACTOR_PROVIDER` (what the ingredient supplies) from the cellular-metabolic
  role `COFACTOR` (what the compound does inside the cell) — these are two
  facets of the same fact, and both should be assignable.

## 9. Sodium sulfide (Na₂S)

- **MIM subject**: `MIM:Na2s` — "Na2S"
- **SSSOM row**: `skos:closeMatch → CHEBI:76208 "sodium sulfide (anhydrous)"`
- **Nutritional**: [SULFUR_SOURCE]
- **Physicochemical**: [REDUCING_AGENT]
- **Cellular-metabolic**: [SUBSTRATE]; ELECTRON_DONOR *(conditional: sulfide-
  oxidising chemolithotrophs — Beggiatoa, Thiobacillus, purple sulfur bacteria,
  etc.)*
- **Reasoning**: the strongest test case for why ELECTRON_DONOR belongs on the
  *cellular-metabolic* facet, not the media facet: whether Na₂S is an electron
  donor depends entirely on the organism being cultured. In an anaerobic
  heterotroph medium it is *only* a reducing agent + S source; in a chemolitho-
  autotrophic sulfur-oxidiser medium it is the primary energy substrate. A
  media-only role vocabulary cannot express that distinction.

## 10. Methanol

- **MIM subject**: `MIM:Methanol` — "Methanol"
- **SSSOM row**: `skos:exactMatch → CHEBI:17790 "methanol"`
- **Nutritional**: [CARBON_SOURCE, ENERGY_SOURCE]
- **Physicochemical**: — *(at ~1% v/v as a carbon substrate; would only be
  SURFACTANT / SOLVENT at radically higher concentrations irrelevant to culture
  media)*
- **Cellular-metabolic**: [SUBSTRATE, ELECTRON_DONOR] *(conditional: methylo-
  trophs and methanogens; for a non-methylotroph its role is inhibitor, not
  substrate, but that is not a default MIM assignment)*
- **Reasoning**: canonical C1 substrate. The ELECTRON_DONOR call here is
  defensible as a *default* for methanol because its predominant use in growth
  media is as an energy + carbon source for methylotrophs — the compound is
  rarely added to non-methylotroph media in growth-promoting concentrations.
  Contrast with Na₂S where the sulfide use case is much broader than
  chemolithotrophy.

---

## Cross-cutting scoring criteria for Codex's proposal

Codex's redesign should reproduce these facts, checkable against the table above:

1. **Every gold row must be expressible.** The proposed enums must admit every
   `[bracketed]` assignment above. Missing values are a fail.
2. **Multi-facet ingredients must resolve cleanly.** L-cysteine (5), K₂HPO₄ (7),
   and TPP (8) each carry three facets simultaneously — the schema must accept
   simultaneous assignments across `NutritionalRoleEnum`,
   `PhysicochemicalRoleEnum`, and `CellularMetabolicRoleEnum` without either
   collapsing them into one enum or forcing the curator to pick one.
3. **Organism-conditional roles must not be media-side defaults.** Na₂S (9) and
   methanol (10) demonstrate that ELECTRON_DONOR is a cellular-metabolic
   attribute conditional on the cultured organism. The redesign must NOT put
   ELECTRON_DONOR / ELECTRON_ACCEPTOR on the medium-side vocabulary as an
   ingredient default — that was the mistake in the current
   `IngredientRoleEnum`.
4. **Inert ingredients must have inert assignments.** Agar (2), resazurin (3),
   and EDTA (4) must NOT accrue nutritional roles by default. If the ChEBI-
   hierarchy backfill rule assigns CARBON_SOURCE to agar because agar is-a
   polysaccharide, the rule is wrong and needs a metabolisability gate.
5. **Recipe-conditional roles must be flagged, not silently promoted.**
   K₂HPO₄'s BUFFER role and NH₄Cl's SALT role apply only in the presence of
   pairing / high concentration. A conforming rule set should mark these as
   *proposed, needs recipe context*, not confirmed defaults.
6. **MIM subject_id → CHEBI → role.** Every default assignment in the backfill
   must be traceable to a MIM SSSOM row + a ChEBI is-a / has-role axiom (or a
   METPO / ENVO fallback). Assignments that cannot be traced are candidate
   METPO-proposal targets, not silent defaults.

## Suggested backfill rule sketch (for the reviewer to critique)

- `CHEBI:17234 glucose` → nutritional: CARBON_SOURCE, ENERGY_SOURCE via is-a
  `CHEBI:33917 aldohexose`.
- `CHEBI:2509 agar` → physicochemical: SOLIDIFYING_AGENT via a hand-maintained
  compound → role map (ChEBI has no clean solidifying-agent role term).
- `CHEBI:8806 Resazurin` → physicochemical: REDOX_INDICATOR via ChEBI has-role
  redox indicator (verify).
- `CHEBI:64755 EDTA(2-)` → physicochemical: CHELATOR via `CHEBI:38161 chelator`
  has-role.
- `CHEBI:17561 L-cysteine` → nutritional: AMINO_ACID_SOURCE, SULFUR_SOURCE via
  is-a `CHEBI:33704 alpha-amino acid` + sulfur-containing-amino-acid subtree;
  physicochemical: REDUCING_AGENT via ChEBI has-role reducing agent (verify).
- `CHEBI:31206 ammonium chloride` → nutritional: NITROGEN_SOURCE via has-part
  ammonium.
- `CHEBI:131527 dipotassium hydrogen phosphate` → nutritional: PHOSPHATE_SOURCE
  via has-part hydrogen phosphate; BUFFER only when paired.
- `CHEBI:9532 thiamine(1+) diphosphate` → nutritional: VITAMIN_SOURCE,
  COFACTOR_PROVIDER via ChEBI has-role B vitamin + cofactor; cellular-metabolic:
  COFACTOR (same axiom, different facet).
- `CHEBI:76208 sodium sulfide` → nutritional: SULFUR_SOURCE via has-part
  sulfide; physicochemical: REDUCING_AGENT via ChEBI has-role reducing agent
  (verify).
- `CHEBI:17790 methanol` → nutritional: CARBON_SOURCE, ENERGY_SOURCE via is-a
  `CHEBI:30879 alcohol`; cellular-metabolic: SUBSTRATE + ELECTRON_DONOR is a
  curator-added exception for the methylotrophy case.

The reviewer should confirm each ChEBI role axiom is real (OAK + chebi.owl) and
flag any assignment that requires an axiom ChEBI does not carry — those become
METPO / ENVO / MICRO proposal candidates.

# Sodium Molybdate Form Conflict

Status: **confirmed conflict in the pinned identity-resolution inputs; unresolved**.
No ontology ID, formula, concentration, or source wording was replaced by this
investigation. This is an identity finding, not five completed record reviews.

## Evidence

1. The retrieved [official MediaDive solution 1383](https://mediadive.dsmz.de/rest/solution/1383)
   names compound 641 `Na2MoO4 x H2O` at `$.data.recipe[4].compound`. Its amount is
   6.3 mg and its declared `g_l` is 0.0063. The complete exact row, capture hash,
   and scoped amount evidence are in the existing solution record and its
   [concentration report](../20261007-mediadive-solutions-1000-1500/records/bacterial/mediadive_1383_Trace_element_solution.yaml.md).
2. The [official EBI OLS ChEBI response](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI%3A75215),
   retrieved 2026-10-07, returns one nonobsolete term with PURL
   <http://purl.obolibrary.org/obo/CHEBI_75215>. Exact field values are
   `sodium molybdate (anhydrous)` at `$._embedded.terms[0].label` and
   `MoO4.2Na` at `$._embedded.terms[0].annotation.generalized_empirical_formula[0]`.
   Response SHA256: `d7b0215cf6aeabdee8f878302fb77ade3086473fc14c7300d1f31260a2343631`.
3. The packaged MIM index contains this exact CSV row at line 6958:

   ```csv
   Na2MoO4 x H2O,synonym,CHEBI:75215,Na2MoO4,CHEBI:75215,MAPPED,unique
   ```

   Package metadata pins MIM commit
   `9f09e4fb97fb0e6cbbd6f25baca40b36512adb88`, source
   `docs/data/label_index.csv`, 9,876 data rows, and SHA256
   `a36cd4683feb89e2fc2a1721dc15008d1e10c12044e89a36c27b6621a8aaf262`.
   `MIMLabelIndex.from_package()` verified that pin. The maintained resolver
   returns `mim_exact`, `CHEBI:75215`, and `unique` for `Na2MoO4 x H2O` even with
   no local fallback term. The literal name `sodium molybdate monohydrate` returns
   `not_found` in this pinned index; that is not proof that the chemical or an
   ontology entry does not exist.

The ontology's anhydrous formula does not establish that the recipe's hydrate
wording is a synonym. Conversely, the recipe spelling alone does not prove which
commercial hydrate was actually used. A source typo remains possible. The
concentration evidence supports the source's explicit mass-per-volume statement,
not this secondary mapping or a molecular-weight conversion.

## Exact-Label Scope

A scan of all 15,910 git-tracked normalized YAML records found five nodes with
the exact `preferred_term` `Na2MoO4 x H2O`, each carrying CHEBI:75215 locally:

| Exact record | Node | Grounding fields |
| --- | --- | --- |
| `data/normalized_yaml/archaea/halophile_medium.yaml` | `ingredients[12]` | `term`, `mediaingredientmech_chebi_term` |
| `data/normalized_yaml/bacterial/elusimicrobium_minutum_medium.yaml` | `ingredients[18]` | `term` |
| `data/normalized_yaml/bacterial/halophile_medium.yaml` | `ingredients[12]` | `term`, `mediaingredientmech_chebi_term` |
| `data/normalized_yaml/bacterial/mediadive_1383_Trace_element_solution.yaml` | `composition[4]` | `chebi_term`; upstream `term` remains compound 641 |
| `data/normalized_yaml/bacterial/trace_element_solution_medium_1263.yaml` | `ingredients[9]` | `term`, `mediaingredientmech_chebi_term` |

The machine-readable [exact-label inventory](inventory.json) accompanies this
finding. This is not an exhaustive audit of other sodium-molybdate aliases or
all ontology mappings. The local text search included ignored/hidden files in
the packaged index, MediaDive raw-source folder, and current curation reports.

## Resolution Requirements

- Inspect the original recipe/specification for each affected formulation before
  choosing a hydrate or correcting source wording. Do not infer equivalence from
  the shared compound name or use another medium's amount as evidence.
- Reconcile the synonym decision in the authoritative MIM source. Current MIM
  `main` was not checked; this finding is about CultureMech's verified pinned
  snapshot. Do not hand-edit the packaged immutable CSV or add a second resolver.
- Refresh the governed snapshot through the maintained full-SHA workflow when a
  reviewed upstream correction exists, then re-check all five record mappings
  and publication-time resolution.
- Attach exact recipe/ontology evidence to any resulting ingredient edit and
  append curation history. Deleting only solution 1383's local `chebi_term` would
  not repair the pinned resolver's same answer, so no partial identity fix is
  represented as a resolution here.

No molar conversion, density assumption, replacement ontology identifier, or
corpus-wide equivalence assertion was introduced. This finding remains in the
all-record ingredient-review scope.

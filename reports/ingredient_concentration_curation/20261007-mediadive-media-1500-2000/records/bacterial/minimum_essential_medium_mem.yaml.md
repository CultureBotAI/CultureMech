# Medium Concentration Review: Minimum Essential Medium (MEM)

- Record: data/normalized_yaml/bacterial/minimum_essential_medium_mem.yaml
- ID: CultureMech:001122
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `71a8efd4cefb0a8ba73956136de3e523624fe5c0944e07033df0ebd5123b3233`
- Proposed/result SHA256: `71a8efd4cefb0a8ba73956136de3e523624fe5c0944e07033df0ebd5123b3233`
- Source: https://mediadive.dsmz.de/rest/medium/1638
- Source SHA256: fd0b4c4a64a5df683464ba220c473fdf4e0d3067a763efde0456ddf154753fd5
- Retrieved: 2026-10-07T13:44:48.464509+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | MEM (1x) Gibco 31095-029 | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1638 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): MEM (1x) Gibco 31095-029, MEM-Medium | unchanged |
| `source.data.solutions[0].recipe[0]` | MEM-Medium | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1638 | {<br>                        "recipe_order": 1,<br>                        "compound": "MEM-Medium",<br>                        "compound_id": 1377,<br>                        "attribute": "Gibco 31095-029",<br>                        "amount": 1,<br>                        "unit": "x",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1638 | {<br>                        "step": "Cultivation of cell lines like DH82 (canine macrophage; ATCC CRL-10389)"<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

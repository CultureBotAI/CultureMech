# Medium Concentration Review: S/W

- Record: data/normalized_yaml/bacterial/s_w.yaml
- ID: CultureMech:000414
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6a653d6f02ed1cab449f6efd877b143d91e6384711de7430e8f4669e9c4a6ae0`
- Proposed/result SHA256: `6a653d6f02ed1cab449f6efd877b143d91e6384711de7430e8f4669e9c4a6ae0`
- Source: https://mediadive.dsmz.de/rest/medium/C99
- Source SHA256: 4e0701c7615764b103f329c1f267ceecce127f2337cf647109e0e6aac377f334
- Retrieved: 2026-10-07T13:48:14.146977+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Air-dried sieved calcareous soil | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/C99 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[1].concentration` | Deionized water | {"unit": "VARIABLE", "value": "7-10 cm above the soil layer"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/C99 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `source.data.solutions[0].recipe[0]` | Soil | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/C99 | {<br>                        "recipe_order": 2,<br>                        "compound": "Soil",<br>                        "compound_id": 2350,<br>                        "attribute": "air-dried, sieved, garden loam",<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/C99 | {<br>                        "step": "Put a layer about 1 cm deep of air-dried, sieved good calcareous garden loam into a\r\ntest tube or jar. (The use of mud from rivers or ponds is rarely satisfactory.)\r\nCarefully add deionised water to a depth of 7 to 10 cm, plug or cover, and steam\r\nfor one hour or autoclave for 15 minutes at 15 psi (longer for larger vessels) on\r\neach of 2 consecutive days; further sterilisation is not needed. Allow to stand for a\r\nfurther day before inoculating, when the pH should be between 7.0 - 8.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

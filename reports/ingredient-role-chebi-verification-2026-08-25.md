# Ingredient-role ChEBI verification

Date: 2026-08-25

Source: local OAK adapter `sqlite:obo:chebi`, queried with `runoak`. A term is marked as a role only when its `rdfs:subClassOf` ancestry includes `CHEBI:50906` (`role`).

| CURIE | current asserted use | actual ChEBI label | is role? | correct CURIE if different | notes |
|---|---|---|---|---|---|
| CHEBI:63247 | REDUCING_AGENT | reducing agent | Yes | Same as asserted | Correct. |
| CHEBI:63248 | OXIDIZING_AGENT | oxidising agent | Yes | Same as asserted | Correct for OXIDIZING_AGENT. The original review prompt's suggestion that this denotes a reducing agent is incorrect. |
| CHEBI:15022 | ELECTRON_DONOR | electron donor | Yes | Same as asserted | Correct; this is not magnesium(2+). |
| CHEBI:17654 | ELECTRON_ACCEPTOR | electron acceptor | Yes | Same as asserted | Correct; this is not 5'-deoxyadenosine. |
| CHEBI:33229 | VITAMIN_SOURCE | vitamin (role) | Yes | Same as asserted | The CURIE denotes the vitamin role, not the distinct medium-side concept "source of vitamins"; retain only if that semantic approximation is intended. |
| CHEBI:35225 | BUFFER | buffer | Yes | Same as asserted | Correct. |
| CHEBI:38161 | CHELATOR | chelator | Yes | Same as asserted | Correct. |
| CHEBI:35195 | SURFACTANT | surfactant | Yes | Same as asserted | Correct. |
| CHEBI:50407 | PH_INDICATOR | acid-base indicator | Yes | Same as asserted | Correct. |
| CHEBI:77973 | ANTIFOAM | antifoaming agent | Yes | Same as asserted | Correct. |
| CHEBI:23357 | COFACTOR / COFACTOR_PROVIDER | cofactor | Yes | Same as asserted | Exact for COFACTOR. For COFACTOR_PROVIDER it is only an approximation: ChEBI names the cofactor role, not a provider-of-cofactor role. |
| CHEBI:35222 | INHIBITOR | inhibitor | Yes | Same as asserted | Correct. |

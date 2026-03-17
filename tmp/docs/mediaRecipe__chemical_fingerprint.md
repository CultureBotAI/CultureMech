
# Slot: chemical_fingerprint

SHA256 hash using parent ingredients (hierarchy-aware)

URI: [culturemech:mediaRecipe__chemical_fingerprint](https://w3id.org/culturemech/mediaRecipe__chemical_fingerprint)


## Domain and Range

None &#8594;  <sub>0..1</sub> [String](types/String.md)

## Parents


## Children


## Used by

 * [MediaRecipe](MediaRecipe.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | Treats chemical variants as equivalent (CaCl2·2H2O = CaCl2) |
|  | | Uses parent CHEBI IDs from MediaIngredientMech hierarchy |
|  | | Enables smart merging of hydrates, salt forms, and anhydrous variants |
|  | | Generated only when hierarchy enrichment is available |


# Class: IngredientReference

Reference to canonical ingredient

URI: [culturemech:IngredientReference](https://w3id.org/culturemech/IngredientReference)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[IngredientDescriptor]++-%20parent_ingredient%200..1>[IngredientReference&#124;preferred_term:string;mediaingredientmech_id:string%20%3F],[IngredientDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[IngredientDescriptor]++-%20parent_ingredient%200..1>[IngredientReference&#124;preferred_term:string;mediaingredientmech_id:string%20%3F],[IngredientDescriptor])

## Referenced by Class

 *  **None** *[➞parent_ingredient](ingredientDescriptor__parent_ingredient.md)*  <sub>0..1</sub>  **[IngredientReference](IngredientReference.md)**

## Attributes


### Own

 * [➞preferred_term](ingredientReference__preferred_term.md)  <sub>1..1</sub>
     * Description: Name of parent ingredient
     * Range: [String](types/String.md)
 * [➞mediaingredientmech_id](ingredientReference__mediaingredientmech_id.md)  <sub>0..1</sub>
     * Description: MediaIngredientMech ID
     * Range: [String](types/String.md)

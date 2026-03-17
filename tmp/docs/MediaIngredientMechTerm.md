
# Class: MediaIngredientMechTerm

A MediaIngredientMech identifier for a media ingredient

URI: [culturemech:MediaIngredientMechTerm](https://w3id.org/culturemech/MediaIngredientMechTerm)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[IngredientDescriptor]++-%20mediaingredientmech_term%200..1>[MediaIngredientMechTerm&#124;id:string;label(i):string%20%3F],[SolutionDescriptor]++-%20mediaingredientmech_term%200..1>[MediaIngredientMechTerm],[Term]^-[MediaIngredientMechTerm],[SolutionDescriptor],[IngredientDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[IngredientDescriptor]++-%20mediaingredientmech_term%200..1>[MediaIngredientMechTerm&#124;id:string;label(i):string%20%3F],[SolutionDescriptor]++-%20mediaingredientmech_term%200..1>[MediaIngredientMechTerm],[Term]^-[MediaIngredientMechTerm],[SolutionDescriptor],[IngredientDescriptor])

## Identifier prefixes

 * MediaIngredientMech

## Parents

 *  is_a: [Term](Term.md) - Base class for ontology term references. Subclasses specify id_prefixes for validation.

## Referenced by Class

 *  **None** *[➞mediaingredientmech_term](ingredientDescriptor__mediaingredientmech_term.md)*  <sub>0..1</sub>  **[MediaIngredientMechTerm](MediaIngredientMechTerm.md)**
 *  **None** *[➞mediaingredientmech_term](solutionDescriptor__mediaingredientmech_term.md)*  <sub>0..1</sub>  **[MediaIngredientMechTerm](MediaIngredientMechTerm.md)**

## Attributes


### Own

 * [MediaIngredientMechTerm➞id](MediaIngredientMechTerm_id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)

### Inherited from Term:

 * [➞label](term__label.md)  <sub>0..1</sub>
     * Description: Ontology term label
     * Range: [String](types/String.md)

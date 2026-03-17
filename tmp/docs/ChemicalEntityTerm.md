
# Class: ChemicalEntityTerm

A CHEBI term representing a chemical entity

URI: [culturemech:ChemicalEntityTerm](https://w3id.org/culturemech/ChemicalEntityTerm)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[CofactorDescriptor]++-%20precursor_term%200..1>[ChemicalEntityTerm&#124;id:string;label(i):string%20%3F],[CofactorDescriptor]++-%20term%200..1>[ChemicalEntityTerm],[IngredientDescriptor]++-%20term%200..1>[ChemicalEntityTerm],[TransporterAnnotation]++-%20substrate_terms%200..*>[ChemicalEntityTerm],[Term]^-[ChemicalEntityTerm],[TransporterAnnotation],[IngredientDescriptor],[CofactorDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[CofactorDescriptor]++-%20precursor_term%200..1>[ChemicalEntityTerm&#124;id:string;label(i):string%20%3F],[CofactorDescriptor]++-%20term%200..1>[ChemicalEntityTerm],[IngredientDescriptor]++-%20term%200..1>[ChemicalEntityTerm],[TransporterAnnotation]++-%20substrate_terms%200..*>[ChemicalEntityTerm],[Term]^-[ChemicalEntityTerm],[TransporterAnnotation],[IngredientDescriptor],[CofactorDescriptor])

## Identifier prefixes

 * CHEBI

## Parents

 *  is_a: [Term](Term.md) - Base class for ontology term references. Subclasses specify id_prefixes for validation.

## Referenced by Class

 *  **None** *[➞precursor_term](cofactorDescriptor__precursor_term.md)*  <sub>0..1</sub>  **[ChemicalEntityTerm](ChemicalEntityTerm.md)**
 *  **None** *[➞term](cofactorDescriptor__term.md)*  <sub>0..1</sub>  **[ChemicalEntityTerm](ChemicalEntityTerm.md)**
 *  **None** *[➞term](ingredientDescriptor__term.md)*  <sub>0..1</sub>  **[ChemicalEntityTerm](ChemicalEntityTerm.md)**
 *  **None** *[➞substrate_terms](transporterAnnotation__substrate_terms.md)*  <sub>0..\*</sub>  **[ChemicalEntityTerm](ChemicalEntityTerm.md)**

## Attributes


### Own

 * [ChemicalEntityTerm➞id](ChemicalEntityTerm_id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)

### Inherited from Term:

 * [➞label](term__label.md)  <sub>0..1</sub>
     * Description: Ontology term label
     * Range: [String](types/String.md)

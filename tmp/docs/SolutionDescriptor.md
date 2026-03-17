
# Class: SolutionDescriptor

A pre-prepared stock solution used as an ingredient

URI: [culturemech:SolutionDescriptor](https://w3id.org/culturemech/SolutionDescriptor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[StorageConditions],[StorageConditions]<storage_conditions%200..1-++[SolutionDescriptor&#124;preferred_term:string;preparation_notes:string%20%3F;shelf_life:string%20%3F],[ConcentrationValue]<concentration%200..1-++[SolutionDescriptor],[IngredientDescriptor]<composition%201..*-++[SolutionDescriptor],[MediaIngredientMechTerm]<mediaingredientmech_term%200..1-++[SolutionDescriptor],[Term]<term%200..1-++[SolutionDescriptor],[MediaRecipe]++-%20solutions%200..*>[SolutionDescriptor],[Descriptor]^-[SolutionDescriptor],[MediaRecipe],[MediaIngredientMechTerm],[IngredientDescriptor],[Descriptor],[ConcentrationValue])](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[StorageConditions],[StorageConditions]<storage_conditions%200..1-++[SolutionDescriptor&#124;preferred_term:string;preparation_notes:string%20%3F;shelf_life:string%20%3F],[ConcentrationValue]<concentration%200..1-++[SolutionDescriptor],[IngredientDescriptor]<composition%201..*-++[SolutionDescriptor],[MediaIngredientMechTerm]<mediaingredientmech_term%200..1-++[SolutionDescriptor],[Term]<term%200..1-++[SolutionDescriptor],[MediaRecipe]++-%20solutions%200..*>[SolutionDescriptor],[Descriptor]^-[SolutionDescriptor],[MediaRecipe],[MediaIngredientMechTerm],[IngredientDescriptor],[Descriptor],[ConcentrationValue])

## Parents

 *  is_a: [Descriptor](Descriptor.md) - Base class for descriptor pattern. Descriptors have a human-readable preferred_term and optional ontology term.

## Referenced by Class

 *  **None** *[➞solutions](mediaRecipe__solutions.md)*  <sub>0..\*</sub>  **[SolutionDescriptor](SolutionDescriptor.md)**

## Attributes


### Own

 * [➞preferred_term](solutionDescriptor__preferred_term.md)  <sub>1..1</sub>
     * Description: Solution name (e.g., "Trace Metal Solution", "Vitamin Stock")
     * Range: [String](types/String.md)
 * [➞term](solutionDescriptor__term.md)  <sub>0..1</sub>
     * Description: Ontology term if available
     * Range: [Term](Term.md)
 * [➞mediaingredientmech_term](solutionDescriptor__mediaingredientmech_term.md)  <sub>0..1</sub>
     * Description: MediaIngredientMech identifier for this solution component
     * Range: [MediaIngredientMechTerm](MediaIngredientMechTerm.md)
 * [➞composition](solutionDescriptor__composition.md)  <sub>1..\*</sub>
     * Description: Ingredients in the stock solution
     * Range: [IngredientDescriptor](IngredientDescriptor.md)
 * [➞concentration](solutionDescriptor__concentration.md)  <sub>0..1</sub>
     * Description: Working concentration when added to medium
     * Range: [ConcentrationValue](ConcentrationValue.md)
 * [➞preparation_notes](solutionDescriptor__preparation_notes.md)  <sub>0..1</sub>
     * Description: How to prepare the stock solution
     * Range: [String](types/String.md)
 * [➞storage_conditions](solutionDescriptor__storage_conditions.md)  <sub>0..1</sub>
     * Description: Storage requirements for the stock
     * Range: [StorageConditions](StorageConditions.md)
 * [➞shelf_life](solutionDescriptor__shelf_life.md)  <sub>0..1</sub>
     * Description: Stability duration (e.g., "6 months at 4°C")
     * Range: [String](types/String.md)


# Class: IngredientDescriptor

Chemical or biological ingredient in a medium

URI: [culturemech:IngredientDescriptor](https://w3id.org/culturemech/IngredientDescriptor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SupplierInfo],[MediaIngredientMechTerm],[IngredientReference],[EvidenceItem]<evidence%200..*-++[IngredientDescriptor&#124;preferred_term:string;variant_type:VariantTypeEnum%20%3F;modifier:ModifierEnum%20%3F;chemical_formula:string%20%3F;molecular_weight:float%20%3F;notes:string%20%3F;role:IngredientRoleEnum%20*],[CofactorDescriptor]<cofactors_provided%200..*-++[IngredientDescriptor],[SupplierInfo]<supplier_catalog%200..1-++[IngredientDescriptor],[ConcentrationValue]<concentration%201..1-++[IngredientDescriptor],[IngredientReference]<parent_ingredient%200..1-++[IngredientDescriptor],[MediaIngredientMechTerm]<mediaingredientmech_term%200..1-++[IngredientDescriptor],[ChemicalEntityTerm]<term%200..1-++[IngredientDescriptor],[MediaRecipe]++-%20ingredients%201..*>[IngredientDescriptor],[SolutionDescriptor]++-%20composition%201..*>[IngredientDescriptor],[Descriptor]^-[IngredientDescriptor],[SolutionDescriptor],[MediaRecipe],[EvidenceItem],[Descriptor],[ConcentrationValue],[CofactorDescriptor],[ChemicalEntityTerm])](https://yuml.me/diagram/nofunky;dir:TB/class/[SupplierInfo],[MediaIngredientMechTerm],[IngredientReference],[EvidenceItem]<evidence%200..*-++[IngredientDescriptor&#124;preferred_term:string;variant_type:VariantTypeEnum%20%3F;modifier:ModifierEnum%20%3F;chemical_formula:string%20%3F;molecular_weight:float%20%3F;notes:string%20%3F;role:IngredientRoleEnum%20*],[CofactorDescriptor]<cofactors_provided%200..*-++[IngredientDescriptor],[SupplierInfo]<supplier_catalog%200..1-++[IngredientDescriptor],[ConcentrationValue]<concentration%201..1-++[IngredientDescriptor],[IngredientReference]<parent_ingredient%200..1-++[IngredientDescriptor],[MediaIngredientMechTerm]<mediaingredientmech_term%200..1-++[IngredientDescriptor],[ChemicalEntityTerm]<term%200..1-++[IngredientDescriptor],[MediaRecipe]++-%20ingredients%201..*>[IngredientDescriptor],[SolutionDescriptor]++-%20composition%201..*>[IngredientDescriptor],[Descriptor]^-[IngredientDescriptor],[SolutionDescriptor],[MediaRecipe],[EvidenceItem],[Descriptor],[ConcentrationValue],[CofactorDescriptor],[ChemicalEntityTerm])

## Parents

 *  is_a: [Descriptor](Descriptor.md) - Base class for descriptor pattern. Descriptors have a human-readable preferred_term and optional ontology term.

## Referenced by Class

 *  **None** *[➞ingredients](mediaRecipe__ingredients.md)*  <sub>1..\*</sub>  **[IngredientDescriptor](IngredientDescriptor.md)**
 *  **None** *[➞composition](solutionDescriptor__composition.md)*  <sub>1..\*</sub>  **[IngredientDescriptor](IngredientDescriptor.md)**

## Attributes


### Own

 * [➞preferred_term](ingredientDescriptor__preferred_term.md)  <sub>1..1</sub>
     * Description: Human-readable ingredient name (e.g., "Glucose", "Yeast Extract")
     * Range: [String](types/String.md)
 * [➞term](ingredientDescriptor__term.md)  <sub>0..1</sub>
     * Description: CHEBI term for the chemical entity
     * Range: [ChemicalEntityTerm](ChemicalEntityTerm.md)
 * [➞mediaingredientmech_term](ingredientDescriptor__mediaingredientmech_term.md)  <sub>0..1</sub>
     * Description: MediaIngredientMech identifier for this ingredient
     * Range: [MediaIngredientMechTerm](MediaIngredientMechTerm.md)
 * [➞parent_ingredient](ingredientDescriptor__parent_ingredient.md)  <sub>0..1</sub>
     * Description: Reference to parent chemical entity from MediaIngredientMech
     * Range: [IngredientReference](IngredientReference.md)
 * [➞variant_type](ingredientDescriptor__variant_type.md)  <sub>0..1</sub>
     * Description: Type of chemical variant
     * Range: [VariantTypeEnum](VariantTypeEnum.md)
 * [➞concentration](ingredientDescriptor__concentration.md)  <sub>1..1</sub>
     * Description: Amount of ingredient
     * Range: [ConcentrationValue](ConcentrationValue.md)
 * [➞modifier](ingredientDescriptor__modifier.md)  <sub>0..1</sub>
     * Description: Modification in variants (INCREASED, DECREASED)
     * Range: [ModifierEnum](ModifierEnum.md)
 * [➞chemical_formula](ingredientDescriptor__chemical_formula.md)  <sub>0..1</sub>
     * Description: Molecular formula (e.g., "C6H12O6")
     * Range: [String](types/String.md)
 * [➞molecular_weight](ingredientDescriptor__molecular_weight.md)  <sub>0..1</sub>
     * Description: Molecular weight in g/mol
     * Range: [Float](types/Float.md)
 * [➞supplier_catalog](ingredientDescriptor__supplier_catalog.md)  <sub>0..1</sub>
     * Description: Supplier information for sourcing
     * Range: [SupplierInfo](SupplierInfo.md)
 * [➞notes](ingredientDescriptor__notes.md)  <sub>0..1</sub>
     * Description: Preparation notes specific to this ingredient
     * Range: [String](types/String.md)
 * [➞role](ingredientDescriptor__role.md)  <sub>0..\*</sub>
     * Description: Functional role(s) in the medium
     * Range: [IngredientRoleEnum](IngredientRoleEnum.md)
 * [➞cofactors_provided](ingredientDescriptor__cofactors_provided.md)  <sub>0..\*</sub>
     * Description: Cofactors supplied by this ingredient
     * Range: [CofactorDescriptor](CofactorDescriptor.md)
 * [➞evidence](ingredientDescriptor__evidence.md)  <sub>0..\*</sub>
     * Description: Evidence for this ingredient's role
     * Range: [EvidenceItem](EvidenceItem.md)


# Class: CofactorDescriptor

A cofactor or coenzyme required for enzymatic activity

URI: [culturemech:CofactorDescriptor](https://w3id.org/culturemech/CofactorDescriptor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Descriptor],[ChemicalEntityTerm]<precursor_term%200..1-++[CofactorDescriptor&#124;preferred_term:string;category:CofactorCategoryEnum%20%3F;precursor:string%20%3F;ec_associations:string%20*;kegg_pathways:string%20*;enzyme_examples:string%20*;biosynthesis_genes:string%20*;bioavailability:string%20%3F;notes:string%20%3F],[ChemicalEntityTerm]<term%200..1-++[CofactorDescriptor],[CofactorRequirement]++-%20cofactor%201..1>[CofactorDescriptor],[IngredientDescriptor]++-%20cofactors_provided%200..*>[CofactorDescriptor],[Descriptor]^-[CofactorDescriptor],[IngredientDescriptor],[CofactorRequirement],[ChemicalEntityTerm])](https://yuml.me/diagram/nofunky;dir:TB/class/[Descriptor],[ChemicalEntityTerm]<precursor_term%200..1-++[CofactorDescriptor&#124;preferred_term:string;category:CofactorCategoryEnum%20%3F;precursor:string%20%3F;ec_associations:string%20*;kegg_pathways:string%20*;enzyme_examples:string%20*;biosynthesis_genes:string%20*;bioavailability:string%20%3F;notes:string%20%3F],[ChemicalEntityTerm]<term%200..1-++[CofactorDescriptor],[CofactorRequirement]++-%20cofactor%201..1>[CofactorDescriptor],[IngredientDescriptor]++-%20cofactors_provided%200..*>[CofactorDescriptor],[Descriptor]^-[CofactorDescriptor],[IngredientDescriptor],[CofactorRequirement],[ChemicalEntityTerm])

## Parents

 *  is_a: [Descriptor](Descriptor.md) - Base class for descriptor pattern. Descriptors have a human-readable preferred_term and optional ontology term.

## Referenced by Class

 *  **None** *[➞cofactor](cofactorRequirement__cofactor.md)*  <sub>1..1</sub>  **[CofactorDescriptor](CofactorDescriptor.md)**
 *  **None** *[➞cofactors_provided](ingredientDescriptor__cofactors_provided.md)*  <sub>0..\*</sub>  **[CofactorDescriptor](CofactorDescriptor.md)**

## Attributes


### Own

 * [➞preferred_term](cofactorDescriptor__preferred_term.md)  <sub>1..1</sub>
     * Description: Human-readable cofactor name (e.g., "Thiamine pyrophosphate", "NAD")
     * Range: [String](types/String.md)
 * [➞term](cofactorDescriptor__term.md)  <sub>0..1</sub>
     * Description: CHEBI term for the cofactor
     * Range: [ChemicalEntityTerm](ChemicalEntityTerm.md)
 * [➞category](cofactorDescriptor__category.md)  <sub>0..1</sub>
     * Description: High-level classification
     * Range: [CofactorCategoryEnum](CofactorCategoryEnum.md)
 * [➞precursor](cofactorDescriptor__precursor.md)  <sub>0..1</sub>
     * Description: Precursor molecule (e.g., thiamine → TPP)
     * Range: [String](types/String.md)
 * [➞precursor_term](cofactorDescriptor__precursor_term.md)  <sub>0..1</sub>
     * Description: CHEBI term for precursor
     * Range: [ChemicalEntityTerm](ChemicalEntityTerm.md)
 * [➞ec_associations](cofactorDescriptor__ec_associations.md)  <sub>0..\*</sub>
     * Description: EC numbers of enzymes using this cofactor
     * Range: [String](types/String.md)
 * [➞kegg_pathways](cofactorDescriptor__kegg_pathways.md)  <sub>0..\*</sub>
     * Description: KEGG pathway IDs for biosynthesis
     * Range: [String](types/String.md)
 * [➞enzyme_examples](cofactorDescriptor__enzyme_examples.md)  <sub>0..\*</sub>
     * Description: Example enzymes requiring this cofactor
     * Range: [String](types/String.md)
 * [➞biosynthesis_genes](cofactorDescriptor__biosynthesis_genes.md)  <sub>0..\*</sub>
     * Description: Genes involved in cofactor biosynthesis
     * Range: [String](types/String.md)
 * [➞bioavailability](cofactorDescriptor__bioavailability.md)  <sub>0..1</sub>
     * Description: Uptake and availability characteristics
     * Range: [String](types/String.md)
 * [➞notes](cofactorDescriptor__notes.md)  <sub>0..1</sub>
     * Description: Additional information about the cofactor
     * Range: [String](types/String.md)


# Class: EvidenceItem

Evidence supporting a claim about media formulation or performance

URI: [culturemech:EvidenceItem](https://w3id.org/culturemech/EvidenceItem)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CofactorRequirement]++-%20evidence%200..*>[EvidenceItem&#124;reference:string;supports:EvidenceItemSupportEnum;snippet:string%20%3F;explanation:string],[IngredientDescriptor]++-%20evidence%200..*>[EvidenceItem],[MediaRecipe]++-%20evidence%200..*>[EvidenceItem],[MediaVariant]++-%20evidence%200..*>[EvidenceItem],[OrganismDescriptor]++-%20evidence%200..*>[EvidenceItem],[SourceData]++-%20evidence%200..*>[EvidenceItem],[SourceData],[OrganismDescriptor],[MediaVariant],[MediaRecipe],[IngredientDescriptor],[CofactorRequirement])](https://yuml.me/diagram/nofunky;dir:TB/class/[CofactorRequirement]++-%20evidence%200..*>[EvidenceItem&#124;reference:string;supports:EvidenceItemSupportEnum;snippet:string%20%3F;explanation:string],[IngredientDescriptor]++-%20evidence%200..*>[EvidenceItem],[MediaRecipe]++-%20evidence%200..*>[EvidenceItem],[MediaVariant]++-%20evidence%200..*>[EvidenceItem],[OrganismDescriptor]++-%20evidence%200..*>[EvidenceItem],[SourceData]++-%20evidence%200..*>[EvidenceItem],[SourceData],[OrganismDescriptor],[MediaVariant],[MediaRecipe],[IngredientDescriptor],[CofactorRequirement])

## Referenced by Class

 *  **None** *[➞evidence](cofactorRequirement__evidence.md)*  <sub>0..\*</sub>  **[EvidenceItem](EvidenceItem.md)**
 *  **None** *[➞evidence](ingredientDescriptor__evidence.md)*  <sub>0..\*</sub>  **[EvidenceItem](EvidenceItem.md)**
 *  **None** *[➞evidence](mediaRecipe__evidence.md)*  <sub>0..\*</sub>  **[EvidenceItem](EvidenceItem.md)**
 *  **None** *[➞evidence](mediaVariant__evidence.md)*  <sub>0..\*</sub>  **[EvidenceItem](EvidenceItem.md)**
 *  **None** *[➞evidence](organismDescriptor__evidence.md)*  <sub>0..\*</sub>  **[EvidenceItem](EvidenceItem.md)**
 *  **None** *[➞evidence](sourceData__evidence.md)*  <sub>0..\*</sub>  **[EvidenceItem](EvidenceItem.md)**

## Attributes


### Own

 * [➞reference](evidenceItem__reference.md)  <sub>1..1</sub>
     * Description: Citation (PMID, DOI, or historical reference)
     * Range: [String](types/String.md)
 * [➞supports](evidenceItem__supports.md)  <sub>1..1</sub>
     * Description: Level of support
     * Range: [EvidenceItemSupportEnum](EvidenceItemSupportEnum.md)
 * [➞snippet](evidenceItem__snippet.md)  <sub>0..1</sub>
     * Description: Exact quote from paper (if PMID/DOI available)
     * Range: [String](types/String.md)
 * [➞explanation](evidenceItem__explanation.md)  <sub>1..1</sub>
     * Description: Why this evidence supports the claim
     * Range: [String](types/String.md)

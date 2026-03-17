
# Class: CofactorRequirement

Cofactor requirement for an organism

URI: [culturemech:CofactorRequirement](https://w3id.org/culturemech/CofactorRequirement)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem],[EvidenceItem]<evidence%200..*-++[CofactorRequirement&#124;can_biosynthesize:boolean;confidence:float%20%3F;genes:string%20*],[CofactorDescriptor]<cofactor%201..1-++[CofactorRequirement],[OrganismDescriptor]++-%20cofactor_requirements%200..*>[CofactorRequirement],[OrganismDescriptor],[CofactorDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem],[EvidenceItem]<evidence%200..*-++[CofactorRequirement&#124;can_biosynthesize:boolean;confidence:float%20%3F;genes:string%20*],[CofactorDescriptor]<cofactor%201..1-++[CofactorRequirement],[OrganismDescriptor]++-%20cofactor_requirements%200..*>[CofactorRequirement],[OrganismDescriptor],[CofactorDescriptor])

## Referenced by Class

 *  **None** *[➞cofactor_requirements](organismDescriptor__cofactor_requirements.md)*  <sub>0..\*</sub>  **[CofactorRequirement](CofactorRequirement.md)**

## Attributes


### Own

 * [➞cofactor](cofactorRequirement__cofactor.md)  <sub>1..1</sub>
     * Description: Required cofactor
     * Range: [CofactorDescriptor](CofactorDescriptor.md)
 * [➞can_biosynthesize](cofactorRequirement__can_biosynthesize.md)  <sub>1..1</sub>
     * Description: Whether organism can synthesize this cofactor
     * Range: [Boolean](types/Boolean.md)
 * [➞confidence](cofactorRequirement__confidence.md)  <sub>0..1</sub>
     * Description: Confidence level (0.0-1.0) based on genome annotation
     * Range: [Float](types/Float.md)
 * [➞evidence](cofactorRequirement__evidence.md)  <sub>0..\*</sub>
     * Description: Supporting evidence for requirement
     * Range: [EvidenceItem](EvidenceItem.md)
 * [➞genes](cofactorRequirement__genes.md)  <sub>0..\*</sub>
     * Description: Genes related to biosynthesis or utilization
     * Range: [String](types/String.md)

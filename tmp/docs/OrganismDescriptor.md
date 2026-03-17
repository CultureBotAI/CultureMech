
# Class: OrganismDescriptor

Target organism for the medium

URI: [culturemech:OrganismDescriptor](https://w3id.org/culturemech/OrganismDescriptor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TransporterAnnotation],[OrganismTerm],[EvidenceItem]<evidence%200..*-++[OrganismDescriptor&#124;preferred_term:string;strain:string%20%3F;growth_phase:string%20%3F;community_role:CellularRoleEnum%20*;target_abundance:float%20%3F;community_function:string%20*],[TransporterAnnotation]<transporters%200..*-++[OrganismDescriptor],[CofactorRequirement]<cofactor_requirements%200..*-++[OrganismDescriptor],[GTDBTerm]<gtdb_term%200..1-++[OrganismDescriptor],[OrganismTerm]<term%200..1-++[OrganismDescriptor],[MediaRecipe]++-%20target_organisms%200..*>[OrganismDescriptor],[Descriptor]^-[OrganismDescriptor],[MediaRecipe],[GTDBTerm],[EvidenceItem],[Descriptor],[CofactorRequirement])](https://yuml.me/diagram/nofunky;dir:TB/class/[TransporterAnnotation],[OrganismTerm],[EvidenceItem]<evidence%200..*-++[OrganismDescriptor&#124;preferred_term:string;strain:string%20%3F;growth_phase:string%20%3F;community_role:CellularRoleEnum%20*;target_abundance:float%20%3F;community_function:string%20*],[TransporterAnnotation]<transporters%200..*-++[OrganismDescriptor],[CofactorRequirement]<cofactor_requirements%200..*-++[OrganismDescriptor],[GTDBTerm]<gtdb_term%200..1-++[OrganismDescriptor],[OrganismTerm]<term%200..1-++[OrganismDescriptor],[MediaRecipe]++-%20target_organisms%200..*>[OrganismDescriptor],[Descriptor]^-[OrganismDescriptor],[MediaRecipe],[GTDBTerm],[EvidenceItem],[Descriptor],[CofactorRequirement])

## Parents

 *  is_a: [Descriptor](Descriptor.md) - Base class for descriptor pattern. Descriptors have a human-readable preferred_term and optional ontology term.

## Referenced by Class

 *  **None** *[➞target_organisms](mediaRecipe__target_organisms.md)*  <sub>0..\*</sub>  **[OrganismDescriptor](OrganismDescriptor.md)**

## Attributes


### Own

 * [➞preferred_term](organismDescriptor__preferred_term.md)  <sub>1..1</sub>
     * Description: Organism name (e.g., "Escherichia coli")
     * Range: [String](types/String.md)
 * [➞term](organismDescriptor__term.md)  <sub>0..1</sub>
     * Description: NCBITaxon identifier
     * Range: [OrganismTerm](OrganismTerm.md)
 * [➞gtdb_term](organismDescriptor__gtdb_term.md)  <sub>0..1</sub>
     * Description: GTDB genome or lineage identifier (alternative to NCBITaxon)
     * Range: [GTDBTerm](GTDBTerm.md)
 * [➞strain](organismDescriptor__strain.md)  <sub>0..1</sub>
     * Description: Specific strain designation (e.g., "K-12", "MG1655")
     * Range: [String](types/String.md)
 * [➞growth_phase](organismDescriptor__growth_phase.md)  <sub>0..1</sub>
     * Description: Target growth phase (e.g., "exponential", "stationary")
     * Range: [String](types/String.md)
 * [➞community_role](organismDescriptor__community_role.md)  <sub>0..\*</sub>
     * Description: Functional role in microbial community
     * Range: [CellularRoleEnum](CellularRoleEnum.md)
 * [➞target_abundance](organismDescriptor__target_abundance.md)  <sub>0..1</sub>
     * Description: Target relative abundance in community (0.0-1.0)
     * Range: [Float](types/Float.md)
 * [➞community_function](organismDescriptor__community_function.md)  <sub>0..\*</sub>
     * Description: Specific functional contribution to community
     * Range: [String](types/String.md)
 * [➞cofactor_requirements](organismDescriptor__cofactor_requirements.md)  <sub>0..\*</sub>
     * Description: Cofactors required by this organism
     * Range: [CofactorRequirement](CofactorRequirement.md)
 * [➞transporters](organismDescriptor__transporters.md)  <sub>0..\*</sub>
     * Description: Annotated transport systems
     * Range: [TransporterAnnotation](TransporterAnnotation.md)
 * [➞evidence](organismDescriptor__evidence.md)  <sub>0..\*</sub>
     * Description: Evidence supporting growth on this medium
     * Range: [EvidenceItem](EvidenceItem.md)

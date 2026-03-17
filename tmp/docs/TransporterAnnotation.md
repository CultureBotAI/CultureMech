
# Class: TransporterAnnotation

Annotation of a transporter or transport system

URI: [culturemech:TransporterAnnotation](https://w3id.org/culturemech/TransporterAnnotation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ChemicalEntityTerm]<substrate_terms%200..*-++[TransporterAnnotation&#124;name:string;transporter_type:TransporterTypeEnum;substrates:string%20*;direction:string%20%3F;genes:string%20*;ec_number:string%20%3F;notes:string%20%3F],[OrganismDescriptor]++-%20transporters%200..*>[TransporterAnnotation],[OrganismDescriptor],[ChemicalEntityTerm])](https://yuml.me/diagram/nofunky;dir:TB/class/[ChemicalEntityTerm]<substrate_terms%200..*-++[TransporterAnnotation&#124;name:string;transporter_type:TransporterTypeEnum;substrates:string%20*;direction:string%20%3F;genes:string%20*;ec_number:string%20%3F;notes:string%20%3F],[OrganismDescriptor]++-%20transporters%200..*>[TransporterAnnotation],[OrganismDescriptor],[ChemicalEntityTerm])

## Referenced by Class

 *  **None** *[➞transporters](organismDescriptor__transporters.md)*  <sub>0..\*</sub>  **[TransporterAnnotation](TransporterAnnotation.md)**

## Attributes


### Own

 * [➞name](transporterAnnotation__name.md)  <sub>1..1</sub>
     * Description: Transporter name or gene name
     * Range: [String](types/String.md)
 * [➞transporter_type](transporterAnnotation__transporter_type.md)  <sub>1..1</sub>
     * Description: Classification of transporter
     * Range: [TransporterTypeEnum](TransporterTypeEnum.md)
 * [➞substrates](transporterAnnotation__substrates.md)  <sub>0..\*</sub>
     * Description: Transported substrates
     * Range: [String](types/String.md)
 * [➞substrate_terms](transporterAnnotation__substrate_terms.md)  <sub>0..\*</sub>
     * Description: CHEBI terms for substrates
     * Range: [ChemicalEntityTerm](ChemicalEntityTerm.md)
 * [➞direction](transporterAnnotation__direction.md)  <sub>0..1</sub>
     * Description: Transport direction (import, export, bidirectional)
     * Range: [String](types/String.md)
 * [➞genes](transporterAnnotation__genes.md)  <sub>0..\*</sub>
     * Description: Gene names or locus tags
     * Range: [String](types/String.md)
 * [➞ec_number](transporterAnnotation__ec_number.md)  <sub>0..1</sub>
     * Description: EC number if enzymatic
     * Range: [String](types/String.md)
 * [➞notes](transporterAnnotation__notes.md)  <sub>0..1</sub>
     * Description: Additional functional notes
     * Range: [String](types/String.md)

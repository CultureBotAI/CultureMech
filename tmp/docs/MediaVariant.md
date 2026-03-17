
# Class: MediaVariant

A variant or modification of the base recipe

URI: [culturemech:MediaVariant](https://w3id.org/culturemech/MediaVariant)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SupplierInfo],[EvidenceItem]<evidence%200..*-++[MediaVariant&#124;name:string;description:string%20%3F;modifications:string%20*;purpose:string%20%3F],[SupplierInfo]<supplier_info%200..1-++[MediaVariant],[MediaRecipe]++-%20variants%200..*>[MediaVariant],[MediaRecipe],[EvidenceItem])](https://yuml.me/diagram/nofunky;dir:TB/class/[SupplierInfo],[EvidenceItem]<evidence%200..*-++[MediaVariant&#124;name:string;description:string%20%3F;modifications:string%20*;purpose:string%20%3F],[SupplierInfo]<supplier_info%200..1-++[MediaVariant],[MediaRecipe]++-%20variants%200..*>[MediaVariant],[MediaRecipe],[EvidenceItem])

## Referenced by Class

 *  **None** *[➞variants](mediaRecipe__variants.md)*  <sub>0..\*</sub>  **[MediaVariant](MediaVariant.md)**

## Attributes


### Own

 * [➞name](mediaVariant__name.md)  <sub>1..1</sub>
     * Description: Variant name (e.g., "Low Salt LB", "LB + Ampicillin")
     * Range: [String](types/String.md)
 * [➞description](mediaVariant__description.md)  <sub>0..1</sub>
     * Description: Purpose and context
     * Range: [String](types/String.md)
 * [➞modifications](mediaVariant__modifications.md)  <sub>0..\*</sub>
     * Description: What differs from base recipe
     * Range: [String](types/String.md)
 * [➞purpose](mediaVariant__purpose.md)  <sub>0..1</sub>
     * Description: Why this variant exists
     * Range: [String](types/String.md)
 * [➞supplier_info](mediaVariant__supplier_info.md)  <sub>0..1</sub>
     * Description: Commercial supplier if premix
     * Range: [SupplierInfo](SupplierInfo.md)
 * [➞evidence](mediaVariant__evidence.md)  <sub>0..\*</sub>
     * Description: Evidence supporting the variant
     * Range: [EvidenceItem](EvidenceItem.md)

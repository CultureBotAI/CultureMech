
# Class: SourceData

Provenance information for imported records

URI: [culturemech:SourceData](https://w3id.org/culturemech/SourceData)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem]<evidence%200..*-++[SourceData&#124;origin:string;community_ids:string%20*;import_date:string%20%3F;notes:string%20%3F],[MediaRecipe]++-%20source_data%200..1>[SourceData],[MediaRecipe],[EvidenceItem])](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem]<evidence%200..*-++[SourceData&#124;origin:string;community_ids:string%20*;import_date:string%20%3F;notes:string%20%3F],[MediaRecipe]++-%20source_data%200..1>[SourceData],[MediaRecipe],[EvidenceItem])

## Referenced by Class

 *  **None** *[➞source_data](mediaRecipe__source_data.md)*  <sub>0..1</sub>  **[SourceData](SourceData.md)**

## Attributes


### Own

 * [➞origin](sourceData__origin.md)  <sub>1..1</sub>
     * Description: Source repository name
     * Range: [String](types/String.md)
     * Example: CommunityMech None
 * [➞community_ids](sourceData__community_ids.md)  <sub>0..\*</sub>
     * Description: List of CommunityMech IDs this recipe was derived from
     * Range: [String](types/String.md)
 * [➞import_date](sourceData__import_date.md)  <sub>0..1</sub>
     * Description: Date of import (ISO 8601)
     * Range: [String](types/String.md)
 * [➞evidence](sourceData__evidence.md)  <sub>0..\*</sub>
     * Description: Evidence records from source repository
     * Range: [EvidenceItem](EvidenceItem.md)
 * [➞notes](sourceData__notes.md)  <sub>0..1</sub>
     * Description: Import notes and additional context
     * Range: [String](types/String.md)

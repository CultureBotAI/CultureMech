
# Class: CurationEvent

Audit trail entry for curation

URI: [culturemech:CurationEvent](https://w3id.org/culturemech/CurationEvent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MediaRecipe]++-%20curation_history%200..*>[CurationEvent&#124;timestamp:string;curator:string;action:string;notes:string%20%3F],[MediaRecipe])](https://yuml.me/diagram/nofunky;dir:TB/class/[MediaRecipe]++-%20curation_history%200..*>[CurationEvent&#124;timestamp:string;curator:string;action:string;notes:string%20%3F],[MediaRecipe])

## Referenced by Class

 *  **None** *[➞curation_history](mediaRecipe__curation_history.md)*  <sub>0..\*</sub>  **[CurationEvent](CurationEvent.md)**

## Attributes


### Own

 * [➞timestamp](curationEvent__timestamp.md)  <sub>1..1</sub>
     * Description: ISO 8601 timestamp
     * Range: [String](types/String.md)
 * [➞curator](curationEvent__curator.md)  <sub>1..1</sub>
     * Description: Name or identifier of curator
     * Range: [String](types/String.md)
 * [➞action](curationEvent__action.md)  <sub>1..1</sub>
     * Description: Action taken (created, updated, validated, etc.)
     * Range: [String](types/String.md)
 * [➞notes](curationEvent__notes.md)  <sub>0..1</sub>
     * Description: Additional context
     * Range: [String](types/String.md)

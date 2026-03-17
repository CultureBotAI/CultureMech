
# Class: PublicationReference

Literature reference

URI: [culturemech:PublicationReference](https://w3id.org/culturemech/PublicationReference)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MediaRecipe]++-%20references%200..*>[PublicationReference&#124;reference:string;title:string%20%3F;authors:string%20%3F;year:integer%20%3F;notes:string%20%3F],[MediaRecipe])](https://yuml.me/diagram/nofunky;dir:TB/class/[MediaRecipe]++-%20references%200..*>[PublicationReference&#124;reference:string;title:string%20%3F;authors:string%20%3F;year:integer%20%3F;notes:string%20%3F],[MediaRecipe])

## Referenced by Class

 *  **None** *[➞references](mediaRecipe__references.md)*  <sub>0..\*</sub>  **[PublicationReference](PublicationReference.md)**

## Attributes


### Own

 * [➞reference](publicationReference__reference.md)  <sub>1..1</sub>
     * Description: Citation (PMID, DOI, or historical reference)
     * Range: [String](types/String.md)
 * [➞title](publicationReference__title.md)  <sub>0..1</sub>
     * Description: Publication title
     * Range: [String](types/String.md)
 * [➞authors](publicationReference__authors.md)  <sub>0..1</sub>
     * Description: Author list
     * Range: [String](types/String.md)
 * [➞year](publicationReference__year.md)  <sub>0..1</sub>
     * Description: Publication year
     * Range: [Integer](types/Integer.md)
 * [➞notes](publicationReference__notes.md)  <sub>0..1</sub>
     * Description: Additional context about the reference
     * Range: [String](types/String.md)

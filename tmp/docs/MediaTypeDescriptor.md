
# Class: MediaTypeDescriptor

Classification and authoritative database reference for the medium

URI: [culturemech:MediaTypeDescriptor](https://w3id.org/culturemech/MediaTypeDescriptor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MediaDatabaseTerm]<term%200..1-++[MediaTypeDescriptor&#124;preferred_term:string],[MediaRecipe]++-%20media_term%200..1>[MediaTypeDescriptor],[Descriptor]^-[MediaTypeDescriptor],[MediaRecipe],[MediaDatabaseTerm],[Descriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[MediaDatabaseTerm]<term%200..1-++[MediaTypeDescriptor&#124;preferred_term:string],[MediaRecipe]++-%20media_term%200..1>[MediaTypeDescriptor],[Descriptor]^-[MediaTypeDescriptor],[MediaRecipe],[MediaDatabaseTerm],[Descriptor])

## Parents

 *  is_a: [Descriptor](Descriptor.md) - Base class for descriptor pattern. Descriptors have a human-readable preferred_term and optional ontology term.

## Referenced by Class

 *  **None** *[➞media_term](mediaRecipe__media_term.md)*  <sub>0..1</sub>  **[MediaTypeDescriptor](MediaTypeDescriptor.md)**

## Attributes


### Own

 * [➞preferred_term](mediaTypeDescriptor__preferred_term.md)  <sub>1..1</sub>
     * Description: Medium designation in source database (e.g., "DSMZ Medium 1", "LB")
     * Range: [String](types/String.md)
 * [➞term](mediaTypeDescriptor__term.md)  <sub>0..1</sub>
     * Description: Authoritative media database identifier
     * Range: [MediaDatabaseTerm](MediaDatabaseTerm.md)

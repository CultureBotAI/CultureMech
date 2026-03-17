
# Class: MediaDatabaseTerm

Identifier from authoritative media database

URI: [culturemech:MediaDatabaseTerm](https://w3id.org/culturemech/MediaDatabaseTerm)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[MediaTypeDescriptor]++-%20term%200..1>[MediaDatabaseTerm&#124;id(i):string;label(i):string%20%3F],[Term]^-[MediaDatabaseTerm],[MediaTypeDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[MediaTypeDescriptor]++-%20term%200..1>[MediaDatabaseTerm&#124;id(i):string;label(i):string%20%3F],[Term]^-[MediaDatabaseTerm],[MediaTypeDescriptor])

## Identifier prefixes

 * mediadive.medium
 * komodo.medium
 * DSMZ
 * TOGO
 * ATCC
 * NCIT

## Parents

 *  is_a: [Term](Term.md) - Base class for ontology term references. Subclasses specify id_prefixes for validation.

## Referenced by Class

 *  **None** *[➞term](mediaTypeDescriptor__term.md)*  <sub>0..1</sub>  **[MediaDatabaseTerm](MediaDatabaseTerm.md)**

## Attributes


### Inherited from Term:

 * [➞id](term__id.md)  <sub>1..1</sub>
     * Description: Ontology identifier (CURIE)
     * Range: [String](types/String.md)
 * [➞label](term__label.md)  <sub>0..1</sub>
     * Description: Ontology term label
     * Range: [String](types/String.md)


# Class: GTDBTerm

A GTDB genome identifier. id = GTDB accession (e.g. GTDB:RS_GCF_000006945.2), label = full GTDB lineage string (e.g. d__Bacteria;p__Proteobacteria;...)

URI: [culturemech:GTDBTerm](https://w3id.org/culturemech/GTDBTerm)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[OrganismDescriptor]++-%20gtdb_term%200..1>[GTDBTerm&#124;id(i):string;label(i):string%20%3F],[Term]^-[GTDBTerm],[OrganismDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[OrganismDescriptor]++-%20gtdb_term%200..1>[GTDBTerm&#124;id(i):string;label(i):string%20%3F],[Term]^-[GTDBTerm],[OrganismDescriptor])

## Identifier prefixes

 * GTDB

## Parents

 *  is_a: [Term](Term.md) - Base class for ontology term references. Subclasses specify id_prefixes for validation.

## Referenced by Class

 *  **None** *[➞gtdb_term](organismDescriptor__gtdb_term.md)*  <sub>0..1</sub>  **[GTDBTerm](GTDBTerm.md)**

## Attributes


### Inherited from Term:

 * [➞id](term__id.md)  <sub>1..1</sub>
     * Description: Ontology identifier (CURIE)
     * Range: [String](types/String.md)
 * [➞label](term__label.md)  <sub>0..1</sub>
     * Description: Ontology term label
     * Range: [String](types/String.md)

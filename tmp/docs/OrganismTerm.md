
# Class: OrganismTerm

An NCBITaxon term representing an organism

URI: [culturemech:OrganismTerm](https://w3id.org/culturemech/OrganismTerm)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[OrganismDescriptor]++-%20term%200..1>[OrganismTerm&#124;id:string;label(i):string%20%3F],[Term]^-[OrganismTerm],[OrganismDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[OrganismDescriptor]++-%20term%200..1>[OrganismTerm&#124;id:string;label(i):string%20%3F],[Term]^-[OrganismTerm],[OrganismDescriptor])

## Identifier prefixes

 * NCBITaxon

## Parents

 *  is_a: [Term](Term.md) - Base class for ontology term references. Subclasses specify id_prefixes for validation.

## Referenced by Class

 *  **None** *[➞term](organismDescriptor__term.md)*  <sub>0..1</sub>  **[OrganismTerm](OrganismTerm.md)**

## Attributes


### Own

 * [OrganismTerm➞id](OrganismTerm_id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)

### Inherited from Term:

 * [➞label](term__label.md)  <sub>0..1</sub>
     * Description: Ontology term label
     * Range: [String](types/String.md)

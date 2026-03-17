
# Class: Term

Base class for ontology term references. Subclasses specify id_prefixes for validation.

URI: [culturemech:Term](https://w3id.org/culturemech/Term)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SolutionDescriptor]++-%20term%200..1>[Term&#124;id:string;label:string%20%3F],[Term]^-[OrganismTerm],[Term]^-[MediaIngredientMechTerm],[Term]^-[MediaDatabaseTerm],[Term]^-[GTDBTerm],[Term]^-[ChemicalEntityTerm],[SolutionDescriptor],[OrganismTerm],[MediaIngredientMechTerm],[MediaDatabaseTerm],[GTDBTerm],[ChemicalEntityTerm])](https://yuml.me/diagram/nofunky;dir:TB/class/[SolutionDescriptor]++-%20term%200..1>[Term&#124;id:string;label:string%20%3F],[Term]^-[OrganismTerm],[Term]^-[MediaIngredientMechTerm],[Term]^-[MediaDatabaseTerm],[Term]^-[GTDBTerm],[Term]^-[ChemicalEntityTerm],[SolutionDescriptor],[OrganismTerm],[MediaIngredientMechTerm],[MediaDatabaseTerm],[GTDBTerm],[ChemicalEntityTerm])

## Children

 * [ChemicalEntityTerm](ChemicalEntityTerm.md) - A CHEBI term representing a chemical entity
 * [GTDBTerm](GTDBTerm.md) - A GTDB genome identifier. id = GTDB accession (e.g. GTDB:RS_GCF_000006945.2), label = full GTDB lineage string (e.g. d__Bacteria;p__Proteobacteria;...)
 * [MediaDatabaseTerm](MediaDatabaseTerm.md) - Identifier from authoritative media database
 * [MediaIngredientMechTerm](MediaIngredientMechTerm.md) - A MediaIngredientMech identifier for a media ingredient
 * [OrganismTerm](OrganismTerm.md) - An NCBITaxon term representing an organism

## Referenced by Class

 *  **None** *[➞term](solutionDescriptor__term.md)*  <sub>0..1</sub>  **[Term](Term.md)**

## Attributes


### Own

 * [➞id](term__id.md)  <sub>1..1</sub>
     * Description: Ontology identifier (CURIE)
     * Range: [String](types/String.md)
 * [➞label](term__label.md)  <sub>0..1</sub>
     * Description: Ontology term label
     * Range: [String](types/String.md)

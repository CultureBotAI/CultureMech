
# Class: RecipeSynonym

An alternate name for a recipe from a specific source

URI: [culturemech:RecipeSynonym](https://w3id.org/culturemech/RecipeSynonym)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MediaRecipe]++-%20synonyms%200..*>[RecipeSynonym&#124;name:string;source:string;source_id:string%20%3F;original_category:CategoryEnum%20%3F],[MediaRecipe])](https://yuml.me/diagram/nofunky;dir:TB/class/[MediaRecipe]++-%20synonyms%200..*>[RecipeSynonym&#124;name:string;source:string;source_id:string%20%3F;original_category:CategoryEnum%20%3F],[MediaRecipe])

## Referenced by Class

 *  **None** *[➞synonyms](mediaRecipe__synonyms.md)*  <sub>0..\*</sub>  **[RecipeSynonym](RecipeSynonym.md)**

## Attributes


### Own

 * [➞name](recipeSynonym__name.md)  <sub>1..1</sub>
     * Description: Alternate recipe name (non-canonical)
     * Range: [String](types/String.md)
 * [➞source](recipeSynonym__source.md)  <sub>1..1</sub>
     * Description: Source database (KOMODO, MediaDive, TOGO, etc.)
     * Range: [String](types/String.md)
 * [➞source_id](recipeSynonym__source_id.md)  <sub>0..1</sub>
     * Description: Original identifier in source database
     * Range: [String](types/String.md)
 * [➞original_category](recipeSynonym__original_category.md)  <sub>0..1</sub>
     * Description: Original category assignment before merge
     * Range: [CategoryEnum](CategoryEnum.md)

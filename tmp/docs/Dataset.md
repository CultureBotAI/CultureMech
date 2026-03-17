
# Class: Dataset

Omics dataset generated using this medium

URI: [culturemech:Dataset](https://w3id.org/culturemech/Dataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MediaRecipe]++-%20datasets%200..*>[Dataset&#124;dataset_id:string;dataset_type:string%20%3F;description:string%20%3F;url:uri%20%3F],[MediaRecipe])](https://yuml.me/diagram/nofunky;dir:TB/class/[MediaRecipe]++-%20datasets%200..*>[Dataset&#124;dataset_id:string;dataset_type:string%20%3F;description:string%20%3F;url:uri%20%3F],[MediaRecipe])

## Referenced by Class

 *  **None** *[➞datasets](mediaRecipe__datasets.md)*  <sub>0..\*</sub>  **[Dataset](Dataset.md)**

## Attributes


### Own

 * [➞dataset_id](dataset__dataset_id.md)  <sub>1..1</sub>
     * Description: Dataset identifier (GEO, SRA, etc.)
     * Range: [String](types/String.md)
 * [➞dataset_type](dataset__dataset_type.md)  <sub>0..1</sub>
     * Description: Type of omics data (genomics, transcriptomics, metabolomics, etc.)
     * Range: [String](types/String.md)
 * [➞description](dataset__description.md)  <sub>0..1</sub>
     * Description: Brief description of the dataset
     * Range: [String](types/String.md)
 * [➞url](dataset__url.md)  <sub>0..1</sub>
     * Description: Direct link to dataset
     * Range: [Uri](types/Uri.md)

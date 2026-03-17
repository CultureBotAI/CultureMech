
# Class: MergeMetadata

Metadata about merge process and quality

URI: [culturemech:MergeMetadata](https://w3id.org/culturemech/MergeMetadata)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MediaRecipe]++-%20merge_metadata%200..1>[MergeMetadata&#124;merge_version:string%20%3F;merge_mode:string%20%3F;merge_reason:MergeReasonEnum%20%3F;merge_confidence:float%20%3F;hierarchy_conflicts:string%20*;fingerprint_mode:string%20%3F],[MediaRecipe])](https://yuml.me/diagram/nofunky;dir:TB/class/[MediaRecipe]++-%20merge_metadata%200..1>[MergeMetadata&#124;merge_version:string%20%3F;merge_mode:string%20%3F;merge_reason:MergeReasonEnum%20%3F;merge_confidence:float%20%3F;hierarchy_conflicts:string%20*;fingerprint_mode:string%20%3F],[MediaRecipe])

## Referenced by Class

 *  **None** *[➞merge_metadata](mediaRecipe__merge_metadata.md)*  <sub>0..1</sub>  **[MergeMetadata](MergeMetadata.md)**

## Attributes


### Own

 * [➞merge_version](mergeMetadata__merge_version.md)  <sub>0..1</sub>
     * Description: Version of merge pipeline used
     * Range: [String](types/String.md)
 * [➞merge_mode](mergeMetadata__merge_mode.md)  <sub>0..1</sub>
     * Description: Merge mode used (conservative/aggressive/variant-aware)
     * Range: [String](types/String.md)
 * [➞merge_reason](mergeMetadata__merge_reason.md)  <sub>0..1</sub>
     * Description: Why these recipes were merged together
     * Range: [MergeReasonEnum](MergeReasonEnum.md)
 * [➞merge_confidence](mergeMetadata__merge_confidence.md)  <sub>0..1</sub>
     * Description: Confidence score for merge decision (0.0-1.0)
     * Range: [Float](types/Float.md)
 * [➞hierarchy_conflicts](mergeMetadata__hierarchy_conflicts.md)  <sub>0..\*</sub>
     * Description: Ingredients with conflicting merge signals
     * Range: [String](types/String.md)
 * [➞fingerprint_mode](mergeMetadata__fingerprint_mode.md)  <sub>0..1</sub>
     * Description: Fingerprinting mode used (chemical/variant/original)
     * Range: [String](types/String.md)

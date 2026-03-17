
# Class: MediaRecipe

A complete growth medium formulation for culturing microorganisms. This is the root entity - one per YAML file.

URI: [culturemech:MediaRecipe](https://w3id.org/culturemech/MediaRecipe)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StorageConditions],[SterilizationDescriptor],[SourceData],[SolutionDescriptor],[RecipeSynonym],[PublicationReference],[PreparationStep],[OrganismDescriptor],[MergeMetadata],[MediaVariant],[MediaTypeDescriptor],[SourceData]<source_data%200..1-++[MediaRecipe&#124;name:string;original_name:string%20%3F;category:CategoryEnum%20%3F;categories:CategoryEnum%20*;high_metal:boolean%20%3F;high_ree:boolean%20%3F;merged_from:string%20*;merge_fingerprint:string%20%3F;chemical_fingerprint:string%20%3F;variant_fingerprint:string%20%3F;fingerprint_version:string%20%3F;description:string%20%3F;organism_culture_type:OrganismCultureTypeEnum%20%3F;medium_type:MediumTypeEnum;physical_state:PhysicalStateEnum;ph_value:float%20%3F;ph_range:string%20%3F;light_intensity:string%20%3F;light_cycle:string%20%3F;light_quality:string%20%3F;temperature_range:string%20%3F;temperature_value:float%20%3F;salinity:string%20%3F;aeration:string%20%3F;culture_vessel:string%20%3F;applications:string%20*;notes:string%20%3F;data_quality_flags:string%20*;incubation_atmosphere:AtmosphereEnum%20%3F],[CurationEvent]<curation_history%200..*-++[MediaRecipe],[Dataset]<datasets%200..*-++[MediaRecipe],[EvidenceItem]<evidence%200..*-++[MediaRecipe],[PublicationReference]<references%200..*-++[MediaRecipe],[MediaVariant]<variants%200..*-++[MediaRecipe],[StorageConditions]<storage%200..1-++[MediaRecipe],[SterilizationDescriptor]<sterilization%200..1-++[MediaRecipe],[PreparationStep]<preparation_steps%200..*-++[MediaRecipe],[SolutionDescriptor]<solutions%200..*-++[MediaRecipe],[IngredientDescriptor]<ingredients%201..*-++[MediaRecipe],[OrganismDescriptor]<target_organisms%200..*-++[MediaRecipe],[MediaTypeDescriptor]<media_term%200..1-++[MediaRecipe],[MergeMetadata]<merge_metadata%200..1-++[MediaRecipe],[RecipeSynonym]<synonyms%200..*-++[MediaRecipe],[IngredientDescriptor],[EvidenceItem],[Dataset],[CurationEvent])](https://yuml.me/diagram/nofunky;dir:TB/class/[StorageConditions],[SterilizationDescriptor],[SourceData],[SolutionDescriptor],[RecipeSynonym],[PublicationReference],[PreparationStep],[OrganismDescriptor],[MergeMetadata],[MediaVariant],[MediaTypeDescriptor],[SourceData]<source_data%200..1-++[MediaRecipe&#124;name:string;original_name:string%20%3F;category:CategoryEnum%20%3F;categories:CategoryEnum%20*;high_metal:boolean%20%3F;high_ree:boolean%20%3F;merged_from:string%20*;merge_fingerprint:string%20%3F;chemical_fingerprint:string%20%3F;variant_fingerprint:string%20%3F;fingerprint_version:string%20%3F;description:string%20%3F;organism_culture_type:OrganismCultureTypeEnum%20%3F;medium_type:MediumTypeEnum;physical_state:PhysicalStateEnum;ph_value:float%20%3F;ph_range:string%20%3F;light_intensity:string%20%3F;light_cycle:string%20%3F;light_quality:string%20%3F;temperature_range:string%20%3F;temperature_value:float%20%3F;salinity:string%20%3F;aeration:string%20%3F;culture_vessel:string%20%3F;applications:string%20*;notes:string%20%3F;data_quality_flags:string%20*;incubation_atmosphere:AtmosphereEnum%20%3F],[CurationEvent]<curation_history%200..*-++[MediaRecipe],[Dataset]<datasets%200..*-++[MediaRecipe],[EvidenceItem]<evidence%200..*-++[MediaRecipe],[PublicationReference]<references%200..*-++[MediaRecipe],[MediaVariant]<variants%200..*-++[MediaRecipe],[StorageConditions]<storage%200..1-++[MediaRecipe],[SterilizationDescriptor]<sterilization%200..1-++[MediaRecipe],[PreparationStep]<preparation_steps%200..*-++[MediaRecipe],[SolutionDescriptor]<solutions%200..*-++[MediaRecipe],[IngredientDescriptor]<ingredients%201..*-++[MediaRecipe],[OrganismDescriptor]<target_organisms%200..*-++[MediaRecipe],[MediaTypeDescriptor]<media_term%200..1-++[MediaRecipe],[MergeMetadata]<merge_metadata%200..1-++[MediaRecipe],[RecipeSynonym]<synonyms%200..*-++[MediaRecipe],[IngredientDescriptor],[EvidenceItem],[Dataset],[CurationEvent])

## Attributes


### Own

 * [➞name](mediaRecipe__name.md)  <sub>1..1</sub>
     * Description: Human-readable medium name (e.g., "LB Broth", "M9 Minimal Medium")
     * Range: [String](types/String.md)
 * [➞original_name](mediaRecipe__original_name.md)  <sub>0..1</sub>
     * Description: Original name from source database before filename sanitization. May contain special characters like /, :, %, (, ), ', ", <, >, &, #, etc. This field preserves the exact name as it appears in the source database.
     * Range: [String](types/String.md)
 * [➞category](mediaRecipe__category.md)  <sub>0..1</sub>
     * Description: Broad category for organization
     * Range: [CategoryEnum](CategoryEnum.md)
 * [➞categories](mediaRecipe__categories.md)  <sub>0..\*</sub>
     * Description: All categories this recipe appears in (for cross-category merges)
     * Range: [CategoryEnum](CategoryEnum.md)
 * [➞high_metal](mediaRecipe__high_metal.md)  <sub>0..1</sub>
     * Description: Indicates media with total metal concentration above the 90th percentile threshold (≥1049.84 mM). Metals include Fe, Cu, Zn, Mn, Co, Ni, Mo, Se, W, V, Cr, Ca, Mg, K, Na. Based on automated concentration analysis of ingredient composition.
     * Range: [Boolean](types/Boolean.md)
 * [➞high_ree](mediaRecipe__high_ree.md)  <sub>0..1</sub>
     * Description: Indicates media with total rare earth element (REE) concentration above the 90th percentile threshold (≥1030.48 mM). REEs include lanthanides (La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu) plus Sc and Y. Based on automated concentration analysis of ingredient composition.
     * Range: [Boolean](types/Boolean.md)
 * [➞synonyms](mediaRecipe__synonyms.md)  <sub>0..\*</sub>
     * Description: Alternate names from merged duplicate recipes
     * Range: [RecipeSynonym](RecipeSynonym.md)
 * [➞merged_from](mediaRecipe__merged_from.md)  <sub>0..\*</sub>
     * Description: Original recipe IDs that were merged into this record
     * Range: [String](types/String.md)
 * [➞merge_fingerprint](mediaRecipe__merge_fingerprint.md)  <sub>0..1</sub>
     * Description: SHA256 hash of ingredient set for deduplication tracking
     * Range: [String](types/String.md)
 * [➞chemical_fingerprint](mediaRecipe__chemical_fingerprint.md)  <sub>0..1</sub>
     * Description: SHA256 hash using parent ingredients (hierarchy-aware)
     * Range: [String](types/String.md)
 * [➞variant_fingerprint](mediaRecipe__variant_fingerprint.md)  <sub>0..1</sub>
     * Description: SHA256 hash preserving variant distinctions
     * Range: [String](types/String.md)
 * [➞fingerprint_version](mediaRecipe__fingerprint_version.md)  <sub>0..1</sub>
     * Description: Version of fingerprinting algorithm used
     * Range: [String](types/String.md)
 * [➞merge_metadata](mediaRecipe__merge_metadata.md)  <sub>0..1</sub>
     * Description: Metadata about merge process and quality
     * Range: [MergeMetadata](MergeMetadata.md)
 * [➞media_term](mediaRecipe__media_term.md)  <sub>0..1</sub>
     * Description: Reference to authoritative media database
     * Range: [MediaTypeDescriptor](MediaTypeDescriptor.md)
 * [➞description](mediaRecipe__description.md)  <sub>0..1</sub>
     * Description: Overview of the medium and its purpose
     * Range: [String](types/String.md)
 * [➞target_organisms](mediaRecipe__target_organisms.md)  <sub>0..\*</sub>
     * Description: Organisms for which this medium is designed
     * Range: [OrganismDescriptor](OrganismDescriptor.md)
 * [➞organism_culture_type](mediaRecipe__organism_culture_type.md)  <sub>0..1</sub>
     * Description: Whether this medium targets a pure isolate culture or a mixed microbial community
     * Range: [OrganismCultureTypeEnum](OrganismCultureTypeEnum.md)
 * [➞medium_type](mediaRecipe__medium_type.md)  <sub>1..1</sub>
     * Description: Classification of the medium
     * Range: [MediumTypeEnum](MediumTypeEnum.md)
 * [➞physical_state](mediaRecipe__physical_state.md)  <sub>1..1</sub>
     * Description: Physical form of the medium
     * Range: [PhysicalStateEnum](PhysicalStateEnum.md)
 * [➞ph_value](mediaRecipe__ph_value.md)  <sub>0..1</sub>
     * Description: Target pH value
     * Range: [Float](types/Float.md)
 * [➞ph_range](mediaRecipe__ph_range.md)  <sub>0..1</sub>
     * Description: Acceptable pH range (e.g., "6.8-7.2")
     * Range: [String](types/String.md)
 * [➞light_intensity](mediaRecipe__light_intensity.md)  <sub>0..1</sub>
     * Description: Light intensity for photosynthetic organisms (e.g., "50 µmol photons m⁻² s⁻¹")
     * Range: [String](types/String.md)
 * [➞light_cycle](mediaRecipe__light_cycle.md)  <sub>0..1</sub>
     * Description: Photoperiod light:dark cycle (e.g., "16:8", "continuous light", "24:0")
     * Range: [String](types/String.md)
 * [➞light_quality](mediaRecipe__light_quality.md)  <sub>0..1</sub>
     * Description: Light spectrum or wavelength (e.g., "cool white fluorescent", "red LED 660nm")
     * Range: [String](types/String.md)
 * [➞temperature_range](mediaRecipe__temperature_range.md)  <sub>0..1</sub>
     * Description: Optimal temperature range (e.g., "20-25°C", "room temperature")
     * Range: [String](types/String.md)
 * [➞temperature_value](mediaRecipe__temperature_value.md)  <sub>0..1</sub>
     * Description: Specific culture temperature in Celsius
     * Range: [Float](types/Float.md)
 * [➞salinity](mediaRecipe__salinity.md)  <sub>0..1</sub>
     * Description: Salt concentration for marine/brackish media (e.g., "35 ppt", "3.5%")
     * Range: [String](types/String.md)
 * [➞aeration](mediaRecipe__aeration.md)  <sub>0..1</sub>
     * Description: Gas exchange method (e.g., "0.5% CO2 in air", "bubbling", "shaking at 150 rpm")
     * Range: [String](types/String.md)
 * [➞culture_vessel](mediaRecipe__culture_vessel.md)  <sub>0..1</sub>
     * Description: Recommended culture container (e.g., "Erlenmeyer flask", "test tube", "petri dish")
     * Range: [String](types/String.md)
 * [➞ingredients](mediaRecipe__ingredients.md)  <sub>1..\*</sub>
     * Description: Chemical and biological ingredients
     * Range: [IngredientDescriptor](IngredientDescriptor.md)
 * [➞solutions](mediaRecipe__solutions.md)  <sub>0..\*</sub>
     * Description: Pre-prepared stock solutions used as ingredients
     * Range: [SolutionDescriptor](SolutionDescriptor.md)
 * [➞preparation_steps](mediaRecipe__preparation_steps.md)  <sub>0..\*</sub>
     * Description: Ordered steps to prepare the medium
     * Range: [PreparationStep](PreparationStep.md)
 * [➞sterilization](mediaRecipe__sterilization.md)  <sub>0..1</sub>
     * Description: Sterilization method and parameters
     * Range: [SterilizationDescriptor](SterilizationDescriptor.md)
 * [➞storage](mediaRecipe__storage.md)  <sub>0..1</sub>
     * Description: Storage conditions for prepared medium
     * Range: [StorageConditions](StorageConditions.md)
 * [➞applications](mediaRecipe__applications.md)  <sub>0..\*</sub>
     * Description: Use cases and applications
     * Range: [String](types/String.md)
 * [➞variants](mediaRecipe__variants.md)  <sub>0..\*</sub>
     * Description: Related formulations or modifications
     * Range: [MediaVariant](MediaVariant.md)
 * [➞references](mediaRecipe__references.md)  <sub>0..\*</sub>
     * Description: Original literature sources
     * Range: [PublicationReference](PublicationReference.md)
 * [➞notes](mediaRecipe__notes.md)  <sub>0..1</sub>
     * Description: Additional context, historical notes, tips
     * Range: [String](types/String.md)
 * [➞evidence](mediaRecipe__evidence.md)  <sub>0..\*</sub>
     * Description: Evidence supporting formulation claims
     * Range: [EvidenceItem](EvidenceItem.md)
 * [➞datasets](mediaRecipe__datasets.md)  <sub>0..\*</sub>
     * Description: Omics datasets generated using this medium
     * Range: [Dataset](Dataset.md)
 * [➞curation_history](mediaRecipe__curation_history.md)  <sub>0..\*</sub>
     * Description: Audit trail of curation events
     * Range: [CurationEvent](CurationEvent.md)
 * [➞data_quality_flags](mediaRecipe__data_quality_flags.md)  <sub>0..\*</sub>
     * Description: Data quality indicators for transparency
     * Range: [String](types/String.md)
 * [➞incubation_atmosphere](mediaRecipe__incubation_atmosphere.md)  <sub>0..1</sub>
     * Description: Atmospheric conditions for incubation
     * Range: [AtmosphereEnum](AtmosphereEnum.md)
 * [➞source_data](mediaRecipe__source_data.md)  <sub>0..1</sub>
     * Description: Provenance tracking for records imported from other repositories
     * Range: [SourceData](SourceData.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | culturemech:MediaRecipe |

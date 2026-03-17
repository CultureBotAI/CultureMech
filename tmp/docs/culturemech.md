
# culturemech


**metamodel version:** 1.7.0

**version:** None


LinkML schema for modeling microbial culture media recipes and formulations.
Follows the dismech architecture pattern with descriptor classes for ontology grounding.


### Classes

 * [CofactorRequirement](CofactorRequirement.md) - Cofactor requirement for an organism
 * [ConcentrationValue](ConcentrationValue.md) - Quantified concentration with units
 * [CurationEvent](CurationEvent.md) - Audit trail entry for curation
 * [Dataset](Dataset.md) - Omics dataset generated using this medium
 * [Descriptor](Descriptor.md) - Base class for descriptor pattern. Descriptors have a human-readable preferred_term and optional ontology term.
     * [CofactorDescriptor](CofactorDescriptor.md) - A cofactor or coenzyme required for enzymatic activity
     * [IngredientDescriptor](IngredientDescriptor.md) - Chemical or biological ingredient in a medium
     * [MediaTypeDescriptor](MediaTypeDescriptor.md) - Classification and authoritative database reference for the medium
     * [OrganismDescriptor](OrganismDescriptor.md) - Target organism for the medium
     * [SolutionDescriptor](SolutionDescriptor.md) - A pre-prepared stock solution used as an ingredient
 * [EvidenceItem](EvidenceItem.md) - Evidence supporting a claim about media formulation or performance
 * [IngredientReference](IngredientReference.md) - Reference to canonical ingredient
 * [MediaRecipe](MediaRecipe.md) - A complete growth medium formulation for culturing microorganisms. This is the root entity - one per YAML file.
 * [MediaVariant](MediaVariant.md) - A variant or modification of the base recipe
 * [MergeMetadata](MergeMetadata.md) - Metadata about merge process and quality
 * [PreparationStep](PreparationStep.md) - A step in medium preparation
 * [PublicationReference](PublicationReference.md) - Literature reference
 * [RecipeSynonym](RecipeSynonym.md) - An alternate name for a recipe from a specific source
 * [SourceData](SourceData.md) - Provenance information for imported records
 * [SterilizationDescriptor](SterilizationDescriptor.md) - Sterilization method and parameters
 * [StorageConditions](StorageConditions.md) - Storage requirements for prepared medium
 * [SupplierInfo](SupplierInfo.md) - Commercial supplier information
 * [TemperatureValue](TemperatureValue.md) - Temperature with units
 * [Term](Term.md) - Base class for ontology term references. Subclasses specify id_prefixes for validation.
     * [ChemicalEntityTerm](ChemicalEntityTerm.md) - A CHEBI term representing a chemical entity
     * [GTDBTerm](GTDBTerm.md) - A GTDB genome identifier. id = GTDB accession (e.g. GTDB:RS_GCF_000006945.2), label = full GTDB lineage string (e.g. d__Bacteria;p__Proteobacteria;...)
     * [MediaDatabaseTerm](MediaDatabaseTerm.md) - Identifier from authoritative media database
     * [MediaIngredientMechTerm](MediaIngredientMechTerm.md) - A MediaIngredientMech identifier for a media ingredient
     * [OrganismTerm](OrganismTerm.md) - An NCBITaxon term representing an organism
 * [TransporterAnnotation](TransporterAnnotation.md) - Annotation of a transporter or transport system

### Mixins


### Slots

 * [➞bioavailability](cofactorDescriptor__bioavailability.md) - Uptake and availability characteristics
 * [➞biosynthesis_genes](cofactorDescriptor__biosynthesis_genes.md) - Genes involved in cofactor biosynthesis
 * [➞category](cofactorDescriptor__category.md) - High-level classification
 * [➞ec_associations](cofactorDescriptor__ec_associations.md) - EC numbers of enzymes using this cofactor
 * [➞enzyme_examples](cofactorDescriptor__enzyme_examples.md) - Example enzymes requiring this cofactor
 * [➞kegg_pathways](cofactorDescriptor__kegg_pathways.md) - KEGG pathway IDs for biosynthesis
 * [➞notes](cofactorDescriptor__notes.md) - Additional information about the cofactor
 * [➞precursor](cofactorDescriptor__precursor.md) - Precursor molecule (e.g., thiamine → TPP)
 * [➞precursor_term](cofactorDescriptor__precursor_term.md) - CHEBI term for precursor
 * [➞preferred_term](cofactorDescriptor__preferred_term.md) - Human-readable cofactor name (e.g., "Thiamine pyrophosphate", "NAD")
 * [➞term](cofactorDescriptor__term.md) - CHEBI term for the cofactor
 * [➞can_biosynthesize](cofactorRequirement__can_biosynthesize.md) - Whether organism can synthesize this cofactor
 * [➞cofactor](cofactorRequirement__cofactor.md) - Required cofactor
 * [➞confidence](cofactorRequirement__confidence.md) - Confidence level (0.0-1.0) based on genome annotation
 * [➞evidence](cofactorRequirement__evidence.md) - Supporting evidence for requirement
 * [➞genes](cofactorRequirement__genes.md) - Genes related to biosynthesis or utilization
 * [➞per_volume](concentrationValue__per_volume.md) - Volume basis (e.g., "per liter", "per 100 mL")
 * [➞unit](concentrationValue__unit.md) - Concentration unit
 * [➞value](concentrationValue__value.md) - Numeric value or range
 * [➞action](curationEvent__action.md) - Action taken (created, updated, validated, etc.)
 * [➞curator](curationEvent__curator.md) - Name or identifier of curator
 * [➞notes](curationEvent__notes.md) - Additional context
 * [➞timestamp](curationEvent__timestamp.md) - ISO 8601 timestamp
 * [➞dataset_id](dataset__dataset_id.md) - Dataset identifier (GEO, SRA, etc.)
 * [➞dataset_type](dataset__dataset_type.md) - Type of omics data (genomics, transcriptomics, metabolomics, etc.)
 * [➞description](dataset__description.md) - Brief description of the dataset
 * [➞url](dataset__url.md) - Direct link to dataset
 * [➞explanation](evidenceItem__explanation.md) - Why this evidence supports the claim
 * [➞reference](evidenceItem__reference.md) - Citation (PMID, DOI, or historical reference)
 * [➞snippet](evidenceItem__snippet.md) - Exact quote from paper (if PMID/DOI available)
 * [➞supports](evidenceItem__supports.md) - Level of support
 * [➞chemical_formula](ingredientDescriptor__chemical_formula.md) - Molecular formula (e.g., "C6H12O6")
 * [➞cofactors_provided](ingredientDescriptor__cofactors_provided.md) - Cofactors supplied by this ingredient
 * [➞concentration](ingredientDescriptor__concentration.md) - Amount of ingredient
 * [➞evidence](ingredientDescriptor__evidence.md) - Evidence for this ingredient's role
 * [➞mediaingredientmech_term](ingredientDescriptor__mediaingredientmech_term.md) - MediaIngredientMech identifier for this ingredient
 * [➞modifier](ingredientDescriptor__modifier.md) - Modification in variants (INCREASED, DECREASED)
 * [➞molecular_weight](ingredientDescriptor__molecular_weight.md) - Molecular weight in g/mol
 * [➞notes](ingredientDescriptor__notes.md) - Preparation notes specific to this ingredient
 * [➞parent_ingredient](ingredientDescriptor__parent_ingredient.md) - Reference to parent chemical entity from MediaIngredientMech
 * [➞preferred_term](ingredientDescriptor__preferred_term.md) - Human-readable ingredient name (e.g., "Glucose", "Yeast Extract")
 * [➞role](ingredientDescriptor__role.md) - Functional role(s) in the medium
 * [➞supplier_catalog](ingredientDescriptor__supplier_catalog.md) - Supplier information for sourcing
 * [➞term](ingredientDescriptor__term.md) - CHEBI term for the chemical entity
 * [➞variant_type](ingredientDescriptor__variant_type.md) - Type of chemical variant
 * [➞mediaingredientmech_id](ingredientReference__mediaingredientmech_id.md) - MediaIngredientMech ID
 * [➞preferred_term](ingredientReference__preferred_term.md) - Name of parent ingredient
 * [➞aeration](mediaRecipe__aeration.md) - Gas exchange method (e.g., "0.5% CO2 in air", "bubbling", "shaking at 150 rpm")
 * [➞applications](mediaRecipe__applications.md) - Use cases and applications
 * [➞categories](mediaRecipe__categories.md) - All categories this recipe appears in (for cross-category merges)
 * [➞category](mediaRecipe__category.md) - Broad category for organization
 * [➞chemical_fingerprint](mediaRecipe__chemical_fingerprint.md) - SHA256 hash using parent ingredients (hierarchy-aware)
 * [➞culture_vessel](mediaRecipe__culture_vessel.md) - Recommended culture container (e.g., "Erlenmeyer flask", "test tube", "petri dish")
 * [➞curation_history](mediaRecipe__curation_history.md) - Audit trail of curation events
 * [➞data_quality_flags](mediaRecipe__data_quality_flags.md) - Data quality indicators for transparency
 * [➞datasets](mediaRecipe__datasets.md) - Omics datasets generated using this medium
 * [➞description](mediaRecipe__description.md) - Overview of the medium and its purpose
 * [➞evidence](mediaRecipe__evidence.md) - Evidence supporting formulation claims
 * [➞fingerprint_version](mediaRecipe__fingerprint_version.md) - Version of fingerprinting algorithm used
 * [➞high_metal](mediaRecipe__high_metal.md) - Indicates media with total metal concentration above the 90th percentile threshold (≥1049.84 mM). Metals include Fe, Cu, Zn, Mn, Co, Ni, Mo, Se, W, V, Cr, Ca, Mg, K, Na. Based on automated concentration analysis of ingredient composition.
 * [➞high_ree](mediaRecipe__high_ree.md) - Indicates media with total rare earth element (REE) concentration above the 90th percentile threshold (≥1030.48 mM). REEs include lanthanides (La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu) plus Sc and Y. Based on automated concentration analysis of ingredient composition.
 * [➞incubation_atmosphere](mediaRecipe__incubation_atmosphere.md) - Atmospheric conditions for incubation
 * [➞ingredients](mediaRecipe__ingredients.md) - Chemical and biological ingredients
 * [➞light_cycle](mediaRecipe__light_cycle.md) - Photoperiod light:dark cycle (e.g., "16:8", "continuous light", "24:0")
 * [➞light_intensity](mediaRecipe__light_intensity.md) - Light intensity for photosynthetic organisms (e.g., "50 µmol photons m⁻² s⁻¹")
 * [➞light_quality](mediaRecipe__light_quality.md) - Light spectrum or wavelength (e.g., "cool white fluorescent", "red LED 660nm")
 * [➞media_term](mediaRecipe__media_term.md) - Reference to authoritative media database
 * [➞medium_type](mediaRecipe__medium_type.md) - Classification of the medium
 * [➞merge_fingerprint](mediaRecipe__merge_fingerprint.md) - SHA256 hash of ingredient set for deduplication tracking
 * [➞merge_metadata](mediaRecipe__merge_metadata.md) - Metadata about merge process and quality
 * [➞merged_from](mediaRecipe__merged_from.md) - Original recipe IDs that were merged into this record
 * [➞name](mediaRecipe__name.md) - Human-readable medium name (e.g., "LB Broth", "M9 Minimal Medium")
 * [➞notes](mediaRecipe__notes.md) - Additional context, historical notes, tips
 * [➞organism_culture_type](mediaRecipe__organism_culture_type.md) - Whether this medium targets a pure isolate culture or a mixed microbial community
 * [➞original_name](mediaRecipe__original_name.md) - Original name from source database before filename sanitization. May contain special characters like /, :, %, (, ), ', ", <, >, &, #, etc. This field preserves the exact name as it appears in the source database.
 * [➞ph_range](mediaRecipe__ph_range.md) - Acceptable pH range (e.g., "6.8-7.2")
 * [➞ph_value](mediaRecipe__ph_value.md) - Target pH value
 * [➞physical_state](mediaRecipe__physical_state.md) - Physical form of the medium
 * [➞preparation_steps](mediaRecipe__preparation_steps.md) - Ordered steps to prepare the medium
 * [➞references](mediaRecipe__references.md) - Original literature sources
 * [➞salinity](mediaRecipe__salinity.md) - Salt concentration for marine/brackish media (e.g., "35 ppt", "3.5%")
 * [➞solutions](mediaRecipe__solutions.md) - Pre-prepared stock solutions used as ingredients
 * [➞source_data](mediaRecipe__source_data.md) - Provenance tracking for records imported from other repositories
 * [➞sterilization](mediaRecipe__sterilization.md) - Sterilization method and parameters
 * [➞storage](mediaRecipe__storage.md) - Storage conditions for prepared medium
 * [➞synonyms](mediaRecipe__synonyms.md) - Alternate names from merged duplicate recipes
 * [➞target_organisms](mediaRecipe__target_organisms.md) - Organisms for which this medium is designed
 * [➞temperature_range](mediaRecipe__temperature_range.md) - Optimal temperature range (e.g., "20-25°C", "room temperature")
 * [➞temperature_value](mediaRecipe__temperature_value.md) - Specific culture temperature in Celsius
 * [➞variant_fingerprint](mediaRecipe__variant_fingerprint.md) - SHA256 hash preserving variant distinctions
 * [➞variants](mediaRecipe__variants.md) - Related formulations or modifications
 * [➞preferred_term](mediaTypeDescriptor__preferred_term.md) - Medium designation in source database (e.g., "DSMZ Medium 1", "LB")
 * [➞term](mediaTypeDescriptor__term.md) - Authoritative media database identifier
 * [➞description](mediaVariant__description.md) - Purpose and context
 * [➞evidence](mediaVariant__evidence.md) - Evidence supporting the variant
 * [➞modifications](mediaVariant__modifications.md) - What differs from base recipe
 * [➞name](mediaVariant__name.md) - Variant name (e.g., "Low Salt LB", "LB + Ampicillin")
 * [➞purpose](mediaVariant__purpose.md) - Why this variant exists
 * [➞supplier_info](mediaVariant__supplier_info.md) - Commercial supplier if premix
 * [➞fingerprint_mode](mergeMetadata__fingerprint_mode.md) - Fingerprinting mode used (chemical/variant/original)
 * [➞hierarchy_conflicts](mergeMetadata__hierarchy_conflicts.md) - Ingredients with conflicting merge signals
 * [➞merge_confidence](mergeMetadata__merge_confidence.md) - Confidence score for merge decision (0.0-1.0)
 * [➞merge_mode](mergeMetadata__merge_mode.md) - Merge mode used (conservative/aggressive/variant-aware)
 * [➞merge_reason](mergeMetadata__merge_reason.md) - Why these recipes were merged together
 * [➞merge_version](mergeMetadata__merge_version.md) - Version of merge pipeline used
 * [➞cofactor_requirements](organismDescriptor__cofactor_requirements.md) - Cofactors required by this organism
 * [➞community_function](organismDescriptor__community_function.md) - Specific functional contribution to community
 * [➞community_role](organismDescriptor__community_role.md) - Functional role in microbial community
 * [➞evidence](organismDescriptor__evidence.md) - Evidence supporting growth on this medium
 * [➞growth_phase](organismDescriptor__growth_phase.md) - Target growth phase (e.g., "exponential", "stationary")
 * [➞gtdb_term](organismDescriptor__gtdb_term.md) - GTDB genome or lineage identifier (alternative to NCBITaxon)
 * [➞preferred_term](organismDescriptor__preferred_term.md) - Organism name (e.g., "Escherichia coli")
 * [➞strain](organismDescriptor__strain.md) - Specific strain designation (e.g., "K-12", "MG1655")
 * [➞target_abundance](organismDescriptor__target_abundance.md) - Target relative abundance in community (0.0-1.0)
 * [➞term](organismDescriptor__term.md) - NCBITaxon identifier
 * [➞transporters](organismDescriptor__transporters.md) - Annotated transport systems
 * [➞action](preparationStep__action.md) - Action type
 * [➞description](preparationStep__description.md) - Detailed instruction
 * [➞duration](preparationStep__duration.md) - Time duration (e.g., "15 minutes", "overnight")
 * [➞equipment](preparationStep__equipment.md) - Required equipment (e.g., "autoclave", "magnetic stirrer")
 * [➞notes](preparationStep__notes.md) - Additional tips or warnings
 * [➞step_number](preparationStep__step_number.md) - Sequential order
 * [➞temperature](preparationStep__temperature.md) - Temperature for this step
 * [➞authors](publicationReference__authors.md) - Author list
 * [➞notes](publicationReference__notes.md) - Additional context about the reference
 * [➞reference](publicationReference__reference.md) - Citation (PMID, DOI, or historical reference)
 * [➞title](publicationReference__title.md) - Publication title
 * [➞year](publicationReference__year.md) - Publication year
 * [➞name](recipeSynonym__name.md) - Alternate recipe name (non-canonical)
 * [➞original_category](recipeSynonym__original_category.md) - Original category assignment before merge
 * [➞source](recipeSynonym__source.md) - Source database (KOMODO, MediaDive, TOGO, etc.)
 * [➞source_id](recipeSynonym__source_id.md) - Original identifier in source database
 * [➞composition](solutionDescriptor__composition.md) - Ingredients in the stock solution
 * [➞concentration](solutionDescriptor__concentration.md) - Working concentration when added to medium
 * [➞mediaingredientmech_term](solutionDescriptor__mediaingredientmech_term.md) - MediaIngredientMech identifier for this solution component
 * [➞preferred_term](solutionDescriptor__preferred_term.md) - Solution name (e.g., "Trace Metal Solution", "Vitamin Stock")
 * [➞preparation_notes](solutionDescriptor__preparation_notes.md) - How to prepare the stock solution
 * [➞shelf_life](solutionDescriptor__shelf_life.md) - Stability duration (e.g., "6 months at 4°C")
 * [➞storage_conditions](solutionDescriptor__storage_conditions.md) - Storage requirements for the stock
 * [➞term](solutionDescriptor__term.md) - Ontology term if available
 * [➞community_ids](sourceData__community_ids.md) - List of CommunityMech IDs this recipe was derived from
 * [➞evidence](sourceData__evidence.md) - Evidence records from source repository
 * [➞import_date](sourceData__import_date.md) - Date of import (ISO 8601)
 * [➞notes](sourceData__notes.md) - Import notes and additional context
 * [➞origin](sourceData__origin.md) - Source repository name
 * [➞duration](sterilizationDescriptor__duration.md) - Sterilization duration
 * [➞method](sterilizationDescriptor__method.md) - Sterilization technique
 * [➞notes](sterilizationDescriptor__notes.md) - Special instructions (e.g., "Filter-sterilize heat-labile components separately")
 * [➞pressure](sterilizationDescriptor__pressure.md) - Pressure in psi or kPa (for autoclaving)
 * [➞temperature](sterilizationDescriptor__temperature.md) - Temperature setting
 * [➞container_type](storageConditions__container_type.md) - Recommended container (e.g., "glass bottle", "polypropylene tube")
 * [➞light_condition](storageConditions__light_condition.md) - Light exposure requirement
 * [➞notes](storageConditions__notes.md) - Additional storage tips
 * [➞shelf_life](storageConditions__shelf_life.md) - Duration of stability
 * [➞temperature](storageConditions__temperature.md) - Storage temperature
 * [➞catalog_number](supplierInfo__catalog_number.md) - Product catalog number
 * [➞notes](supplierInfo__notes.md) - Additional sourcing notes
 * [➞product_url](supplierInfo__product_url.md) - Direct product link
 * [➞supplier_name](supplierInfo__supplier_name.md) - Vendor name (e.g., "Sigma-Aldrich", "Thermo Fisher")
 * [➞unit](temperatureValue__unit.md) - Temperature unit
 * [➞value](temperatureValue__value.md) - Numeric temperature value
 * [➞id](term__id.md) - Ontology identifier (CURIE)
     * [ChemicalEntityTerm➞id](ChemicalEntityTerm_id.md)
     * [MediaIngredientMechTerm➞id](MediaIngredientMechTerm_id.md)
     * [OrganismTerm➞id](OrganismTerm_id.md)
 * [➞label](term__label.md) - Ontology term label
 * [➞direction](transporterAnnotation__direction.md) - Transport direction (import, export, bidirectional)
 * [➞ec_number](transporterAnnotation__ec_number.md) - EC number if enzymatic
 * [➞genes](transporterAnnotation__genes.md) - Gene names or locus tags
 * [➞name](transporterAnnotation__name.md) - Transporter name or gene name
 * [➞notes](transporterAnnotation__notes.md) - Additional functional notes
 * [➞substrate_terms](transporterAnnotation__substrate_terms.md) - CHEBI terms for substrates
 * [➞substrates](transporterAnnotation__substrates.md) - Transported substrates
 * [➞transporter_type](transporterAnnotation__transporter_type.md) - Classification of transporter

### Enums

 * [AtmosphereEnum](AtmosphereEnum.md) - Atmospheric conditions for incubation
 * [CategoryEnum](CategoryEnum.md) - Organizational category for media recipes
 * [CellularRoleEnum](CellularRoleEnum.md) - Functional role of organism in microbial community
 * [CofactorCategoryEnum](CofactorCategoryEnum.md) - High-level classification of cofactor types
 * [ConcentrationUnitEnum](ConcentrationUnitEnum.md) - Units for concentration
 * [EvidenceItemSupportEnum](EvidenceItemSupportEnum.md) - Level of evidence support
 * [IngredientRoleEnum](IngredientRoleEnum.md) - Functional role of an ingredient in growth medium
 * [LightConditionEnum](LightConditionEnum.md) - Light exposure requirements
 * [MediumTypeEnum](MediumTypeEnum.md) - Classification of culture medium
 * [MergeReasonEnum](MergeReasonEnum.md) - Reason why recipes were merged together
 * [ModifierEnum](ModifierEnum.md) - Modification type for variants
 * [OrganismCultureTypeEnum](OrganismCultureTypeEnum.md) - Whether the medium targets a pure isolate or a mixed microbial community
 * [PhysicalStateEnum](PhysicalStateEnum.md) - Physical form of the medium
 * [PreparationActionEnum](PreparationActionEnum.md) - Controlled vocabulary for preparation steps
 * [SterilizationMethodEnum](SterilizationMethodEnum.md) - Sterilization techniques
 * [TemperatureUnitEnum](TemperatureUnitEnum.md) - Units for temperature
 * [TransporterTypeEnum](TransporterTypeEnum.md) - Classification of membrane transporter systems
 * [VariantTypeEnum](VariantTypeEnum.md) - Type of chemical variant relationship to parent

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE

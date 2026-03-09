ERROR:linkml.utils.generator:slot_usage for undefined slot: id
ERROR:linkml.utils.generator:slot_usage for undefined slot: id
WARNING:linkml.utils.generator:Unrecognized prefix: mediadive.medium
WARNING:linkml.utils.generator:Unrecognized prefix: komodo.medium
# Auto generated from culturemech.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-08T23:47:25
# Schema: culturemech
#
# id: https://w3id.org/culturemech
# description: LinkML schema for modeling microbial culture media recipes and formulations.
#   Follows the dismech architecture pattern with descriptor classes for ontology grounding.
#
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI

metamodel_version = "1.7.0"
version = None

# Namespaces
ATCC = CurieNamespace('ATCC', 'https://www.atcc.org/products/')
CCAP = CurieNamespace('CCAP', 'https://www.ccap.ac.uk/catalogue/strain-')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
DOI = CurieNamespace('DOI', 'https://doi.org/')
DSMZ = CurieNamespace('DSMZ', 'https://mediadive.dsmz.de/medium/')
EC = CurieNamespace('EC', 'https://enzyme.expasy.org/EC/')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
GTDB = CurieNamespace('GTDB', 'https://gtdb.ecogenomic.org/genome?gid=')
KEGG = CurieNamespace('KEGG', 'https://www.genome.jp/entry/')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
SAG = CurieNamespace('SAG', 'https://sagdb.uni-goettingen.de/detailedList.php?str_number=')
TOGO = CurieNamespace('TOGO', 'http://togodb.org/db/medium/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
UTEX = CurieNamespace('UTEX', 'https://utex.org/products/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
CULTUREMECH = CurieNamespace('culturemech', 'https://w3id.org/culturemech/')
GEO = CurieNamespace('geo', 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=')
KOMODO_MEDIUM = CurieNamespace('komodo_medium', 'http://example.org/UNKNOWN/komodo.medium/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MEDIADIVE_MEDIUM = CurieNamespace('mediadive_medium', 'http://example.org/UNKNOWN/mediadive.medium/')
SIGMA = CurieNamespace('sigma', 'https://www.sigmaaldrich.com/catalog/product/')
SRA = CurieNamespace('sra', 'https://www.ncbi.nlm.nih.gov/sra/')
THERMOFISHER = CurieNamespace('thermofisher', 'https://www.thermofisher.com/order/catalog/product/')
DEFAULT_ = CULTUREMECH


# Types

# Class references
class MediaRecipeName(extended_str):
    pass


class TermId(extended_str):
    pass


class ChemicalEntityTermId(TermId):
    pass


class OrganismTermId(TermId):
    pass


class GTDBTermId(TermId):
    pass


class MediaDatabaseTermId(TermId):
    pass


@dataclass(repr=False)
class MediaRecipe(YAMLRoot):
    """
    A complete growth medium formulation for culturing microorganisms. This is the root entity - one per YAML file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["MediaRecipe"]
    class_class_curie: ClassVar[str] = "culturemech:MediaRecipe"
    class_name: ClassVar[str] = "MediaRecipe"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.MediaRecipe

    name: Union[str, MediaRecipeName] = None
    medium_type: Union[str, "MediumTypeEnum"] = None
    physical_state: Union[str, "PhysicalStateEnum"] = None
    ingredients: Union[Union[dict, "IngredientDescriptor"], list[Union[dict, "IngredientDescriptor"]]] = None
    original_name: Optional[str] = None
    category: Optional[Union[str, "CategoryEnum"]] = None
    categories: Optional[Union[Union[str, "CategoryEnum"], list[Union[str, "CategoryEnum"]]]] = empty_list()
    high_metal: Optional[Union[bool, Bool]] = None
    high_ree: Optional[Union[bool, Bool]] = None
    synonyms: Optional[Union[Union[dict, "RecipeSynonym"], list[Union[dict, "RecipeSynonym"]]]] = empty_list()
    merged_from: Optional[Union[str, list[str]]] = empty_list()
    merge_fingerprint: Optional[str] = None
    media_term: Optional[Union[dict, "MediaTypeDescriptor"]] = None
    description: Optional[str] = None
    target_organisms: Optional[Union[Union[dict, "OrganismDescriptor"], list[Union[dict, "OrganismDescriptor"]]]] = empty_list()
    organism_culture_type: Optional[Union[str, "OrganismCultureTypeEnum"]] = None
    ph_value: Optional[float] = None
    ph_range: Optional[str] = None
    light_intensity: Optional[str] = None
    light_cycle: Optional[str] = None
    light_quality: Optional[str] = None
    temperature_range: Optional[str] = None
    temperature_value: Optional[float] = None
    salinity: Optional[str] = None
    aeration: Optional[str] = None
    culture_vessel: Optional[str] = None
    solutions: Optional[Union[Union[dict, "SolutionDescriptor"], list[Union[dict, "SolutionDescriptor"]]]] = empty_list()
    preparation_steps: Optional[Union[Union[dict, "PreparationStep"], list[Union[dict, "PreparationStep"]]]] = empty_list()
    sterilization: Optional[Union[dict, "SterilizationDescriptor"]] = None
    storage: Optional[Union[dict, "StorageConditions"]] = None
    applications: Optional[Union[str, list[str]]] = empty_list()
    variants: Optional[Union[Union[dict, "MediaVariant"], list[Union[dict, "MediaVariant"]]]] = empty_list()
    references: Optional[Union[Union[dict, "PublicationReference"], list[Union[dict, "PublicationReference"]]]] = empty_list()
    notes: Optional[str] = None
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()
    datasets: Optional[Union[Union[dict, "Dataset"], list[Union[dict, "Dataset"]]]] = empty_list()
    curation_history: Optional[Union[Union[dict, "CurationEvent"], list[Union[dict, "CurationEvent"]]]] = empty_list()
    data_quality_flags: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, MediaRecipeName):
            self.name = MediaRecipeName(self.name)

        if self._is_empty(self.medium_type):
            self.MissingRequiredField("medium_type")
        if not isinstance(self.medium_type, MediumTypeEnum):
            self.medium_type = MediumTypeEnum(self.medium_type)

        if self._is_empty(self.physical_state):
            self.MissingRequiredField("physical_state")
        if not isinstance(self.physical_state, PhysicalStateEnum):
            self.physical_state = PhysicalStateEnum(self.physical_state)

        if self._is_empty(self.ingredients):
            self.MissingRequiredField("ingredients")
        if not isinstance(self.ingredients, list):
            self.ingredients = [self.ingredients] if self.ingredients is not None else []
        self.ingredients = [v if isinstance(v, IngredientDescriptor) else IngredientDescriptor(**as_dict(v)) for v in self.ingredients]

        if self.original_name is not None and not isinstance(self.original_name, str):
            self.original_name = str(self.original_name)

        if self.category is not None and not isinstance(self.category, CategoryEnum):
            self.category = CategoryEnum(self.category)

        if not isinstance(self.categories, list):
            self.categories = [self.categories] if self.categories is not None else []
        self.categories = [v if isinstance(v, CategoryEnum) else CategoryEnum(v) for v in self.categories]

        if self.high_metal is not None and not isinstance(self.high_metal, Bool):
            self.high_metal = Bool(self.high_metal)

        if self.high_ree is not None and not isinstance(self.high_ree, Bool):
            self.high_ree = Bool(self.high_ree)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, RecipeSynonym) else RecipeSynonym(**as_dict(v)) for v in self.synonyms]

        if not isinstance(self.merged_from, list):
            self.merged_from = [self.merged_from] if self.merged_from is not None else []
        self.merged_from = [v if isinstance(v, str) else str(v) for v in self.merged_from]

        if self.merge_fingerprint is not None and not isinstance(self.merge_fingerprint, str):
            self.merge_fingerprint = str(self.merge_fingerprint)

        if self.media_term is not None and not isinstance(self.media_term, MediaTypeDescriptor):
            self.media_term = MediaTypeDescriptor(**as_dict(self.media_term))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_dict(slot_name="target_organisms", slot_type=OrganismDescriptor, key_name="preferred_term", keyed=False)

        if self.organism_culture_type is not None and not isinstance(self.organism_culture_type, OrganismCultureTypeEnum):
            self.organism_culture_type = OrganismCultureTypeEnum(self.organism_culture_type)

        if self.ph_value is not None and not isinstance(self.ph_value, float):
            self.ph_value = float(self.ph_value)

        if self.ph_range is not None and not isinstance(self.ph_range, str):
            self.ph_range = str(self.ph_range)

        if self.light_intensity is not None and not isinstance(self.light_intensity, str):
            self.light_intensity = str(self.light_intensity)

        if self.light_cycle is not None and not isinstance(self.light_cycle, str):
            self.light_cycle = str(self.light_cycle)

        if self.light_quality is not None and not isinstance(self.light_quality, str):
            self.light_quality = str(self.light_quality)

        if self.temperature_range is not None and not isinstance(self.temperature_range, str):
            self.temperature_range = str(self.temperature_range)

        if self.temperature_value is not None and not isinstance(self.temperature_value, float):
            self.temperature_value = float(self.temperature_value)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.aeration is not None and not isinstance(self.aeration, str):
            self.aeration = str(self.aeration)

        if self.culture_vessel is not None and not isinstance(self.culture_vessel, str):
            self.culture_vessel = str(self.culture_vessel)

        if not isinstance(self.solutions, list):
            self.solutions = [self.solutions] if self.solutions is not None else []
        self.solutions = [v if isinstance(v, SolutionDescriptor) else SolutionDescriptor(**as_dict(v)) for v in self.solutions]

        if not isinstance(self.preparation_steps, list):
            self.preparation_steps = [self.preparation_steps] if self.preparation_steps is not None else []
        self.preparation_steps = [v if isinstance(v, PreparationStep) else PreparationStep(**as_dict(v)) for v in self.preparation_steps]

        if self.sterilization is not None and not isinstance(self.sterilization, SterilizationDescriptor):
            self.sterilization = SterilizationDescriptor(**as_dict(self.sterilization))

        if self.storage is not None and not isinstance(self.storage, StorageConditions):
            self.storage = StorageConditions(**as_dict(self.storage))

        if not isinstance(self.applications, list):
            self.applications = [self.applications] if self.applications is not None else []
        self.applications = [v if isinstance(v, str) else str(v) for v in self.applications]

        if not isinstance(self.variants, list):
            self.variants = [self.variants] if self.variants is not None else []
        self.variants = [v if isinstance(v, MediaVariant) else MediaVariant(**as_dict(v)) for v in self.variants]

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, PublicationReference) else PublicationReference(**as_dict(v)) for v in self.references]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if not isinstance(self.datasets, list):
            self.datasets = [self.datasets] if self.datasets is not None else []
        self.datasets = [v if isinstance(v, Dataset) else Dataset(**as_dict(v)) for v in self.datasets]

        if not isinstance(self.curation_history, list):
            self.curation_history = [self.curation_history] if self.curation_history is not None else []
        self.curation_history = [v if isinstance(v, CurationEvent) else CurationEvent(**as_dict(v)) for v in self.curation_history]

        if not isinstance(self.data_quality_flags, list):
            self.data_quality_flags = [self.data_quality_flags] if self.data_quality_flags is not None else []
        self.data_quality_flags = [v if isinstance(v, str) else str(v) for v in self.data_quality_flags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecipeSynonym(YAMLRoot):
    """
    An alternate name for a recipe from a specific source
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["RecipeSynonym"]
    class_class_curie: ClassVar[str] = "culturemech:RecipeSynonym"
    class_name: ClassVar[str] = "RecipeSynonym"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.RecipeSynonym

    name: str = None
    source: str = None
    source_id: Optional[str] = None
    original_category: Optional[Union[str, "CategoryEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self.source_id is not None and not isinstance(self.source_id, str):
            self.source_id = str(self.source_id)

        if self.original_category is not None and not isinstance(self.original_category, CategoryEnum):
            self.original_category = CategoryEnum(self.original_category)

        super().__post_init__(**kwargs)


class Descriptor(YAMLRoot):
    """
    Base class for descriptor pattern. Descriptors have a human-readable preferred_term and optional ontology term.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["Descriptor"]
    class_class_curie: ClassVar[str] = "culturemech:Descriptor"
    class_name: ClassVar[str] = "Descriptor"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.Descriptor


@dataclass(repr=False)
class Term(YAMLRoot):
    """
    Base class for ontology term references. Subclasses specify id_prefixes for validation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["Term"]
    class_class_curie: ClassVar[str] = "culturemech:Term"
    class_name: ClassVar[str] = "Term"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.Term

    id: Union[str, TermId] = None
    label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TermId):
            self.id = TermId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MediaTypeDescriptor(Descriptor):
    """
    Classification and authoritative database reference for the medium
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["MediaTypeDescriptor"]
    class_class_curie: ClassVar[str] = "culturemech:MediaTypeDescriptor"
    class_name: ClassVar[str] = "MediaTypeDescriptor"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.MediaTypeDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, "MediaDatabaseTerm"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self.term is not None and not isinstance(self.term, MediaDatabaseTerm):
            self.term = MediaDatabaseTerm(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IngredientDescriptor(Descriptor):
    """
    Chemical or biological ingredient in a medium
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["IngredientDescriptor"]
    class_class_curie: ClassVar[str] = "culturemech:IngredientDescriptor"
    class_name: ClassVar[str] = "IngredientDescriptor"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.IngredientDescriptor

    preferred_term: str = None
    concentration: Union[dict, "ConcentrationValue"] = None
    term: Optional[Union[dict, "ChemicalEntityTerm"]] = None
    modifier: Optional[Union[str, "ModifierEnum"]] = None
    chemical_formula: Optional[str] = None
    molecular_weight: Optional[float] = None
    supplier_catalog: Optional[Union[dict, "SupplierInfo"]] = None
    notes: Optional[str] = None
    role: Optional[Union[Union[str, "IngredientRoleEnum"], list[Union[str, "IngredientRoleEnum"]]]] = empty_list()
    cofactors_provided: Optional[Union[Union[dict, "CofactorDescriptor"], list[Union[dict, "CofactorDescriptor"]]]] = empty_list()
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self._is_empty(self.concentration):
            self.MissingRequiredField("concentration")
        if not isinstance(self.concentration, ConcentrationValue):
            self.concentration = ConcentrationValue(**as_dict(self.concentration))

        if self.term is not None and not isinstance(self.term, ChemicalEntityTerm):
            self.term = ChemicalEntityTerm(**as_dict(self.term))

        if self.modifier is not None and not isinstance(self.modifier, ModifierEnum):
            self.modifier = ModifierEnum(self.modifier)

        if self.chemical_formula is not None and not isinstance(self.chemical_formula, str):
            self.chemical_formula = str(self.chemical_formula)

        if self.molecular_weight is not None and not isinstance(self.molecular_weight, float):
            self.molecular_weight = float(self.molecular_weight)

        if self.supplier_catalog is not None and not isinstance(self.supplier_catalog, SupplierInfo):
            self.supplier_catalog = SupplierInfo(**as_dict(self.supplier_catalog))

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.role, list):
            self.role = [self.role] if self.role is not None else []
        self.role = [v if isinstance(v, IngredientRoleEnum) else IngredientRoleEnum(v) for v in self.role]

        if not isinstance(self.cofactors_provided, list):
            self.cofactors_provided = [self.cofactors_provided] if self.cofactors_provided is not None else []
        self.cofactors_provided = [v if isinstance(v, CofactorDescriptor) else CofactorDescriptor(**as_dict(v)) for v in self.cofactors_provided]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SolutionDescriptor(Descriptor):
    """
    A pre-prepared stock solution used as an ingredient
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["SolutionDescriptor"]
    class_class_curie: ClassVar[str] = "culturemech:SolutionDescriptor"
    class_name: ClassVar[str] = "SolutionDescriptor"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.SolutionDescriptor

    preferred_term: str = None
    composition: Union[Union[dict, IngredientDescriptor], list[Union[dict, IngredientDescriptor]]] = None
    term: Optional[Union[dict, Term]] = None
    concentration: Optional[Union[dict, "ConcentrationValue"]] = None
    preparation_notes: Optional[str] = None
    storage_conditions: Optional[Union[dict, "StorageConditions"]] = None
    shelf_life: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self._is_empty(self.composition):
            self.MissingRequiredField("composition")
        if not isinstance(self.composition, list):
            self.composition = [self.composition] if self.composition is not None else []
        self.composition = [v if isinstance(v, IngredientDescriptor) else IngredientDescriptor(**as_dict(v)) for v in self.composition]

        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        if self.concentration is not None and not isinstance(self.concentration, ConcentrationValue):
            self.concentration = ConcentrationValue(**as_dict(self.concentration))

        if self.preparation_notes is not None and not isinstance(self.preparation_notes, str):
            self.preparation_notes = str(self.preparation_notes)

        if self.storage_conditions is not None and not isinstance(self.storage_conditions, StorageConditions):
            self.storage_conditions = StorageConditions(**as_dict(self.storage_conditions))

        if self.shelf_life is not None and not isinstance(self.shelf_life, str):
            self.shelf_life = str(self.shelf_life)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrganismDescriptor(Descriptor):
    """
    Target organism for the medium
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["OrganismDescriptor"]
    class_class_curie: ClassVar[str] = "culturemech:OrganismDescriptor"
    class_name: ClassVar[str] = "OrganismDescriptor"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.OrganismDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, "OrganismTerm"]] = None
    gtdb_term: Optional[Union[dict, "GTDBTerm"]] = None
    strain: Optional[str] = None
    growth_phase: Optional[str] = None
    community_role: Optional[Union[Union[str, "CellularRoleEnum"], list[Union[str, "CellularRoleEnum"]]]] = empty_list()
    target_abundance: Optional[float] = None
    community_function: Optional[Union[str, list[str]]] = empty_list()
    cofactor_requirements: Optional[Union[Union[dict, "CofactorRequirement"], list[Union[dict, "CofactorRequirement"]]]] = empty_list()
    transporters: Optional[Union[Union[dict, "TransporterAnnotation"], list[Union[dict, "TransporterAnnotation"]]]] = empty_list()
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self.term is not None and not isinstance(self.term, OrganismTerm):
            self.term = OrganismTerm(**as_dict(self.term))

        if self.gtdb_term is not None and not isinstance(self.gtdb_term, GTDBTerm):
            self.gtdb_term = GTDBTerm(**as_dict(self.gtdb_term))

        if self.strain is not None and not isinstance(self.strain, str):
            self.strain = str(self.strain)

        if self.growth_phase is not None and not isinstance(self.growth_phase, str):
            self.growth_phase = str(self.growth_phase)

        if not isinstance(self.community_role, list):
            self.community_role = [self.community_role] if self.community_role is not None else []
        self.community_role = [v if isinstance(v, CellularRoleEnum) else CellularRoleEnum(v) for v in self.community_role]

        if self.target_abundance is not None and not isinstance(self.target_abundance, float):
            self.target_abundance = float(self.target_abundance)

        if not isinstance(self.community_function, list):
            self.community_function = [self.community_function] if self.community_function is not None else []
        self.community_function = [v if isinstance(v, str) else str(v) for v in self.community_function]

        if not isinstance(self.cofactor_requirements, list):
            self.cofactor_requirements = [self.cofactor_requirements] if self.cofactor_requirements is not None else []
        self.cofactor_requirements = [v if isinstance(v, CofactorRequirement) else CofactorRequirement(**as_dict(v)) for v in self.cofactor_requirements]

        if not isinstance(self.transporters, list):
            self.transporters = [self.transporters] if self.transporters is not None else []
        self.transporters = [v if isinstance(v, TransporterAnnotation) else TransporterAnnotation(**as_dict(v)) for v in self.transporters]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CofactorDescriptor(Descriptor):
    """
    A cofactor or coenzyme required for enzymatic activity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["CofactorDescriptor"]
    class_class_curie: ClassVar[str] = "culturemech:CofactorDescriptor"
    class_name: ClassVar[str] = "CofactorDescriptor"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.CofactorDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, "ChemicalEntityTerm"]] = None
    category: Optional[Union[str, "CofactorCategoryEnum"]] = None
    precursor: Optional[str] = None
    precursor_term: Optional[Union[dict, "ChemicalEntityTerm"]] = None
    ec_associations: Optional[Union[str, list[str]]] = empty_list()
    kegg_pathways: Optional[Union[str, list[str]]] = empty_list()
    enzyme_examples: Optional[Union[str, list[str]]] = empty_list()
    biosynthesis_genes: Optional[Union[str, list[str]]] = empty_list()
    bioavailability: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self.term is not None and not isinstance(self.term, ChemicalEntityTerm):
            self.term = ChemicalEntityTerm(**as_dict(self.term))

        if self.category is not None and not isinstance(self.category, CofactorCategoryEnum):
            self.category = CofactorCategoryEnum(self.category)

        if self.precursor is not None and not isinstance(self.precursor, str):
            self.precursor = str(self.precursor)

        if self.precursor_term is not None and not isinstance(self.precursor_term, ChemicalEntityTerm):
            self.precursor_term = ChemicalEntityTerm(**as_dict(self.precursor_term))

        if not isinstance(self.ec_associations, list):
            self.ec_associations = [self.ec_associations] if self.ec_associations is not None else []
        self.ec_associations = [v if isinstance(v, str) else str(v) for v in self.ec_associations]

        if not isinstance(self.kegg_pathways, list):
            self.kegg_pathways = [self.kegg_pathways] if self.kegg_pathways is not None else []
        self.kegg_pathways = [v if isinstance(v, str) else str(v) for v in self.kegg_pathways]

        if not isinstance(self.enzyme_examples, list):
            self.enzyme_examples = [self.enzyme_examples] if self.enzyme_examples is not None else []
        self.enzyme_examples = [v if isinstance(v, str) else str(v) for v in self.enzyme_examples]

        if not isinstance(self.biosynthesis_genes, list):
            self.biosynthesis_genes = [self.biosynthesis_genes] if self.biosynthesis_genes is not None else []
        self.biosynthesis_genes = [v if isinstance(v, str) else str(v) for v in self.biosynthesis_genes]

        if self.bioavailability is not None and not isinstance(self.bioavailability, str):
            self.bioavailability = str(self.bioavailability)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConcentrationValue(YAMLRoot):
    """
    Quantified concentration with units
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["ConcentrationValue"]
    class_class_curie: ClassVar[str] = "culturemech:ConcentrationValue"
    class_name: ClassVar[str] = "ConcentrationValue"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.ConcentrationValue

    value: str = None
    unit: Union[str, "ConcentrationUnitEnum"] = None
    per_volume: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, ConcentrationUnitEnum):
            self.unit = ConcentrationUnitEnum(self.unit)

        if self.per_volume is not None and not isinstance(self.per_volume, str):
            self.per_volume = str(self.per_volume)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TemperatureValue(YAMLRoot):
    """
    Temperature with units
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["TemperatureValue"]
    class_class_curie: ClassVar[str] = "culturemech:TemperatureValue"
    class_name: ClassVar[str] = "TemperatureValue"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.TemperatureValue

    value: float = None
    unit: Union[str, "TemperatureUnitEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, TemperatureUnitEnum):
            self.unit = TemperatureUnitEnum(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PreparationStep(YAMLRoot):
    """
    A step in medium preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["PreparationStep"]
    class_class_curie: ClassVar[str] = "culturemech:PreparationStep"
    class_name: ClassVar[str] = "PreparationStep"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.PreparationStep

    step_number: int = None
    action: Union[str, "PreparationActionEnum"] = None
    description: str = None
    temperature: Optional[Union[dict, TemperatureValue]] = None
    duration: Optional[str] = None
    equipment: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.step_number):
            self.MissingRequiredField("step_number")
        if not isinstance(self.step_number, int):
            self.step_number = int(self.step_number)

        if self._is_empty(self.action):
            self.MissingRequiredField("action")
        if not isinstance(self.action, PreparationActionEnum):
            self.action = PreparationActionEnum(self.action)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.temperature is not None and not isinstance(self.temperature, TemperatureValue):
            self.temperature = TemperatureValue(**as_dict(self.temperature))

        if self.duration is not None and not isinstance(self.duration, str):
            self.duration = str(self.duration)

        if self.equipment is not None and not isinstance(self.equipment, str):
            self.equipment = str(self.equipment)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SterilizationDescriptor(YAMLRoot):
    """
    Sterilization method and parameters
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["SterilizationDescriptor"]
    class_class_curie: ClassVar[str] = "culturemech:SterilizationDescriptor"
    class_name: ClassVar[str] = "SterilizationDescriptor"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.SterilizationDescriptor

    method: Union[str, "SterilizationMethodEnum"] = None
    temperature: Optional[Union[dict, TemperatureValue]] = None
    pressure: Optional[float] = None
    duration: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, SterilizationMethodEnum):
            self.method = SterilizationMethodEnum(self.method)

        if self.temperature is not None and not isinstance(self.temperature, TemperatureValue):
            self.temperature = TemperatureValue(**as_dict(self.temperature))

        if self.pressure is not None and not isinstance(self.pressure, float):
            self.pressure = float(self.pressure)

        if self.duration is not None and not isinstance(self.duration, str):
            self.duration = str(self.duration)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StorageConditions(YAMLRoot):
    """
    Storage requirements for prepared medium
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["StorageConditions"]
    class_class_curie: ClassVar[str] = "culturemech:StorageConditions"
    class_name: ClassVar[str] = "StorageConditions"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.StorageConditions

    temperature: Union[dict, TemperatureValue] = None
    light_condition: Optional[Union[str, "LightConditionEnum"]] = None
    shelf_life: Optional[str] = None
    container_type: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.temperature):
            self.MissingRequiredField("temperature")
        if not isinstance(self.temperature, TemperatureValue):
            self.temperature = TemperatureValue(**as_dict(self.temperature))

        if self.light_condition is not None and not isinstance(self.light_condition, LightConditionEnum):
            self.light_condition = LightConditionEnum(self.light_condition)

        if self.shelf_life is not None and not isinstance(self.shelf_life, str):
            self.shelf_life = str(self.shelf_life)

        if self.container_type is not None and not isinstance(self.container_type, str):
            self.container_type = str(self.container_type)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MediaVariant(YAMLRoot):
    """
    A variant or modification of the base recipe
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["MediaVariant"]
    class_class_curie: ClassVar[str] = "culturemech:MediaVariant"
    class_name: ClassVar[str] = "MediaVariant"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.MediaVariant

    name: str = None
    description: Optional[str] = None
    modifications: Optional[Union[str, list[str]]] = empty_list()
    purpose: Optional[str] = None
    supplier_info: Optional[Union[dict, "SupplierInfo"]] = None
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.modifications, list):
            self.modifications = [self.modifications] if self.modifications is not None else []
        self.modifications = [v if isinstance(v, str) else str(v) for v in self.modifications]

        if self.purpose is not None and not isinstance(self.purpose, str):
            self.purpose = str(self.purpose)

        if self.supplier_info is not None and not isinstance(self.supplier_info, SupplierInfo):
            self.supplier_info = SupplierInfo(**as_dict(self.supplier_info))

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupplierInfo(YAMLRoot):
    """
    Commercial supplier information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["SupplierInfo"]
    class_class_curie: ClassVar[str] = "culturemech:SupplierInfo"
    class_name: ClassVar[str] = "SupplierInfo"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.SupplierInfo

    supplier_name: str = None
    catalog_number: Optional[str] = None
    product_url: Optional[Union[str, URI]] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.supplier_name):
            self.MissingRequiredField("supplier_name")
        if not isinstance(self.supplier_name, str):
            self.supplier_name = str(self.supplier_name)

        if self.catalog_number is not None and not isinstance(self.catalog_number, str):
            self.catalog_number = str(self.catalog_number)

        if self.product_url is not None and not isinstance(self.product_url, URI):
            self.product_url = URI(self.product_url)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicationReference(YAMLRoot):
    """
    Literature reference
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["PublicationReference"]
    class_class_curie: ClassVar[str] = "culturemech:PublicationReference"
    class_name: ClassVar[str] = "PublicationReference"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.PublicationReference

    reference: str = None
    title: Optional[str] = None
    authors: Optional[str] = None
    year: Optional[int] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.authors is not None and not isinstance(self.authors, str):
            self.authors = str(self.authors)

        if self.year is not None and not isinstance(self.year, int):
            self.year = int(self.year)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceItem(YAMLRoot):
    """
    Evidence supporting a claim about media formulation or performance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["EvidenceItem"]
    class_class_curie: ClassVar[str] = "culturemech:EvidenceItem"
    class_name: ClassVar[str] = "EvidenceItem"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.EvidenceItem

    reference: str = None
    supports: Union[str, "EvidenceItemSupportEnum"] = None
    explanation: str = None
    snippet: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self._is_empty(self.supports):
            self.MissingRequiredField("supports")
        if not isinstance(self.supports, EvidenceItemSupportEnum):
            self.supports = EvidenceItemSupportEnum(self.supports)

        if self._is_empty(self.explanation):
            self.MissingRequiredField("explanation")
        if not isinstance(self.explanation, str):
            self.explanation = str(self.explanation)

        if self.snippet is not None and not isinstance(self.snippet, str):
            self.snippet = str(self.snippet)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    Omics dataset generated using this medium
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["Dataset"]
    class_class_curie: ClassVar[str] = "culturemech:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.Dataset

    dataset_id: str = None
    dataset_type: Optional[str] = None
    description: Optional[str] = None
    url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.dataset_id):
            self.MissingRequiredField("dataset_id")
        if not isinstance(self.dataset_id, str):
            self.dataset_id = str(self.dataset_id)

        if self.dataset_type is not None and not isinstance(self.dataset_type, str):
            self.dataset_type = str(self.dataset_type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CurationEvent(YAMLRoot):
    """
    Audit trail entry for curation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["CurationEvent"]
    class_class_curie: ClassVar[str] = "culturemech:CurationEvent"
    class_name: ClassVar[str] = "CurationEvent"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.CurationEvent

    timestamp: str = None
    curator: str = None
    action: str = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.timestamp):
            self.MissingRequiredField("timestamp")
        if not isinstance(self.timestamp, str):
            self.timestamp = str(self.timestamp)

        if self._is_empty(self.curator):
            self.MissingRequiredField("curator")
        if not isinstance(self.curator, str):
            self.curator = str(self.curator)

        if self._is_empty(self.action):
            self.MissingRequiredField("action")
        if not isinstance(self.action, str):
            self.action = str(self.action)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CofactorRequirement(YAMLRoot):
    """
    Cofactor requirement for an organism
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["CofactorRequirement"]
    class_class_curie: ClassVar[str] = "culturemech:CofactorRequirement"
    class_name: ClassVar[str] = "CofactorRequirement"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.CofactorRequirement

    cofactor: Union[dict, CofactorDescriptor] = None
    can_biosynthesize: Union[bool, Bool] = None
    confidence: Optional[float] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    genes: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cofactor):
            self.MissingRequiredField("cofactor")
        if not isinstance(self.cofactor, CofactorDescriptor):
            self.cofactor = CofactorDescriptor(**as_dict(self.cofactor))

        if self._is_empty(self.can_biosynthesize):
            self.MissingRequiredField("can_biosynthesize")
        if not isinstance(self.can_biosynthesize, Bool):
            self.can_biosynthesize = Bool(self.can_biosynthesize)

        if self.confidence is not None and not isinstance(self.confidence, float):
            self.confidence = float(self.confidence)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, str) else str(v) for v in self.genes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TransporterAnnotation(YAMLRoot):
    """
    Annotation of a transporter or transport system
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["TransporterAnnotation"]
    class_class_curie: ClassVar[str] = "culturemech:TransporterAnnotation"
    class_name: ClassVar[str] = "TransporterAnnotation"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.TransporterAnnotation

    name: str = None
    transporter_type: Union[str, "TransporterTypeEnum"] = None
    substrates: Optional[Union[str, list[str]]] = empty_list()
    substrate_terms: Optional[Union[dict[Union[str, ChemicalEntityTermId], Union[dict, "ChemicalEntityTerm"]], list[Union[dict, "ChemicalEntityTerm"]]]] = empty_dict()
    direction: Optional[str] = None
    genes: Optional[Union[str, list[str]]] = empty_list()
    ec_number: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.transporter_type):
            self.MissingRequiredField("transporter_type")
        if not isinstance(self.transporter_type, TransporterTypeEnum):
            self.transporter_type = TransporterTypeEnum(self.transporter_type)

        if not isinstance(self.substrates, list):
            self.substrates = [self.substrates] if self.substrates is not None else []
        self.substrates = [v if isinstance(v, str) else str(v) for v in self.substrates]

        self._normalize_inlined_as_list(slot_name="substrate_terms", slot_type=ChemicalEntityTerm, key_name="id", keyed=True)

        if self.direction is not None and not isinstance(self.direction, str):
            self.direction = str(self.direction)

        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, str) else str(v) for v in self.genes]

        if self.ec_number is not None and not isinstance(self.ec_number, str):
            self.ec_number = str(self.ec_number)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntityTerm(Term):
    """
    A CHEBI term representing a chemical entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["ChemicalEntityTerm"]
    class_class_curie: ClassVar[str] = "culturemech:ChemicalEntityTerm"
    class_name: ClassVar[str] = "ChemicalEntityTerm"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.ChemicalEntityTerm

    id: Union[str, ChemicalEntityTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityTermId):
            self.id = ChemicalEntityTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrganismTerm(Term):
    """
    An NCBITaxon term representing an organism
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["OrganismTerm"]
    class_class_curie: ClassVar[str] = "culturemech:OrganismTerm"
    class_name: ClassVar[str] = "OrganismTerm"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.OrganismTerm

    id: Union[str, OrganismTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismTermId):
            self.id = OrganismTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GTDBTerm(Term):
    """
    A GTDB genome identifier. id = GTDB accession (e.g. GTDB:RS_GCF_000006945.2), label = full GTDB lineage string
    (e.g. d__Bacteria;p__Proteobacteria;...)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["GTDBTerm"]
    class_class_curie: ClassVar[str] = "culturemech:GTDBTerm"
    class_name: ClassVar[str] = "GTDBTerm"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.GTDBTerm

    id: Union[str, GTDBTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GTDBTermId):
            self.id = GTDBTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MediaDatabaseTerm(Term):
    """
    Identifier from authoritative media database
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["MediaDatabaseTerm"]
    class_class_curie: ClassVar[str] = "culturemech:MediaDatabaseTerm"
    class_name: ClassVar[str] = "MediaDatabaseTerm"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.MediaDatabaseTerm

    id: Union[str, MediaDatabaseTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MediaDatabaseTermId):
            self.id = MediaDatabaseTermId(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class MediumTypeEnum(EnumDefinitionImpl):
    """
    Classification of culture medium
    """
    DEFINED = PermissibleValue(
        text="DEFINED",
        description="Chemically defined medium with known composition",
        meaning=NCIT["C64372"])
    COMPLEX = PermissibleValue(
        text="COMPLEX",
        description="Medium with undefined components (e.g., yeast extract)",
        meaning=NCIT["C64371"])
    SELECTIVE = PermissibleValue(
        text="SELECTIVE",
        description="Medium that selects for specific organisms")
    DIFFERENTIAL = PermissibleValue(
        text="DIFFERENTIAL",
        description="Medium that differentiates organism types")
    ENRICHMENT = PermissibleValue(
        text="ENRICHMENT",
        description="Medium that enriches for specific organisms")
    MINIMAL = PermissibleValue(
        text="MINIMAL",
        description="Medium with minimal nutrients required for growth")

    _defn = EnumDefinition(
        name="MediumTypeEnum",
        description="Classification of culture medium",
    )

class PhysicalStateEnum(EnumDefinitionImpl):
    """
    Physical form of the medium
    """
    LIQUID = PermissibleValue(
        text="LIQUID",
        description="Liquid broth medium")
    SOLID_AGAR = PermissibleValue(
        text="SOLID_AGAR",
        description="Solidified with agar")
    SEMISOLID = PermissibleValue(
        text="SEMISOLID",
        description="Reduced agar concentration for motility testing")
    BIPHASIC = PermissibleValue(
        text="BIPHASIC",
        description="Both liquid and solid phases")

    _defn = EnumDefinition(
        name="PhysicalStateEnum",
        description="Physical form of the medium",
    )

class ConcentrationUnitEnum(EnumDefinitionImpl):
    """
    Units for concentration
    """
    G_PER_L = PermissibleValue(
        text="G_PER_L",
        description="grams per liter",
        meaning=UO["0000175"])
    MG_PER_L = PermissibleValue(
        text="MG_PER_L",
        description="milligrams per liter")
    MICROG_PER_L = PermissibleValue(
        text="MICROG_PER_L",
        description="micrograms per liter")
    MOLAR = PermissibleValue(
        text="MOLAR",
        description="moles per liter",
        meaning=UO["0000062"])
    MILLIMOLAR = PermissibleValue(
        text="MILLIMOLAR",
        description="millimoles per liter")
    MICROMOLAR = PermissibleValue(
        text="MICROMOLAR",
        description="micromoles per liter")
    PERCENT_W_V = PermissibleValue(
        text="PERCENT_W_V",
        description="percent weight per volume")
    PERCENT_V_V = PermissibleValue(
        text="PERCENT_V_V",
        description="percent volume per volume")
    VARIABLE = PermissibleValue(
        text="VARIABLE",
        description="variable or unspecified concentration")

    _defn = EnumDefinition(
        name="ConcentrationUnitEnum",
        description="Units for concentration",
    )

class TemperatureUnitEnum(EnumDefinitionImpl):
    """
    Units for temperature
    """
    CELSIUS = PermissibleValue(
        text="CELSIUS",
        description="Degrees Celsius",
        meaning=UO["0000027"])
    FAHRENHEIT = PermissibleValue(
        text="FAHRENHEIT",
        description="Degrees Fahrenheit")
    KELVIN = PermissibleValue(
        text="KELVIN",
        description="Kelvin",
        meaning=UO["0000012"])

    _defn = EnumDefinition(
        name="TemperatureUnitEnum",
        description="Units for temperature",
    )

class PreparationActionEnum(EnumDefinitionImpl):
    """
    Controlled vocabulary for preparation steps
    """
    DISSOLVE = PermissibleValue(
        text="DISSOLVE",
        description="Dissolve ingredients in solvent")
    MIX = PermissibleValue(
        text="MIX",
        description="Mix or stir components")
    HEAT = PermissibleValue(
        text="HEAT",
        description="Apply heat")
    COOL = PermissibleValue(
        text="COOL",
        description="Cool to specified temperature")
    AUTOCLAVE = PermissibleValue(
        text="AUTOCLAVE",
        description="Steam sterilization under pressure")
    FILTER_STERILIZE = PermissibleValue(
        text="FILTER_STERILIZE",
        description="Filter through 0.22 μm membrane")
    ADJUST_PH = PermissibleValue(
        text="ADJUST_PH",
        description="Adjust pH with acid or base")
    ADD_AGAR = PermissibleValue(
        text="ADD_AGAR",
        description="Add agar for solidification")
    POUR_PLATES = PermissibleValue(
        text="POUR_PLATES",
        description="Dispense into petri dishes")
    ALIQUOT = PermissibleValue(
        text="ALIQUOT",
        description="Divide into smaller portions")
    STORE = PermissibleValue(
        text="STORE",
        description="Store under specified conditions")

    _defn = EnumDefinition(
        name="PreparationActionEnum",
        description="Controlled vocabulary for preparation steps",
    )

class SterilizationMethodEnum(EnumDefinitionImpl):
    """
    Sterilization techniques
    """
    AUTOCLAVE = PermissibleValue(
        text="AUTOCLAVE",
        description="Steam sterilization under pressure (121°C, 15 psi, 15-20 min)")
    FILTER = PermissibleValue(
        text="FILTER",
        description="Filtration through 0.22 μm filter")
    DRY_HEAT = PermissibleValue(
        text="DRY_HEAT",
        description="Dry heat sterilization (160-180°C)")
    TYNDALLIZATION = PermissibleValue(
        text="TYNDALLIZATION",
        description="Intermittent sterilization for heat-sensitive media")
    NONE = PermissibleValue(
        text="NONE",
        description="No sterilization (non-sterile media)")

    _defn = EnumDefinition(
        name="SterilizationMethodEnum",
        description="Sterilization techniques",
    )

class LightConditionEnum(EnumDefinitionImpl):
    """
    Light exposure requirements
    """
    DARK = PermissibleValue(
        text="DARK",
        description="Store in complete darkness")
    LIGHT_PROTECTED = PermissibleValue(
        text="LIGHT_PROTECTED",
        description="Protect from light (amber bottle or foil wrap)")
    AMBIENT = PermissibleValue(
        text="AMBIENT",
        description="Normal laboratory lighting")

    _defn = EnumDefinition(
        name="LightConditionEnum",
        description="Light exposure requirements",
    )

class ModifierEnum(EnumDefinitionImpl):
    """
    Modification type for variants
    """
    INCREASED = PermissibleValue(
        text="INCREASED",
        description="Elevated concentration relative to base recipe")
    DECREASED = PermissibleValue(
        text="DECREASED",
        description="Reduced concentration relative to base recipe")
    ABSENT = PermissibleValue(
        text="ABSENT",
        description="Ingredient omitted in this variant")

    _defn = EnumDefinition(
        name="ModifierEnum",
        description="Modification type for variants",
    )

class EvidenceItemSupportEnum(EnumDefinitionImpl):
    """
    Level of evidence support
    """
    SUPPORT = PermissibleValue(
        text="SUPPORT",
        description="Evidence supports the claim")
    REFUTE = PermissibleValue(
        text="REFUTE",
        description="Evidence refutes the claim")
    PARTIAL = PermissibleValue(
        text="PARTIAL",
        description="Evidence partially supports the claim")
    NO_EVIDENCE = PermissibleValue(
        text="NO_EVIDENCE",
        description="No evidence found")
    WRONG_STATEMENT = PermissibleValue(
        text="WRONG_STATEMENT",
        description="Statement is incorrect")

    _defn = EnumDefinition(
        name="EvidenceItemSupportEnum",
        description="Level of evidence support",
    )

class CategoryEnum(EnumDefinitionImpl):
    """
    Organizational category for media recipes
    """
    bacterial = PermissibleValue(
        text="bacterial",
        description="Media for bacterial cultivation")
    fungal = PermissibleValue(
        text="fungal",
        description="Media for fungal cultivation")
    archaea = PermissibleValue(
        text="archaea",
        description="Media for archaeal cultivation")
    specialized = PermissibleValue(
        text="specialized",
        description="Specialized or multi-domain media")
    algae = PermissibleValue(
        text="algae",
        description="Media for algal cultivation")
    imported = PermissibleValue(
        text="imported",
        description="Imported from external sources (to be recategorized)")

    _defn = EnumDefinition(
        name="CategoryEnum",
        description="Organizational category for media recipes",
    )

class OrganismCultureTypeEnum(EnumDefinitionImpl):
    """
    Whether the medium targets a pure isolate or a mixed microbial community
    """
    isolate = PermissibleValue(
        text="isolate",
        description="Pure culture of one or more specific strains")
    community = PermissibleValue(
        text="community",
        description="Mixed/consortium culture of multiple organisms")

    _defn = EnumDefinition(
        name="OrganismCultureTypeEnum",
        description="Whether the medium targets a pure isolate or a mixed microbial community",
    )

class IngredientRoleEnum(EnumDefinitionImpl):
    """
    Functional role of an ingredient in growth medium
    """
    CARBON_SOURCE = PermissibleValue(
        text="CARBON_SOURCE",
        description="Primary carbon source for metabolism")
    NITROGEN_SOURCE = PermissibleValue(
        text="NITROGEN_SOURCE",
        description="Nitrogen source for biomass synthesis")
    MINERAL = PermissibleValue(
        text="MINERAL",
        description="Mineral nutrient (major element)")
    TRACE_ELEMENT = PermissibleValue(
        text="TRACE_ELEMENT",
        description="Trace element or micronutrient")
    BUFFER = PermissibleValue(
        text="BUFFER",
        description="pH buffering agent")
    VITAMIN_SOURCE = PermissibleValue(
        text="VITAMIN_SOURCE",
        description="Provides vitamins or vitamin precursors")
    SALT = PermissibleValue(
        text="SALT",
        description="Salt for osmotic balance or ionic strength")
    PROTEIN_SOURCE = PermissibleValue(
        text="PROTEIN_SOURCE",
        description="Complex protein source (e.g., peptone, casein)")
    AMINO_ACID_SOURCE = PermissibleValue(
        text="AMINO_ACID_SOURCE",
        description="Provides amino acids")
    SOLIDIFYING_AGENT = PermissibleValue(
        text="SOLIDIFYING_AGENT",
        description="Gelling agent (e.g., agar)")
    ENERGY_SOURCE = PermissibleValue(
        text="ENERGY_SOURCE",
        description="Energy source (often overlaps with carbon source)")
    ELECTRON_ACCEPTOR = PermissibleValue(
        text="ELECTRON_ACCEPTOR",
        description="Terminal electron acceptor for respiration")
    ELECTRON_DONOR = PermissibleValue(
        text="ELECTRON_DONOR",
        description="Electron donor for chemolithotrophs")
    COFACTOR_PROVIDER = PermissibleValue(
        text="COFACTOR_PROVIDER",
        description="Supplies essential cofactors or their precursors")

    _defn = EnumDefinition(
        name="IngredientRoleEnum",
        description="Functional role of an ingredient in growth medium",
    )

class CofactorCategoryEnum(EnumDefinitionImpl):
    """
    High-level classification of cofactor types
    """
    VITAMINS = PermissibleValue(
        text="VITAMINS",
        description="Vitamins and vitamin-derived cofactors")
    METALS = PermissibleValue(
        text="METALS",
        description="Metal ions and metal-containing cofactors")
    NUCLEOTIDES = PermissibleValue(
        text="NUCLEOTIDES",
        description="Nucleotide cofactors")
    ENERGY_TRANSFER = PermissibleValue(
        text="ENERGY_TRANSFER",
        description="Energy transfer and group transfer cofactors")
    OTHER_SPECIALIZED = PermissibleValue(
        text="OTHER_SPECIALIZED",
        description="Specialized cofactors (PQQ, F420, etc.)")

    _defn = EnumDefinition(
        name="CofactorCategoryEnum",
        description="High-level classification of cofactor types",
    )

class CellularRoleEnum(EnumDefinitionImpl):
    """
    Functional role of organism in microbial community
    """
    PRIMARY_DEGRADER = PermissibleValue(
        text="PRIMARY_DEGRADER",
        description="Primary degrader with direct substrate degradation capability (40-60% abundance)")
    REDUCTIVE_DEGRADER = PermissibleValue(
        text="REDUCTIVE_DEGRADER",
        description="Specialized degrader using reductive pathways")
    OXIDATIVE_DEGRADER = PermissibleValue(
        text="OXIDATIVE_DEGRADER",
        description="Specialized degrader using oxidative pathways")
    BIOTRANSFORMER = PermissibleValue(
        text="BIOTRANSFORMER",
        description="Converts substrates to intermediates without complete degradation")
    SYNERGIST = PermissibleValue(
        text="SYNERGIST",
        description="Provides complementary metabolic functions (15-30% abundance)")
    BRIDGE_ORGANISM = PermissibleValue(
        text="BRIDGE_ORGANISM",
        description="Biosynthesizes and provides essential cofactors to community")
    ELECTRON_SHUTTLE = PermissibleValue(
        text="ELECTRON_SHUTTLE",
        description="Facilitates electron transfer between community members")
    DETOXIFIER = PermissibleValue(
        text="DETOXIFIER",
        description="Handles and detoxifies metabolic intermediates")
    COMMENSAL = PermissibleValue(
        text="COMMENSAL",
        description="General commensal organism")
    COMPETITOR = PermissibleValue(
        text="COMPETITOR",
        description="Competitive organism")

    _defn = EnumDefinition(
        name="CellularRoleEnum",
        description="Functional role of organism in microbial community",
    )

class TransporterTypeEnum(EnumDefinitionImpl):
    """
    Classification of membrane transporter systems
    """
    ABC = PermissibleValue(
        text="ABC",
        description="ATP-binding cassette transporter")
    MFS = PermissibleValue(
        text="MFS",
        description="Major facilitator superfamily transporter")
    PTS = PermissibleValue(
        text="PTS",
        description="Phosphotransferase system")
    TONB = PermissibleValue(
        text="TONB",
        description="TonB-dependent receptor")
    SYMPORTER = PermissibleValue(
        text="SYMPORTER",
        description="Symporter or co-transporter")
    ANTIPORTER = PermissibleValue(
        text="ANTIPORTER",
        description="Antiporter or exchanger")
    UNIPORTER = PermissibleValue(
        text="UNIPORTER",
        description="Uniporter or channel")
    PORIN = PermissibleValue(
        text="PORIN",
        description="Porin or outer membrane protein")
    SIDEROPHORE_RECEPTOR = PermissibleValue(
        text="SIDEROPHORE_RECEPTOR",
        description="Siderophore receptor for iron uptake")
    DEHALOGENASE = PermissibleValue(
        text="DEHALOGENASE",
        description="Dehalogenase enzyme for halogenated compounds")
    FLUORIDE_EXPORTER = PermissibleValue(
        text="FLUORIDE_EXPORTER",
        description="Fluoride-specific exporter")

    _defn = EnumDefinition(
        name="TransporterTypeEnum",
        description="Classification of membrane transporter systems",
    )

# Slots
class slots:
    pass

slots.mediaRecipe__name = Slot(uri=CULTUREMECH.name, name="mediaRecipe__name", curie=CULTUREMECH.curie('name'),
                   model_uri=CULTUREMECH.mediaRecipe__name, domain=None, range=URIRef)

slots.mediaRecipe__original_name = Slot(uri=CULTUREMECH.original_name, name="mediaRecipe__original_name", curie=CULTUREMECH.curie('original_name'),
                   model_uri=CULTUREMECH.mediaRecipe__original_name, domain=None, range=Optional[str])

slots.mediaRecipe__category = Slot(uri=CULTUREMECH.category, name="mediaRecipe__category", curie=CULTUREMECH.curie('category'),
                   model_uri=CULTUREMECH.mediaRecipe__category, domain=None, range=Optional[Union[str, "CategoryEnum"]])

slots.mediaRecipe__categories = Slot(uri=CULTUREMECH.categories, name="mediaRecipe__categories", curie=CULTUREMECH.curie('categories'),
                   model_uri=CULTUREMECH.mediaRecipe__categories, domain=None, range=Optional[Union[Union[str, "CategoryEnum"], list[Union[str, "CategoryEnum"]]]])

slots.mediaRecipe__high_metal = Slot(uri=CULTUREMECH.high_metal, name="mediaRecipe__high_metal", curie=CULTUREMECH.curie('high_metal'),
                   model_uri=CULTUREMECH.mediaRecipe__high_metal, domain=None, range=Optional[Union[bool, Bool]])

slots.mediaRecipe__high_ree = Slot(uri=CULTUREMECH.high_ree, name="mediaRecipe__high_ree", curie=CULTUREMECH.curie('high_ree'),
                   model_uri=CULTUREMECH.mediaRecipe__high_ree, domain=None, range=Optional[Union[bool, Bool]])

slots.mediaRecipe__synonyms = Slot(uri=CULTUREMECH.synonyms, name="mediaRecipe__synonyms", curie=CULTUREMECH.curie('synonyms'),
                   model_uri=CULTUREMECH.mediaRecipe__synonyms, domain=None, range=Optional[Union[Union[dict, RecipeSynonym], list[Union[dict, RecipeSynonym]]]])

slots.mediaRecipe__merged_from = Slot(uri=CULTUREMECH.merged_from, name="mediaRecipe__merged_from", curie=CULTUREMECH.curie('merged_from'),
                   model_uri=CULTUREMECH.mediaRecipe__merged_from, domain=None, range=Optional[Union[str, list[str]]])

slots.mediaRecipe__merge_fingerprint = Slot(uri=CULTUREMECH.merge_fingerprint, name="mediaRecipe__merge_fingerprint", curie=CULTUREMECH.curie('merge_fingerprint'),
                   model_uri=CULTUREMECH.mediaRecipe__merge_fingerprint, domain=None, range=Optional[str])

slots.mediaRecipe__media_term = Slot(uri=CULTUREMECH.media_term, name="mediaRecipe__media_term", curie=CULTUREMECH.curie('media_term'),
                   model_uri=CULTUREMECH.mediaRecipe__media_term, domain=None, range=Optional[Union[dict, MediaTypeDescriptor]])

slots.mediaRecipe__description = Slot(uri=CULTUREMECH.description, name="mediaRecipe__description", curie=CULTUREMECH.curie('description'),
                   model_uri=CULTUREMECH.mediaRecipe__description, domain=None, range=Optional[str])

slots.mediaRecipe__target_organisms = Slot(uri=CULTUREMECH.target_organisms, name="mediaRecipe__target_organisms", curie=CULTUREMECH.curie('target_organisms'),
                   model_uri=CULTUREMECH.mediaRecipe__target_organisms, domain=None, range=Optional[Union[Union[dict, OrganismDescriptor], list[Union[dict, OrganismDescriptor]]]])

slots.mediaRecipe__organism_culture_type = Slot(uri=CULTUREMECH.organism_culture_type, name="mediaRecipe__organism_culture_type", curie=CULTUREMECH.curie('organism_culture_type'),
                   model_uri=CULTUREMECH.mediaRecipe__organism_culture_type, domain=None, range=Optional[Union[str, "OrganismCultureTypeEnum"]])

slots.mediaRecipe__medium_type = Slot(uri=CULTUREMECH.medium_type, name="mediaRecipe__medium_type", curie=CULTUREMECH.curie('medium_type'),
                   model_uri=CULTUREMECH.mediaRecipe__medium_type, domain=None, range=Union[str, "MediumTypeEnum"])

slots.mediaRecipe__physical_state = Slot(uri=CULTUREMECH.physical_state, name="mediaRecipe__physical_state", curie=CULTUREMECH.curie('physical_state'),
                   model_uri=CULTUREMECH.mediaRecipe__physical_state, domain=None, range=Union[str, "PhysicalStateEnum"])

slots.mediaRecipe__ph_value = Slot(uri=CULTUREMECH.ph_value, name="mediaRecipe__ph_value", curie=CULTUREMECH.curie('ph_value'),
                   model_uri=CULTUREMECH.mediaRecipe__ph_value, domain=None, range=Optional[float])

slots.mediaRecipe__ph_range = Slot(uri=CULTUREMECH.ph_range, name="mediaRecipe__ph_range", curie=CULTUREMECH.curie('ph_range'),
                   model_uri=CULTUREMECH.mediaRecipe__ph_range, domain=None, range=Optional[str])

slots.mediaRecipe__light_intensity = Slot(uri=CULTUREMECH.light_intensity, name="mediaRecipe__light_intensity", curie=CULTUREMECH.curie('light_intensity'),
                   model_uri=CULTUREMECH.mediaRecipe__light_intensity, domain=None, range=Optional[str])

slots.mediaRecipe__light_cycle = Slot(uri=CULTUREMECH.light_cycle, name="mediaRecipe__light_cycle", curie=CULTUREMECH.curie('light_cycle'),
                   model_uri=CULTUREMECH.mediaRecipe__light_cycle, domain=None, range=Optional[str])

slots.mediaRecipe__light_quality = Slot(uri=CULTUREMECH.light_quality, name="mediaRecipe__light_quality", curie=CULTUREMECH.curie('light_quality'),
                   model_uri=CULTUREMECH.mediaRecipe__light_quality, domain=None, range=Optional[str])

slots.mediaRecipe__temperature_range = Slot(uri=CULTUREMECH.temperature_range, name="mediaRecipe__temperature_range", curie=CULTUREMECH.curie('temperature_range'),
                   model_uri=CULTUREMECH.mediaRecipe__temperature_range, domain=None, range=Optional[str])

slots.mediaRecipe__temperature_value = Slot(uri=CULTUREMECH.temperature_value, name="mediaRecipe__temperature_value", curie=CULTUREMECH.curie('temperature_value'),
                   model_uri=CULTUREMECH.mediaRecipe__temperature_value, domain=None, range=Optional[float])

slots.mediaRecipe__salinity = Slot(uri=CULTUREMECH.salinity, name="mediaRecipe__salinity", curie=CULTUREMECH.curie('salinity'),
                   model_uri=CULTUREMECH.mediaRecipe__salinity, domain=None, range=Optional[str])

slots.mediaRecipe__aeration = Slot(uri=CULTUREMECH.aeration, name="mediaRecipe__aeration", curie=CULTUREMECH.curie('aeration'),
                   model_uri=CULTUREMECH.mediaRecipe__aeration, domain=None, range=Optional[str])

slots.mediaRecipe__culture_vessel = Slot(uri=CULTUREMECH.culture_vessel, name="mediaRecipe__culture_vessel", curie=CULTUREMECH.curie('culture_vessel'),
                   model_uri=CULTUREMECH.mediaRecipe__culture_vessel, domain=None, range=Optional[str])

slots.mediaRecipe__ingredients = Slot(uri=CULTUREMECH.ingredients, name="mediaRecipe__ingredients", curie=CULTUREMECH.curie('ingredients'),
                   model_uri=CULTUREMECH.mediaRecipe__ingredients, domain=None, range=Union[Union[dict, IngredientDescriptor], list[Union[dict, IngredientDescriptor]]])

slots.mediaRecipe__solutions = Slot(uri=CULTUREMECH.solutions, name="mediaRecipe__solutions", curie=CULTUREMECH.curie('solutions'),
                   model_uri=CULTUREMECH.mediaRecipe__solutions, domain=None, range=Optional[Union[Union[dict, SolutionDescriptor], list[Union[dict, SolutionDescriptor]]]])

slots.mediaRecipe__preparation_steps = Slot(uri=CULTUREMECH.preparation_steps, name="mediaRecipe__preparation_steps", curie=CULTUREMECH.curie('preparation_steps'),
                   model_uri=CULTUREMECH.mediaRecipe__preparation_steps, domain=None, range=Optional[Union[Union[dict, PreparationStep], list[Union[dict, PreparationStep]]]])

slots.mediaRecipe__sterilization = Slot(uri=CULTUREMECH.sterilization, name="mediaRecipe__sterilization", curie=CULTUREMECH.curie('sterilization'),
                   model_uri=CULTUREMECH.mediaRecipe__sterilization, domain=None, range=Optional[Union[dict, SterilizationDescriptor]])

slots.mediaRecipe__storage = Slot(uri=CULTUREMECH.storage, name="mediaRecipe__storage", curie=CULTUREMECH.curie('storage'),
                   model_uri=CULTUREMECH.mediaRecipe__storage, domain=None, range=Optional[Union[dict, StorageConditions]])

slots.mediaRecipe__applications = Slot(uri=CULTUREMECH.applications, name="mediaRecipe__applications", curie=CULTUREMECH.curie('applications'),
                   model_uri=CULTUREMECH.mediaRecipe__applications, domain=None, range=Optional[Union[str, list[str]]])

slots.mediaRecipe__variants = Slot(uri=CULTUREMECH.variants, name="mediaRecipe__variants", curie=CULTUREMECH.curie('variants'),
                   model_uri=CULTUREMECH.mediaRecipe__variants, domain=None, range=Optional[Union[Union[dict, MediaVariant], list[Union[dict, MediaVariant]]]])

slots.mediaRecipe__references = Slot(uri=CULTUREMECH.references, name="mediaRecipe__references", curie=CULTUREMECH.curie('references'),
                   model_uri=CULTUREMECH.mediaRecipe__references, domain=None, range=Optional[Union[Union[dict, PublicationReference], list[Union[dict, PublicationReference]]]])

slots.mediaRecipe__notes = Slot(uri=CULTUREMECH.notes, name="mediaRecipe__notes", curie=CULTUREMECH.curie('notes'),
                   model_uri=CULTUREMECH.mediaRecipe__notes, domain=None, range=Optional[str])

slots.mediaRecipe__evidence = Slot(uri=CULTUREMECH.evidence, name="mediaRecipe__evidence", curie=CULTUREMECH.curie('evidence'),
                   model_uri=CULTUREMECH.mediaRecipe__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.mediaRecipe__datasets = Slot(uri=CULTUREMECH.datasets, name="mediaRecipe__datasets", curie=CULTUREMECH.curie('datasets'),
                   model_uri=CULTUREMECH.mediaRecipe__datasets, domain=None, range=Optional[Union[Union[dict, Dataset], list[Union[dict, Dataset]]]])

slots.mediaRecipe__curation_history = Slot(uri=CULTUREMECH.curation_history, name="mediaRecipe__curation_history", curie=CULTUREMECH.curie('curation_history'),
                   model_uri=CULTUREMECH.mediaRecipe__curation_history, domain=None, range=Optional[Union[Union[dict, CurationEvent], list[Union[dict, CurationEvent]]]])

slots.mediaRecipe__data_quality_flags = Slot(uri=CULTUREMECH.data_quality_flags, name="mediaRecipe__data_quality_flags", curie=CULTUREMECH.curie('data_quality_flags'),
                   model_uri=CULTUREMECH.mediaRecipe__data_quality_flags, domain=None, range=Optional[Union[str, list[str]]])

slots.recipeSynonym__name = Slot(uri=CULTUREMECH.name, name="recipeSynonym__name", curie=CULTUREMECH.curie('name'),
                   model_uri=CULTUREMECH.recipeSynonym__name, domain=None, range=str)

slots.recipeSynonym__source = Slot(uri=CULTUREMECH.source, name="recipeSynonym__source", curie=CULTUREMECH.curie('source'),
                   model_uri=CULTUREMECH.recipeSynonym__source, domain=None, range=str)

slots.recipeSynonym__source_id = Slot(uri=CULTUREMECH.source_id, name="recipeSynonym__source_id", curie=CULTUREMECH.curie('source_id'),
                   model_uri=CULTUREMECH.recipeSynonym__source_id, domain=None, range=Optional[str])

slots.recipeSynonym__original_category = Slot(uri=CULTUREMECH.original_category, name="recipeSynonym__original_category", curie=CULTUREMECH.curie('original_category'),
                   model_uri=CULTUREMECH.recipeSynonym__original_category, domain=None, range=Optional[Union[str, "CategoryEnum"]])

slots.term__id = Slot(uri=CULTUREMECH.id, name="term__id", curie=CULTUREMECH.curie('id'),
                   model_uri=CULTUREMECH.term__id, domain=None, range=URIRef)

slots.term__label = Slot(uri=CULTUREMECH.label, name="term__label", curie=CULTUREMECH.curie('label'),
                   model_uri=CULTUREMECH.term__label, domain=None, range=Optional[str])

slots.mediaTypeDescriptor__preferred_term = Slot(uri=CULTUREMECH.preferred_term, name="mediaTypeDescriptor__preferred_term", curie=CULTUREMECH.curie('preferred_term'),
                   model_uri=CULTUREMECH.mediaTypeDescriptor__preferred_term, domain=None, range=str)

slots.mediaTypeDescriptor__term = Slot(uri=CULTUREMECH.term, name="mediaTypeDescriptor__term", curie=CULTUREMECH.curie('term'),
                   model_uri=CULTUREMECH.mediaTypeDescriptor__term, domain=None, range=Optional[Union[dict, MediaDatabaseTerm]])

slots.ingredientDescriptor__preferred_term = Slot(uri=CULTUREMECH.preferred_term, name="ingredientDescriptor__preferred_term", curie=CULTUREMECH.curie('preferred_term'),
                   model_uri=CULTUREMECH.ingredientDescriptor__preferred_term, domain=None, range=str)

slots.ingredientDescriptor__term = Slot(uri=CULTUREMECH.term, name="ingredientDescriptor__term", curie=CULTUREMECH.curie('term'),
                   model_uri=CULTUREMECH.ingredientDescriptor__term, domain=None, range=Optional[Union[dict, ChemicalEntityTerm]])

slots.ingredientDescriptor__concentration = Slot(uri=CULTUREMECH.concentration, name="ingredientDescriptor__concentration", curie=CULTUREMECH.curie('concentration'),
                   model_uri=CULTUREMECH.ingredientDescriptor__concentration, domain=None, range=Union[dict, ConcentrationValue])

slots.ingredientDescriptor__modifier = Slot(uri=CULTUREMECH.modifier, name="ingredientDescriptor__modifier", curie=CULTUREMECH.curie('modifier'),
                   model_uri=CULTUREMECH.ingredientDescriptor__modifier, domain=None, range=Optional[Union[str, "ModifierEnum"]])

slots.ingredientDescriptor__chemical_formula = Slot(uri=CULTUREMECH.chemical_formula, name="ingredientDescriptor__chemical_formula", curie=CULTUREMECH.curie('chemical_formula'),
                   model_uri=CULTUREMECH.ingredientDescriptor__chemical_formula, domain=None, range=Optional[str])

slots.ingredientDescriptor__molecular_weight = Slot(uri=CULTUREMECH.molecular_weight, name="ingredientDescriptor__molecular_weight", curie=CULTUREMECH.curie('molecular_weight'),
                   model_uri=CULTUREMECH.ingredientDescriptor__molecular_weight, domain=None, range=Optional[float])

slots.ingredientDescriptor__supplier_catalog = Slot(uri=CULTUREMECH.supplier_catalog, name="ingredientDescriptor__supplier_catalog", curie=CULTUREMECH.curie('supplier_catalog'),
                   model_uri=CULTUREMECH.ingredientDescriptor__supplier_catalog, domain=None, range=Optional[Union[dict, SupplierInfo]])

slots.ingredientDescriptor__notes = Slot(uri=CULTUREMECH.notes, name="ingredientDescriptor__notes", curie=CULTUREMECH.curie('notes'),
                   model_uri=CULTUREMECH.ingredientDescriptor__notes, domain=None, range=Optional[str])

slots.ingredientDescriptor__role = Slot(uri=CULTUREMECH.role, name="ingredientDescriptor__role", curie=CULTUREMECH.curie('role'),
                   model_uri=CULTUREMECH.ingredientDescriptor__role, domain=None, range=Optional[Union[Union[str, "IngredientRoleEnum"], list[Union[str, "IngredientRoleEnum"]]]])

slots.ingredientDescriptor__cofactors_provided = Slot(uri=CULTUREMECH.cofactors_provided, name="ingredientDescriptor__cofactors_provided", curie=CULTUREMECH.curie('cofactors_provided'),
                   model_uri=CULTUREMECH.ingredientDescriptor__cofactors_provided, domain=None, range=Optional[Union[Union[dict, CofactorDescriptor], list[Union[dict, CofactorDescriptor]]]])

slots.ingredientDescriptor__evidence = Slot(uri=CULTUREMECH.evidence, name="ingredientDescriptor__evidence", curie=CULTUREMECH.curie('evidence'),
                   model_uri=CULTUREMECH.ingredientDescriptor__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.solutionDescriptor__preferred_term = Slot(uri=CULTUREMECH.preferred_term, name="solutionDescriptor__preferred_term", curie=CULTUREMECH.curie('preferred_term'),
                   model_uri=CULTUREMECH.solutionDescriptor__preferred_term, domain=None, range=str)

slots.solutionDescriptor__term = Slot(uri=CULTUREMECH.term, name="solutionDescriptor__term", curie=CULTUREMECH.curie('term'),
                   model_uri=CULTUREMECH.solutionDescriptor__term, domain=None, range=Optional[Union[dict, Term]])

slots.solutionDescriptor__composition = Slot(uri=CULTUREMECH.composition, name="solutionDescriptor__composition", curie=CULTUREMECH.curie('composition'),
                   model_uri=CULTUREMECH.solutionDescriptor__composition, domain=None, range=Union[Union[dict, IngredientDescriptor], list[Union[dict, IngredientDescriptor]]])

slots.solutionDescriptor__concentration = Slot(uri=CULTUREMECH.concentration, name="solutionDescriptor__concentration", curie=CULTUREMECH.curie('concentration'),
                   model_uri=CULTUREMECH.solutionDescriptor__concentration, domain=None, range=Optional[Union[dict, ConcentrationValue]])

slots.solutionDescriptor__preparation_notes = Slot(uri=CULTUREMECH.preparation_notes, name="solutionDescriptor__preparation_notes", curie=CULTUREMECH.curie('preparation_notes'),
                   model_uri=CULTUREMECH.solutionDescriptor__preparation_notes, domain=None, range=Optional[str])

slots.solutionDescriptor__storage_conditions = Slot(uri=CULTUREMECH.storage_conditions, name="solutionDescriptor__storage_conditions", curie=CULTUREMECH.curie('storage_conditions'),
                   model_uri=CULTUREMECH.solutionDescriptor__storage_conditions, domain=None, range=Optional[Union[dict, StorageConditions]])

slots.solutionDescriptor__shelf_life = Slot(uri=CULTUREMECH.shelf_life, name="solutionDescriptor__shelf_life", curie=CULTUREMECH.curie('shelf_life'),
                   model_uri=CULTUREMECH.solutionDescriptor__shelf_life, domain=None, range=Optional[str])

slots.organismDescriptor__preferred_term = Slot(uri=CULTUREMECH.preferred_term, name="organismDescriptor__preferred_term", curie=CULTUREMECH.curie('preferred_term'),
                   model_uri=CULTUREMECH.organismDescriptor__preferred_term, domain=None, range=str)

slots.organismDescriptor__term = Slot(uri=CULTUREMECH.term, name="organismDescriptor__term", curie=CULTUREMECH.curie('term'),
                   model_uri=CULTUREMECH.organismDescriptor__term, domain=None, range=Optional[Union[dict, OrganismTerm]])

slots.organismDescriptor__gtdb_term = Slot(uri=CULTUREMECH.gtdb_term, name="organismDescriptor__gtdb_term", curie=CULTUREMECH.curie('gtdb_term'),
                   model_uri=CULTUREMECH.organismDescriptor__gtdb_term, domain=None, range=Optional[Union[dict, GTDBTerm]])

slots.organismDescriptor__strain = Slot(uri=CULTUREMECH.strain, name="organismDescriptor__strain", curie=CULTUREMECH.curie('strain'),
                   model_uri=CULTUREMECH.organismDescriptor__strain, domain=None, range=Optional[str])

slots.organismDescriptor__growth_phase = Slot(uri=CULTUREMECH.growth_phase, name="organismDescriptor__growth_phase", curie=CULTUREMECH.curie('growth_phase'),
                   model_uri=CULTUREMECH.organismDescriptor__growth_phase, domain=None, range=Optional[str])

slots.organismDescriptor__community_role = Slot(uri=CULTUREMECH.community_role, name="organismDescriptor__community_role", curie=CULTUREMECH.curie('community_role'),
                   model_uri=CULTUREMECH.organismDescriptor__community_role, domain=None, range=Optional[Union[Union[str, "CellularRoleEnum"], list[Union[str, "CellularRoleEnum"]]]])

slots.organismDescriptor__target_abundance = Slot(uri=CULTUREMECH.target_abundance, name="organismDescriptor__target_abundance", curie=CULTUREMECH.curie('target_abundance'),
                   model_uri=CULTUREMECH.organismDescriptor__target_abundance, domain=None, range=Optional[float])

slots.organismDescriptor__community_function = Slot(uri=CULTUREMECH.community_function, name="organismDescriptor__community_function", curie=CULTUREMECH.curie('community_function'),
                   model_uri=CULTUREMECH.organismDescriptor__community_function, domain=None, range=Optional[Union[str, list[str]]])

slots.organismDescriptor__cofactor_requirements = Slot(uri=CULTUREMECH.cofactor_requirements, name="organismDescriptor__cofactor_requirements", curie=CULTUREMECH.curie('cofactor_requirements'),
                   model_uri=CULTUREMECH.organismDescriptor__cofactor_requirements, domain=None, range=Optional[Union[Union[dict, CofactorRequirement], list[Union[dict, CofactorRequirement]]]])

slots.organismDescriptor__transporters = Slot(uri=CULTUREMECH.transporters, name="organismDescriptor__transporters", curie=CULTUREMECH.curie('transporters'),
                   model_uri=CULTUREMECH.organismDescriptor__transporters, domain=None, range=Optional[Union[Union[dict, TransporterAnnotation], list[Union[dict, TransporterAnnotation]]]])

slots.organismDescriptor__evidence = Slot(uri=CULTUREMECH.evidence, name="organismDescriptor__evidence", curie=CULTUREMECH.curie('evidence'),
                   model_uri=CULTUREMECH.organismDescriptor__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.cofactorDescriptor__preferred_term = Slot(uri=CULTUREMECH.preferred_term, name="cofactorDescriptor__preferred_term", curie=CULTUREMECH.curie('preferred_term'),
                   model_uri=CULTUREMECH.cofactorDescriptor__preferred_term, domain=None, range=str)

slots.cofactorDescriptor__term = Slot(uri=CULTUREMECH.term, name="cofactorDescriptor__term", curie=CULTUREMECH.curie('term'),
                   model_uri=CULTUREMECH.cofactorDescriptor__term, domain=None, range=Optional[Union[dict, ChemicalEntityTerm]])

slots.cofactorDescriptor__category = Slot(uri=CULTUREMECH.category, name="cofactorDescriptor__category", curie=CULTUREMECH.curie('category'),
                   model_uri=CULTUREMECH.cofactorDescriptor__category, domain=None, range=Optional[Union[str, "CofactorCategoryEnum"]])

slots.cofactorDescriptor__precursor = Slot(uri=CULTUREMECH.precursor, name="cofactorDescriptor__precursor", curie=CULTUREMECH.curie('precursor'),
                   model_uri=CULTUREMECH.cofactorDescriptor__precursor, domain=None, range=Optional[str])

slots.cofactorDescriptor__precursor_term = Slot(uri=CULTUREMECH.precursor_term, name="cofactorDescriptor__precursor_term", curie=CULTUREMECH.curie('precursor_term'),
                   model_uri=CULTUREMECH.cofactorDescriptor__precursor_term, domain=None, range=Optional[Union[dict, ChemicalEntityTerm]])

slots.cofactorDescriptor__ec_associations = Slot(uri=CULTUREMECH.ec_associations, name="cofactorDescriptor__ec_associations", curie=CULTUREMECH.curie('ec_associations'),
                   model_uri=CULTUREMECH.cofactorDescriptor__ec_associations, domain=None, range=Optional[Union[str, list[str]]])

slots.cofactorDescriptor__kegg_pathways = Slot(uri=CULTUREMECH.kegg_pathways, name="cofactorDescriptor__kegg_pathways", curie=CULTUREMECH.curie('kegg_pathways'),
                   model_uri=CULTUREMECH.cofactorDescriptor__kegg_pathways, domain=None, range=Optional[Union[str, list[str]]])

slots.cofactorDescriptor__enzyme_examples = Slot(uri=CULTUREMECH.enzyme_examples, name="cofactorDescriptor__enzyme_examples", curie=CULTUREMECH.curie('enzyme_examples'),
                   model_uri=CULTUREMECH.cofactorDescriptor__enzyme_examples, domain=None, range=Optional[Union[str, list[str]]])

slots.cofactorDescriptor__biosynthesis_genes = Slot(uri=CULTUREMECH.biosynthesis_genes, name="cofactorDescriptor__biosynthesis_genes", curie=CULTUREMECH.curie('biosynthesis_genes'),
                   model_uri=CULTUREMECH.cofactorDescriptor__biosynthesis_genes, domain=None, range=Optional[Union[str, list[str]]])

slots.cofactorDescriptor__bioavailability = Slot(uri=CULTUREMECH.bioavailability, name="cofactorDescriptor__bioavailability", curie=CULTUREMECH.curie('bioavailability'),
                   model_uri=CULTUREMECH.cofactorDescriptor__bioavailability, domain=None, range=Optional[str])

slots.cofactorDescriptor__notes = Slot(uri=CULTUREMECH.notes, name="cofactorDescriptor__notes", curie=CULTUREMECH.curie('notes'),
                   model_uri=CULTUREMECH.cofactorDescriptor__notes, domain=None, range=Optional[str])

slots.concentrationValue__value = Slot(uri=CULTUREMECH.value, name="concentrationValue__value", curie=CULTUREMECH.curie('value'),
                   model_uri=CULTUREMECH.concentrationValue__value, domain=None, range=str)

slots.concentrationValue__unit = Slot(uri=CULTUREMECH.unit, name="concentrationValue__unit", curie=CULTUREMECH.curie('unit'),
                   model_uri=CULTUREMECH.concentrationValue__unit, domain=None, range=Union[str, "ConcentrationUnitEnum"])

slots.concentrationValue__per_volume = Slot(uri=CULTUREMECH.per_volume, name="concentrationValue__per_volume", curie=CULTUREMECH.curie('per_volume'),
                   model_uri=CULTUREMECH.concentrationValue__per_volume, domain=None, range=Optional[str])

slots.temperatureValue__value = Slot(uri=CULTUREMECH.value, name="temperatureValue__value", curie=CULTUREMECH.curie('value'),
                   model_uri=CULTUREMECH.temperatureValue__value, domain=None, range=float)

slots.temperatureValue__unit = Slot(uri=CULTUREMECH.unit, name="temperatureValue__unit", curie=CULTUREMECH.curie('unit'),
                   model_uri=CULTUREMECH.temperatureValue__unit, domain=None, range=Union[str, "TemperatureUnitEnum"])

slots.preparationStep__step_number = Slot(uri=CULTUREMECH.step_number, name="preparationStep__step_number", curie=CULTUREMECH.curie('step_number'),
                   model_uri=CULTUREMECH.preparationStep__step_number, domain=None, range=int)

slots.preparationStep__action = Slot(uri=CULTUREMECH.action, name="preparationStep__action", curie=CULTUREMECH.curie('action'),
                   model_uri=CULTUREMECH.preparationStep__action, domain=None, range=Union[str, "PreparationActionEnum"])

slots.preparationStep__description = Slot(uri=CULTUREMECH.description, name="preparationStep__description", curie=CULTUREMECH.curie('description'),
                   model_uri=CULTUREMECH.preparationStep__description, domain=None, range=str)

slots.preparationStep__temperature = Slot(uri=CULTUREMECH.temperature, name="preparationStep__temperature", curie=CULTUREMECH.curie('temperature'),
                   model_uri=CULTUREMECH.preparationStep__temperature, domain=None, range=Optional[Union[dict, TemperatureValue]])

slots.preparationStep__duration = Slot(uri=CULTUREMECH.duration, name="preparationStep__duration", curie=CULTUREMECH.curie('duration'),
                   model_uri=CULTUREMECH.preparationStep__duration, domain=None, range=Optional[str])

slots.preparationStep__equipment = Slot(uri=CULTUREMECH.equipment, name="preparationStep__equipment", curie=CULTUREMECH.curie('equipment'),
                   model_uri=CULTUREMECH.preparationStep__equipment, domain=None, range=Optional[str])

slots.preparationStep__notes = Slot(uri=CULTUREMECH.notes, name="preparationStep__notes", curie=CULTUREMECH.curie('notes'),
                   model_uri=CULTUREMECH.preparationStep__notes, domain=None, range=Optional[str])

slots.sterilizationDescriptor__method = Slot(uri=CULTUREMECH.method, name="sterilizationDescriptor__method", curie=CULTUREMECH.curie('method'),
                   model_uri=CULTUREMECH.sterilizationDescriptor__method, domain=None, range=Union[str, "SterilizationMethodEnum"])

slots.sterilizationDescriptor__temperature = Slot(uri=CULTUREMECH.temperature, name="sterilizationDescriptor__temperature", curie=CULTUREMECH.curie('temperature'),
                   model_uri=CULTUREMECH.sterilizationDescriptor__temperature, domain=None, range=Optional[Union[dict, TemperatureValue]])

slots.sterilizationDescriptor__pressure = Slot(uri=CULTUREMECH.pressure, name="sterilizationDescriptor__pressure", curie=CULTUREMECH.curie('pressure'),
                   model_uri=CULTUREMECH.sterilizationDescriptor__pressure, domain=None, range=Optional[float])

slots.sterilizationDescriptor__duration = Slot(uri=CULTUREMECH.duration, name="sterilizationDescriptor__duration", curie=CULTUREMECH.curie('duration'),
                   model_uri=CULTUREMECH.sterilizationDescriptor__duration, domain=None, range=Optional[str])

slots.sterilizationDescriptor__notes = Slot(uri=CULTUREMECH.notes, name="sterilizationDescriptor__notes", curie=CULTUREMECH.curie('notes'),
                   model_uri=CULTUREMECH.sterilizationDescriptor__notes, domain=None, range=Optional[str])

slots.storageConditions__temperature = Slot(uri=CULTUREMECH.temperature, name="storageConditions__temperature", curie=CULTUREMECH.curie('temperature'),
                   model_uri=CULTUREMECH.storageConditions__temperature, domain=None, range=Union[dict, TemperatureValue])

slots.storageConditions__light_condition = Slot(uri=CULTUREMECH.light_condition, name="storageConditions__light_condition", curie=CULTUREMECH.curie('light_condition'),
                   model_uri=CULTUREMECH.storageConditions__light_condition, domain=None, range=Optional[Union[str, "LightConditionEnum"]])

slots.storageConditions__shelf_life = Slot(uri=CULTUREMECH.shelf_life, name="storageConditions__shelf_life", curie=CULTUREMECH.curie('shelf_life'),
                   model_uri=CULTUREMECH.storageConditions__shelf_life, domain=None, range=Optional[str])

slots.storageConditions__container_type = Slot(uri=CULTUREMECH.container_type, name="storageConditions__container_type", curie=CULTUREMECH.curie('container_type'),
                   model_uri=CULTUREMECH.storageConditions__container_type, domain=None, range=Optional[str])

slots.storageConditions__notes = Slot(uri=CULTUREMECH.notes, name="storageConditions__notes", curie=CULTUREMECH.curie('notes'),
                   model_uri=CULTUREMECH.storageConditions__notes, domain=None, range=Optional[str])

slots.mediaVariant__name = Slot(uri=CULTUREMECH.name, name="mediaVariant__name", curie=CULTUREMECH.curie('name'),
                   model_uri=CULTUREMECH.mediaVariant__name, domain=None, range=str)

slots.mediaVariant__description = Slot(uri=CULTUREMECH.description, name="mediaVariant__description", curie=CULTUREMECH.curie('description'),
                   model_uri=CULTUREMECH.mediaVariant__description, domain=None, range=Optional[str])

slots.mediaVariant__modifications = Slot(uri=CULTUREMECH.modifications, name="mediaVariant__modifications", curie=CULTUREMECH.curie('modifications'),
                   model_uri=CULTUREMECH.mediaVariant__modifications, domain=None, range=Optional[Union[str, list[str]]])

slots.mediaVariant__purpose = Slot(uri=CULTUREMECH.purpose, name="mediaVariant__purpose", curie=CULTUREMECH.curie('purpose'),
                   model_uri=CULTUREMECH.mediaVariant__purpose, domain=None, range=Optional[str])

slots.mediaVariant__supplier_info = Slot(uri=CULTUREMECH.supplier_info, name="mediaVariant__supplier_info", curie=CULTUREMECH.curie('supplier_info'),
                   model_uri=CULTUREMECH.mediaVariant__supplier_info, domain=None, range=Optional[Union[dict, SupplierInfo]])

slots.mediaVariant__evidence = Slot(uri=CULTUREMECH.evidence, name="mediaVariant__evidence", curie=CULTUREMECH.curie('evidence'),
                   model_uri=CULTUREMECH.mediaVariant__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.supplierInfo__supplier_name = Slot(uri=CULTUREMECH.supplier_name, name="supplierInfo__supplier_name", curie=CULTUREMECH.curie('supplier_name'),
                   model_uri=CULTUREMECH.supplierInfo__supplier_name, domain=None, range=str)

slots.supplierInfo__catalog_number = Slot(uri=CULTUREMECH.catalog_number, name="supplierInfo__catalog_number", curie=CULTUREMECH.curie('catalog_number'),
                   model_uri=CULTUREMECH.supplierInfo__catalog_number, domain=None, range=Optional[str])

slots.supplierInfo__product_url = Slot(uri=CULTUREMECH.product_url, name="supplierInfo__product_url", curie=CULTUREMECH.curie('product_url'),
                   model_uri=CULTUREMECH.supplierInfo__product_url, domain=None, range=Optional[Union[str, URI]])

slots.supplierInfo__notes = Slot(uri=CULTUREMECH.notes, name="supplierInfo__notes", curie=CULTUREMECH.curie('notes'),
                   model_uri=CULTUREMECH.supplierInfo__notes, domain=None, range=Optional[str])

slots.publicationReference__reference = Slot(uri=CULTUREMECH.reference, name="publicationReference__reference", curie=CULTUREMECH.curie('reference'),
                   model_uri=CULTUREMECH.publicationReference__reference, domain=None, range=str)

slots.publicationReference__title = Slot(uri=CULTUREMECH.title, name="publicationReference__title", curie=CULTUREMECH.curie('title'),
                   model_uri=CULTUREMECH.publicationReference__title, domain=None, range=Optional[str])

slots.publicationReference__authors = Slot(uri=CULTUREMECH.authors, name="publicationReference__authors", curie=CULTUREMECH.curie('authors'),
                   model_uri=CULTUREMECH.publicationReference__authors, domain=None, range=Optional[str])

slots.publicationReference__year = Slot(uri=CULTUREMECH.year, name="publicationReference__year", curie=CULTUREMECH.curie('year'),
                   model_uri=CULTUREMECH.publicationReference__year, domain=None, range=Optional[int])

slots.publicationReference__notes = Slot(uri=CULTUREMECH.notes, name="publicationReference__notes", curie=CULTUREMECH.curie('notes'),
                   model_uri=CULTUREMECH.publicationReference__notes, domain=None, range=Optional[str])

slots.evidenceItem__reference = Slot(uri=CULTUREMECH.reference, name="evidenceItem__reference", curie=CULTUREMECH.curie('reference'),
                   model_uri=CULTUREMECH.evidenceItem__reference, domain=None, range=str)

slots.evidenceItem__supports = Slot(uri=CULTUREMECH.supports, name="evidenceItem__supports", curie=CULTUREMECH.curie('supports'),
                   model_uri=CULTUREMECH.evidenceItem__supports, domain=None, range=Union[str, "EvidenceItemSupportEnum"])

slots.evidenceItem__snippet = Slot(uri=CULTUREMECH.snippet, name="evidenceItem__snippet", curie=CULTUREMECH.curie('snippet'),
                   model_uri=CULTUREMECH.evidenceItem__snippet, domain=None, range=Optional[str])

slots.evidenceItem__explanation = Slot(uri=CULTUREMECH.explanation, name="evidenceItem__explanation", curie=CULTUREMECH.curie('explanation'),
                   model_uri=CULTUREMECH.evidenceItem__explanation, domain=None, range=str)

slots.dataset__dataset_id = Slot(uri=CULTUREMECH.dataset_id, name="dataset__dataset_id", curie=CULTUREMECH.curie('dataset_id'),
                   model_uri=CULTUREMECH.dataset__dataset_id, domain=None, range=str)

slots.dataset__dataset_type = Slot(uri=CULTUREMECH.dataset_type, name="dataset__dataset_type", curie=CULTUREMECH.curie('dataset_type'),
                   model_uri=CULTUREMECH.dataset__dataset_type, domain=None, range=Optional[str])

slots.dataset__description = Slot(uri=CULTUREMECH.description, name="dataset__description", curie=CULTUREMECH.curie('description'),
                   model_uri=CULTUREMECH.dataset__description, domain=None, range=Optional[str])

slots.dataset__url = Slot(uri=CULTUREMECH.url, name="dataset__url", curie=CULTUREMECH.curie('url'),
                   model_uri=CULTUREMECH.dataset__url, domain=None, range=Optional[Union[str, URI]])

slots.curationEvent__timestamp = Slot(uri=CULTUREMECH.timestamp, name="curationEvent__timestamp", curie=CULTUREMECH.curie('timestamp'),
                   model_uri=CULTUREMECH.curationEvent__timestamp, domain=None, range=str)

slots.curationEvent__curator = Slot(uri=CULTUREMECH.curator, name="curationEvent__curator", curie=CULTUREMECH.curie('curator'),
                   model_uri=CULTUREMECH.curationEvent__curator, domain=None, range=str)

slots.curationEvent__action = Slot(uri=CULTUREMECH.action, name="curationEvent__action", curie=CULTUREMECH.curie('action'),
                   model_uri=CULTUREMECH.curationEvent__action, domain=None, range=str)

slots.curationEvent__notes = Slot(uri=CULTUREMECH.notes, name="curationEvent__notes", curie=CULTUREMECH.curie('notes'),
                   model_uri=CULTUREMECH.curationEvent__notes, domain=None, range=Optional[str])

slots.cofactorRequirement__cofactor = Slot(uri=CULTUREMECH.cofactor, name="cofactorRequirement__cofactor", curie=CULTUREMECH.curie('cofactor'),
                   model_uri=CULTUREMECH.cofactorRequirement__cofactor, domain=None, range=Union[dict, CofactorDescriptor])

slots.cofactorRequirement__can_biosynthesize = Slot(uri=CULTUREMECH.can_biosynthesize, name="cofactorRequirement__can_biosynthesize", curie=CULTUREMECH.curie('can_biosynthesize'),
                   model_uri=CULTUREMECH.cofactorRequirement__can_biosynthesize, domain=None, range=Union[bool, Bool])

slots.cofactorRequirement__confidence = Slot(uri=CULTUREMECH.confidence, name="cofactorRequirement__confidence", curie=CULTUREMECH.curie('confidence'),
                   model_uri=CULTUREMECH.cofactorRequirement__confidence, domain=None, range=Optional[float])

slots.cofactorRequirement__evidence = Slot(uri=CULTUREMECH.evidence, name="cofactorRequirement__evidence", curie=CULTUREMECH.curie('evidence'),
                   model_uri=CULTUREMECH.cofactorRequirement__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.cofactorRequirement__genes = Slot(uri=CULTUREMECH.genes, name="cofactorRequirement__genes", curie=CULTUREMECH.curie('genes'),
                   model_uri=CULTUREMECH.cofactorRequirement__genes, domain=None, range=Optional[Union[str, list[str]]])

slots.transporterAnnotation__name = Slot(uri=CULTUREMECH.name, name="transporterAnnotation__name", curie=CULTUREMECH.curie('name'),
                   model_uri=CULTUREMECH.transporterAnnotation__name, domain=None, range=str)

slots.transporterAnnotation__transporter_type = Slot(uri=CULTUREMECH.transporter_type, name="transporterAnnotation__transporter_type", curie=CULTUREMECH.curie('transporter_type'),
                   model_uri=CULTUREMECH.transporterAnnotation__transporter_type, domain=None, range=Union[str, "TransporterTypeEnum"])

slots.transporterAnnotation__substrates = Slot(uri=CULTUREMECH.substrates, name="transporterAnnotation__substrates", curie=CULTUREMECH.curie('substrates'),
                   model_uri=CULTUREMECH.transporterAnnotation__substrates, domain=None, range=Optional[Union[str, list[str]]])

slots.transporterAnnotation__substrate_terms = Slot(uri=CULTUREMECH.substrate_terms, name="transporterAnnotation__substrate_terms", curie=CULTUREMECH.curie('substrate_terms'),
                   model_uri=CULTUREMECH.transporterAnnotation__substrate_terms, domain=None, range=Optional[Union[dict[Union[str, ChemicalEntityTermId], Union[dict, ChemicalEntityTerm]], list[Union[dict, ChemicalEntityTerm]]]])

slots.transporterAnnotation__direction = Slot(uri=CULTUREMECH.direction, name="transporterAnnotation__direction", curie=CULTUREMECH.curie('direction'),
                   model_uri=CULTUREMECH.transporterAnnotation__direction, domain=None, range=Optional[str])

slots.transporterAnnotation__genes = Slot(uri=CULTUREMECH.genes, name="transporterAnnotation__genes", curie=CULTUREMECH.curie('genes'),
                   model_uri=CULTUREMECH.transporterAnnotation__genes, domain=None, range=Optional[Union[str, list[str]]])

slots.transporterAnnotation__ec_number = Slot(uri=CULTUREMECH.ec_number, name="transporterAnnotation__ec_number", curie=CULTUREMECH.curie('ec_number'),
                   model_uri=CULTUREMECH.transporterAnnotation__ec_number, domain=None, range=Optional[str])

slots.transporterAnnotation__notes = Slot(uri=CULTUREMECH.notes, name="transporterAnnotation__notes", curie=CULTUREMECH.curie('notes'),
                   model_uri=CULTUREMECH.transporterAnnotation__notes, domain=None, range=Optional[str])

slots.ChemicalEntityTerm_id = Slot(uri=CULTUREMECH.id, name="ChemicalEntityTerm_id", curie=CULTUREMECH.curie('id'),
                   model_uri=CULTUREMECH.ChemicalEntityTerm_id, domain=ChemicalEntityTerm, range=Union[str, ChemicalEntityTermId],
                   pattern=re.compile(r'^CHEBI:\d+$'))

slots.OrganismTerm_id = Slot(uri=CULTUREMECH.id, name="OrganismTerm_id", curie=CULTUREMECH.curie('id'),
                   model_uri=CULTUREMECH.OrganismTerm_id, domain=OrganismTerm, range=Union[str, OrganismTermId],
                   pattern=re.compile(r'^NCBITaxon:\d+$'))


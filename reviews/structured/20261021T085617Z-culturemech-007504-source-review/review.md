# Source and formulation review: 915 (CultureMech:007504)

- Review: 20261021T085617Z-culturemech-007504-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T08:49:02Z
- Finished UTC: 2026-10-21T08:56:17Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

NBRC 913 Casamino acids-peptone-Czapek’s agar is resolved by import provenance and the maintained owner despite local name 915. The generated target loses all nine recovered source rows in a collapsed table plus an empty ingredient and retains unsupported default preparation. The owner preserves both heptahydrates and the 10 mg iron sulfate amount, but two canonical labels need correction. The exact source supplies no pH or detailed sterilization protocol. All four diagnostics pass without establishing usable formulation semantics.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 120; batch 012 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding eleven task batches contain 110 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 112 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007504 | data/merge_yaml/merged/915.yaml | generated | 915 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007504 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007504 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch012/120/strict.tsv |
| validate-terms | passed | True | CultureMech:007504 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007504 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007504 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Scoped history timestamp syntax and timezone check | passed | False | CultureMech:007504 | 14 timestamp instances inspected; 0 malformed or timezone-naive instances. Existing provenance is preserved; no timestamps were rewritten. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007504.

The four documented recipes completed; interpret the scope of each separately.

### NBRC 913 provenance despite local 915 label

identity: supported. Targets: CultureMech:007504.

The stable CultureMech ID, merge source basename, import-history accession 913, maintained owner source term and captured primary page resolve one medium. The local name 915 does not license substitution of actual NBRC 915; that different source is only an identity countercheck. The legacy HTTP import URL was read as provenance, not represented as a newly retrieved response.

### Every target row and every recovered source amount

quantity: concern. Targets: CultureMech:007504.

The target has two malformed direct ingredient rows: one collapsed table at VARIABLE and an empty name with 'Casamino Acids (Difco)' as its g/L value. The 9 separate owner rows preserve the inspected source amounts and units as itemized. Solid masses expressed by the owner per liter are interpreted on the nominal listed recipe basis, without claiming that a source water amount establishes measured final volume.

[{"owner_field": "ingredients[0].concentration", "name": "Casamino Acids (Difco)", "owner_value": "1", "owner_unit": "G_PER_L", "source_amount": "1", "source_unit": "g", "source_quote": "Casamino Acids (Difco) 1 g", "source_locator": "Medium Composition quantified row 1", "condition": "Named complex acid hydrolysate; supplier identity preserved.", "decision": "verified", "decision_rationale": "Source amount verified on the nominal batch basis; final volume is not independently established.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-1"}, {"owner_field": "ingredients[1].concentration", "name": "Bacto Peptone (Difco)", "owner_value": "2", "owner_unit": "G_PER_L", "source_amount": "2", "source_unit": "g", "source_quote": "Bacto Peptone (Difco) 2 g", "source_locator": "Medium Composition quantified row 2", "condition": "Source commercial peptone retained; ontology class does not enumerate its composition.", "decision": "verified", "decision_rationale": "Source amount verified on the nominal batch basis; final volume is not independently established.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-2"}, {"owner_field": "ingredients[2].concentration", "name": "K2HPO4", "owner_value": "1", "owner_unit": "G_PER_L", "source_amount": "1", "source_unit": "g", "source_quote": "K 2 HPO 4 1 g", "source_locator": "Medium Composition quantified row 3", "condition": "Dipotassium hydrogen phosphate as stated; no hydrate addition or substitution.", "decision": "verified", "decision_rationale": "Source amount verified on the nominal batch basis; final volume is not independently established.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-3"}, {"owner_field": "ingredients[3].concentration", "name": "KCl", "owner_value": "0.5", "owner_unit": "G_PER_L", "source_amount": "0.5", "source_unit": "g", "source_quote": "KCl 0.5 g", "source_locator": "Medium Composition quantified row 4", "condition": "Potassium chloride as stated.", "decision": "verified", "decision_rationale": "Source amount verified on the nominal batch basis; final volume is not independently established.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-4"}, {"owner_field": "ingredients[4].concentration", "name": "MgSO4·7H2O", "owner_value": "0.5", "owner_unit": "G_PER_L", "source_amount": "0.5", "source_unit": "g", "source_quote": "MgSO 4 ·7H 2 O 0.5 g", "source_locator": "Medium Composition quantified row 5", "condition": "Magnesium sulfate heptahydrate; preserve seven waters of hydration.", "decision": "verified", "decision_rationale": "Source amount verified on the nominal batch basis; final volume is not independently established.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-5"}, {"owner_field": "ingredients[5].concentration", "name": "FeSO4·7H2O", "owner_value": "10", "owner_unit": "MG_PER_L", "source_amount": "10", "source_unit": "mg", "source_quote": "FeSO 4 ·7H 2 O 10 mg", "source_locator": "Medium Composition quantified row 6", "condition": "Iron(II) sulfate heptahydrate in milligrams, not grams; no anhydrous molar conversion.", "decision": "verified", "decision_rationale": "Source amount verified on the nominal batch basis; final volume is not independently established.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-6"}, {"owner_field": "ingredients[6].concentration", "name": "Sucrose", "owner_value": "30", "owner_unit": "G_PER_L", "source_amount": "30", "source_unit": "g", "source_quote": "Sucrose 30 g", "source_locator": "Medium Composition quantified row 7", "condition": "Source sucrose mass retained.", "decision": "verified", "decision_rationale": "Source amount verified on the nominal batch basis; final volume is not independently established.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-7"}, {"owner_field": "ingredients[7].concentration", "name": "Agar", "owner_value": "15", "owner_unit": "G_PER_L", "source_amount": "15", "source_unit": "g", "source_quote": "Agar 15 g", "source_locator": "Medium Composition quantified row 8", "condition": "Unconditional agar amount in this exact source.", "decision": "verified", "decision_rationale": "Source amount verified on the nominal batch basis; final volume is not independently established.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-8"}, {"owner_field": "ingredients[8].concentration", "name": "Distilled water", "owner_value": "1", "owner_unit": "L", "source_amount": "1", "source_unit": "L", "source_quote": "Distilled water 1 L", "source_locator": "Medium Composition quantified row 9", "condition": "Literal solvent amount; not a mass or an independently stated final volume.", "decision": "verified", "decision_rationale": "Literal liquid amount verified; no mass conversion is asserted.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-9"}]

### All asserted primary IDs, canonical labels and current secondary keys

grounding: concern. Targets: CultureMech:007504.

The generated target has 0/2 primary ontology links and 0/2 secondary links. The owner has 8/9 primary ontology links, including 7 CHEBI instances, and 0/9 verified secondary links. 2 owner primary labels differ from canonical labels. These are separate layer-specific linkage denominators on a 0–100 scale, not scientific accuracy scores. No secondary denominator of zero is invented when no keys are asserted.

{"counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances": 0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent": 0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 9, "primary_ontology_instances": 8, "primary_CHEBI_instances": 7, "canonical_primary_label_instances": 6, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent": 88.89, "primary_CHEBI_percent": 77.78, "secondary_verified_percent": 0.0}}, "label_drift": [{"field_path": "ingredients[1].term.label", "id": "MICRO:0000178", "asserted_label": "Bacto peptone", "canonical_label": "peptone", "source_key": "micro0000178"}, {"field_path": "ingredients[5].term.label", "id": "CHEBI:75836", "asserted_label": "FeSO4 x 7 H2O", "canonical_label": "iron(2+) sulfate heptahydrate", "source_key": "chebi75836"}], "instances": [{"layer": "target", "path": "data/merge_yaml/merged/915.yaml", "field": "ingredients[0]", "preferred_term": "Casamino Acids (Difco)1gBacto Peptone (Difco)2gK2HPO41gKCl0.5gMgSO4·7H2O0.5gFeSO4·7H2O10mgSucrose30gAgar15gDistilled water1L"}, {"layer": "target", "path": "data/merge_yaml/merged/915.yaml", "field": "ingredients[1]", "preferred_term": ""}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "ingredients[0]", "preferred_term": "Casamino Acids (Difco)"}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "ingredients[1]", "preferred_term": "Bacto Peptone (Difco)", "primary_id": "MICRO:0000178", "asserted_label": "Bacto peptone", "canonical_label": "peptone", "label_equal": false, "source_key": "micro0000178", "description": [], "synonyms": [], "form_annotations": {"createdBy": ["Carrine Blank"], "definition": ["An enzymatic digest of animal (mammalian) protein (of unspecified orgin), used for the culturing of microorganisms."], "definition source": ["From BD Bionutrients Technical Manual (3rd edition revised).:\n\nBacto™ Peptone is an enzymatic digest of animal protein. Bacto Peptone was first introduced in 1914 and became the standard Peptone for the preparation of bacteriological culture media. The nutritive value of Bacto Peptone is largely dependent on the amino acid content that supplies essential nitrogen. Bacto Peptone contains only a negligible quantity of proteoses and more complex constituents.\n\nAsh content is 6.9%\nNaCl content is 1.7%"], "has_exact_synonym": ["Bacto Peptone", "Bacto-peptone", "bacterial peptone", "peptones"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "ingredients[2]", "preferred_term": "K2HPO4", "primary_id": "CHEBI:131527", "asserted_label": "dipotassium hydrogen phosphate", "canonical_label": "dipotassium hydrogen phosphate", "label_equal": true, "source_key": "chebi131527", "description": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433", "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula": ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "ingredients[3]", "preferred_term": "KCl", "primary_id": "CHEBI:32588", "asserted_label": "potassium chloride", "canonical_label": "potassium chloride", "label_equal": true, "source_key": "chebi32588", "description": ["A metal chloride salt with a K(+) counterion."], "synonyms": ["KCl", "Kaliumchlorid", "Kaon-Cl 10", "Klor-con", "Klotrix", "Monopotassium chloride", "[KCl]", "muriate of potash", "potassium chloride", "potassium chloride", "sylvite"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:7447-40-7", "drugbank:DB00761", "kegg.drug:D02060", "metacyc.compound:KCL", "molbase:881", "reaxys:3534978", "wikipedia.en:Potassium_Chloride"], "generalized_empirical_formula": ["Cl.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32588"], "inchi_key_string": ["WCUXLLCKKVVCTQ-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "monoisotopic_mass": ["73.93256"], "smiles_string": ["[Cl-].[K+]"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "ingredients[4]", "preferred_term": "MgSO4·7H2O", "primary_id": "CHEBI:31795", "asserted_label": "magnesium sulfate heptahydrate", "canonical_label": "magnesium sulfate heptahydrate", "label_equal": true, "source_key": "chebi31795", "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505", "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222", "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"], "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "ingredients[5]", "preferred_term": "FeSO4·7H2O", "primary_id": "CHEBI:75836", "asserted_label": "FeSO4 x 7 H2O", "canonical_label": "iron(2+) sulfate heptahydrate", "label_equal": false, "source_key": "chebi75836", "description": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O", "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "ingredients[6]", "preferred_term": "Sucrose", "primary_id": "CHEBI:17992", "asserted_label": "sucrose", "canonical_label": "sucrose", "label_equal": true, "source_key": "chebi17992", "description": ["A glycosyl glycoside formed by glucose and fructose units joined by an acetal oxygen bridge from hemiacetal of glucose to the hemiketal of the fructose."], "synonyms": ["1-alpha-D-Glucopyranosyl-2-beta-D-fructofuranoside", "Cane sugar", "SUCROSE", "Saccharose", "Sacharose", "Sucrose", "White sugar", "beta-D-Fruf-(2&lt;-&gt;1)-alpha-D-Glcp", "beta-D-fructofuranosyl alpha-D-glucopyranoside", "beta-D-fructofuranosyl alpha-D-glucopyranoside", "sacarosa", "sucrose", "table sugar"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:57-50-1", "drugbank:DB02772", "drugcentral:4610", "gmelin:97695", "hmdb:HMDB0000258", "kegg.compound:C00089", "kegg.drug:D00025", "kegg.drug:D06533", "kegg.glycan:G00370", "knapsack:C00001151", "metacyc.compound:SUCROSE", "pdb-ccd:SUC", "pubmed:11021636", "pubmed:11093712", "pubmed:11111003", "pubmed:12065720", "pubmed:12706980", "pubmed:13508893", "pubmed:15291457", "pubmed:15660210", "pubmed:15792978", "pubmed:15845855", "pubmed:16228482", "pubmed:16304615", "pubmed:16313996", "pubmed:16525719", "pubmed:16660545", "pubmed:16663947", "pubmed:16665852", "pubmed:17233733", "pubmed:17439666", "pubmed:17597061", "pubmed:18625236", "pubmed:19199566", "pubmed:19726178", "pubmed:21703290", "pubmed:21972845", "pubmed:22085755", "pubmed:22311778", "pubmed:22404833", "pubmed:22751876", "reaxys:1435311", "reaxys:90825", "wikipedia.en:Sucrose"], "generalized_empirical_formula": ["C12H22O11"], "has_alternative_id": ["CHEBI:15128", "CHEBI:26812", "CHEBI:45795", "CHEBI:9314"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17992"], "inchi_key_string": ["CZMRCDWAGMRECN-UGDNZRGBSA-N"], "inchi_string": ["InChI=1S/C12H22O11/c13-1-4-6(16)8(18)9(19)11(21-4)23-12(3-15)10(20)7(17)5(2-14)22-12/h4-11,13-20H,1-3H2/t4-,5-,6-,7-,8+,9-,10+,11-,12+/m1/s1"], "mass": ["342.297"], "monoisotopic_mass": ["342.11621"], "smiles_string": ["OC[C@H]1O[C@@](CO)(O[C@H]2O[C@H](CO)[C@@H](O)[C@H](O)[C@H]2O)[C@@H](O)[C@@H]1O"], "wurcs_representation": ["WURCS=2.0/2,2,1/[a2122h-1a_1-5][ha122h-2b_2-5]/1-2/a1-b2"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "ingredients[7]", "preferred_term": "Agar", "primary_id": "CHEBI:2509", "asserted_label": "agar", "canonical_label": "agar", "label_equal": true, "source_key": "chebi2509", "description": ["A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties."], "synonyms": [], "form_annotations": {"database_cross_reference": ["cas:9002-18-0", "kegg.compound:C08815", "pubmed:25603143", "pubmed:25842535", "pubmed:25959629", "pubmed:26043937", "pubmed:26050892", "pubmed:26116384", "reaxys:8538728", "wikipedia.en:Agar"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:2509"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "ingredients[8]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_equal": true, "source_key": "chebi15377", "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5", "gmelin:117", "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001", "metacyc.compound:WATER", "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"], "generalized_empirical_formula": ["H2O"], "has_alternative_id": ["CHEBI:10743", "CHEBI:13352", "CHEBI:27313", "CHEBI:42043", "CHEBI:42857", "CHEBI:43228", "CHEBI:44292", "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15377"], "inchi_key_string": ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "monoisotopic_mass": ["18.01056"], "smiles_string": ["[H]O[H]"]}}]}

### Source ingredient identities, mixtures and exact chemical forms

grounding: supported. Targets: CultureMech:007504.

The seven owner CHEBI identities cover dipotassium hydrogen phosphate, potassium chloride, magnesium sulfate heptahydrate, iron(2+) sulfate heptahydrate, sucrose, agar and water. Hydration annotations explicitly agree with the two source heptahydrates. MICRO:0000178 is canonically peptone; its annotation includes Bacto Peptone as an exact synonym and an enzymatic animal-protein digest definition, supporting the source mixture identity at that scope. The Bacto and iron sulfate labels need canonicalization without changing their identities or amounts. Casamino Acids remains ungrounded rather than assigned an invented molecular term.

### Preparation, pH and physical-state conditions

consistency: concern. Targets: CultureMech:007504.

Both target and owner lack a source-supported pH, matching the source’s silence; no arbitrary pH is proposed. Source agar is unconditional. The owner leaves preparation empty. The target instead asserts generic dissolve, adjust-pH and autoclaving steps; Sterilize by autoclaving is tagged DISSOLVE and lacks support in the exact source. Do not import source 915 filtration or pH conditions.

### Classification and bounded biological claims

scope: supported. Targets: CultureMech:007504.

COMPLEX/UNDEFINED is consistent with Casamino Acids and Bacto Peptone, while the specified 15 g agar supports SOLID_AGAR. Opaque commercial ingredients remain mixtures despite ontology linkage. Neither target nor owner asserts organisms, strains, taxon IDs, assemblies, DOI/PMID papers, growth outcomes, parent media or variants. Source catalogue scope is not experimental growth evidence. Optional omissions are not populated with invented organisms.

### Maintained recovery versus generated representation

ownership: concern. Targets: CultureMech:007504.

The generated August merge precedes later owner recovery and source metadata. The owner now contains 9 explicit source rows and an official source term/reference; the target retains two collapsed rows and no structured source term/reference. Owner label differences must be corrected before regeneration. The nine owner rows include eight primary ontology links, seven of them CHEBI, with no asserted secondary keys. The owner already carries the official source name and reference; its description still preserves the local 915 versus actual 913 import distinction.

### Claim-level amount evidence and checked reference scope

evidence: concern. Targets: CultureMech:007504.

Each source amount is traced to an exact table row above. The owner has the official recipe reference but lacks ingredient-level amount evidence; the target has no structured reference and its reference checker checked zero entries. Add scoped amount evidence while recovering the structured formulation, retaining source batch and condition qualifiers. Ontology citations verify identities and labels rather than recipe amounts. No separate paper was asserted or required to identify this catalogue recipe.

### Append-only event history and timestamp interpretation

provenance: supported. Targets: CultureMech:007504.

All 14 scoped timestamps were checked for ISO syntax and timezone. Every instance parses and has an explicit timezone. Curation events are process provenance rather than independent confirmation of recipe correctness.

[]

### Iron sulfate milligram scale and solvent volume

quantity: supported. Targets: CultureMech:007504.

The source and owner agree on FeSO4·7H2O at 10 mg on the nominal recipe basis; 10 mg equals 0.010 g, not 10 g. The 0.5 g magnesium sulfate is also explicitly the heptahydrate. Water remains 1 L as a volume. No molarity, density or final post-dissolution volume is assumed.

## Findings

### f1: Generated target loses the recovered 9-row NBRC 913 formula

blocker / open / confirmed; issue key: cm007504-stale-collapsed-source913-formula.

The whole-table ingredient string at VARIABLE and the empty ingredient with a reagent name as a g/L value cannot represent a usable named formulation. The owner already has 9 explicit source rows and the official source accession/reference, with source conditions where stated. This prevents faithful scientific use of the generated formulation despite all four documented checks passing. Native P1 reflects unusable identity/representation; this is not P1.1 and is not a reported schema-validator failure.

### f2: Generated autoclaving is unsupported and action-mismatched

major / open / confirmed; issue key: cm007504-unsupported-default-autoclave.

The inspected exact NBRC 913 page does not provide a sterilization protocol. The target nevertheless states Sterilize by autoclaving with action DISSOLVE, matching the importer fallback and keyword mismatch. The current owner has already removed that generic autoclaving instruction; the stale generated instruction should not be reintroduced as primary-source evidence. Neither a neighboring accession nor a routine laboratory convention supplies missing source-specific support.

### f3: Maintained owner labels differ from canonical ontology labels

minor / open / confirmed; issue key: cm007504-owner-canonical-label-drift.

[{"field_path": "ingredients[1].term.label", "id": "MICRO:0000178", "asserted_label": "Bacto peptone", "canonical_label": "peptone", "source_key": "micro0000178"}, {"field_path": "ingredients[5].term.label", "id": "CHEBI:75836", "asserted_label": "FeSO4 x 7 H2O", "canonical_label": "iron(2+) sulfate heptahydrate", "source_key": "chebi75836"}] These are literal label differences in the maintained input and would propagate on regeneration. They do not by themselves prove that the asserted ontology IDs identify the wrong substances; preserve supplier/source names in preferred_term and exact recipe forms separately.

## Recommended Actions And Acceptance Checks

### a1

Verify the maintained source rows and their exact forms/units against the bound primary page, correct owner label or classification issues listed separately, add scoped amount evidence, and regenerate derived records while retaining the same stable ID and source accession.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain supported source pH/formulation details and regenerate from the verified owner without the unsupported default. Any later sterilization instruction needs exact source support and a corresponding action; keep unknown time, temperature and procedure explicit.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Update only the canonical term labels after verifying the same IDs and source-specific ingredient identities. Preserve source names, brands, supplied hydration forms and amounts, then ensure regeneration keeps both canonical labels and preferred terms. Run the documented ID-label correspondence check on the authorized correction.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/915.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_915.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/915.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/915.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch012/120/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch012/120/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/915.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/915.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| nbrc913 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913; Medium No. header; complete Medium Composition table, footnotes and Comment section | supports | Read the full official NBRC 913 Casamino acids-peptone-Czapek agar page: nine quantified source rows including magnesium sulfate heptahydrate 0.5 g and iron sulfate heptahydrate 10 mg. No pH, autoclaving protocol or other detailed preparation is stated. |
| nbrc915 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=915; Medium No. header, complete composition and preparation; identity countercheck only | context_only | Actual NBRC 915 contains Bacto Tryptone, yeast extract, calcium chloride and rifampicin/spectinomycin stocks, with pH 7.0 and separate filtration instructions. It is a different medium; its antibiotic stocks and preparation are not part of source 913. |
| amount-1 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913; Medium Composition table, quantified row 1: Casamino Acids (Difco) | supports | Exact source amount for owner ingredients[0].concentration; Named complex acid hydrolysate; supplier identity preserved. Source value and unit are 1 g. The target retains this only inside its collapsed table string. |
| amount-2 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913; Medium Composition table, quantified row 2: Bacto Peptone (Difco) | supports | Exact source amount for owner ingredients[1].concentration; Source commercial peptone retained; ontology class does not enumerate its composition. Source value and unit are 2 g. The target retains this only inside its collapsed table string. |
| amount-3 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913; Medium Composition table, quantified row 3: K 2 HPO 4 | supports | Exact source amount for owner ingredients[2].concentration; Dipotassium hydrogen phosphate as stated; no hydrate addition or substitution. Source value and unit are 1 g. The target retains this only inside its collapsed table string. |
| amount-4 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913; Medium Composition table, quantified row 4: KCl | supports | Exact source amount for owner ingredients[3].concentration; Potassium chloride as stated. Source value and unit are 0.5 g. The target retains this only inside its collapsed table string. |
| amount-5 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913; Medium Composition table, quantified row 5: MgSO 4 ·7H 2 O | supports | Exact source amount for owner ingredients[4].concentration; Magnesium sulfate heptahydrate; preserve seven waters of hydration. Source value and unit are 0.5 g. The target retains this only inside its collapsed table string. |
| amount-6 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913; Medium Composition table, quantified row 6: FeSO 4 ·7H 2 O | supports | Exact source amount for owner ingredients[5].concentration; Iron(II) sulfate heptahydrate in milligrams, not grams; no anhydrous molar conversion. Source value and unit are 10 mg. The target retains this only inside its collapsed table string. |
| amount-7 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913; Medium Composition table, quantified row 7: Sucrose | supports | Exact source amount for owner ingredients[6].concentration; Source sucrose mass retained. Source value and unit are 30 g. The target retains this only inside its collapsed table string. |
| amount-8 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913; Medium Composition table, quantified row 8: Agar | supports | Exact source amount for owner ingredients[7].concentration; Unconditional agar amount in this exact source. Source value and unit are 15 g. The target retains this only inside its collapsed table string. |
| amount-9 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913; Medium Composition table, quantified row 9: Distilled water | supports | Exact source amount for owner ingredients[8].concentration; Literal solvent amount; not a mass or an independently stated final volume. Source value and unit are 1 L. The target retains this only inside its collapsed table string. |
| micro0000178 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | MICRO:0000178 resolves to canonical label peptone and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:131527 resolves to canonical label dipotassium hydrogen phosphate and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:32588 resolves to canonical label potassium chloride and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:31795 resolves to canonical label magnesium sulfate heptahydrate and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:75836 resolves to canonical label iron(2+) sulfate heptahydrate and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| chebi17992 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17992; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:17992 resolves to canonical label sucrose and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:2509 resolves to canonical label agar and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:15377 resolves to canonical label water and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact MAPPED/preferred_term rows for each asserted secondary key; adjacent pinned metadata | supports | {"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count": 9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id", "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"}, "counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances": 0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent": 0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 9, "primary_ontology_instances": 8, "primary_CHEBI_instances": 7, "canonical_primary_label_instances": 6, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent": 88.89, "primary_CHEBI_percent": 77.78, "secondary_verified_percent": 0.0}}, "secondary_instances": []} |
| importer | src/culturemech/import/nbrc_importer.py; _map_ingredients; _map_preparation_steps; _infer_medium_type | context_only | Current importer maps quantities mechanically and creates generic dissolve, adjust-pH and autoclaving prose when preparation text is absent. Its action test uses the substring autoclave, which is not present in autoclaving, explaining the generated DISSOLVE action. The classification heuristic can use parentheses as a defined-medium hint. Code inspection is not a historical execution replay. |
| recovery | scripts/recover_nbrc_composition.py; parse_composition; recover | context_only | Current recovery code parses explicit composition rows and separate footnote stock sections from #medium-comp and records recovery history. Its presence and later owner data do not prove the generated merged record was regenerated. |
| exporter | src/culturemech/export/kgx_export.py; transform; medium_to_ingredient_edge; _resolved_ingredient_id; nodes | context_only | The current exporter walks structured ingredient rows and uses a MIM resolver before local identity fallback; it returns no ingredient edge if resolution yields no identity. A missing explicit term alone does not establish a zero-edge export. No export was executed or edge count asserted. The record type is also consumed for node/type semantics, so source-unsupported classification is consequential. |
| history | data/merge_yaml/merged/915.yaml; Every timestamp in target, owner and explicitly listed contextual dependencies | supports | [{"path": "data/merge_yaml/merged/915.yaml", "field": "curation_history[0].timestamp", "value": "2026-02-20T00:22:35.987896Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/915.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-13T03:09:00.219545Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/915.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-13T06:19:49.281640Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/915.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/915.yaml", "field": "curation_history[4].timestamp", "value": "2026-05-16T09:03:06.744708+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/915.yaml", "field": "curation_history[5].timestamp", "value": "2026-08-06T03:05:04.698210+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[0].timestamp", "value": "2026-02-20T00:22:35.987896Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-13T03:09:00.219545Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-13T06:19:49.281640Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[4].timestamp", "value": "2026-05-16T09:03:06.744708+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[5].timestamp", "value": "2026-08-19T21:54:23.057496+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[6].timestamp", "value": "2026-08-20T19:01:16.137919+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[7].timestamp", "value": "2026-09-08T00:00:00-07:00", "valid_ISO_datetime": true, "timezone_aware": true}] |

## Limits And Additional Notes

- Source masses and 1 L distilled water are assessed on the nominal catalogue recipe basis. The page does not establish measured final volume, and no solvent mass or molar conversion is inferred.
- The exact source 913 page gives no pH, sterilization parameters, incubation conditions or storage procedure. These remain unquantified rather than being copied from actual source 915.
- Casamino Acids and Bacto Peptone retain their source-specific commercial mixture names. No supplier formulation, organism growth claim or pure-molecule substitute was invented.
- The historical owner repair event is provenance. No missing historical writer was reconstructed or executed, and the similarly numbered current antibiotic-medium repair writer was not treated as this owner’s authority.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T085617Z-culturemech-007504-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 915 (CultureMech:007504)'
started_at: '2026-10-21T08:49:02Z'
finished_at: '2026-10-21T08:56:17Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the assessed recipe bytes.
    This is an independent agent review of captured local inputs and inspected primary/database
    sources, not experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: NBRC 913 Casamino acids-peptone-Czapek’s agar is resolved by import provenance
  and the maintained owner despite local name 915. The generated target loses all
  nine recovered source rows in a collapsed table plus an empty ingredient and retains
  unsupported default preparation. The owner preserves both heptahydrates and the
  10 mg iron sulfate amount, but two canonical labels need correction. The exact source
  supplies no pH or detailed sterilization protocol. All four diagnostics pass without
  establishing usable formulation semantics.
source:
  git_revision: 24a1d277eb7f0437af53af0d178a30f9bfa6374c
  state: working_tree
  inputs:
  - path: .claude/skills/audit-schema-gaps/SKILL.md
    sha256: 86467f280ecdd2d60531d3b2a9249d7a38efa4cfeab714d55421b9a62cfabb7d
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
    role: context
  - path: .claude/skills/review-ingredient-concentrations/references/evidence-contract.md
    sha256: 5eb4783f02a0567b45b462dfb5e8c0393fb34daf842a3ce23ff7946652f157d1
    role: context
  - path: .claude/skills/review-recipes/reference/linkage-and-duplicates.md
    sha256: e792d47f2b9e169d2306ac920f87aa1ced9b9d07c7650dd7d2feb7aee48c2234
    role: context
  - path: .claude/skills/review-recipes/reference/validation-rules.md
    sha256: 3b8666d58fc0c9deb02981053a50760a937675e6e22a6ecd53e92678e8d422f0
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: e3f1aeccd3d249f78739c902ea8d95052fec26fc5db752b5ca732d96ab37e466
    role: context
  - path: .claude/skills/schema-gap-analysis/SKILL.md
    sha256: 09665fe53584559e776f75ab41dfabd997eff0cac10bafcca0a721b678ccee93
    role: context
  - path: AGENTS.md
    sha256: 72737a531548de8636bcf70b972e71a7630a0e579215b6ded392d88d1b51a4fc
    role: context
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/oak_config.yaml
    sha256: e35781d4fd66de4289411141b4c8a94189782d864ba6c45e49bf46537c46c5a1
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/915.yaml
    sha256: 39f8ec00f03a141c68b5a67be679aa028eaa5aa6649a87e601301da3100f0b9c
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_915.yaml
    sha256: 903acf58833ada39a82f65116a6c85dcbe0cf859211427b33e4dda5d3c4cbe80
    role: context
  - path: docs/DATA_LAYERS.md
    sha256: 381cbb9ad2ba80f2a849507c4ce8b10839546ae4ce2757dad065e86fe381d236
    role: context
  - path: docs/record-review-profile.md
    sha256: 99eebe27f0079cb816c974f58ee457148da5a3c346ec9c30ff853b95dade9127
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 552166976136ed158a253773f0b763e670d2484e7354b48ec0f9b77b4250da77
    role: context
  - path: project.justfile
    sha256: 3576f5ce2adee0179be4f2d3fd134841249eb9a54a7eed8b388c3b345883a5fe
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/recover_nbrc_composition.py
    sha256: a723e458895350a68ffae3e446006205b2e00cb185bee13976d5047be56405f0
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/nbrc_raw_yaml.py
    sha256: de5654d4eed2e01a2383dcf417b7d8e2779dbb622de9351c28373fb691812ec1
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/fetch/nbrc_scraper.py
    sha256: 5c5bbda489abe0b6d000b9318a76913ab5496ee83aff58b530c2b42b5989d1e3
    role: context
  - path: src/culturemech/import/nbrc_importer.py
    sha256: 857b7e0ac88aef783ce4bc9b35c4c6a3d9fc38824a5d463010a6046ac4180924
    role: context
  - path: src/culturemech/merge/fingerprint.py
    sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
    role: context
  - path: src/culturemech/merge/formulation.py
    sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
    role: context
  - path: src/culturemech/merge/matcher.py
    sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
    role: context
  - path: src/culturemech/merge/merge_recipes.py
    sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 120; batch 012 item 10 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding eleven task batches contain
    110 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 112 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007504
targets:
- target_id: CultureMech:007504
  path: data/merge_yaml/merged/915.yaml
  label: '915'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_915.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/915.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/915.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch012/120/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch012/120/strict.tsv"
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/915.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/915.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - validate-references
- check_id: structured-source-adapter
  name: iModulonDB applicability
  required: false
  status: not_applicable
  summary: The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic
    dataset requiring an iModulonDB cross-check; expression-module membership cannot
    establish this formulation.
  target_ids:
  - CultureMech:007504
- check_id: scoped-history-timestamps
  name: Scoped history timestamp syntax and timezone check
  required: false
  status: passed
  summary: 14 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Existing provenance is preserved; no timestamps were rewritten.
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - history
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/915.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T08:56:17Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_915.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T08:56:17Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/915.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:49:54.551790Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/915.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch012/120/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T08:49:57.076980Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch012/120/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/915.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:50:03.403557Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/915.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:50:05.746457Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: nbrc913
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913
  locator: Medium No. header; complete Medium Composition table, footnotes and Comment
    section
  accessed_at: '2026-10-21T08:42:36.471214Z'
  support: supports
  summary: 'Read the full official NBRC 913 Casamino acids-peptone-Czapek agar page:
    nine quantified source rows including magnesium sulfate heptahydrate 0.5 g and
    iron sulfate heptahydrate 10 mg. No pH, autoclaving protocol or other detailed
    preparation is stated.'
  snapshot_sha256: a8225b61b1a90fa1cc294eec3ca36ae05f499833ad454362e71a4407fef274e9
- evidence_id: nbrc915
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=915
  locator: Medium No. header, complete composition and preparation; identity countercheck
    only
  accessed_at: '2026-10-21T08:42:37.083060Z'
  support: context_only
  summary: Actual NBRC 915 contains Bacto Tryptone, yeast extract, calcium chloride
    and rifampicin/spectinomycin stocks, with pH 7.0 and separate filtration instructions.
    It is a different medium; its antibiotic stocks and preparation are not part of
    source 913.
  snapshot_sha256: fb5233c25f8ebadb8f0c6e7702de4275b07692059b941cd365318e5eb3d0437c
- evidence_id: amount-1
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913
  locator: 'Medium Composition table, quantified row 1: Casamino Acids (Difco)'
  accessed_at: '2026-10-21T08:42:36.471214Z'
  support: supports
  summary: Exact source amount for owner ingredients[0].concentration; Named complex
    acid hydrolysate; supplier identity preserved. Source value and unit are 1 g.
    The target retains this only inside its collapsed table string.
  quote: Casamino Acids (Difco) 1 g
  snapshot_sha256: a8225b61b1a90fa1cc294eec3ca36ae05f499833ad454362e71a4407fef274e9
- evidence_id: amount-2
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913
  locator: 'Medium Composition table, quantified row 2: Bacto Peptone (Difco)'
  accessed_at: '2026-10-21T08:42:36.471214Z'
  support: supports
  summary: Exact source amount for owner ingredients[1].concentration; Source commercial
    peptone retained; ontology class does not enumerate its composition. Source value
    and unit are 2 g. The target retains this only inside its collapsed table string.
  quote: Bacto Peptone (Difco) 2 g
  snapshot_sha256: a8225b61b1a90fa1cc294eec3ca36ae05f499833ad454362e71a4407fef274e9
- evidence_id: amount-3
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913
  locator: 'Medium Composition table, quantified row 3: K 2 HPO 4'
  accessed_at: '2026-10-21T08:42:36.471214Z'
  support: supports
  summary: Exact source amount for owner ingredients[2].concentration; Dipotassium
    hydrogen phosphate as stated; no hydrate addition or substitution. Source value
    and unit are 1 g. The target retains this only inside its collapsed table string.
  quote: K 2 HPO 4 1 g
  snapshot_sha256: a8225b61b1a90fa1cc294eec3ca36ae05f499833ad454362e71a4407fef274e9
- evidence_id: amount-4
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913
  locator: 'Medium Composition table, quantified row 4: KCl'
  accessed_at: '2026-10-21T08:42:36.471214Z'
  support: supports
  summary: Exact source amount for owner ingredients[3].concentration; Potassium chloride
    as stated. Source value and unit are 0.5 g. The target retains this only inside
    its collapsed table string.
  quote: KCl 0.5 g
  snapshot_sha256: a8225b61b1a90fa1cc294eec3ca36ae05f499833ad454362e71a4407fef274e9
- evidence_id: amount-5
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913
  locator: 'Medium Composition table, quantified row 5: MgSO 4 ·7H 2 O'
  accessed_at: '2026-10-21T08:42:36.471214Z'
  support: supports
  summary: Exact source amount for owner ingredients[4].concentration; Magnesium sulfate
    heptahydrate; preserve seven waters of hydration. Source value and unit are 0.5
    g. The target retains this only inside its collapsed table string.
  quote: MgSO 4 ·7H 2 O 0.5 g
  snapshot_sha256: a8225b61b1a90fa1cc294eec3ca36ae05f499833ad454362e71a4407fef274e9
- evidence_id: amount-6
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913
  locator: 'Medium Composition table, quantified row 6: FeSO 4 ·7H 2 O'
  accessed_at: '2026-10-21T08:42:36.471214Z'
  support: supports
  summary: Exact source amount for owner ingredients[5].concentration; Iron(II) sulfate
    heptahydrate in milligrams, not grams; no anhydrous molar conversion. Source value
    and unit are 10 mg. The target retains this only inside its collapsed table string.
  quote: FeSO 4 ·7H 2 O 10 mg
  snapshot_sha256: a8225b61b1a90fa1cc294eec3ca36ae05f499833ad454362e71a4407fef274e9
- evidence_id: amount-7
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913
  locator: 'Medium Composition table, quantified row 7: Sucrose'
  accessed_at: '2026-10-21T08:42:36.471214Z'
  support: supports
  summary: Exact source amount for owner ingredients[6].concentration; Source sucrose
    mass retained. Source value and unit are 30 g. The target retains this only inside
    its collapsed table string.
  quote: Sucrose 30 g
  snapshot_sha256: a8225b61b1a90fa1cc294eec3ca36ae05f499833ad454362e71a4407fef274e9
- evidence_id: amount-8
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913
  locator: 'Medium Composition table, quantified row 8: Agar'
  accessed_at: '2026-10-21T08:42:36.471214Z'
  support: supports
  summary: Exact source amount for owner ingredients[7].concentration; Unconditional
    agar amount in this exact source. Source value and unit are 15 g. The target retains
    this only inside its collapsed table string.
  quote: Agar 15 g
  snapshot_sha256: a8225b61b1a90fa1cc294eec3ca36ae05f499833ad454362e71a4407fef274e9
- evidence_id: amount-9
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=913
  locator: 'Medium Composition table, quantified row 9: Distilled water'
  accessed_at: '2026-10-21T08:42:36.471214Z'
  support: supports
  summary: Exact source amount for owner ingredients[8].concentration; Literal solvent
    amount; not a mass or an independently stated final volume. Source value and unit
    are 1 L. The target retains this only inside its collapsed table string.
  quote: Distilled water 1 L
  snapshot_sha256: a8225b61b1a90fa1cc294eec3ca36ae05f499833ad454362e71a4407fef274e9
- evidence_id: micro0000178
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T08:00:49.423450Z'
  support: supports
  summary: MICRO:0000178 resolves to canonical label peptone and is not obsolete.
    The complete response, including available formula, hydration, structure, synonyms
    and definitions, was inspected. Literal owner-label equality is assessed separately;
    ontology descriptions do not establish recipe quantities.
  snapshot_sha256: ef45aa186438f91d015280171fde8ccb25740a50cc6f2c6e848de6aad3339b31
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to canonical label dipotassium hydrogen phosphate
    and is not obsolete. The complete response, including available formula, hydration,
    structure, synonyms and definitions, was inspected. Literal owner-label equality
    is assessed separately; ontology descriptions do not establish recipe quantities.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to canonical label potassium chloride and is not obsolete.
    The complete response, including available formula, hydration, structure, synonyms
    and definitions, was inspected. Literal owner-label equality is assessed separately;
    ontology descriptions do not establish recipe quantities.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T08:17:28.683169Z'
  support: supports
  summary: CHEBI:31795 resolves to canonical label magnesium sulfate heptahydrate
    and is not obsolete. The complete response, including available formula, hydration,
    structure, synonyms and definitions, was inspected. Literal owner-label equality
    is assessed separately; ontology descriptions do not establish recipe quantities.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to canonical label iron(2+) sulfate heptahydrate and
    is not obsolete. The complete response, including available formula, hydration,
    structure, synonyms and definitions, was inspected. Literal owner-label equality
    is assessed separately; ontology descriptions do not establish recipe quantities.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi17992
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17992
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T08:42:31.913996Z'
  support: supports
  summary: CHEBI:17992 resolves to canonical label sucrose and is not obsolete. The
    complete response, including available formula, hydration, structure, synonyms
    and definitions, was inspected. Literal owner-label equality is assessed separately;
    ontology descriptions do not establish recipe quantities.
  snapshot_sha256: 509f9cbc014a0211d3a8e536a2c68048a090719ce68ee80550c8bbf532f150aa
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: CHEBI:2509 resolves to canonical label agar and is not obsolete. The complete
    response, including available formula, hydration, structure, synonyms and definitions,
    was inspected. Literal owner-label equality is assessed separately; ontology descriptions
    do not establish recipe quantities.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 resolves to canonical label water and is not obsolete. The
    complete response, including available formula, hydration, structure, synonyms
    and definitions, was inspected. Literal owner-label equality is assessed separately;
    ontology descriptions do not establish recipe quantities.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact MAPPED/preferred_term rows for each asserted secondary key; adjacent
    pinned metadata
  accessed_at: '2026-10-21T08:56:17Z'
  support: supports
  summary: '{"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count":
    9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id",
    "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech",
    "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5",
    "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"},
    "counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances":
    0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances":
    0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent":
    0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 9,
    "primary_ontology_instances": 8, "primary_CHEBI_instances": 7, "canonical_primary_label_instances":
    6, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent":
    88.89, "primary_CHEBI_percent": 77.78, "secondary_verified_percent": 0.0}}, "secondary_instances":
    []}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/nbrc_importer.py
  locator: _map_ingredients; _map_preparation_steps; _infer_medium_type
  accessed_at: '2026-10-21T08:56:17Z'
  support: context_only
  summary: Current importer maps quantities mechanically and creates generic dissolve,
    adjust-pH and autoclaving prose when preparation text is absent. Its action test
    uses the substring autoclave, which is not present in autoclaving, explaining
    the generated DISSOLVE action. The classification heuristic can use parentheses
    as a defined-medium hint. Code inspection is not a historical execution replay.
- evidence_id: recovery
  kind: record_content
  reference: scripts/recover_nbrc_composition.py
  locator: parse_composition; recover
  accessed_at: '2026-10-21T08:56:17Z'
  support: context_only
  summary: 'Current recovery code parses explicit composition rows and separate footnote
    stock sections from #medium-comp and records recovery history. Its presence and
    later owner data do not prove the generated merged record was regenerated.'
- evidence_id: exporter
  kind: record_content
  reference: src/culturemech/export/kgx_export.py
  locator: transform; medium_to_ingredient_edge; _resolved_ingredient_id; nodes
  accessed_at: '2026-10-21T08:56:17Z'
  support: context_only
  summary: The current exporter walks structured ingredient rows and uses a MIM resolver
    before local identity fallback; it returns no ingredient edge if resolution yields
    no identity. A missing explicit term alone does not establish a zero-edge export.
    No export was executed or edge count asserted. The record type is also consumed
    for node/type semantics, so source-unsupported classification is consequential.
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/915.yaml
  locator: Every timestamp in target, owner and explicitly listed contextual dependencies
  accessed_at: '2026-10-21T08:56:17Z'
  support: supports
  summary: '[{"path": "data/merge_yaml/merged/915.yaml", "field": "curation_history[0].timestamp",
    "value": "2026-02-20T00:22:35.987896Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/915.yaml", "field": "curation_history[1].timestamp",
    "value": "2026-03-13T03:09:00.219545Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/915.yaml", "field": "curation_history[2].timestamp",
    "value": "2026-03-13T06:19:49.281640Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/915.yaml", "field": "curation_history[3].timestamp",
    "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/915.yaml", "field": "curation_history[4].timestamp",
    "value": "2026-05-16T09:03:06.744708+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/915.yaml", "field": "curation_history[5].timestamp",
    "value": "2026-08-06T03:05:04.698210+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[0].timestamp",
    "value": "2026-02-20T00:22:35.987896Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[1].timestamp",
    "value": "2026-03-13T03:09:00.219545Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[2].timestamp",
    "value": "2026-03-13T06:19:49.281640Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[3].timestamp",
    "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[4].timestamp",
    "value": "2026-05-16T09:03:06.744708+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[5].timestamp",
    "value": "2026-08-19T21:54:23.057496+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[6].timestamp",
    "value": "2026-08-20T19:01:16.137919+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "curation_history[7].timestamp",
    "value": "2026-09-08T00:00:00-07:00", "valid_ISO_datetime": true, "timezone_aware":
    true}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: NBRC 913 provenance despite local 915 label
  outcome: supported
  summary: The stable CultureMech ID, merge source basename, import-history accession
    913, maintained owner source term and captured primary page resolve one medium.
    The local name 915 does not license substitution of actual NBRC 915; that different
    source is only an identity countercheck. The legacy HTTP import URL was read as
    provenance, not represented as a newly retrieved response.
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - record
  - owner-0
  - nbrc913
  - nbrc915
- assessment_id: amounts
  area: quantity
  topic: Every target row and every recovered source amount
  outcome: concern
  summary: 'The target has two malformed direct ingredient rows: one collapsed table
    at VARIABLE and an empty name with ''Casamino Acids (Difco)'' as its g/L value.
    The 9 separate owner rows preserve the inspected source amounts and units as itemized.
    Solid masses expressed by the owner per liter are interpreted on the nominal listed
    recipe basis, without claiming that a source water amount establishes measured
    final volume.'
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - record
  - owner-0
  - nbrc913
  - amount-1
  - amount-2
  - amount-3
  - amount-4
  - amount-5
  - amount-6
  - amount-7
  - amount-8
  - amount-9
  details: '[{"owner_field": "ingredients[0].concentration", "name": "Casamino Acids
    (Difco)", "owner_value": "1", "owner_unit": "G_PER_L", "source_amount": "1", "source_unit":
    "g", "source_quote": "Casamino Acids (Difco) 1 g", "source_locator": "Medium Composition
    quantified row 1", "condition": "Named complex acid hydrolysate; supplier identity
    preserved.", "decision": "verified", "decision_rationale": "Source amount verified
    on the nominal batch basis; final volume is not independently established.", "target_correspondence":
    "Embedded text only; no equivalent usable direct ingredient row", "evidence_id":
    "amount-1"}, {"owner_field": "ingredients[1].concentration", "name": "Bacto Peptone
    (Difco)", "owner_value": "2", "owner_unit": "G_PER_L", "source_amount": "2", "source_unit":
    "g", "source_quote": "Bacto Peptone (Difco) 2 g", "source_locator": "Medium Composition
    quantified row 2", "condition": "Source commercial peptone retained; ontology
    class does not enumerate its composition.", "decision": "verified", "decision_rationale":
    "Source amount verified on the nominal batch basis; final volume is not independently
    established.", "target_correspondence": "Embedded text only; no equivalent usable
    direct ingredient row", "evidence_id": "amount-2"}, {"owner_field": "ingredients[2].concentration",
    "name": "K2HPO4", "owner_value": "1", "owner_unit": "G_PER_L", "source_amount":
    "1", "source_unit": "g", "source_quote": "K 2 HPO 4 1 g", "source_locator": "Medium
    Composition quantified row 3", "condition": "Dipotassium hydrogen phosphate as
    stated; no hydrate addition or substitution.", "decision": "verified", "decision_rationale":
    "Source amount verified on the nominal batch basis; final volume is not independently
    established.", "target_correspondence": "Embedded text only; no equivalent usable
    direct ingredient row", "evidence_id": "amount-3"}, {"owner_field": "ingredients[3].concentration",
    "name": "KCl", "owner_value": "0.5", "owner_unit": "G_PER_L", "source_amount":
    "0.5", "source_unit": "g", "source_quote": "KCl 0.5 g", "source_locator": "Medium
    Composition quantified row 4", "condition": "Potassium chloride as stated.", "decision":
    "verified", "decision_rationale": "Source amount verified on the nominal batch
    basis; final volume is not independently established.", "target_correspondence":
    "Embedded text only; no equivalent usable direct ingredient row", "evidence_id":
    "amount-4"}, {"owner_field": "ingredients[4].concentration", "name": "MgSO4·7H2O",
    "owner_value": "0.5", "owner_unit": "G_PER_L", "source_amount": "0.5", "source_unit":
    "g", "source_quote": "MgSO 4 ·7H 2 O 0.5 g", "source_locator": "Medium Composition
    quantified row 5", "condition": "Magnesium sulfate heptahydrate; preserve seven
    waters of hydration.", "decision": "verified", "decision_rationale": "Source amount
    verified on the nominal batch basis; final volume is not independently established.",
    "target_correspondence": "Embedded text only; no equivalent usable direct ingredient
    row", "evidence_id": "amount-5"}, {"owner_field": "ingredients[5].concentration",
    "name": "FeSO4·7H2O", "owner_value": "10", "owner_unit": "MG_PER_L", "source_amount":
    "10", "source_unit": "mg", "source_quote": "FeSO 4 ·7H 2 O 10 mg", "source_locator":
    "Medium Composition quantified row 6", "condition": "Iron(II) sulfate heptahydrate
    in milligrams, not grams; no anhydrous molar conversion.", "decision": "verified",
    "decision_rationale": "Source amount verified on the nominal batch basis; final
    volume is not independently established.", "target_correspondence": "Embedded
    text only; no equivalent usable direct ingredient row", "evidence_id": "amount-6"},
    {"owner_field": "ingredients[6].concentration", "name": "Sucrose", "owner_value":
    "30", "owner_unit": "G_PER_L", "source_amount": "30", "source_unit": "g", "source_quote":
    "Sucrose 30 g", "source_locator": "Medium Composition quantified row 7", "condition":
    "Source sucrose mass retained.", "decision": "verified", "decision_rationale":
    "Source amount verified on the nominal batch basis; final volume is not independently
    established.", "target_correspondence": "Embedded text only; no equivalent usable
    direct ingredient row", "evidence_id": "amount-7"}, {"owner_field": "ingredients[7].concentration",
    "name": "Agar", "owner_value": "15", "owner_unit": "G_PER_L", "source_amount":
    "15", "source_unit": "g", "source_quote": "Agar 15 g", "source_locator": "Medium
    Composition quantified row 8", "condition": "Unconditional agar amount in this
    exact source.", "decision": "verified", "decision_rationale": "Source amount verified
    on the nominal batch basis; final volume is not independently established.", "target_correspondence":
    "Embedded text only; no equivalent usable direct ingredient row", "evidence_id":
    "amount-8"}, {"owner_field": "ingredients[8].concentration", "name": "Distilled
    water", "owner_value": "1", "owner_unit": "L", "source_amount": "1", "source_unit":
    "L", "source_quote": "Distilled water 1 L", "source_locator": "Medium Composition
    quantified row 9", "condition": "Literal solvent amount; not a mass or an independently
    stated final volume.", "decision": "verified", "decision_rationale": "Literal
    liquid amount verified; no mass conversion is asserted.", "target_correspondence":
    "Embedded text only; no equivalent usable direct ingredient row", "evidence_id":
    "amount-9"}]'
- assessment_id: grounding
  area: grounding
  topic: All asserted primary IDs, canonical labels and current secondary keys
  outcome: concern
  summary: The generated target has 0/2 primary ontology links and 0/2 secondary links.
    The owner has 8/9 primary ontology links, including 7 CHEBI instances, and 0/9
    verified secondary links. 2 owner primary labels differ from canonical labels.
    These are separate layer-specific linkage denominators on a 0–100 scale, not scientific
    accuracy scores. No secondary denominator of zero is invented when no keys are
    asserted.
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - record
  - owner-0
  - mim
  - micro0000178
  - chebi131527
  - chebi32588
  - chebi31795
  - chebi75836
  - chebi17992
  - chebi2509
  - chebi15377
  details: '{"counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances":
    0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances":
    0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent":
    0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 9,
    "primary_ontology_instances": 8, "primary_CHEBI_instances": 7, "canonical_primary_label_instances":
    6, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent":
    88.89, "primary_CHEBI_percent": 77.78, "secondary_verified_percent": 0.0}}, "label_drift":
    [{"field_path": "ingredients[1].term.label", "id": "MICRO:0000178", "asserted_label":
    "Bacto peptone", "canonical_label": "peptone", "source_key": "micro0000178"},
    {"field_path": "ingredients[5].term.label", "id": "CHEBI:75836", "asserted_label":
    "FeSO4 x 7 H2O", "canonical_label": "iron(2+) sulfate heptahydrate", "source_key":
    "chebi75836"}], "instances": [{"layer": "target", "path": "data/merge_yaml/merged/915.yaml",
    "field": "ingredients[0]", "preferred_term": "Casamino Acids (Difco)1gBacto Peptone
    (Difco)2gK2HPO41gKCl0.5gMgSO4·7H2O0.5gFeSO4·7H2O10mgSucrose30gAgar15gDistilled
    water1L"}, {"layer": "target", "path": "data/merge_yaml/merged/915.yaml", "field":
    "ingredients[1]", "preferred_term": ""}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml",
    "field": "ingredients[0]", "preferred_term": "Casamino Acids (Difco)"}, {"layer":
    "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field": "ingredients[1]",
    "preferred_term": "Bacto Peptone (Difco)", "primary_id": "MICRO:0000178", "asserted_label":
    "Bacto peptone", "canonical_label": "peptone", "label_equal": false, "source_key":
    "micro0000178", "description": [], "synonyms": [], "form_annotations": {"createdBy":
    ["Carrine Blank"], "definition": ["An enzymatic digest of animal (mammalian) protein
    (of unspecified orgin), used for the culturing of microorganisms."], "definition
    source": ["From BD Bionutrients Technical Manual (3rd edition revised).:\n\nBacto™
    Peptone is an enzymatic digest of animal protein. Bacto Peptone was first introduced
    in 1914 and became the standard Peptone for the preparation of bacteriological
    culture media. The nutritive value of Bacto Peptone is largely dependent on the
    amino acid content that supplies essential nitrogen. Bacto Peptone contains only
    a negligible quantity of proteoses and more complex constituents.\n\nAsh content
    is 6.9%\nNaCl content is 1.7%"], "has_exact_synonym": ["Bacto Peptone", "Bacto-peptone",
    "bacterial peptone", "peptones"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml",
    "field": "ingredients[2]", "preferred_term": "K2HPO4", "primary_id": "CHEBI:131527",
    "asserted_label": "dipotassium hydrogen phosphate", "canonical_label": "dipotassium
    hydrogen phosphate", "label_equal": true, "source_key": "chebi131527", "description":
    ["A potassium salt that is the dipotassium salt of phosphoric acid."], "synonyms":
    ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium
    monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate",
    "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric
    acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen
    phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium
    phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate",
    "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "form_annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7758-11-4", "kegg.compound:C13197",
    "kegg.drug:D02403", "metacyc.compound:CPD0-2433", "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"],
    "generalized_empirical_formula": ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131527"], "inchi_key_string":
    ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"],
    "mass": ["174.174"], "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field":
    "ingredients[3]", "preferred_term": "KCl", "primary_id": "CHEBI:32588", "asserted_label":
    "potassium chloride", "canonical_label": "potassium chloride", "label_equal":
    true, "source_key": "chebi32588", "description": ["A metal chloride salt with
    a K(+) counterion."], "synonyms": ["KCl", "Kaliumchlorid", "Kaon-Cl 10", "Klor-con",
    "Klotrix", "Monopotassium chloride", "[KCl]", "muriate of potash", "potassium
    chloride", "potassium chloride", "sylvite"], "form_annotations": {"charge": [0.0],
    "database_cross_reference": ["cas:7447-40-7", "drugbank:DB00761", "kegg.drug:D02060",
    "metacyc.compound:KCL", "molbase:881", "reaxys:3534978", "wikipedia.en:Potassium_Chloride"],
    "generalized_empirical_formula": ["Cl.K"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:32588"], "inchi_key_string": ["WCUXLLCKKVVCTQ-UHFFFAOYSA-M"], "inchi_string":
    ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "monoisotopic_mass": ["73.93256"],
    "smiles_string": ["[Cl-].[K+]"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml",
    "field": "ingredients[4]", "preferred_term": "MgSO4·7H2O", "primary_id": "CHEBI:31795",
    "asserted_label": "magnesium sulfate heptahydrate", "canonical_label": "magnesium
    sulfate heptahydrate", "label_equal": true, "source_key": "chebi31795", "description":
    ["A hydrate that is the heptahydrate form of magnesium sulfate."], "synonyms":
    ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt",
    "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate",
    "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium
    sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "form_annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:10034-99-8", "drugbank:DBSALT001240",
    "foodb.food:FDB015432", "kegg.compound:C12505", "kegg.drug:D01108", "metacyc.compound:CPD0-2387",
    "pubmed:12078740", "pubmed:21595222", "pubmed:26281883", "pubmed:28970193", "pubmed:30510660",
    "pubmed:5492983", "wikipedia.en:Epsomite"], "generalized_empirical_formula": ["7H2O.Mg.O4S"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31795"], "inchi_key_string":
    ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field":
    "ingredients[5]", "preferred_term": "FeSO4·7H2O", "primary_id": "CHEBI:75836",
    "asserted_label": "FeSO4 x 7 H2O", "canonical_label": "iron(2+) sulfate heptahydrate",
    "label_equal": false, "source_key": "chebi75836", "description": ["A hydrate that
    is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in
    the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments;
    for solid-dosage treatments, the monohydrate is normally used)."], "synonyms":
    ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous sulfate heptahydrate",
    "ferrous sulfate.7H2O", "green vitriol", "iron vitriol", "iron(2+) sulfate--water
    (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O", "iron(II) sulfate.7H2O",
    "melanterite mineral", "melanterite"], "form_annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890",
    "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id":
    ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"],
    "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]}},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field":
    "ingredients[6]", "preferred_term": "Sucrose", "primary_id": "CHEBI:17992", "asserted_label":
    "sucrose", "canonical_label": "sucrose", "label_equal": true, "source_key": "chebi17992",
    "description": ["A glycosyl glycoside formed by glucose and fructose units joined
    by an acetal oxygen bridge from hemiacetal of glucose to the hemiketal of the
    fructose."], "synonyms": ["1-alpha-D-Glucopyranosyl-2-beta-D-fructofuranoside",
    "Cane sugar", "SUCROSE", "Saccharose", "Sacharose", "Sucrose", "White sugar",
    "beta-D-Fruf-(2<->1)-alpha-D-Glcp", "beta-D-fructofuranosyl alpha-D-glucopyranoside",
    "beta-D-fructofuranosyl alpha-D-glucopyranoside", "sacarosa", "sucrose", "table
    sugar"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:57-50-1",
    "drugbank:DB02772", "drugcentral:4610", "gmelin:97695", "hmdb:HMDB0000258", "kegg.compound:C00089",
    "kegg.drug:D00025", "kegg.drug:D06533", "kegg.glycan:G00370", "knapsack:C00001151",
    "metacyc.compound:SUCROSE", "pdb-ccd:SUC", "pubmed:11021636", "pubmed:11093712",
    "pubmed:11111003", "pubmed:12065720", "pubmed:12706980", "pubmed:13508893", "pubmed:15291457",
    "pubmed:15660210", "pubmed:15792978", "pubmed:15845855", "pubmed:16228482", "pubmed:16304615",
    "pubmed:16313996", "pubmed:16525719", "pubmed:16660545", "pubmed:16663947", "pubmed:16665852",
    "pubmed:17233733", "pubmed:17439666", "pubmed:17597061", "pubmed:18625236", "pubmed:19199566",
    "pubmed:19726178", "pubmed:21703290", "pubmed:21972845", "pubmed:22085755", "pubmed:22311778",
    "pubmed:22404833", "pubmed:22751876", "reaxys:1435311", "reaxys:90825", "wikipedia.en:Sucrose"],
    "generalized_empirical_formula": ["C12H22O11"], "has_alternative_id": ["CHEBI:15128",
    "CHEBI:26812", "CHEBI:45795", "CHEBI:9314"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:17992"], "inchi_key_string": ["CZMRCDWAGMRECN-UGDNZRGBSA-N"], "inchi_string":
    ["InChI=1S/C12H22O11/c13-1-4-6(16)8(18)9(19)11(21-4)23-12(3-15)10(20)7(17)5(2-14)22-12/h4-11,13-20H,1-3H2/t4-,5-,6-,7-,8+,9-,10+,11-,12+/m1/s1"],
    "mass": ["342.297"], "monoisotopic_mass": ["342.11621"], "smiles_string": ["OC[C@H]1O[C@@](CO)(O[C@H]2O[C@H](CO)[C@@H](O)[C@H](O)[C@H]2O)[C@@H](O)[C@@H]1O"],
    "wurcs_representation": ["WURCS=2.0/2,2,1/[a2122h-1a_1-5][ha122h-2b_2-5]/1-2/a1-b2"]}},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml", "field":
    "ingredients[7]", "preferred_term": "Agar", "primary_id": "CHEBI:2509", "asserted_label":
    "agar", "canonical_label": "agar", "label_equal": true, "source_key": "chebi2509",
    "description": ["A complex mixture of polysaccharides extracted from species of
    red algae. Its two main components are agarose and agaropectin. Agarose is the
    component responsible for the high-strength gelling properties of agar, while
    agaropectin provides the viscous properties."], "synonyms": [], "form_annotations":
    {"database_cross_reference": ["cas:9002-18-0", "kegg.compound:C08815", "pubmed:25603143",
    "pubmed:25842535", "pubmed:25959629", "pubmed:26043937", "pubmed:26050892", "pubmed:26116384",
    "reaxys:8538728", "wikipedia.en:Agar"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:2509"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_915.yaml",
    "field": "ingredients[8]", "preferred_term": "Distilled water", "primary_id":
    "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_equal":
    true, "source_key": "chebi15377", "description": ["An oxygen hydride consisting
    of an oxygen atom that is covalently bonded to two hydrogen atoms"], "synonyms":
    ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water",
    "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau",
    "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5", "gmelin:117",
    "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001", "metacyc.compound:WATER",
    "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"], "generalized_empirical_formula":
    ["H2O"], "has_alternative_id": ["CHEBI:10743", "CHEBI:13352", "CHEBI:27313", "CHEBI:42043",
    "CHEBI:42857", "CHEBI:43228", "CHEBI:44292", "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15377"], "inchi_key_string":
    ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass":
    ["18.015"], "monoisotopic_mass": ["18.01056"], "smiles_string": ["[H]O[H]"]}}]}'
- assessment_id: forms
  area: grounding
  topic: Source ingredient identities, mixtures and exact chemical forms
  outcome: supported
  summary: The seven owner CHEBI identities cover dipotassium hydrogen phosphate,
    potassium chloride, magnesium sulfate heptahydrate, iron(2+) sulfate heptahydrate,
    sucrose, agar and water. Hydration annotations explicitly agree with the two source
    heptahydrates. MICRO:0000178 is canonically peptone; its annotation includes Bacto
    Peptone as an exact synonym and an enzymatic animal-protein digest definition,
    supporting the source mixture identity at that scope. The Bacto and iron sulfate
    labels need canonicalization without changing their identities or amounts. Casamino
    Acids remains ungrounded rather than assigned an invented molecular term.
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - record
  - owner-0
  - nbrc913
  - micro0000178
  - chebi131527
  - chebi32588
  - chebi31795
  - chebi75836
  - chebi17992
  - chebi2509
  - chebi15377
- assessment_id: conditions
  area: consistency
  topic: Preparation, pH and physical-state conditions
  outcome: concern
  summary: Both target and owner lack a source-supported pH, matching the source’s
    silence; no arbitrary pH is proposed. Source agar is unconditional. The owner
    leaves preparation empty. The target instead asserts generic dissolve, adjust-pH
    and autoclaving steps; Sterilize by autoclaving is tagged DISSOLVE and lacks support
    in the exact source. Do not import source 915 filtration or pH conditions.
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - record
  - owner-0
  - nbrc913
  - importer
- assessment_id: classification
  area: scope
  topic: Classification and bounded biological claims
  outcome: supported
  summary: COMPLEX/UNDEFINED is consistent with Casamino Acids and Bacto Peptone,
    while the specified 15 g agar supports SOLID_AGAR. Opaque commercial ingredients
    remain mixtures despite ontology linkage. Neither target nor owner asserts organisms,
    strains, taxon IDs, assemblies, DOI/PMID papers, growth outcomes, parent media
    or variants. Source catalogue scope is not experimental growth evidence. Optional
    omissions are not populated with invented organisms.
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - record
  - owner-0
  - nbrc913
  - nbrc915
  - exporter
- assessment_id: owner-correspondence
  area: ownership
  topic: Maintained recovery versus generated representation
  outcome: concern
  summary: The generated August merge precedes later owner recovery and source metadata.
    The owner now contains 9 explicit source rows and an official source term/reference;
    the target retains two collapsed rows and no structured source term/reference.
    Owner label differences must be corrected before regeneration. The nine owner
    rows include eight primary ontology links, seven of them CHEBI, with no asserted
    secondary keys. The owner already carries the official source name and reference;
    its description still preserves the local 915 versus actual 913 import distinction.
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - record
  - owner-0
  - nbrc913
  - recovery
  - mim
- assessment_id: evidence
  area: evidence
  topic: Claim-level amount evidence and checked reference scope
  outcome: concern
  summary: Each source amount is traced to an exact table row above. The owner has
    the official recipe reference but lacks ingredient-level amount evidence; the
    target has no structured reference and its reference checker checked zero entries.
    Add scoped amount evidence while recovering the structured formulation, retaining
    source batch and condition qualifiers. Ontology citations verify identities and
    labels rather than recipe amounts. No separate paper was asserted or required
    to identify this catalogue recipe.
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - record
  - owner-0
  - nbrc913
  - validate-references
- assessment_id: history
  area: provenance
  topic: Append-only event history and timestamp interpretation
  outcome: supported
  summary: All 14 scoped timestamps were checked for ISO syntax and timezone. Every
    instance parses and has an explicit timezone. Curation events are process provenance
    rather than independent confirmation of recipe correctness.
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - record
  - owner-0
  - history
  details: '[]'
- assessment_id: arithmetic
  area: quantity
  topic: Iron sulfate milligram scale and solvent volume
  outcome: supported
  summary: The source and owner agree on FeSO4·7H2O at 10 mg on the nominal recipe
    basis; 10 mg equals 0.010 g, not 10 g. The 0.5 g magnesium sulfate is also explicitly
    the heptahydrate. Water remains 1 L as a volume. No molarity, density or final
    post-dissolution volume is assumed.
  target_ids:
  - CultureMech:007504
  evidence_ids:
  - nbrc913
  - amount-5
  - amount-6
  - amount-9
  - chebi31795
  - chebi75836
findings:
- finding_id: f1
  issue_key: cm007504-stale-collapsed-source913-formula
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated target loses the recovered 9-row NBRC 913 formula
  description: The whole-table ingredient string at VARIABLE and the empty ingredient
    with a reagent name as a g/L value cannot represent a usable named formulation.
    The owner already has 9 explicit source rows and the official source accession/reference,
    with source conditions where stated. This prevents faithful scientific use of
    the generated formulation despite all four documented checks passing. Native P1
    reflects unusable identity/representation; this is not P1.1 and is not a reported
    schema-validator failure.
  target_ids:
  - CultureMech:007504
  field_paths:
  - ingredients
  - media_term
  - references
  - name
  - original_name
  evidence_ids:
  - record
  - owner-0
  - nbrc913
  - recovery
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_915.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: cm007504-unsupported-default-autoclave
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated autoclaving is unsupported and action-mismatched
  description: The inspected exact NBRC 913 page does not provide a sterilization
    protocol. The target nevertheless states Sterilize by autoclaving with action
    DISSOLVE, matching the importer fallback and keyword mismatch. The current owner
    has already removed that generic autoclaving instruction; the stale generated
    instruction should not be reintroduced as primary-source evidence. Neither a neighboring
    accession nor a routine laboratory convention supplies missing source-specific
    support.
  target_ids:
  - CultureMech:007504
  field_paths:
  - preparation_steps[2].description
  - preparation_steps[2].action
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - nbrc913
  - importer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_915.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: cm007504-owner-canonical-label-drift
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Maintained owner labels differ from canonical ontology labels
  description: '[{"field_path": "ingredients[1].term.label", "id": "MICRO:0000178",
    "asserted_label": "Bacto peptone", "canonical_label": "peptone", "source_key":
    "micro0000178"}, {"field_path": "ingredients[5].term.label", "id": "CHEBI:75836",
    "asserted_label": "FeSO4 x 7 H2O", "canonical_label": "iron(2+) sulfate heptahydrate",
    "source_key": "chebi75836"}] These are literal label differences in the maintained
    input and would propagate on regeneration. They do not by themselves prove that
    the asserted ontology IDs identify the wrong substances; preserve supplier/source
    names in preferred_term and exact recipe forms separately.'
  target_ids:
  - CultureMech:007504
  field_paths:
  - owner:data/normalized_yaml/bacterial/NBRC_915.yaml:ingredients[1].term.label
  - owner:data/normalized_yaml/bacterial/NBRC_915.yaml:ingredients[5].term.label
  evidence_ids:
  - owner-0
  - micro0000178
  - chebi75836
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_915.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Verify the maintained source rows and their exact forms/units against
    the bound primary page, correct owner label or classification issues listed separately,
    add scoped amount evidence, and regenerate derived records while retaining the
    same stable ID and source accession.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007504
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_915.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a2
  description: Retain supported source pH/formulation details and regenerate from
    the verified owner without the unsupported default. Any later sterilization instruction
    needs exact source support and a corresponding action; keep unknown time, temperature
    and procedure explicit.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007504
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_915.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a3
  description: Update only the canonical term labels after verifying the same IDs
    and source-specific ingredient identities. Preserve source names, brands, supplied
    hydration forms and amounts, then ensure regeneration keeps both canonical labels
    and preferred terms. Run the documented ID-label correspondence check on the authorized
    correction.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007504
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_915.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
limitations:
- Source masses and 1 L distilled water are assessed on the nominal catalogue recipe
  basis. The page does not establish measured final volume, and no solvent mass or
  molar conversion is inferred.
- The exact source 913 page gives no pH, sterilization parameters, incubation conditions
  or storage procedure. These remain unquantified rather than being copied from actual
  source 915.
- Casamino Acids and Bacto Peptone retain their source-specific commercial mixture
  names. No supplier formulation, organism growth claim or pure-molecule substitute
  was invented.
- The historical owner repair event is provenance. No missing historical writer was
  reconstructed or executed, and the similarly numbered current antibiotic-medium
  repair writer was not treated as this owner’s authority.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-012
- generated-medium
```

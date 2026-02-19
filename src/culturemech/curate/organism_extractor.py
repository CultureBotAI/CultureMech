"""Conservative organism data extraction from medium metadata."""

import re
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import yaml
import requests
from time import sleep

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class OrganismData:
    """Extracted organism information."""
    organism_name: Optional[str] = None
    strain: Optional[str] = None
    culture_type: Optional[str] = None  # 'isolate' | 'community' | None
    confidence: str = 'low'  # 'high' | 'medium' | 'low'
    ncbi_taxon_id: Optional[str] = None
    ncbi_taxon_label: Optional[str] = None
    extraction_pattern: Optional[str] = None


class OrganismExtractor:
    """Conservative organism data extraction from medium metadata."""

    # Patterns for organism name extraction (all case-insensitive with (?i) flag)
    ORGANISM_PATTERNS = [
        # Pattern 1: [Genus species] MEDIUM
        # Matches: "Escherichia coli Medium", "BACILLUS PASTEURII MEDIUM"
        (r'(?i)^([A-Za-z]+\s+[A-Za-z]+)\s+MEDIUM', 'genus_species_medium', 'high'),

        # Pattern 2: MEDIUM FOR [Genus species]
        # Matches: "MEDIUM FOR Halorhodospira", "Medium for Chlorobium ferrooxidans"
        (r'(?i)MEDIUM\s+FOR\s+([A-Za-z]+(?:\s+[A-Za-z]+)?)', 'medium_for_genus_species', 'high'),

        # Pattern 3: Organism at start with strain/variant
        # Matches: "Escherichia coli K-12 MEDIUM"
        (r'(?i)^([A-Za-z]+\s+[A-Za-z]+)\s+[A-Z0-9-]+\s+MEDIUM', 'genus_species_strain_medium', 'high'),

        # Pattern 4: DSMZ format - DSMZ_###_GENUS_SPECIES_MEDIUM
        # Matches: "DSMZ 1457 ALCALILIMNICOLA EHRLICHII MEDIUM"
        (r'(?i)DSMZ[_\s]\d+[_\s]([A-Z]+(?:[_\s][A-Z]+)+?)[_\s]MEDIUM', 'dsmz_genus_species_medium', 'high'),

        # Pattern 5: Single genus name MEDIUM (medium confidence - could be generic)
        # Matches: "AZOTOBACTER MEDIUM", "Chloroflexus MEDIUM"
        (r'(?i)^([A-Za-z]+)\s+MEDIUM', 'genus_medium', 'medium'),

        # Pattern 6: DSMZ format - single genus (medium confidence)
        (r'(?i)DSMZ[_\s]\d+[_\s]([A-Z]+)[_\s]MEDIUM', 'dsmz_genus_medium', 'medium'),
    ]

    # Patterns for strain extraction
    STRAIN_PATTERNS = [
        (r'MODIFIED FOR DSM[_\s](\d+)', 'dsm_modified'),
        (r'DSM[_\s](\d+)', 'dsm'),
        (r'ATCC[_\s](\d+)', 'atcc'),
        (r'JCM[_\s](\d+)', 'jcm'),
    ]

    # Community/co-culture indicators
    COMMUNITY_PATTERNS = [
        r'co-culture',
        r'consortium',
        r'mixed culture',
        r'community',
    ]

    # Generic media to exclude (not organism-specific)
    GENERIC_MEDIA = {
        'NUTRIENT', 'LB', 'R2A', 'TSA', 'TSB', 'M9', 'MINIMAL',
        'RICH', 'STANDARD', 'GENERAL', 'BASIC', 'COMPLEX'
    }

    def __init__(self, ncbi_email: Optional[str] = None):
        """Initialize extractor.

        Args:
            ncbi_email: Email for NCBI API (required for higher rate limits)
        """
        self.ncbi_email = ncbi_email
        self.ncbi_cache: Dict[str, Optional[Dict]] = {}

    def extract_from_name(self, name: str, original_name: Optional[str] = None) -> OrganismData:
        """Extract organism info from medium name.

        Args:
            name: Normalized medium name
            original_name: Original medium name

        Returns:
            OrganismData with extracted information
        """
        data = OrganismData()

        # Try both names
        names_to_check = [name]
        if original_name and original_name != name:
            names_to_check.append(original_name)

        # Check for community patterns first
        for check_name in names_to_check:
            for pattern in self.COMMUNITY_PATTERNS:
                if re.search(pattern, check_name, re.IGNORECASE):
                    data.culture_type = 'community'
                    data.confidence = 'high'
                    data.extraction_pattern = pattern
                    return data

        # Extract organism name
        for check_name in names_to_check:
            for pattern, pattern_name, confidence in self.ORGANISM_PATTERNS:
                match = re.search(pattern, check_name)
                if match:
                    organism = match.group(1)

                    # For DSMZ format, convert underscores/spaces to spaces and title case
                    if 'dsmz' in pattern_name:
                        organism = organism.replace('_', ' ').replace('  ', ' ').strip()
                        # Convert to title case properly
                        organism = ' '.join(word.capitalize() for word in organism.split())

                    # Normalize spacing
                    organism = ' '.join(organism.split())

                    # Skip if it's a generic medium name (use word boundaries to avoid false positives)
                    organism_upper = organism.upper()
                    is_generic = any(
                        re.search(r'\b' + re.escape(generic) + r'\b', organism_upper)
                        for generic in self.GENERIC_MEDIA
                    )
                    if is_generic:
                        continue

                    data.organism_name = organism
                    data.confidence = confidence
                    data.extraction_pattern = pattern_name
                    data.culture_type = 'isolate'  # Default for organism-specific media
                    break

            if data.organism_name:
                break

        # Extract strain IDs
        for check_name in names_to_check:
            for pattern, pattern_name in self.STRAIN_PATTERNS:
                match = re.search(pattern, check_name, re.IGNORECASE)
                if match:
                    data.strain = f"{pattern_name.upper().replace('_', ' ')}: {match.group(1)}"
                    break
            if data.strain:
                break

        return data

    def lookup_ncbi_taxon(self, organism_name: str) -> Optional[Dict]:
        """Query NCBI Taxonomy API for taxon ID.

        Args:
            organism_name: Scientific name to look up

        Returns:
            Dict with 'id' and 'label' or None if not found
        """
        # Check cache
        if organism_name in self.ncbi_cache:
            return self.ncbi_cache[organism_name]

        try:
            # NCBI E-utilities API
            base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

            # Search for taxon ID
            search_url = f"{base_url}esearch.fcgi"
            search_params = {
                'db': 'taxonomy',
                'term': organism_name,
                'retmode': 'json'
            }
            if self.ncbi_email:
                search_params['email'] = self.ncbi_email

            response = requests.get(search_url, params=search_params, timeout=10)
            response.raise_for_status()
            search_data = response.json()

            # Check if we got exactly one result
            id_list = search_data.get('esearchresult', {}).get('idlist', [])
            if len(id_list) != 1:
                logger.debug(f"NCBI search for '{organism_name}' returned {len(id_list)} results")
                self.ncbi_cache[organism_name] = None
                return None

            taxon_id = id_list[0]

            # Be nice to NCBI servers
            sleep(0.34)  # ~3 requests per second

            # Fetch taxon details
            fetch_url = f"{base_url}efetch.fcgi"
            fetch_params = {
                'db': 'taxonomy',
                'id': taxon_id,
                'retmode': 'xml'
            }
            if self.ncbi_email:
                fetch_params['email'] = self.ncbi_email

            response = requests.get(fetch_url, params=fetch_params, timeout=10)
            response.raise_for_status()

            # Parse XML to get scientific name
            import xml.etree.ElementTree as ET
            root = ET.fromstring(response.content)
            sci_name = root.find('.//ScientificName')

            if sci_name is not None:
                result = {
                    'id': f'NCBITaxon:{taxon_id}',
                    'label': sci_name.text
                }
                self.ncbi_cache[organism_name] = result
                logger.info(f"Found NCBI taxon for '{organism_name}': {result}")
                return result

            self.ncbi_cache[organism_name] = None
            return None

        except Exception as e:
            logger.warning(f"Error looking up NCBI taxon for '{organism_name}': {e}")
            self.ncbi_cache[organism_name] = None
            return None

    def extract_from_yaml(self, yaml_path: Path, confidence_threshold: str = 'high',
                         lookup_ncbi: bool = True) -> Optional[OrganismData]:
        """Extract organism data from a YAML file.

        Args:
            yaml_path: Path to YAML file
            confidence_threshold: Minimum confidence level
            lookup_ncbi: Whether to lookup NCBI taxon IDs

        Returns:
            OrganismData or None if below confidence threshold
        """
        try:
            with open(yaml_path, 'r') as f:
                data = yaml.safe_load(f)

            name = data.get('name', '')
            original_name = data.get('original_name')

            # Extract organism info
            org_data = self.extract_from_name(name, original_name)

            # Check confidence threshold
            confidence_levels = {'low': 0, 'medium': 1, 'high': 2}
            if confidence_levels.get(org_data.confidence, -1) < confidence_levels.get(confidence_threshold, 2):
                return None

            # Lookup NCBI taxon if we have an organism name and lookups are enabled
            if lookup_ncbi and org_data.organism_name:
                ncbi_result = self.lookup_ncbi_taxon(org_data.organism_name)
                if ncbi_result:
                    org_data.ncbi_taxon_id = ncbi_result['id']
                    org_data.ncbi_taxon_label = ncbi_result['label']

            return org_data

        except Exception as e:
            logger.error(f"Error processing {yaml_path}: {e}")
            return None

    def process_directory(self, yaml_dir: Path, output_json: Path,
                         confidence_threshold: str = 'high',
                         lookup_ncbi: bool = True) -> Dict:
        """Process all YAML files in directory.

        Args:
            yaml_dir: Directory containing YAML files
            output_json: Output JSON file path
            confidence_threshold: Minimum confidence ('high', 'medium', 'low')
            lookup_ncbi: Whether to lookup NCBI taxon IDs

        Returns:
            Dictionary mapping filenames to organism data
        """
        results = {}
        yaml_files = list(yaml_dir.rglob('*.yaml'))

        logger.info(f"Processing {len(yaml_files)} YAML files...")
        if not lookup_ncbi:
            logger.info("Skipping NCBI taxon lookups (can be done later)")

        for i, yaml_file in enumerate(yaml_files):
            if i % 100 == 0:
                logger.info(f"Processed {i}/{len(yaml_files)} files...")

            org_data = self.extract_from_yaml(yaml_file, confidence_threshold, lookup_ncbi)

            if org_data:
                # Store relative path from yaml_dir
                rel_path = yaml_file.relative_to(yaml_dir)
                results[str(rel_path)] = asdict(org_data)

        # Save results
        output_json.parent.mkdir(parents=True, exist_ok=True)
        with open(output_json, 'w') as f:
            json.dump(results, f, indent=2)

        logger.info(f"Extracted {len(results)} high-confidence organism records")
        logger.info(f"Results saved to {output_json}")

        # Print summary statistics
        culture_types = {}
        with_ncbi = 0
        with_strain = 0

        for data in results.values():
            ct = data.get('culture_type', 'unknown')
            culture_types[ct] = culture_types.get(ct, 0) + 1
            if data.get('ncbi_taxon_id'):
                with_ncbi += 1
            if data.get('strain'):
                with_strain += 1

        logger.info(f"\nSummary:")
        logger.info(f"  Culture types: {culture_types}")
        logger.info(f"  With NCBI taxon: {with_ncbi}")
        logger.info(f"  With strain: {with_strain}")

        return results


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Extract organism data from CultureMech YAML files'
    )
    parser.add_argument(
        '--input',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Input directory containing YAML files'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('data/curation/organism_candidates.json'),
        help='Output JSON file'
    )
    parser.add_argument(
        '--confidence-threshold',
        choices=['high', 'medium', 'low'],
        default='high',
        help='Minimum confidence level for extraction'
    )
    parser.add_argument(
        '--ncbi-email',
        help='Email for NCBI API (recommended for better rate limits)'
    )
    parser.add_argument(
        '--skip-ncbi',
        action='store_true',
        help='Skip NCBI taxon lookups (faster, can be done later)'
    )

    args = parser.parse_args()

    extractor = OrganismExtractor(ncbi_email=args.ncbi_email)
    extractor.process_directory(
        args.input,
        args.output,
        args.confidence_threshold,
        lookup_ncbi=not args.skip_ncbi
    )


if __name__ == '__main__':
    main()

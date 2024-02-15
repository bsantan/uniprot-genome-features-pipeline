
"""Constants for robot_utilities."""

from pathlib import Path

RAW_DATA_DIR = Path(__file__).parents[2] / "data" / "raw"

# ROBOT
ROBOT_REMOVED_SUFFIX = "_removed_subset"
EXCLUSION_TERMS_FILE = "exclusion_branches.tsv"
NCBITAXON_PREFIX = "NCBITaxon:"

#Uniprot
ORGANISM_ID_MIXED_CASE = "Organism_ID"
TAXONOMY_ID_UNIPROT_PREFIX = "taxonomy_id:"
UNIPROT_BASE_URL = "https://rest.uniprot.org/uniprotkb/"
UNIPROT_DESIRED_FORMAT = "tsv"
NIPROT_FIELDS = ["organism_id", "id", "accession", "protein_name", "ec", "ft_binding"]
UNIPROT_KEYWORDS = ["Reference+proteome"]
UNIPROT_SIZE,UNIPROT_SIZE = 500
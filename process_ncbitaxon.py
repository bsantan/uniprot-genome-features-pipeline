

from robot_utils import remove_convert_to_json

from constants import (
    ROBOT_REMOVED_SUFFIX,
    EXCLUSION_TERMS_FILE,
    NCBITAXON_PREFIX
)

def ncbitaxon_extract_subset(self, data_file: Optional[Path]) -> None:
    """
    Process the data_file.

    :param data_file: data file to parse.
    :return: None.
    """
    if data_file.suffixes == [".owl", ".gz"]:
        json_path = str(data_file).replace(".owl.gz", ROBOT_REMOVED_SUFFIX + ".json")
        if not Path(json_path).is_file():
            self.decompress(data_file)
            with open(str(self.input_base_dir / EXCLUSION_TERMS_FILE), "r") as f:
                terms = [
                    line.strip() for line in f if line.lower().startswith(name.lower())
                ]
            remove_convert_to_json(str(self.input_base_dir), NCBITAXON_PREFIX, terms)
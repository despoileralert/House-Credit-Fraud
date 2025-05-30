import yaml
from houseclassifier.utils.logger import src_logger

def read_yaml(file) -> dict:
        with open(file) as stream:
            try:
                y = yaml.safe_load(stream)
                src_logger.info(f"{file} has been successfully loaded.")
                return y
            except Exception as e:
                raise e
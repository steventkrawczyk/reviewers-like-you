

import logging
import os
import yaml
from app.config.default_config import DefaultConfig


class ConfigLoader:
    @staticmethod
    def load(filepath: str):
        if os.path.isfile(filepath):
            with open(filepath, 'r') as config_yaml:
                config = yaml.load(config_yaml, Loader=yaml.SafeLoader)
        else:
            config = DefaultConfig()
        logging.debug("Loaded config: " + str(config))
        return config

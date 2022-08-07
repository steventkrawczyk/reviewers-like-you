import logging
import os
import yaml
from app.common.python.config.default_config import DefaultConfig


class ConfigLoader:
    '''
    Used to load in configuration for Flask apps.
    '''

    @staticmethod
    def load(filepath: str):
        if os.path.isfile(filepath):
            with open(filepath, 'r') as config_yaml:
                config = yaml.load(config_yaml, Loader=yaml.SafeLoader)
        else:
            config = DefaultConfig()
        logging.debug("Loaded config: " + str(config))
        return config

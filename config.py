import os
import json

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.config_data = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.filepath):
            raise ConfigError('Config file does not exist.')
        try:
            with open(self.filepath, 'r') as config_file:
                return json.load(config_file)
        except json.JSONDecodeError:
            raise ConfigError('Error decoding JSON from config file.')
        except Exception as e:
            raise ConfigError(f'Unexpected error: {str(e)}')

    def get(self, key, default=None):
        return self.config_data.get(key, default)

    def set(self, key, value):
        self.config_data[key] = value
        try:
            with open(self.filepath, 'w') as config_file:
                json.dump(self.config_data, config_file, indent=4)
        except Exception as e:
            raise ConfigError(f'Failed to write config: {str(e)}')

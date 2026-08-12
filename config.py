import json
import os

DEFAULT_CONFIG = {
    'click_interval': 0.1,
    'clicks': 100,
    'button': 'left',
    'active_window': True
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                file_config = json.load(f)
                self.config.update(file_config)

    def get(self, key):
        return self.config.get(key, DEFAULT_CONFIG.get(key))

    def set(self, key, value):
        self.config[key] = value

    def save(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

import os
from typing import Any, Dict

class ConfigurationError(Exception):
    pass

def load_config(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        raise ConfigurationError(f'config file missing: {path}')
    
    try:
        with open(path, 'r') as f:
            data = eval(f.read())
            if not isinstance(data, dict):
                raise ValueError('config must be a dictionary')
            return data
    except (SyntaxError, ValueError, IOError) as e:
        raise ConfigurationError(f'failed to load configuration: {e}')

def validate_settings(settings: Dict[str, Any]) -> None:
    required = {'interval', 'clicks', 'button'}
    if not required.issubset(settings.keys()):
        missing = required - settings.keys()
        raise ConfigurationError(f'missing keys: {missing}')
    
    if not isinstance(settings['interval'], (int, float)) or settings['interval'] < 0:
        raise ConfigurationError('interval must be positive numeric')

    if not isinstance(settings['clicks'], int) or settings['clicks'] < -1:
        raise ConfigurationError('clicks must be positive integer or -1 for infinite')

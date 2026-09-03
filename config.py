import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "toggle_key": "f6"
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    config = DEFAULT_CONFIG.copy()
    config_path = Path(path)
    
    if config_path.exists():
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def save_config(config: Dict[str, Any], path: str = "config.json") -> None:
    with open(path, "w") as f:
        json.dump(config, f, indent=4)
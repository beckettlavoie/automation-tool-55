import json
import os
from typing import Dict, Any


def save_click_profile(path: str, data: Dict[str, Any]) -> bool:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False


def load_click_profile(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        return {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def validate_coordinates(x: int, y: int) -> bool:
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0


def format_click_interval(ms: int) -> float:
    return max(0.01, ms / 1000.0)


def get_default_config() -> Dict[str, Any]:
    return {
        'interval_ms': 100,
        'button': 'left',
        'repeat': True,
        'coordinates': {'x': 0, 'y': 0}
    }
import json
import os
from typing import Any, Dict

def load_click_profile(filepath: str) -> Dict[str, Any]:
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeat": 0}
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_click_profile(filepath: str, data: Dict[str, Any]) -> None:
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"failed to save profile: {e}")

def validate_coordinates(coords: Dict[str, int]) -> bool:
    required = {"x", "y"}
    if not isinstance(coords, dict):
        return False
    return required.issubset(coords.keys()) and all(isinstance(v, int) for v in coords.values())

def format_click_stats(count: int, duration: float) -> str:
    cps = count / duration if duration > 0 else 0
    return f"clicks: {count} | duration: {duration:.2f}s | cps: {cps:.2f}"
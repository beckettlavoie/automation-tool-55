"""Validators for autoclicker parameters.
"""

from typing import Any, Dict, Optional, Tuple

def validate_coordinates(x: int, y: int, max_width: int = 1920, max_height: int = 1080) -> bool:
    """Return True if coordinates are within valid screen area."""
    return isinstance(x, int) and isinstance(y, int) and 0 <= x <= max_width and 0 <= y <= max_height

def validate_delay(delay: float) -> bool:
    """Return True if delay is a positive value within limits."""
    return isinstance(delay, (int, float)) and 0.001 <= delay <= 3600.0

def validate_repetitions(repetitions: Optional[int]) -> bool:
    """Return True if repetitions is None or positive integer."""
    if repetitions is None:
        return True
    return isinstance(repetitions, int) and repetitions > 0

def validate_clicker_params(x: int, y: int, delay: float, repetitions: Optional[int], max_width: int = 1920, max_height: int = 1080) -> Tuple[bool, str]:
    """Validate all autoclicker settings.

    Returns a tuple of (valid, message) where message is empty if valid.
    """
    if not validate_coordinates(x, y, max_width, max_height):
        return False, "Coordinates out of bounds"
    if not validate_delay(delay):
        return False, "Delay must be between 0.001 and 3600 seconds"
    if not validate_repetitions(repetitions):
        return False, "Repetitions must be positive integer or None"
    return True, ""

def format_error(error: str) -> str:
    """Format error message for display."""
    return f"Validation error: {error}"

def validate_hotkey(hotkey: str) -> bool:
    """Check if hotkey string is non-empty."""
    return isinstance(hotkey, str) and len(hotkey) > 0

def get_default_params() -> Dict[str, Any]:
    """Return default valid parameters for autoclicker."""
    return {
        "x": 100,
        "y": 100,
        "delay": 1.0,
        "repetitions": None
    }
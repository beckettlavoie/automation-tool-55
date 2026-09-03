from typing import Final

CLICK_INTERVAL_MIN: Final[float] = 0.01
CLICK_INTERVAL_MAX: Final[float] = 60.0
DEFAULT_CLICK_INTERVAL: Final[float] = 0.5

SUPPORTED_BUTTONS: Final[list[str]] = ['left', 'right', 'middle']

MAX_RETRIES: Final[int] = 3
TIMEOUT_SECONDS: Final[int] = 5

LOG_FILE: Final[str] = 'automation.log'
CONFIG_FILE: Final[str] = 'settings.json'

class AppState:
    """Enum-like container for application runtime states."""
    IDLE: Final[str] = 'idle'
    RUNNING: Final[str] = 'running'
    PAUSED: Final[str] = 'paused'
    STOPPED: Final[str] = 'stopped'
from typing import Dict, Any

class Config:
    def __init__(self, settings: Dict[str, Any]) -> None:
        self.settings = settings

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a setting by key, returning a default if not found."""
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration key to a value."""
        self.settings[key] = value

    def load(self, filepath: str) -> None:
        """Load configuration from a file."""
        import json
        with open(filepath, 'r') as file:
            self.settings.update(json.load(file))

    def save(self, filepath: str) -> None:
        """Save current configuration to a file."""
        import json
        with open(filepath, 'w') as file:
            json.dump(self.settings, file, indent=4)
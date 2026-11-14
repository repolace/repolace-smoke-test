"""Loading and validating application configuration."""

import json
from pathlib import Path

DEFAULT_TIMEOUT_SECONDS = 30


def parse_config(path):
    """Read a JSON config file and return it as a dict.

    Applies defaults for any key the file leaves out.
    """
    text = Path(path).read_text(encoding="utf-8")
    data = json.loads(text) if text.strip() else {}
    data.setdefault("timeout_seconds", DEFAULT_TIMEOUT_SECONDS)
    return data


def validate_config(config):
    """Raise ValueError if the config is missing anything required."""
    if "name" not in config:
        raise ValueError("config must define a name")
    if config["timeout_seconds"] <= 0:
        raise ValueError("timeout_seconds must be positive")
    return config

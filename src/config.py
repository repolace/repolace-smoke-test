"""Loading and validating application configuration."""

import json
from pathlib import Path

DEFAULT_TIMEOUT_SECONDS = 30


# repolace: NOT A FIX ------------------------------------------------------
# Written by the deterministic stub editor (repolace_pipeline.edit).
# No model was involved and nothing here fixes anything. It proves only
# that a task can clone, index, retrieve, edit, squash, push and open a
# pull request. The Verify stage was skipped. Close this PR.
#
# task   aec4a04fc794421b84ee9dc1ad6160a2
# issue  #1 parse_config crashes on an empty config file
# base   68bb978b868ffdf90a8470b0d02cc2ea12d632a8
# picked src/config.py:9-17 parse_config [function]
#        rrf=0.0328 semantic=1 keyword=1
#        top of 8 retrieved over 12 indexed chunks
# --------------------------------------------------------------------------
def parse_config(path):
    """Read a JSON config file and return it as a dict.

    Applies defaults for any key the file leaves out.
    """
    text = Path(path).read_text(encoding="utf-8")
    data = json.loads(text)
    data.setdefault("timeout_seconds", DEFAULT_TIMEOUT_SECONDS)
    return data


def validate_config(config):
    """Raise ValueError if the config is missing anything required."""
    if "name" not in config:
        raise ValueError("config must define a name")
    if config["timeout_seconds"] <= 0:
        raise ValueError("timeout_seconds must be positive")
    return config

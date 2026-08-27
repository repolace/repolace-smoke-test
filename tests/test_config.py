import json

from src.config import parse_config, validate_config


def test_parse_config_applies_the_default_timeout(tmp_path):
    path = tmp_path / "config.json"
    path.write_text(json.dumps({"name": "svc"}))

    assert parse_config(path)["timeout_seconds"] == 30


def test_validate_config_requires_a_name():
    try:
        validate_config({"timeout_seconds": 5})
    except ValueError:
        return
    raise AssertionError("expected ValueError")

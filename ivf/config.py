import json
import hjson
import yaml
from pathlib import Path


def save_json(file: Path, data):
    with file.open("w+") as f:
        json.dump(data, f, indent=4, sort_keys=True)


def save_hjson(file: Path, data):
    with file.open("w+") as f:
        hjson.dump(data, f, indent=4, sort_keys=True)


def save_yaml(file: Path, data):
    with file.open("w+") as f:
        yaml.dump(data, f)


def load_json(file: Path):
    with file.open("r") as f:
        json_data = json.load(f)
    return json_data


def load_hjson(file: Path):
    with file.open("r") as f:
        hjson_data = hjson.load(f)
    return hjson_data


def load_yaml(file: Path):
    with file.open("r") as f:
        yaml_data = yaml.load(f)
    return yaml_data

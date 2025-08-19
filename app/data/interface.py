from pathlib import Path
import json
from functools import lru_cache

DATA_PATH = Path(__file__).with_name("planets.json")

@lru_cache(maxsize=1)
def _load_planets():
    try:
        return json.loads(DATA_PATH.read_text(encoding='utf-8'))
    except FileNotFoundError as e:
        raise RuntimeError(f"Missing data file: {DATA_PATH}") from e
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON in {DATA_PATH}") from e

def get_planet_by_id(planet_id: str):
    return _load_planets().get(planet_id)

def get_planet_by_name(planet_name: str):
    return next((p for p in _load_planets().values() if p.get("name") == planet_name), None)

def get_planets():
    return list(_load_planets().values())

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

def get_planet_main_data(planet):
    return planet.get("mainData")

def get_planets(sort_by=None, search_term=None) -> list:
    return list(_load_planets().values())

def get_planet_by_id(planet_id: str):
    all_planets = _load_planets()
    return all_planets.get(planet_id)

def get_planet_data(planet_id) -> list | None:
    if not planet_id:
        return None

    planet = get_planet_by_id(planet_id)

    if not planet:
        return None

    planet_data = planet["planetData"]
    return list(planet_data)

def get_planet_names():
    return [ p.get("name") for p in get_planets() ]

def get_planet_taglines():
    return [ p.get("tagline") for p in get_planets() ]

def get_planet_images():
    return

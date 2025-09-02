from pathlib import Path
import json
from functools import lru_cache

_PLANET_DATA_PATH = Path(__file__).with_name("planets.json")
_TIMELINE_DATA_PATH = Path(__file__).with_name("timeline.json")

@lru_cache(maxsize=1)
def _load_planets():
    try:
        return json.loads(_PLANET_DATA_PATH.read_text(encoding='utf-8'))
    except FileNotFoundError as e:
        raise RuntimeError(f"Missing data file: {_PLANET_DATA_PATH}") from e
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON in {_PLANET_DATA_PATH}") from e

@lru_cache(maxsize=1)
def _load_timelines():
    try:
        return json.loads(_TIMELINE_DATA_PATH.read_text(encoding='utf-8'))
    except FileNotFoundError as e:
        raise RuntimeError(f"Missing data file: {_TIMELINE_DATA_PATH}") from e
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON in {_TIMELINE_DATA_PATH}") from e

def get_planet_main_data(planet):
    return planet.get("mainData")

def get_planets() -> list:
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

def get_timeline() -> list:
    return list(_load_timelines().values())

def get_decades() -> list:
    return list(_load_timelines().keys())

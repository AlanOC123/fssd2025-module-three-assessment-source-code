from pathlib import Path
import json
from functools import lru_cache

_PLANET_DATA_PATH = Path(__file__).with_name("planets.json")
_TIMELINE_DATA_PATH = Path(__file__).with_name("timeline.json")
_ASSETS_DATA_PATH = Path(__file__).with_name("asset-manifest.json")

def _load_file(path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except FileNotFoundError as e:
        raise RuntimeError(f"Missing data file: {path}") from e
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON in {path}") from e

@lru_cache(maxsize=1)
def _load_planets():
    return _load_file(_PLANET_DATA_PATH)

@lru_cache(maxsize=1)
def _load_timelines():
    return _load_file(_TIMELINE_DATA_PATH)
    
@lru_cache(maxsize=1)
def _load_assets():
    return _load_file(_ASSETS_DATA_PATH)

def get_assets_map():
    return _load_assets()

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

def get_timeline_data(timeline_id):
    timelines = _load_timelines();
    timeline = timelines.get(timeline_id)
    return dict(timeline)

def get_decades() -> list:
    return list(_load_timelines().keys())

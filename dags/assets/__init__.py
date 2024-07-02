from dagster import load_assets_from_modules

from dags.assets.overpass_data import (
    download_overpass_data
    , clean_data
    , create_map
)

OVERPASS_DATA = load_assets_from_modules([
    download_overpass_data,
    clean_data,
    create_map
])





from dagster import load_assets_from_modules

from dags.maps import (
    download_overpass_data
)

MAPS = load_assets_from_modules([
    download_overpass_data
])
from dagster import load_assets_from_modules

from dags.assets.overpass_data import (
    download_overpass_data
    , clean_data
    , create_map
)

from dags.assets.trends_elixir import (
    download_trends_data
)

OVERPASS_DATA = load_assets_from_modules([
    download_overpass_data,
    clean_data,
    create_map,
    download_trends_data
])





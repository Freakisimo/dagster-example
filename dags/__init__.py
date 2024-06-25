from dagster import Definitions

from dags.assets import OVERPASS_DATA

defs = Definitions(
    assets=OVERPASS_DATA
)
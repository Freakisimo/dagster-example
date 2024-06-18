from dagster import Definitions

from dags.maps import MAPS

defs = Definitions(
    assets=MAPS
)
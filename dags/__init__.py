from dagster import Definitions

from dags.assets import OVERPASS_DATA

from dags.defs import JOBS, SCHEDULES

defs = Definitions(
    assets=OVERPASS_DATA
    , jobs=JOBS
    , schedules=SCHEDULES
)
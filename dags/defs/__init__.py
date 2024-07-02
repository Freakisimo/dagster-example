from dags.defs.jobs import (
    overpass_job
)

from dags.defs.schedules import(
    overpass_schedule
)

JOBS = [
    overpass_job,
]

SCHEDULES = [
    overpass_schedule
]
from dagster import ScheduleDefinition

from dags.defs.jobs import (
    overpass_job,
)

overpass_schedule = ScheduleDefinition(
    job=overpass_job,
    cron_schedule='0 0 1 * *'
)
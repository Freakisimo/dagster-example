from dagster import DailyPartitionsDefinition

dayly_partition = DailyPartitionsDefinition(
    start_date = '2024-01-01'
)
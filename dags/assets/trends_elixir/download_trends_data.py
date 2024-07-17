from dagster import asset
from pytrends.request import TrendReq
import pandas as pd

from dags.defs.partitions import dayly_partition

GROUP_NAME = 'download_trends'

@asset(
    group_name=GROUP_NAME
    , partitions_def=dayly_partition
)
def get_trends_data(context) -> pd.DataFrame:
    partition = context.asset_partition_key_for_output()

    start_hour = f'{partition}T00'
    end_hour = f'{partition}T23'
    timeframe = f'{start_hour} {end_hour}'

    context.log.info(timeframe)

    pt = TrendReq()
    kw_list = ["elixir lang"]
    pt.build_payload(kw_list, cat=0, timeframe=timeframe)
    df = pt.interest_by_region()
    return df
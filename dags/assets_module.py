from dagster import asset

@asset
def call_none() -> None:
    print('asset')
    pass

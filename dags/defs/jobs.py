from dagster import AssetSelection, define_asset_job

overpass_job = define_asset_job(
    name='overpass_job',
    selection=AssetSelection.groups('*overpass*')
)
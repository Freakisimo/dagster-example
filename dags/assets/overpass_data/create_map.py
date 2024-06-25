from dagster import asset

from dags.assets.overpass_data.download_overpass_data import create_data

import folium

GROUP_NAME = 'create_map'

@asset(
    group_name=GROUP_NAME
)
def marker_map(context, create_data: list):
    m = folium.Map(location=(19.5236, -99.6750))
    m.save("dags/maps/index.html")
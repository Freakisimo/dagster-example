from dagster import asset

from dags.assets.overpass_data.clean_data import sanitized_data

import folium
from folium.plugins import MarkerCluster, BeautifyIcon

GROUP_NAME = 'create_overpass_map'

@asset(
    group_name=GROUP_NAME
)
def marker_map(context, sanitized_data: list):
    m = folium.Map(location=(19.5236, -99.6750), zoom_start=6)

    marker_cluster = MarkerCluster().add_to(m)

    for entry in sanitized_data:

        icon = BeautifyIcon(
            icon='cutlery',
            icon_shape='marker',
            border_color='#00AA00',
            text_color='#FFFFFF',
            background_color='#00AA00',
            inner_icon_style='font-size:12px;padding:2px;'
        )

        folium.Marker(
            location=[float(entry['lat']), float(entry['lon'])],
            popup=f"{entry['name']}<br>Brand: {entry['brand']}<br>Cuisine: {entry['cuisine']}",
            tooltip=entry['name'],
            icon=icon
        ).add_to(marker_cluster)


    m.save("dags/maps/index.html")
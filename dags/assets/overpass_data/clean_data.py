from dagster import asset

import re
import html

from dags.assets.overpass_data.download_overpass_data import create_data

GROUP_NAME = 'clean_overpass_data'

@asset(
    group_name=GROUP_NAME
)
def clean_name(context, create_data: list) -> list:
    for item in create_data:
        name = item.get('name', '')
        clean_name = re.sub(r'[,"\'`]', '', name)
        item['name'] = clean_name
    return create_data


@asset(
    group_name=GROUP_NAME
)
def sanitized_data(context, clean_name: list) -> list:
    for item in clean_name:
        item['name'] = html.escape(item['name'])
        item['brand'] = html.escape(item['brand'])
        item['cuisine'] = html.escape(item['cuisine'])
    return clean_name



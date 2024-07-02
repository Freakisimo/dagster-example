from dagster import asset
import overpy

GROUP_NAME = 'download_overpass_data'

QUERY = """
[out:json];
area["ISO3166-1"="MX"][admin_level=2];
(
    node["{ntype}"="{nsubtype}"](area);
);
out;
"""

TYPES = {
    "amenity": ["restaurant", "cafe", "fast_food","nightclub", "bar"]
}

@asset(
    group_name=GROUP_NAME
)
def build_queries(context) -> list:
    query_list = [
        QUERY.format(**{'ntype':ntype, 'nsubtype':nsubtype})
            for ntype, subtypes in TYPES.items() 
            for nsubtype in subtypes
        ]
    context.log.info(query_list)
    return query_list



@asset(
    group_name=GROUP_NAME
)
def create_data(context, build_queries: list) -> list:
    api = overpy.Overpass()
    places = []
    for qry in build_queries:
        result = api.query(qry)
        for node in result.nodes:
            place = {
                'name': node.tags.get('name', 'no proporcionado'),
                'brand': node.tags.get('brand', 'no proporcionado'),
                'cuisine': node.tags.get('cuisine', 'no proporcionado'),
                'lat': node.lat,
                'lon': node.lon,
                'id': node.id
            }
            places.append(place)
    context.log.info(places)
    return places
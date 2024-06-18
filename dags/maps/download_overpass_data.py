from dagster import asset, op, OpExecutionContext
import overpy

GROUP_NAME = 'overpass_download'

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
def build_queries(context: OpExecutionContext) -> list:
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
def create_query(context, build_queries: list) -> list:
    api = overpy.Overpass()
    places = []
    for qry in build_queries:
        result = api.query(qry)
        for node in result.nodes:
            place = {
                'name': node.tags.get('name', 'n/a'),
                'brand': node.tags.get('brand', 'n/a'),
                'cuisine': node.tags.get('cuisine', 'n/a'),
                'lat': node.lat,
                'lon': node.lon,
                'id': node.id
            }
            places.append(place)
    context.log.info(places)
    return places
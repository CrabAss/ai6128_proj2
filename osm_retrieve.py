import osmnx as ox

# place_county = "Porto, Tâmega e Sousa, North, Portugal"
# G = ox.graph_from_place(place_county, network_type='drive', which_result=0)
# ox.save_graphml(G, 'data/porto-county.graphml')

x_min, x_max, y_min, y_max = -8.709399, -8.486757, 41.008275, 41.260086
G = ox.graph_from_bbox(north=y_max, south=y_min, west=x_min, east=x_max, network_type='drive')
ox.save_graphml(G, 'data/porto-bbox.graphml')



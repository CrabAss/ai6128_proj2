import osmnx as ox
import os


def save_graph_shapefile_directional(G, filepath=None, encoding="utf-8"):
    # default filepath if none was provided
    if filepath is None:
        filepath = os.path.join(ox.settings.data_folder, "graph_shapefile")

    # if save folder does not already exist, create it (shapefiles
    # get saved as set of files)
    if not filepath == "" and not os.path.exists(filepath):
        os.makedirs(filepath)
    filepath_nodes = os.path.join(filepath, "nodes.shp")
    filepath_edges = os.path.join(filepath, "edges.shp")

    # convert undirected graph to gdfs and stringify non-numeric columns
    gdf_nodes, gdf_edges = ox.utils_graph.graph_to_gdfs(G)
    gdf_nodes = ox.io._stringify_nonnumeric_cols(gdf_nodes)
    gdf_edges = ox.io._stringify_nonnumeric_cols(gdf_edges)
    # We need an unique ID for each edge
    gdf_edges["fid"] = gdf_edges.index
    # save the nodes and edges as separate ESRI shapefiles
    gdf_nodes.to_file(filepath_nodes, encoding=encoding)
    gdf_edges.to_file(filepath_edges, encoding=encoding)


# place_county = "Porto, Tâmega e Sousa, North, Portugal"
# G = ox.graph_from_place(place_county, network_type='drive', which_result=0)
# ox.save_graphml(G, 'data/porto-county.graphml')

x_min, x_max, y_min, y_max = -8.709399, -8.486757, 41.008275, 41.260086
G = ox.graph_from_bbox(north=y_max, south=y_min, west=x_min, east=x_max, network_type='drive')
# ox.save_graphml(G, 'data/porto-bbox.graphml')

save_graph_shapefile_directional(G, filepath='data/porto-bbox')

import osmnx as ox
place = "Porto, Área Metropolitana do Porto, North, Portugal"
G = ox.graph_from_place(place, network_type='drive', which_result=1)
ox.save_graphml(G, 'data/porto.graphml')
from typing import List, Dict, Set
from collections import defaultdict
# Clump in a phylogenetic tree is called a taxon (taxa plural)
import sys
from io import TextIOWrapper
def old_method(num_nodes:int, graph_list:List):
    # First convert edge list to adjacency dict that is bidirectional 
    graph:Dict[str,Set] = dict()
    
    edges = list(map(str.split, graph_list))
    for edge in edges:
        if graph.get(edge[0]) is None:
            graph[edge[0]] = set()
        graph[edge[0]].add(edge[1])
        if graph.get(edge[1]) is None:
            graph[edge[1]] = set()
        graph[edge[1]].add(edge[0])

    
    # Walk through the graph defining all clusters/connected groups
    visited = set()
    clusters = list()
    for node in list(graph.keys()):
        # Start at the node
        # print(f"node{node}")
        to_visit = [node]
        cluster = set() # Define the cluster, a set of nodes that are connected
        while len(to_visit) > 0 and to_visit[0] not in visited:
            curr = to_visit.pop(0)

            visited.add(curr) # Visit the current node, add to cluster
            cluster.add(curr)
            # print(f"curr{curr}")

            # add child nodes to the next up queue
            # Visit all connected nodes in a walk
            
            children = graph.get(curr) 
            ch_arr = children - visited if children is not None else []
            to_visit.extend(ch_arr)  

        if len(cluster) > 0:
            clusters.append(cluster)
   



    # If we already know the graph has no cycles, its clusters have no cycles either
    # Therefore we can connect each cluster to the other clusters with just one edge
    cluster_count = len(clusters)
    min_edge = 0
    if cluster_count > 1:
        min_edge = min_edge + cluster_count - 1
    else:
        min_edge = cluster_count
    

    # For the isolated (non seen in any walks, we can connect one edge to each node to a poitn in the graph)
    isolated_nodes = num_nodes  - len(visited) 
    min_edge = min_edge + isolated_nodes
    print(min_edge)

def constant_time_method(num_nodes:int, graph_list:List):
    return num_nodes -1 - len(graph_list)
dataset_name = sys.argv[1]

with open(dataset_name, "r") as data_set:
    num_nodes = int(data_set.readline())
    graph_list =data_set.readlines()
    # old_method(num_nodes, graph_list)
    print(constant_time_method(num_nodes, graph_list))
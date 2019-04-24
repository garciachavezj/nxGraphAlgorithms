from functions.global_properties import *
from functions.local_properties import *

G = nx.read_edgelist('graph_library/G1.txt')

def greedy_proper_coloring(G):
    colored_verticies = {v: None for v in V(G)}
    for v in V(G):
        avoid_colors = [colored_verticies[j] for j in neighbors(G, v)]
        i = 1
        while colored_verticies[v] == None:
            if i in avoid_colors:
                i += 1
            else:
                colored_verticies[v] = i
    return colored_verticies

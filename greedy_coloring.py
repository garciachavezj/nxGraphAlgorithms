from functions.global_properties import *
from functions.local_properties import *

def greedy_proper_coloring(G)
    colored_verticies = {v: None for v in V(G)}
    colored_verticies[V(G)[0]] = 1
    for v in V(G):
        if colored_verticies[v] == None:
            N = neigbors(G, v)
            avoid_colors = [colors[w] for w in N]
            i = 1
            while colored_verticies[v] == None:
                if i in avoid_colors:
                    i += 1
                else:
                    colored_verticies[v] = i
    return colored_verticies
  

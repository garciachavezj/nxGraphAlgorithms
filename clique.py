import networkx as nx

from functions.global_properties import *
from functions.local_properties import *

G = nx.read_edgelist('graph_library/G1.txt')


def is_clique(G, S):
    for v in S:
        for w in v:
            path = neighbors(G, v)
            if(w == v):
                continue
            elif(path != None and w not in path):
                return False
    return True

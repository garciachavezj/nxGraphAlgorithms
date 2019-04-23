import networkx as nx
from functions.global_properties import *
from functions.local_properties import *

G = nx.read_edgelist('graph_library/G1.txt')



def is_matching(G, M): 
    n_list = []
    switch = True
    G_edges = E(G)
    
    for e in M:
        if e not in G_edges:
            switch = False
    if switch is True:
        for outter in M:
            temp = outter[1]
            n_list.append(temp)
        for outter in M:
            temp = outter[0]
            if temp in n_list:
                return False

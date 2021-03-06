import networkx as nx

from functions.global_properties import *
from functions.local_properties import *

G = nx.read_edgelist('graph_library/G1.txt')


def is_clique(G,S): # S = M1 = [('0','1'),('4','6')]  
    answer = True
    if all(x in (E(G)) for x in S):
        node_list = []  #collection of all nodes that appear in edge list
        for v in S:
            for w in v:
                node_list.append(w)
                total_nodes = set(node_list) # total_nodes is a set of all nodes in edge list i.e. [0,1,2]
        for x in total_nodes:
            if node_list.count(x) == len(total_nodes)-1:
                continue
            else:
                answer = False
    else:
        answer = False
    return answer

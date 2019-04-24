import networkx as nx

G = nx.read_edgelist('graph_library/G1.txt')

def neighbors(G,v):
    return list(nx.neighbors(G,v)) # requires 'v'
                                # returns each other node connected to the vert

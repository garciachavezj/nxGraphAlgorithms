import networkx as nx

G = nx.read_edgelist('test_graphs/G1.txt')

def V(G):
  return nx.nodes(G)

def E(G):
  return nx.edges(G)

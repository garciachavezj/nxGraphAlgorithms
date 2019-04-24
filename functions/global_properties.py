import networkx as nx
G = nx.read_edgelist('graph_library/G1.txt')


def V(G):              # prints all of a graph's nodes
    return nx.nodes(G) # produces: ['0', '1', '2', '3', '4', '5', '6', '7', '9', '8', '10']

def E(G):
    return nx.edges(G) #prints the edge list for a graph
                       #produces: [('0', '1'), ('0', '2'), ('0', '3'), ('0', '4'), ('0', '5'), ('1', '2'), ('1', '3'), ('2', '3'), ('4', '6'), ('5', '7'), ('5', '9'), ('6', '7'), ('6', '8'), ('9', '10')]

def n(G):
    return len(V(G)) #prints number of graph nodes
                     #produces: 11 
def m(G):
    return len(E(G)) #prints edges for a graph
                     #produces: 14
                     
def degree_sequence(G):
    D = [degree(G, v) for v in V(G)]
    D.sort(reverse = True)
    return D           #returns the degree of each vert in descending order
                     
def radius(G):
    return min([eccentricity(G,v) for v in V(G)])   #works

def diameter(G):
    return max([eccentricity(G, v) for v in V(G)]) #works

def maximum_degree(G):
    return degree_sequence(G) [0]  #works

def minimum_degree(G):
    return degree_sequence(G) [-1]  #works

def avg_degree(G):
    return sum(degree_sequence(G)) /n(G) #works

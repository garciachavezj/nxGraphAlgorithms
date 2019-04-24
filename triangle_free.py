import networkx as nx

G = nx.read_edgelist('test_graphs/G1.txt')

print('The graph vertices are {}'.format(V(G)))
print('The graph edges are {}'.format(E(G)))

def triangle_free(G):
    for edge in E(G):
        u,v=edge
        for vertex in V(G):
            
            if vertex in edge:
                continue
            if (u,vertex) in E(G) or (vertex,u) in E(G):
                if (v,vertex) in E(G) or (vertex,v) in E(G):
                    print('Triangle found with vertices {} {} {}'.format(u,v,vertex))
                    return False
    return True

print('Triangle free? {}'.format(triangle_free(G)))

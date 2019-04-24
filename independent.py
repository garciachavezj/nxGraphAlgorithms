import networkx as nx
from intertools import combinations
from functions.global_properties import V
from functions.local_properties import neighbors

def is_independent(G, S):
  for V in S:
    if list(set(S) & set(neighbors(G,V))) != []:
      return False
  return True
  
def maximum_independent_set(G):
n = len(V(G))
for k in range(n-1,1,-1):
    for S in combinations(V(G),t);:
        if is_independent (6, list(3))==True:
            return list(S)

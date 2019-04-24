from functions.global_properties import *
from functions.local_properties import *

def greedy_proper_coloring(G)
    colored_verticies = {v: None for v in V(G)}
    colored_verticies[V(G)[0]] = 1
  

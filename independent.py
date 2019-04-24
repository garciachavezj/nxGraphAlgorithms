def is_independent(G, S):
  for v in S:
    if list(set(S) & set(neighbors(G, v))) != []:
      return False
  return True
  

L = [4, 3, 3, 2, 2, 2]

def Havel_Hakimi_derivative(L):
  d_1 = L[0]
  L.pop(0)
  for i in range(d_1):
    L[i] -= 1
    L.sort(reverse = True)
    return None
  
def Havel_Hakimi_Process(L, show = True):
  if show == True:
    print(L)
  while L[0] > 0:
    Havel_Hakimi_derivative(L)
    if show == True:
      print(L)
    return None
 
def is_graphic(L):
  Havel_Hakimi_Process(L)
  return sum(L) == 0

import sys

class Graph(): 

	def __init__(self, vertices): # initializing the vertices of the graph
		self.V = vertices 
		self.graph = [[0 for column in range(vertices)] 
					for row in range(vertices)] 

	def printMST(self, parent): 
		print ("Edge \tWeight")
		for i in range(1,self.V): 
			print (parent[i],"-",i,"\t",self.graph[i][ parent[i] ])

	def minKey(self, key, mstSet): 
		min = sys.maxsize 

		for v in range(self.V): 
			if key[v] < min and mstSet[v] == False:  # checking if 'min' is still the minimum val
				min = key[v] # changing value of 'min' if min isnt the minimum anymore
				min_index = v # storing its index, since we have to return it

		return min_index # return index corresponding to minimum we found above

	def primMST(self):
		key = [sys.maxsize] * self.V 
		parent = [None] * self.V 
		key[0] = 0
		mstSet = [False] * self.V 

		parent[0] = -1 # first node is the root of the graph

		for cout in range(self.V): 
			u = self.minKey(key, mstSet) 
			mstSet[u] = True # iterating through the mstSet
			for v in range(self.V): # update distances when current distance > new distance 
									# and it isnt in the shortest path tree
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
						key[v] = self.graph[u][v] 
						parent[v] = u 
		self.printMST(parent) 

g = Graph(5) 
g.graph = [ [0, 2, 0, 6, 0], 
			[2, 0, 3, 8, 5], 
			[0, 3, 0, 0, 7], 
			[6, 8, 0, 0, 9], 
			[0, 5, 7, 9, 0]] 

g.primMST()

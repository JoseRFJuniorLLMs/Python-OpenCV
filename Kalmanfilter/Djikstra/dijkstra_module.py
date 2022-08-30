# Python program for Dijkstra's single 
# source shortest path algorithm. The program is 
# for adjacency matrix representation of the graph 

#Website Reference:
#https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

import sys

class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printSolution(self, dist): 
        print ("Vertex \tDistance from Source")
        for node in range(self.V): 
            print (node, "\t", dist[node]) 
  
    def minDistance(self, dist, sptSet):
        min = sys.maxsize
  
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v
                #print(v)
  
        return min_index 
  

    def dijkstra(self, src): 
  
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V

        paths = []  #Added list to track sequence of vertices in the path
  
        for cout in range(self.V): 
  
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
  
            for v in range(self.V):
                #print(u,v, self.graph[u][v])
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v]
                        #print("selected:", u,v, self.graph[u][v])
                        #print("path length", dist[v])
                        paths.append((u,v,self.graph[u][v], dist[v]))
  
        self.printSolution(dist)
        #print(paths)
        return paths

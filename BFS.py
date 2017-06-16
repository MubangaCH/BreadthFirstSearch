#finds the shortest paths between two cities using breadth first search

import sys 
from collections import deque

def Breadth_first_search(adj, start, end):
    
   
    frontier=deque() #create a queue to add unexplored cities
    frontier.append(start) #add the start city 
    
    dist = [len(adj)] * len(adj) #initialize a list to store maximum distances (infity) from start to each city
    dist[start] = 0 # give the start city the smallest distance
    
    while frontier:
        
		current_city=frontier.popleft()
        
        for neighbor in adj[current_city]: #traverse each neighbor of the current city 
            if dist[neighbor] == len(adj): #check if node hasn't been discovered yet
                frontier.append(neighbor) # add unexplored neighbors to frontier
                dist[neighbor]=dist[current_city] + 1 #update the distance of the neighbor with a finite value after it's been discovered
    
    if dist[end] != len(adj):
        return dist[end]
    
    return -1 #returns -1 for a city that can't be visited from the start

	#allows you to enter your own data as a graph.
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2] # n is the number of vertices (cities) in your graph, m is the number of edges (paths) between your vertices
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    #creates adjacency list
	adj = [[] for _ in range(n)] 
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    start, end = data[2 * m] - 1, data[2 * m + 1] - 1
    print(Breadth_first_search(adj, start, end))
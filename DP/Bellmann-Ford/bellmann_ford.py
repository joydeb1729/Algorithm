import sys
INF = sys.maxsize

'''
This Python program implements the Bellman-Ford algorithm to compute the shortest path 
from a single source vertex (vertex 1, represented as index 0 internally) to all other vertices in a directed weighted graph. 
The graph is input as a list of edges, where each edge contains the source vertex, destination vertex, and weight. 
The algorithm initializes all distances from the source as infinity, except the source itself which is 0. 
It then relaxes all edges (V-1) times to ensure the shortest distances are computed. 
The `parent` array is used to reconstruct the path from the source to each vertex. 
After the main loop, the program prints the cost and the actual path from the source to every vertex. 
If a vertex is unreachable, it displays an appropriate message.
'''

def print_path(parent, v):
    if v == -1:
        return []
    return print_path(parent, parent[v]) + [v + 1]

def bellman_ford(edges, V):
    parent = [-1] * V
    dist = [INF] * V
    dist[0] = 0  # Start from vertex 0 (which is vertex 1 for the user)

    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > w + dist[u]:
                dist[v] = w + dist[u]
                parent[v] = u

    for i in range(V):
        if dist[i] == INF:
            print(f'There is no path from 1 to {i + 1}')
        else:
            print(f'Cost from 1 to {i + 1} = {dist[i]}')
            path = print_path(parent, i)
            path_str = ' -> '.join(map(str, path))
            print(f'Path: {path_str}\n')

if __name__ == '__main__':
    V, E = map(int, input('Enter number of Vertices and Edges: ').split())
    edges = []
    print(f'Enter {E} edges in the format: src dst wt')
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append([u - 1, v - 1, w])

    bellman_ford(edges, V)
    
    
'''
Book Example:
V = 7, E = 10
src dst wt:
1 2 6
1 3 5
1 4 5
3 2 -2
4 3 -2
2 5 -1
3 5 1
4 6 -1
5 7 3
6 7 3    
'''
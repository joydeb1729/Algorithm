import sys
INF = sys.maxsize

'''
This function implements the Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices in a given weighted graph.
The input graph is represented as a 2D list, where graph[i][j] holds the weight of the edge from vertex i to vertex j. If there is no
direct edge between two vertices, the value is set to a very large number (INF) to simulate infinity. The algorithm initializes a distance
matrix with the original weights and then attempts to improve the shortest distance between every pair (i, j) by checking if an intermediate
vertex k offers a shorter path. If a shorter path is found via k, the distance is updated. This process is repeated for all vertices as
intermediate points. After all iterations, the matrix contains the shortest distances between all vertex pairs, which is then printed out
in a formatted way for easy interpretation.
'''

def all_pair_shortest_path(graph):
    V = len(graph)
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] == INF or dist[k][j] == INF:
                    continue
                dist[i][j] = min(dist[i][j], (dist[i][k] + dist[k][j]))

    [[print(f'{i+1} -> {j+1} = {dist[i][j]}') for j in range(V)] for i in range(V)]
    

if __name__ == '__main__':
    
    graph = [
        [0, 3, INF, 7],
        [INF, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ]
    
    all_pair_shortest_path(graph)

import sys
INF = sys.maxsize

def all_pair_shortest_path(graph):
    V = len(graph)
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] == INF or dist[k][j] == INF:
                    continue
                dist[i][j] = min(dist[i][j], (dist[i][k]+dist[k][j]))

    
    [[print(f'{i+1} -> {j+1} = {dist[i][j]}') for j in range(V)] for i in range(V)]
    

if __name__ == '__main__':
    
    graph = [
        [0, 3, INF, 7],
        [INF, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ]
    
    all_pair_shortest_path(graph)

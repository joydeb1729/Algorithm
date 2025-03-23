import sys

V = 8  # Number of vertices in the graph

def select_min_vertex(value, processed, V):
    """
    Selects the vertex with the minimum value that has not been processed yet.
    :param value: List of shortest path estimates for each vertex.
    :param processed: List indicating whether a vertex has been processed.
    :param V: Total number of vertices.
    :return: Index of the vertex with the smallest value.
    """
    minimum = sys.maxsize
    vertex = -1
    for i in range(V):
        if not processed[i] and value[i] < minimum:
            vertex = i
            minimum = value[i]
    return vertex

def dijkstra(graph, V, start):
    """
    Implements Dijkstra's algorithm to find the shortest paths from the start vertex.
    :param graph: Adjacency matrix representation of the graph.
    :param V: Total number of vertices.
    :param start: Starting vertex index.
    """
    parent = [-1] * V  # Stores shortest path structure
    value = [sys.maxsize] * V  # Keeps shortest path values to each vertex from source
    processed = [False] * V  # TRUE -> Vertex is processed
    
    value[start] = 0  # Start node has value=0 to get picked first
    
    for _ in range(V - 1):
        U = select_min_vertex(value, processed, V)  # Select the vertex with the smallest value
        if U == -1:
            break  # No more reachable vertices
        processed[U] = True  # Mark the vertex as processed
        
        for j in range(V):
            # Check if an edge exists, if the vertex is unprocessed, and if a shorter path is found
            if (graph[U][j] != 0 and not processed[j] and value[U] != sys.maxsize and
                    (value[U] + graph[U][j] < value[j])):
                value[j] = value[U] + graph[U][j]
                parent[j] = U  # Store the parent vertex in the shortest path
    
    # Print shortest path results
    for i in range(V):
        print(f'Source({start+1}) to node {i+1} cost = {value[i]}')
        

# Initialize graph with infinity values (unreachable paths)
graph = [[sys.maxsize for _ in range(8)] for _ in range(8)]

# Define graph connections and weights
graph[0][0] = 0
graph[1][0] = 300; graph[1][1] = 0
graph[2][0] = 1000; graph[2][1] = 800; graph[2][2] = 0
graph[3][2] = 1200; graph[3][3] = 0
graph[4][3] = 1500; graph[4][4] = 0; graph[4][5] = 250
graph[5][3] = 1000; graph[5][5] = 0; graph[5][6] = 900; graph[5][7] = 1400
graph[6][6] = 0; graph[6][7] = 1000
graph[7][0] = 1700; graph[7][7] = 0

start = 4  # Starting vertex index
dijkstra(graph, V, start)
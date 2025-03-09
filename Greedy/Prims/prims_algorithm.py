def find_min_vertex(V, value, visited):
    minVal = float('inf')  
    vertex = -1  
    for i in range(V):
        # Check if the vertex is not yet included in the MST and has a smaller value
        if not visited[i] and value[i] < minVal:
            vertex = i  
            minVal = value[i]  
    return vertex  # Return the vertex with the minimum value

def prims_algo(graph, V):
    parent = [-1] * V  # Array to store the parent of each vertex in the MST
    value = [float('inf')] * V  # Array for edge relaxation, initialized to infinity
    visited = [False] * V  # Boolean array to track if a vertex is included in the MST
    
    value[0] = 0  # Start from vertex 0, set its value to 0
    
    for _ in range(V - 1):
        # Select the best vertex using a greedy approach
        u = find_min_vertex(V, value, visited)
        visited[u] = True  # Mark the selected vertex as included in the MST
        
        # Relax adjacent vertices that are not yet in MST
        for j in range(V):
            # Conditions for relaxing edge (u, j):
            # 1. There is an edge from u to j (graph[u][j] != 0)
            # 2. Vertex j is not in MST (visited[j] is False)
            # 3. The edge weight from u to j is smaller than the current value of vertex j
            if graph[u][j] != 0 and not visited[j] and graph[u][j] < value[j]:
                value[j] = graph[u][j]  # Update the value (edge weight) for vertex j
                parent[j] = u  # Set the parent of vertex j to u

    return parent  # Return the parent array representing the MST

if __name__ == '__main__':
    # Adjacency matrix representation of the graph
    graph = [
        [0, 11, 13, 0, 2, 0, 0, 0],  
        [11, 0, 15, 8, 12, 0, 6, 0],  
        [13, 15, 0, 0, 0, 0, 0, 0],  
        [0, 8, 0, 0, 14, 0, 10, 17], 
        [2, 12, 0, 14, 0, 5, 0, 0],  
        [0, 0, 0, 0, 5, 0, 0, 7],    
        [0, 6, 0, 10, 0, 0, 0, 21],  
        [0, 0, 0, 17, 0, 7, 21, 0]   
    ]
    
    V = len(graph)  # Get the number of vertices in the graph
    
    # Call the function to find the MST of the graph
    mst = prims_algo(graph, V)
    
    total_cost = 0  
    
    # Print the edges and their costs in the MST
    for i in range(1, V):
        print(f"Path: {mst[i]+1} -> {i+1} : cost = {graph[i][mst[i]]}") #added 1 to get actuall vertex numbers
        total_cost += graph[i][mst[i]]  

    # Print the total cost of the MST
    print(f"Total Cost = {total_cost}")

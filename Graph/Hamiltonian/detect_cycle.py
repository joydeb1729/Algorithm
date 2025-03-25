class Graph:
    def __init__(self, V):
        """
        Initializes a graph with V vertices and an empty adjacency list for each vertex.

        Parameters:
        V (int): The number of vertices in the graph.
        """
        self.V = V
        self.adj_list = [[] for _ in range(V)]  # Create an empty adjacency list for each vertex
    
    def add_edge(self, v, w):
        """
        Adds an edge between vertex v and vertex w in an undirected graph.

        Parameters:
        v (int): The first vertex of the edge.
        w (int): The second vertex of the edge.
        """
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)
        
    def printCycle(self, path):
        """
        Prints the Hamiltonian cycle.

        Parameters:
        path (list): A list of vertices representing the Hamiltonian cycle.
        """
        for vertex in path:
            print(vertex, end=' ')  # Print each vertex in the cycle
        print()  # Print newline after the cycle
    
    def isValid(self, vertex, pos, path):
        """
        Checks if a vertex can be added to the Hamiltonian cycle path.

        Parameters:
        vertex (int): The vertex to be checked.
        pos (int): The current position in the path where the vertex is to be added.
        path (list): The list representing the current path.

        Returns:
        bool: True if the vertex can be added, False otherwise.
        """
        # Ensure the vertex is adjacent to the previous vertex in the path
        if vertex not in self.adj_list[path[pos - 1]]:
            return False
        
        # Ensure the vertex is not already in the path
        if vertex in path:
            return False
        
        return True
    
    def search(self, path, pos):
        """
        Recursively searches for a Hamiltonian cycle in the graph using backtracking.

        Parameters:
        path (list): The list representing the current path.
        pos (int): The current position in the path being explored.

        Returns:
        bool: True if a Hamiltonian cycle is found, False otherwise.
        """
        if pos == self.V:  # All vertices are included in the path
            # Check if the last vertex connects to the first vertex
            if path[0] in self.adj_list[path[pos - 1]]:
                return True
        
        # Try adding each vertex to the path and recursively search further
        for vertex in range(1, self.V):
            if self.isValid(vertex, pos, path):
                path[pos] = vertex  # Add vertex to path
                
                # Recursively try to add the next vertex
                if self.search(path, pos + 1):
                    return True
    
                # If adding vertex doesn't lead to a solution, backtrack
                path[pos] = -1
        
        return False
    
    def find_hamiltonian_cycle(self):
        """
        Attempts to find a Hamiltonian cycle in the graph.

        If a Hamiltonian cycle is found, it prints the cycle. 
        If not, it prints a message indicating that no cycle was found.
        """
        path = [-1] * self.V  # Initialize path with -1
        path[0] = 0  # Start the path from vertex 0
        
        # Call the recursive search function to find a Hamiltonian cycle
        if self.search(path, 1):
            print('Hamiltonian Cycle detected:')
            self.printCycle(path)  # Print the found cycle
        else:
            print('No Hamiltonian Cycle.')  # If no cycle is found, print this message


# Example Usage

# Create a graph with 5 vertices
g1 = Graph(5)
edges = [(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4)]  # Define edges for graph 1
for u, v in edges:
    g1.add_edge(u, v)  # Add each edge to the graph

g1.find_hamiltonian_cycle()  # Find and print Hamiltonian cycle for g1

# Create a graph with 5 vertices for testing
g2 = Graph(5)
edges2 = [(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 4)]  # Define edges for graph 2
for u, v in edges2:
    g2.add_edge(u, v)  # Add each edge to the graph

g2.find_hamiltonian_cycle()  # Find and print Hamiltonian cycle for g2



# Graph1->
#        0
#       / \
#      /   \
#     1-----3
#    / \   / 
#   2----4

# Graph2 ->
#        0
#       / \
#      /   \
#     1-----3
#    / \   
#   2----4




# Expected Output ->
# Graph1->
# Hamiltonian Cycle detected:
# 0 1 2 4 3 

# Graph2->
# No Hamiltonian Cycle.


class Graph:
    def __init__(self, V):
        """
        Initializes a graph with V vertices.
        
        :param V: Number of vertices in the graph
        """
        self.V = V  # Store the number of vertices
        # Initialize adjacency list with empty lists for each vertex
        self.adj_list = [[] for _ in range(V)]

    def add_edge(self, v, w):
        """
        Adds an undirected edge between vertices v and w.
        
        :param v: The starting vertex of the edge
        :param w: The ending vertex of the edge
        """
        # Add w to the adjacency list of v and vice versa (undirected edge)
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)

    def printCycle(self, path):
        """
        Prints the Hamiltonian cycle represented by the path.
        
        :param path: The list of vertices in the current Hamiltonian cycle
        """
        for vertex in path:
            print(vertex, end=' ')  # Print each vertex in the cycle
        print(path[0])  # Print starting of the cycle

    def isValid(self, vertex, path, pos):
        """
        Checks if a vertex can be added to the current path at position pos.
        
        :param vertex: The vertex to be added to the path
        :param path: The current path of vertices
        :param pos: The current position in the path
        :return: True if the vertex can be added, False otherwise
        """
        # Check if the vertex is adjacent to the last added vertex in the path
        if vertex not in self.adj_list[path[pos - 1]]:
            return False
        
        # Check if the vertex has already been added to the path
        if vertex in path:
            return False
        
        return True

    def search(self, path, pos):
        """
        Recursively searches for all Hamiltonian cycles in the graph.
        
        :param path: The current path of vertices
        :param pos: The current position in the path
        """
        # Base case: if all vertices are included in the path
        if pos == self.V:
            # If the last vertex is adjacent to the first vertex, print the cycle
            if path[0] in self.adj_list[path[pos - 1]]:
                self.printCycle(path)
            return
        
        # Try adding each vertex to the path
        for vertex in range(1, self.V):
            if self.isValid(vertex, path, pos):  # Check if the vertex is safe to add
                path[pos] = vertex  # Add vertex to the path
                
                # Recur to add the next vertex to the path
                self.search(path, pos + 1)
                
                # Backtrack: remove vertex from the path if it doesn't lead to a solution
                path[pos] = -1

    def find_hamiltonian_cycles(self):
        """
        Initializes the search for Hamiltonian cycles and starts the recursive process.
        """
        # Initialize the path with -1 for each vertex, and start from vertex 0
        path = [-1] * self.V
        path[0] = 0  # Start the cycle from vertex 0
        
        # Start the recursive search for Hamiltonian cycles
        self.search(path, 1)


# Example Usage

# Test graph 1 with Hamiltonian cycles
g = Graph(5)  # Create a graph with 5 vertices
edges = [(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4)]  # Define edges for graph 1
for u, v in edges:
    g.add_edge(u, v)  # Add each edge to the graph

g.find_hamiltonian_cycles()  # Find and print all Hamiltonian cycles for g1


#        0
#       / \
#      /   \
#     1-----3
#    / \   / 
#   2----4

# Expected output:
# 0 1 2 4 3 0
# 0 3 4 2 1 0

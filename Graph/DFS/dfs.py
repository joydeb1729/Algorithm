class Graph:
    def __init__(self, V):
        self.V = V  # Number of vertices in the graph
        self.adj_list = [[] for _ in range(V)]  # Adjacency list representation
    
    def add_edge(self, v, w):
        """Adds a directed edge from vertex v to vertex w."""
        self.adj_list[v].append(w)
        
    def dfs(self, start_v):
        """Performs Depth First Search (DFS) starting from vertex v."""
        visited = [False] * self.V  # Initialize all vertices as not visited
        self.search(visited, start_v)  # Start DFS traversal
        
    def search(self, visited, v):
        """Recursive function to visit nodes in DFS manner."""
        visited[v] = True  # Mark the current node as visited
        print(v, end=" ")  # Print the current node
        
        # Recur for all adjacent vertices that have not been visited
        for neighbour in self.adj_list[v]:
            if not visited[neighbour]:
                self.search(visited, neighbour)




# Driver code to test the implementation
g = Graph(8)  # Create a graph with 8 vertices
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(3, 7)
g.add_edge(4, 7)
g.add_edge(5, 6)
g.add_edge(6, 7)

start_v = 0

print("Following is Depth First Traversal (starting from vertex 0)")
g.dfs(start_v)  # Perform DFS starting from vertex 0

# Expected Output:
# Following is Depth First Traversal (starting from vertex 0)
# 0 1 3 7 4 2 5 6

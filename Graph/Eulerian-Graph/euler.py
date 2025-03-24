class Graph:
    def __init__(self, V):
        """
        Initializes a graph with V vertices.
        :param V: Number of vertices in the graph
        """
        self.V = V
        self.adj_list = [[] for _ in range(V)]  # Adjacency list representation of the graph
        
    def add_edge(self, v, w):
        """
        Adds an undirected edge between vertex v and vertex w.
        :param v: First vertex
        :param w: Second vertex
        """
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)
        
    def dfs(self, visited, v):
        """
        Depth-First Search (DFS) traversal to mark visited vertices.
        :param visited: List of visited vertices
        :param v: The current vertex being visited
        """
        visited[v] = True
        for neighbour in self.adj_list[v]:
            if not visited[neighbour]:
                self.dfs(visited, neighbour)
                
    def is_connected(self, visited):
        """
        Checks if the graph is connected (i.e., all non-isolated vertices are reachable from any other vertex).
        :param visited: List of visited vertices
        :return: True if the graph is connected, False otherwise
        """
        start_v = -1
        
        # Find the first non-isolated vertex
        for i in range(self.V):
            if len(self.adj_list[i]) > 0:
                start_v = i
                break
            
        if start_v == -1:  # If all vertices are isolated, consider it connected
            return True
        
        # Perform DFS from the first non-isolated vertex
        self.dfs(visited, start_v)
        
        # Check if all non-isolated vertices were visited
        for i in range(self.V):
            if not visited[i] and len(self.adj_list[i]) > 0:
                return False
        
        return True
    
    def find_euler_type(self):
        """
        Determines the Eulerian nature of the graph.
        :return: 0 (Not Eulerian), 1 (Semi-Eulerian), or 2 (Eulerian)
        """
        visited = [False] * self.V
        
        # Check if the graph is connected
        if not self.is_connected(visited):
            return 0
        
        # Count the number of vertices with an odd degree
        odd_degree_count = 0
        for i in range(self.V):
            if len(self.adj_list[i]) % 2 == 1:
                odd_degree_count += 1
        
        if odd_degree_count > 2:
            return 0  # More than two vertices with odd degree means no Eulerian path or circuit
        elif odd_degree_count == 0:
            return 2  # Eulerian circuit (all vertices have even degree)
        else:
            return 1  # Semi-Eulerian (exactly two vertices have odd degree)
        
    def euler_type(self):
        """
        Prints the type of Eulerian property the graph holds.
        """
        e_type = self.find_euler_type()
        
        if e_type == 0:
            print("Graph is NOT a Euler graph")
        elif e_type == 1:
            print("Graph is Semi-Eulerian")
        else:
            print("Graph is Eulerian (Euler circuit)")


            
# Creating three different graphs for testing
print("Testing Eulerian Graph:")
g1 = Graph(4)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(3, 0)
g1.euler_type()  # Expected: Graph is Eulerian (Euler circuit)

print("\nTesting Semi-Eulerian Graph:")
g2 = Graph(5)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(1, 3)
g2.add_edge(1, 3)
g2.add_edge(2, 3)
g2.add_edge(3, 4)
g2.euler_type()  # Expected: Graph is Semi-Eulerian

print("\nTesting Non-Eulerian Graph:")
g3 = Graph(5)
g3.add_edge(0, 1)
g3.add_edge(1, 2)
g3.add_edge(0, 2)
g3.add_edge(3, 4)
g3.euler_type()  # Expected: Graph is NOT a Euler graph

        
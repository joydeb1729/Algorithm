from queue import Queue

class Graph:
    def __init__(self, V):
        """
        Initializes a graph with V vertices.
        :param V: Number of vertices
        """
        self.V = V
        self.adj_list = [[] for _ in range(V)]  # Create an adjacency list representation
        
    def add_edge(self, v, w):
        """
        Adds a directed edge from vertex v to vertex w.
        :param v: Start vertex
        :param w: End vertex
        """
        self.adj_list[v].append(w)
        
    def bfs(self, start_v):
        """
        Performs Breadth-First Search (BFS) starting from a given vertex.
        :param start_v: The starting vertex for BFS traversal
        """
        visited = [False] * self.V  # List to keep track of visited vertices
        queue = Queue()  # Initialize a queue for BFS
        queue.put(start_v)  # Enqueue the starting vertex
        
        while not queue.empty():
            cur_vertex = queue.get()  # Dequeue a vertex
            visited[cur_vertex] = True  # Mark the vertex as visited
            print(cur_vertex, end=' ')  # Print the current vertex
            
            # Iterate over all adjacent vertices
            for neighbour in self.adj_list[cur_vertex]:
                if not visited[neighbour]:
                    queue.put(neighbour)  # Enqueue the unvisited adjacent vertex
    
# Create a graph with 10 vertices
g = Graph(10)

# Adding multiple edges to make the graph larger
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(3, 7)
g.add_edge(4, 7)
g.add_edge(5, 8)
g.add_edge(6, 9)
g.add_edge(7, 8)
g.add_edge(8, 9)

start_v = 0  # Define the starting vertex

print("Following is Breadth First Traversal (starting from vertex 0)")
g.bfs(start_v)

# Expected Output:
# 0 1 2 3 4 5 6 7 8 9
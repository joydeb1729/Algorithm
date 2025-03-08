# Class to implement Disjoint Set Union (DSU) or Union-Find with rank optimization
class DSU:
    def __init__(self, n):
        """
        Initialize DSU with 'n' elements.
        Each element is initially its own parent (-1), and the rank is initialized to 0.
        """
        self.parent = [-1] * n  # Parent array initialized to -1 (each node is its own root)
        self.rank = [0] * n  # Rank array to store the depth of trees

    def find_absolute_parent(self, v):
        """
        Find operation with Path Compression.
        Returns the absolute parent (root) of element 'v'.
        Updates parent[v] to the root for optimization.
        """
        if self.parent[v] == -1:
            return v
        self.parent[v] = self.find_absolute_parent(self.parent[v])  # Path compression
        return self.parent[v]

    def union_operation(self, from_v, to_v):
        """
        Union operation with Rank Optimization.
        Attaches the tree with a lower rank under the tree with a higher rank.
        """
        from_p = self.find_absolute_parent(from_v)  # Find root of 'from_v'
        to_p = self.find_absolute_parent(to_v)  # Find root of 'to_v'

        if from_p != to_p:  # Only merge if they belong to different sets
            if self.rank[from_p] > self.rank[to_p]:
                self.parent[to_p] = from_p  # Attach 'to_p' under 'from_p'
            elif self.rank[from_p] < self.rank[to_p]:
                self.parent[from_p] = to_p  # Attach 'from_p' under 'to_p'
            else:
                # If both have the same rank, attach 'to_p' under 'from_p' and increase rank
                self.parent[to_p] = from_p
                self.rank[from_p] += 1

# Function to check if the given undirected graph contains a cycle
def is_cyclic(edge_list, tot_v):
    """
    Detects a cycle in an undirected graph using DSU with Rank Optimization.
    :param edge_list: List of edges where each edge is represented as a tuple (u, v).
    :param tot_v: Total number of vertices in the graph.
    :return: True if there is a cycle, False otherwise.
    """
    dsu = DSU(tot_v)  # Initialize DSU for 'tot_v' vertices

    # Iterate through all edges
    for from_v, to_v in edge_list:
        from_p = dsu.find_absolute_parent(from_v)  # Find root of 'from_v'
        to_p = dsu.find_absolute_parent(to_v)  # Find root of 'to_v'

        if from_p == to_p:
            return True  # Cycle detected if both vertices have the same absolute parent

        dsu.union_operation(from_p, to_p)  # Perform union operation with rank optimization

    return False  # No cycle found

# Main execution starts here
if __name__ == "__main__":
    num_e = 3  # Number of edges
    num_v = 3  # Number of vertices
    edge_list = [(0, 1), (1, 2), (2, 0)]  # List to store edges

    '''
    # Uncomment below lines to take input dynamically
    num_e = int(input())  # Input number of edges
    num_v = int(input())  # Input number of vertices

    for i in range(num_e):
        u, v = map(int, input().split())  # Input each edge as two space-separated integers
        edge_list.append((u, v))
    '''

    # Check if the graph contains a cycle
    if is_cyclic(edge_list=edge_list, tot_v=num_v):
        print("Cycle Formed")  # If cycle is detected
    else:
        print("No Cycle Formed")  # If no cycle is detected

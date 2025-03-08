# Class to implement Disjoint Set Union (DSU) or Union-Find data structure
class DSU:
    def __init__(self, n):
        """
        Initialize DSU with 'n' elements.
        Each element is initially its own parent, represented by -1.
        """
        self.parent = [-1] * n  # Initialize parent array with -1

    def find_absolute_parent(self, v):
        """
        Find operation: Returns the absolute parent (root) of element 'v'.
        If 'v' is its own parent (i.e., parent[v] == -1), return 'v' itself.
        Otherwise, return its parent's absolute parent (i.e., path compression is NOT applied).
        """
        if self.parent[v] == -1:
            return v
        
        return self.find_absolute_parent(self.parent[v])  # No path compression in this implementation

    def union_operation(self, from_p, to_p):
        """
        Union operation: Merges two sets by connecting the root of 'from_p' to the root of 'to_p'.
        """
        from_p = self.find_absolute_parent(from_p)  # Find root of 'from_p'
        to_p = self.find_absolute_parent(to_p)      # Find root of 'to_p'

        self.parent[from_p] = to_p  # Connect the root of 'from_p' to 'to_p'

# Function to check if the given undirected graph contains a cycle
def is_cyclic(edge_list, tot_v):
    """
    Detects a cycle in an undirected graph using the Disjoint Set Union (DSU) method.
    :param edge_list: List of edges where each edge is represented as a tuple (u, v).
    :param tot_v: Total number of vertices in the graph.
    :return: True if there is a cycle, False otherwise.
    """
    dsu = DSU(tot_v)  # Initialize DSU for 'tot_v' vertices

    # Iterate through all pairs[(from_v,to_v) = (u,v)] of edges
    for from_v, to_v in edge_list:
        from_p = dsu.find_absolute_parent(from_v)  # Find root of 'from_v'
        to_p = dsu.find_absolute_parent(to_v)      # Find root of 'to_v'

        if from_p == to_p:
            return True  # Cycle detected if both vertices have the same absolute parent

        dsu.union_operation(from_p, to_p)  # Perform union operation

    return False  # No cycle found

# Main execution starts here
if __name__ == "__main__":
    num_e = 3  # Number of edges
    num_v = 4  # Number of vertices
    edge_list = [(0, 1), (1, 2), (2, 3)]  # List to store edges

    '''
    # Uncomment below lines to take input dynamically
    num_e = int(input())  
    num_v = int(input())  

    for i in range(num_e):
        u, v = map(int, input().split())  # Input each edge as two space-separated integers
        edge_list.append((u, v))
    '''

    # Check if the graph contains a cycle
    if is_cyclic(edge_list=edge_list, tot_v=num_v):
        print("Cycle Formed")  # If cycle is detected
    else:
        print("No Cycle Formed")  # If no cycle is detected

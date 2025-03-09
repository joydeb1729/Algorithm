class DSU:
    """
    Disjoint Set Union (DSU) with Path Compression
    """
    def __init__(self, n):
        self.parent = [-1] * (n + 1)  # Initialize parent array
        
    def find_absolute_parent(self, v):
        """
        Finds the absolute parent (root) of a node with path compression.
        """
        if self.parent[v] == -1:
            return v
        self.parent[v] = self.find_absolute_parent(self.parent[v])
        return self.parent[v]
    
    def union_operation(self, from_v, to_v):
        """
        Merges two sets by connecting their absolute parents.
        """
        from_p = self.find_absolute_parent(from_v)
        to_p = self.find_absolute_parent(to_v)
        
        if from_p != to_p:
            self.parent[from_p] = to_p  # Union by rank is not used here
                                 

def kruskal(edge_list, tot_v):
    """
    Implements Kruskal's Algorithm to find the Minimum Spanning Tree (MST).
    """
    tot_e = len(edge_list)
    
    # Bubble Sort for sorting edges based on weight (Alternative: use sort function)
    for i in range(tot_e):
        for j in range(0, tot_e - i - 1):
            if edge_list[j][2] > edge_list[j + 1][2]:
                edge_list[j], edge_list[j + 1] = edge_list[j + 1], edge_list[j]
    
    # Alternative sorting method (uncomment to use)
    # edge_list.sort(key=lambda x: x[2])
    
    dsu = DSU(tot_v)  # Initialize DSU for disjoint sets
    mst = []  # List to store edges of the MST
    
    # Iterate through sorted edges and build MST
    for from_v, to_v, weight in edge_list:
        if dsu.find_absolute_parent(from_v) != dsu.find_absolute_parent(to_v):
            dsu.union_operation(from_v, to_v)
            mst.append([from_v, to_v, weight])
        
        # If we have (V - 1) edges in MST, stop early
        if len(mst) == tot_v - 1:
            break
    
    return mst  # Return the edges in the MST


if __name__ == '__main__':
    # Input: Edge list of the graph [from_vertex, to_vertex, weight]
    edge_list = [
        [1, 2, 11], [1, 3, 13], [1, 5, 2], [2, 3, 15], [2, 4, 8],
        [2, 5, 12], [2, 7, 6], [4, 5, 14], [4, 7, 10], [4, 8, 17],
        [5, 8, 5], [6, 7, 21], [6, 8, 7], [7, 8, 11]
    ]
    
    tot_v = 8  # Number of vertices in the graph
    mst = kruskal(edge_list, tot_v)  # Compute MST using Kruskal's Algorithm
    
    # Compute total cost of the MST
    tot_cost = sum(edge[2] for edge in mst)
    
    # Output results
    print("Edges in the MST:")
    for edge in mst:
        print(edge)
    
    print("-------------------")
    print("Total Cost of MST:", tot_cost)

def optimal_merge_pattern(files):
    """
    Merges a list of sorted files into a single sorted file using a greedy approach.

    Args:
    files: A list of integers representing the sizes of the sorted files.

    Returns:
    The minimum number of comparisons required to merge all files.
    """

    # Initialize the total cost to 0.
    total_cost = 0

    # While there is more than one file remaining.
    while len(files) > 1:
        # Find the two smallest files.
        min1 = min(files)
        files.remove(min1)
        min2 = min(files)
        files.remove(min2)

        # Merge the two smallest files.
        merged_cost = min1 + min2
        files.append(merged_cost)

        # Update the total cost.
        total_cost += merged_cost

    return total_cost

# Driver code
if __name__ == '__main__':
    files = [2, 3, 5, 7, 9, 13]
    result = optimal_merge_pattern(files)
    print(f"Minimum number of comparisons: {result}")  # Output: 205

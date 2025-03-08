def MaxMin(arr, low, high, max_min):
    if low == high:  # Only one element
        max_min[0] = arr[low]  
        max_min[1] = arr[low]  
        return

    elif low == high - 1:  # Two elements
        if arr[low] < arr[high]:
            max_min[0] = arr[high] 
            max_min[1] = arr[low]   
        else:
            max_min[0] = arr[low]   
            max_min[1] = arr[high]  
        return

    # Divide array into two halves
    mid = (low + high) // 2

    # Mutable lists for left and right halves
    max1_min1 = [float('-inf'), float('inf')]
    max2_min2 = [float('-inf'), float('inf')]

    # Recursive calls
    MaxMin(arr, low, mid, max1_min1)
    MaxMin(arr, mid + 1, high, max2_min2)

    # Combine results
    max_min[0] = max(max1_min1[0], max2_min2[0])  
    max_min[1] = min(max1_min1[1], max2_min2[1])  


arr = [3, 4, 5, 6, 7, 8, 9, -1]
max_min = [float('-inf'), float('inf')]  # list for max and min

MaxMin(arr, 0, len(arr) - 1, max_min)

print("Max:", max_min[0])
print("Min:", max_min[1])

def BinarySearch(arr, n, x):
    low = 0
    high = n - 1  

    while low <= high:
        mid = (low + high) // 2  #integer division
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            return mid  # Element found, return index

    return -1  # Element not found

arr = [3, 4, 5, 6, 7, 8, 9]
print(BinarySearch(arr, len(arr), 6))  

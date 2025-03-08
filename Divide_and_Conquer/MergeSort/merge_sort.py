def MergeSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        MergeSort(arr, low, mid)        # Left half
        MergeSort(arr, mid + 1, high)   # Right half
        Merge(arr, low, mid, high)      # Merging both halves

def Merge(arr, low, mid, high):
    i = low
    j = mid + 1
    b = []  # Temporary list to hold merged values
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            b.append(arr[i])  # Append to list
            i += 1
        else:
            b.append(arr[j])  
            j += 1

    # If there are remaining elements in the left half
    while i <= mid:
        b.append(arr[i]) 
        i += 1

    # If there are remaining elements in the right half
    while j <= high:
        b.append(arr[j])  
        j += 1

    # Copy the sorted elements back into the original array
    for k in range(len(b)):
        arr[low + k] = b[k]

# Testing the function
arr = [45, 4, 3, 89, 56, 34, 21]
MergeSort(arr, 0, len(arr) - 1)
print(arr)

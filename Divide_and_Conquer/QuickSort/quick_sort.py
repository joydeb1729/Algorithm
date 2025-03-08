def QuickSort(arr, low, high):
    if(low<high):
        p = Partition(arr, low, high)
        QuickSort(arr, low, p-1)
        QuickSort(arr, p+1, high)
        
def Partition(arr, low, high):
    pivot = arr[high]
    i = low
    
    for j in range(low, high+1):
        if(arr[j]<pivot):
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i+=1
    
    temp = arr[high]
    arr[high] = arr[i]
    arr[i] = temp
    
    return i

arr = [45, 4, 3, 89, 56, 34, 21]
QuickSort(arr, 0, len(arr) - 1)
print(arr)

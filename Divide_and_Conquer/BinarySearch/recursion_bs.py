def BinarySearch(arr, low, high,x):
    
    if(low==high):
        if(arr[low]==x):
            return low
        else: return -1
        
    else:
        mid = (low+high)//2
        
        if(arr[mid]==x):
            return mid
        elif(arr[mid]<x):
            return BinarySearch(arr, mid+1, high,x)
        else:
            return BinarySearch(arr,low,mid-1,x)
    


arr = [3, 4, 5, 6, 7, 8, 9]
print(BinarySearch(arr, 0, len(arr)-1, 8))          
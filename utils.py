def BinarySearch(x, arr):
    mid = len(arr) // 2
    low = 0
    high = len(arr) - 1
    
    while arr[mid] != x and low <= high:
        if x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    
    return mid

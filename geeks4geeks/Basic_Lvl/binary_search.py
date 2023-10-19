# Given a sorted array of size N and an integer K, 
# find the position(0-based indexing) 
# at which K is present in the array using binary search.

# Example 1:

# Input:
# N = 5
# arr[] = {1 2 3 4 5} 
# K = 4
# Output: 3
# Explanation: 4 appears at index 3.

def binarysearch(arr, n, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 

arr = 1, 2, 3, 4, 5
n = 5
x = 4
print(binarysearch(arr, n , x))
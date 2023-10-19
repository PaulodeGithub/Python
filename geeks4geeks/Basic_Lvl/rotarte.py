# Given an array, 
# rotate the array by one position in clock-wise direction.
 

# Example 1:

# Input:
# N = 5
# A[] = {1, 2, 3, 4, 5}
# Output:
# 5 1 2 3 4

def rotate( arr, n):
    temp = arr[n -1]
    
    for i in range(n -1, 0 , -1):
        arr[i] = arr[i -1]
    arr[0] = temp
    
    return arr

arr = [1, 2, 3, 4, 5, 6, 77777]
n = 7
print(rotate(arr, n))
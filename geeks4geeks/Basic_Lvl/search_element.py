# Given an integer array and another integer element.
# The task is to find if the given element is present in array or not.

# Example 1:

# Input:
# n = 4
# arr[] = {1,2,3,4}
# x = 3
# Output: 2
# Explanation: There is one test case 
# with array as {1, 2, 3 4} and element 
# to be searched as 3.  Since 3 is 
# present at index 2, output is 2.

def search(arr, N, X):
    if X in arr:
        return arr.index(X)
    else:
        return -1
    

arr = [1, 2, 3, 4, 5, 6, 7]
N = 7
X = 3

print(search(arr, N, X))
# Given two arrays A and B of equal size N, 
# the task is to find if given arrays are equal or not. 
# Two arrays are said to be equal if both of them contain same set of elements, 
# arrangements (or permutation) of elements may be different though.
# Note : If there are repetitions, 
# then counts of repeated elements must also be same for two array to be equal.

# Example 1:

# Input:
# N = 5
# A[] = {1,2,5,4,0}
# B[] = {2,4,5,0,1}
# Output: 1
# Explanation: Both the array can be 
# rearranged to {0,1,2,4,5}

def check(A,B,N):
    
    if sorted(A) == sorted(B):
        return True
    else:
        return False

N = 10
arr1= [1,2,3,4,5,6,77,5,5,5]
arr2 = [3, 3, 4, 5, 6, 6, 7, 4768368648263, 4, 56] 

print(check(arr1, arr2, N))
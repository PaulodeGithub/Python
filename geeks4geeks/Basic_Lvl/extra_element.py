# # Given two sorted arrays of distinct elements. 
# There is only 1 difference between the arrays. 
# First array has one element extra added in between. 
# Find the index of the extra element.

# Example 1:

# Input:
# N = 7
# A[] = {2,4,6,8,9,10,12}
# B[] = {2,4,6,8,10,12}
# Output: 4
# Explanation: In the second array, 9 is
# missing and it's index in the first array
# is 4.
# Example 2:

# Input:
# N = 6
# A[] = {3,5,7,9,11,13}
# B[] = {3,5,7,11,13}
# Output: 3
# Your Task:
# You don't have to take any input.
#  Just complete the provided function findExtra() 
# that takes array A[], B[] and size of A[] 
# and return the valid index (0 based indexing).


def findExtra(a,b,n):
    left, right = 0, n - 1
    while left < right:
        mid = left + (right - left) // 2  # Calculate the middle index
            # If the middle elements are equal, the extra element is on the right side.
        if a[mid] == b[mid]:
            left = mid + 1
        else:
            right = mid
        
        
    print(left)


a= [3,5,7,9,11,12,13]
b = [3,5,7,9,11,13]
n = 7
findExtra(a,b,n)
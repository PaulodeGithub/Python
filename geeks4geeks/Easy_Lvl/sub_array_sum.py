# Given an unsorted array A of size N that contains only positive integers, 
# find a continuous sub-array that adds to a given number S
# and return the left and right index(1-based indexing) of that subarray.
# # In case of multiple subarrays,
# # return the subarray indexes which come first on moving from left to right.
# Note:- You have to return an ArrayList consisting of two elements left and right.
# In case no such subarray exists return an array consisting of element -1.

# # Example 1:

# # Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements 
# from 2nd position to 4th position 
# is 12.
# Example 2:

# Input:
# N = 10, S = 15
# A[] = {1,2,3,4,5,6,7,8,9,10}
# Output: 1 5
# Explanation: The sum of elements 
# from 1st position to 5th position
# is 15.

def subArraySum(arr, n, s):
    left, right = 0, 0
    current_sum = arr[0]

    while right < len(arr) and left <= right:
        if current_sum == s:
            return [left + 1, right + 1]  # Add 1 to indices for 1-based indexing

        if current_sum < s:
            right += 1
            if right < len(arr):
                current_sum += arr[right]
        else:
            current_sum -= arr[left]
            left += 1

    return [-1]  # If no subarray found 

arr = [1,2,3,4,5,6,7,8,9,10]
s = 0
n =10
print(subArraySum(arr, n, s))
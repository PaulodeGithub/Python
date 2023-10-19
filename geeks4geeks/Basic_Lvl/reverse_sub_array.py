# Given an array arr[] of positive integers of size N.
#  Reverse every sub-array group of size K.

# # Note: If at any instance, 
# there are no more subarrays of size greater than or equal to K, 
# then reverse the last subarray (irrespective of its size). 
# You shouldn't return any array, modify the given array in-place.

# Example 1:

# Input:
# N = 5, K = 3
# arr[] = {1,2,3,4,5}
# Output: 3 2 1 5 4
# Explanation: First group consists of elements
# 1, 2, 3. Second group consists of 4,5.

def reverseInGroups(arr, N, K):
    # Reverse the first 5 elements
    reversed_first_k = arr[:K][::-1]
    reversed_second_k = arr[K:][::-1]

# Combine the reversed part with the rest of the array
    result = reversed_first_k + reversed_second_k
    return result

      

N = 5
arr = [1, 2, 3, 4, 5]
K = 3

print(reverseInGroups(arr, N, K))

###########################################################

#another variation which replaces the current array
# for i in range(0, N, K):
#             start = i
#             end = min(i + K, N)
            
#             # Reverse the subarray from start to end
#             arr[start:end] = arr[start:end][::-1]

#             return arr




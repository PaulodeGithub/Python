# Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).

# Note: There can be more than one element in the array which have the same value as its index. You need to include every such element's index. Follows 1-based indexing of the array.

# Example 1:

# Input:
# N = 5
# Arr[] = {15, 2, 45, 12, 7}
# Output: 2
# Explanation: Only Arr[2] = 2 exists here.

def valueEqualToIndex(arr, n):
	arr2 = []
	for index, value in enumerate(arr):
		new_index = index + 1
		if value == new_index and new_index != 0:
			arr2.append(value)
	print(arr2)

a = 23, 2, 45, 4, 5, 6
n = 6

valueEqualToIndex(a, n)
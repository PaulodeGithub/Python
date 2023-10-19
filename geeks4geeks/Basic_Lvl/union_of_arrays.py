# Given two arrays a[] and b[] of size n and m respectively. 
# The task is to find the number of elements in the union between these two arrays.

# # Union of the two arrays can be defined 
# as the set containing distinct elements from both the arrays. 
# If there are repetitions, then only one occurrence of element should be printed in the union.
# # # Note : Elements are not necessarily distinct.

# # Example 1:

# Input:
# 5 3
# 1 2 3 4 5
# 1 2 3
# Output: 
# 5
# Explanation: 
# 1, 2, 3, 4 and 5 are the
# elements which comes in the union set
# of both arrays. So count is 5.


def doUnion(a,b):
        unique_elements = set(a)

        # Extend the set with elements from list2 that are not already in the set
        unique_elements.update(x for x in b if x not in unique_elements)
    
        # Convert the set back to a list (if you need a list as the result)
        merged_list = list(unique_elements)
    
        return len(merged_list)

arr1 = [1, 2, 3, 45, 5, 6, 6777,]
arr2 =[1, 2, 3, 45, 255, 254, 253]

print(doUnion(arr1, arr2))
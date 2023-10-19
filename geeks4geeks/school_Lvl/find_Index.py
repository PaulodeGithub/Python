# Given an unsorted array Arr[] of N integers 
# and a Key which is present in this array. 
# You need to write a program to find the start 
# index( index where the element is first found from left in the array ) 
# and end index( index where the element is first found from right in the array ).
# If the key does not exist in the array then return -1 for both start and end 
# index in this case.

# Example 1:

# Input:
# N = 6
# arr[] = { 1, 2, 3, 4, 5, 5 }
# Key = 5
# Output:  4 5
# Explanation:
# 5 appears first time at index 4 and
# appears last time at index 5.
# (0 based indexing)

def findIndex (a, N, key ):
        start_index = -1 # -1 indicates we havnt found/ dont know yet our start index
        end_index = -1
    
        for index, value in enumerate(a):
            if value == key:
                if start_index == -1:
                    start_index = index  # We found the key for the first time
                end_index = index  # We update end_index for each occurrence of the key
        
        print(start_index, end_index)
        
        
arr = [1, 2, 3, 4, 5, 5, 4, 55, 666,43,]
num = 6
key = 5

findIndex(arr, num, key)
# Given a Integer array A[] of n elements. 
# Your task is to complete the function PalinArray. 
# Which will return 1 if all the elements of 
# the Array are palindrome otherwise it will return 0.  

# Example 1:

# Input:
# 5
# 111 222 333 444 555

# Output:
# 1

def PalinArray(arr ,n):
    for i in range(n): # checking each num in the array
        chars = str(arr[i]) # converted to string to compare chars forward and backwards
        if chars != chars[::-1]: # if not equal to reversed i.e is Palindrome
            return 0   
    return 1
    


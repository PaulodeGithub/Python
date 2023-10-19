# Given an sorted array A of size N. 
# Find number of elements which are less than
# or equal to given element X.

#  Example 1:

# Input:
# N = 6
# A[] = {1, 2, 4, 5, 8, 10}
# X = 9
# Output:
# 5

def countOfElements( a, n, x):
    less_eq = []
    for i in a:
        if i <= x:
            less_eq.append(i)
    print(len(less_eq)) 
n = 6
a = {1, 2, 4, 5, 8, 10}
x = 9  
countOfElements(a , n, x)
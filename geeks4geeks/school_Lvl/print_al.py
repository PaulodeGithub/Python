

# You are given an array A of size N. 
# You need to print elements of A in alternate order (starting from index 0).

# Example 1:

# Input:
# N = 4
# A[] = {1, 2, 3, 4}
# Output:
# 1 3

def printAl(arr, n):
    for i in range(0, n, 2):  # Start from index 0 and increment by 2
        print(arr[i], end=' ') # end ensure arr[i] is printed on same line


a = 1, 2, 3, 4
num = 4
printAl(a, num)

# Given a number N, find the first N Fibonacci numbers. 
# The first two number of the series are 1 and 1.

# Example 1:

# Input:
# N = 5
# Output: 1 1 2 3 5

def fibonnaci(n):
    fibonacci = []
    a, b = 1, 1
    for i in range(n):
        fibonacci.append(a)
        a ,b = b, a + b
            
    return fibonacci

n = 124
print(fibonnaci(n))
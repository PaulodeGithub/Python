# Given a non-negative integer N. 
# The task is to check if N is a power of 2.
# More formally, check if N can be expressed as 2x for some integer x.
# Return true if N is power of 2 else return false.

# Example 1:

# Input: 
# N = 8
# Output: 
# YES
# Explanation:
# 8 is equal to 2 raised to 3 (23 = 8).
def powerOf2(n):
    if n <= 0:
            return False
    while n > 1:
        if n % 2 != 0:
            return False
        n /= 2

    return True

print(powerOf2(1000))
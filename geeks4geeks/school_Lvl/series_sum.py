# Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms) 

# Example 1:

# n = 5 
# 1 + 2 + 3 + 4 + 5 = 15
# output = 15

def seriesSum(n):
   total = n * (n + 1) // 2
   print(total)

seriesSum(6)
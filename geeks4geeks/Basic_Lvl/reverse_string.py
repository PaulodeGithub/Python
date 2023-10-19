# You are given a string s.
# You need to reverse the string.

# Example 1:

# Input:
# s = Geeks
# Output: skeeG

def reverseWord(str: str) -> str:
        rev_str = str[::-1]
        
        return rev_str

s = "Python is the best programming language"

print(reverseWord(s))
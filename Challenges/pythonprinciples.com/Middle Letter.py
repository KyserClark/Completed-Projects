"""
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
"""

# My code that solved the challenge:

def mid(string):
    length = len(string)
    print(length)
    if length % 2 == 0:
        return ""
    else:
        return string[(len(string)-1)//2:(len(string)+2)//2]
        
mid("abc")

# Example Solution

# this approach uses // which is integer division in Python 3
# alternatively, use / and int() in combination.
def mid(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]

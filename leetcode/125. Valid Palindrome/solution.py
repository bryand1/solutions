# 125. Valid Palindrome
#
# Given a string, determine if it is a palindrome, considering
# only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we
#       define empty string as valid palindrome.
#
# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
# Example 2:
#
# Input: "race a car"
# Output: false
from string import ascii_letters

class Solution:
    def isPalindrome(self, s):
        f = lambda x: x == x[::-1]
        v = set(ascii_letters + ''.join(map(str, range(10))))
        t = [c.lower() for c in s if c in v]
        return f(''.join(t))

if __name__ == '__main__':
    solution = Solution()

    ex1 = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(ex1))

    ex2 = "race a car"
    print(solution.isPalindrome(ex2))

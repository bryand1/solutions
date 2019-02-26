# 345. Reverse Vowels of a String
#
# Time Complexity: O(n)
#
# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
# Input: "hello"
# Output: "holle"
#

class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        i, j = 0, len(s) - 1
        vowels = set(tuple("aeiouAEIOU"))
        while i < j:
            if l[i] in vowels and l[j] in vowels:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            while i < j and l[i] not in vowels:
                i += 1
            while i < j and l[j] not in vowels:
                j -= 1
        return ''.join(l)


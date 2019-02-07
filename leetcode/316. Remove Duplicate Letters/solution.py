class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        for c in sorted(set(s)):
            suffix = s[s.find(c):]
            if len(set(suffix)) == len(set(s)):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))

if __name__ == '__main__':
    # Example 1:
    #
    # Input: "bcabc"
    # Output: "abc"

    # Example 2:
    #
    # Input: "cbacdcbc"
    # Output: "acdb"

    # Example 3:
    # Input: "rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws"

    solution = Solution()

    # ex1 = "bcabc"
    # print(solution.removeDuplicateLetters(ex1))

    # ex2 = "cbacdcbc"
    # print(solution.removeDuplicateLetters(ex2))

    ex3 = "rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws"
    print(solution.removeDuplicateLetters(ex3))

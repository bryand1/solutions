class Solution:

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)  # text length
        n = len(p)  # pattern length
        T = [[False for _ in range(n + 1)] for _ in range(m + 1)]  # 2-dim matrix
        T[0][0] = True

        # Handle patterns like a* or a*b*
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                T[0][j] = T[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    T[i][j] = T[i - 1][j - 1]
                elif p[j - 1] == '*':
                    T[i][j] = T[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        T[i][j] = T[i][j] or T[i - 1][j]
                else:
                    T[i][j] = False

        return T[m][n]

if __name__ == '__main__':
    # Example 1: false
    # s = "aa"
    # p = "a"
    
    # Example 2: true
    # s = "aa"
    # p = "a*"

    # Example 3: true
    # s = "ab"
    # p = ".*"
    
    # Example 4: true
    # s = "aab"
    # p = "c*a*b"
    
    # Example 5: false
    # s = "mississippi"
    # p = "mis*is*p*."

    # Example 6: False
    # s = "ab"
    # p = ".*c"

    # Example 7: True
    # s = "a"
    # p = "ab*"

    test_cases = (
        (("aa", "a"), False),
        (("aa", "a*"), True),
        (("ab", ".*"), True),
        (("aab", "c*a*b"), True),
        (("mississippi", "mis*is*p*"), False),
        (("ab", ".*c"), False),
        (("a", "ab*"), True),
    )

    solution = Solution()
    for args, boolean in test_cases:
        print(args, boolean)
        print(solution.isMatch(*args))

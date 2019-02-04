class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        # If pattern contains multiple asterisks
        # rewrite it to condense to single asterisk
        n = len(p)
        arr = [0] * n
        write_index = 0
        first = True
        for j in range(n):
            if p[j] == '*':
                if first:
                    arr[write_index] = p[j]
                    write_index += 1
                    first = False
            else:
                arr[write_index] = p[j]
                write_index += 1
                first = True
        p = ''.join(arr[:write_index])

        m = len(s)
        n = len(p)
        T = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        T[0][0] = True

        if p[:1] == '*':
            T[0][1] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    T[i][j] = T[i - 1][j - 1]
                elif p[j - 1] == '*':
                    T[i][j] = T[i - 1][j] or T[i][j - 1]

        return T[m][n]


if __name__ == '__main__':
    # Example 1:

    # Input:
    # s = "aa"
    # p = "a"
    # Output: false
    # Explanation: "a" does not match the entire string "aa".

    # Example 2:

    # Input:
    # s = "aa"
    # p = "*"
    # Output: true
    # Explanation: '*' matches any sequence.

    # Example 3:

    # Input:
    # s = "cb"
    # p = "?a"
    # Output: false
    # Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

    # Example 4:

    # Input:
    # s = "adceb"
    # p = "*a*b"
    # Output: true
    # Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

    # Example 5:

    # Input:
    # s = "acdcb"
    # p = "a*c?b"
    # Output: false

    # Example 6:

    # Input:
    # s = ""
    # p = ""
    # Output: true

    # Example 7:

    # Input:
    # s = "ho"
    # p = "**ho"
    # Output: true

    solution = Solution()

    test_cases = (
        (("aa", "a"), False),
        (("aa", "*"), True),
        (("cb", "?a"), False),
        (("adceb", "*a*b"), True),
        (("acdcb", "a*c?b"), False),
        (("", ""), True),
        (("ho", "**ho"), True),
    )

    for args, boolean in test_cases:
        print(args, boolean)
        assert solution.isMatch(*args) == boolean

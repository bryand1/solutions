class Solution:
    def longestPalindromeSubseq(self, s: 'str') -> 'int':
        n = len(s)
        T = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            T[i][i] = 1
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if l == 2 and s[i] == s[j]:
                    T[i][j] = 2
                elif s[i] == s[j]:
                    T[i][j] = T[i + 1][j - 1] + 2
                else:
                    T[i][j] = max(T[i + 1][j], T[i][j - 1])
        return T[0][-1]


if __name__ == '__main__':
    ex1 = "bbbab"
    ex2 = "cbbd"

    solution = Solution()
    print(solution.longestPalindromeSubseq(ex1))
    print(solution.longestPalindromeSubseq(ex2))

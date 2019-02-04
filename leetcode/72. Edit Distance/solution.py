class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        T = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for j in range(n + 1):
            T[0][j] = j
        for i in range(m + 1):
            T[i][0] = i
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    T[i][j] = T[i - 1][j - 1]
                else:
                    T[i][j] = 1 + min(
                        T[i - 1][j - 1],
                        T[i][j - 1],
                        T[i - 1][j]
                    )
        return T[m][n]


if __name__ == '__main__':
    solution = Solution()
     
    word1 = "horse"
    word2 = "ros"
    print(solution.minDistance(word1, word2))
    
    word1 = "intention"
    word2 = "execution"
    print(solution.minDistance(word1, word2))

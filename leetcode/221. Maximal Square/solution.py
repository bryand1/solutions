# LeetCode 221. Maximal Square
#
# Given a 2D binary matrix filled with 0's and 1's, find
# the largest square containing only 1's and return its area.
#
# Example:
#
# Input: 
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4

class Solution:

    def maximalSquare(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix:
            return 0
        smax = 0
        y = len(matrix)
        x = len(matrix[0])
        T = [[0 for _ in range(x + 1)] for _ in range(y + 1)]
        for i in range(1, y + 1):
            for j in range(1, x + 1):
                if matrix[i - 1][j - 1] == "1":
                    T[i][j] = 1 + min(T[i][j - 1], T[i - 1][j - 1], T[i - 1][j])
                    smax = max(smax, T[i][j])
        return smax


if __name__ == '__main__':
    solution = Solution()

    ex1 = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]    
    print(solution.maximalSquare(ex1))  # 2

    ex2 = [
        ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "1", "1"],
        ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0"],
    ]
    print(solution.maximalSquare(ex2))  # 3

    ex3 = [["0"]]
    print(solution.maximalSquare(ex3))

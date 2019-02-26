# 279. Perfect Squares
#
#    | 0  1  2  3  4  5  6  7  8  9  10  11  12
# --------------------------------------------
# 1  | 0  1  2  3  4  5  6  7  8  9  10  11  12
# 4  | 0  1  2  3  1  2  3  4  2  3   4   5   3
# 9  | 0  1  2  3  1  2  3  4  2  1   2   3   3
#
from math import sqrt, floor

class Solution:
    
    def numSquares(self, n: int) -> int:
        T = [[0 for _ in range(n + 1)] for _ in range(floor(sqrt(n)) + 1)]
        for i in range(n + 1):
            T[0][i] = i
        for i in range(1, len(T)):
            sq = i * i
            for j in range(1, n + 1):
                div = j // sq 
                if div == 0:
                    T[i][j] = T[i - 1][j]
                else:
                    T[i][j] = min(
                        T[i - 1][j],
                        div + T[i - 1][j % sq]
                    )
        return T[-1][n]

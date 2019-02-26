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
        T = list(range(n + 1))
        for i in range(1, floor(sqrt(n)) + 1):
            sq = i * i
            for j in range(1, n + 1):
                div = j // sq
                if div:
                    T[j] = min(T[j], div + T[j % sq])
        return T[n]

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            m = l + (r - l) // 2
            if m * m <= x < (m + 1) * (m + 1):
                return m
            elif x < m * m:
                r = m
            else:
                l = m + 1

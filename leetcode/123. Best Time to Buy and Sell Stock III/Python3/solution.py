import sys


class Solution:
    def _maxProfit(self, prices, k=2):
        s = [0] * (k + 1)
        b = [-sys.maxsize] * (k + 1)
        for p in prices:
            for i in range(k, 0, -1):
                s[i] = max(s[i], b[i] + p)
                b[i] = max(b[i], s[i - 1] - p)
        return s[k]

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self._maxProfit(prices)


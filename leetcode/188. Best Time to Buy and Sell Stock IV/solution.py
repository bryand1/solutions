# LeetCode 188. Best Time to Buy and Sell Stock IV
#
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# Design an algorithm to find the maximum profit.
# You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, k: 'int', prices: 'List[int]') -> 'int':
        if not prices:
            return 0
        n = len(prices)
        if k >= n // 2:
            return sum(x - y for x, y in zip(prices[1:], prices[:-1]) if x > y)
        profits = [0] * n
        for _ in range(k):
            max_all = max_here = max_prev = 0
            for i in range(1, n):
                profit = prices[i] - prices[i - 1]
                max_here = max(max_here + profit, max_prev + profit, max_prev)
                max_prev = profits[i]
                max_all = max(max_all, max_here)
                profits[i] = max_all
        return profits[-1]


if __name__ == '__main__':
    solution = Solution()

    print(solution.maxProfit(2, [2, 5, 7, 1, 4, 3]))

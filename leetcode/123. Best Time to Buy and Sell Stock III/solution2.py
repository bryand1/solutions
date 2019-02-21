class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(3)]
        for i in range(1, 3):
            for j in range(1, n):
                profit = 0
                for m in range(j):
                    profit = max(profit, prices[j] - prices[m] + dp[i - 1][m])
                dp[i][j] = max(profit, dp[i][j - 1])
        return dp[-1][-1]

if __name__ == '__main__':
    # Example 1:

    # Input: [3,3,5,0,0,3,1,4]
    # Output: 6

    ex1 = [3,3,5,0,0,3,1,4]

    solution = Solution()
    print(solution.maxProfit(ex1))

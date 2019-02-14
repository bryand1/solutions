class Solution:
    def maxCoins(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        n = len(nums)
        T = [[0 for _ in range(n)] for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                left_val = 1 if i == 0 else nums[i - 1]
                right_val = 1 if j == n - 1 else nums[j + 1]
                for k in range(i, j + 1):
                    before = 0 if k == i else T[i][k - 1]
                    after = 0 if k == j else T[k + 1][j]
                    T[i][j] = max(T[i][j], before + after + left_val * nums[k] * right_val)
        return T[0][-1]


if __name__ == '__main__':
    # Input: [3,1,5,8]
    # Output: 167 
    # Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
    #              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167  
    s = Solution()
    print(s.maxCoins([3, 1, 5, 8]))

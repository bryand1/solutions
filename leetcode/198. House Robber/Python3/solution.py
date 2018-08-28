class Solution:

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        t = [0] * n
        t[0], t[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n): 
            t[i] = max(nums[i], nums[i] + t[i - 2]) 
            t[i - 1] = max(t[i - 1], t[i - 2]) 
        return max(t[-2], t[-1])


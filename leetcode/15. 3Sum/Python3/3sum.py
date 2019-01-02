import bisect


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = []
        d = {}
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                d[nums[i] + nums[j]] = [i, j]
        for i in range(n):
            indices = d.get(-nums[i])
            if indices and i not in indices:
                values = sorted([nums[j] for j in indices] + [nums[i]])
                if values not in r:
                    r.append(values)
        return r

# import pdb
# pdb.set_trace()
print(Solution().threeSum([0, 0, 0, 0]))


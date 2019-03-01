class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {0: 1}
        acc = res = 0
        for v in nums:
            acc += v
            res += count.get(acc - k, 0)
            count[acc] = count.get(acc, 0) + 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([1, 0, 2, -1, 1, -1, 0], 2))

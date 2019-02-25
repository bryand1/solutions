# 128. Longest Consecutive Sequence
#
# Solution: walk each streak

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        m = 0
        for x in s:
            if x - 1 not in s:
                y = x + 1
                while y in s:
                    y += 1
                m = max(m, y - x)
        return m

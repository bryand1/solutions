class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        res = i = j = 0
        d = {}
        while j < len(s):
            if len(d) <= 2:
                d[s[j]] = j
                j += 1
            if len(d) > 2:
                m = min(d.values())
                i = m + 1
                d.pop(s[m])
            res = max(res, j - i)
        return res


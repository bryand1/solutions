class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return n
        k = 1
        seen = dict()
        i = j = 0
        while j < n - 1:
            seen[s[j]] = j
            j += 1
            if s[j] in seen:
                target = seen[s[j]] + 1
                while i < target and i < j:
                    del seen[s[i]]
                    i += 1
            else:
                k = max(k, j - i + 1)
        return k

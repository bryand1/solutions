from collections import Counter
import sys

class Solution:

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target_map = Counter(t)
        count = len(t)
        start = end = head = 0
        min_substring_length = sys.maxsize

        while end < len(s):
            if target_map[s[end]] > 0:
                count -= 1
            target_map[s[end]] -= 1
            end += 1
            while count == 0:
                if (end - start) < min_substring_length:
                    min_substring_length = end - start
                    head = start
                target_map[s[start]] += 1
                if target_map[s[start]] > 0:
                    count += 1
                start += 1

        return "" if min_substring_length == sys.maxsize else s[head:head + min_substring_length]


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    solution = Solution()
    print(solution.minWindow(S, T))

    S = "a"
    T = "aa"
    print(solution.minWindow(S, T))

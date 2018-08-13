class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map = {')': '(', '}': '{', ']': '['}
        values = set(map.values())
        for char in s:
            if char in values:
                stack.append(char)
            elif char in map:
                try:
                    opening = stack.pop()
                except IndexError:
                    return False
                if opening != map[char]:
                    return False
        return len(stack) == 0


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
            else:
                if stack == [] or map[char] != stack.pop():
                    return False
        return len(stack) == 0

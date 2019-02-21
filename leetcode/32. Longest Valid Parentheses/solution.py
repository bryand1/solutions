class Solution:
    def longestValidParentheses(self, s: 'str') -> 'int':
        stack = [-1]
        r = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    r = max(r, i - stack[-1])
                else:
                    stack.append(i)
        return r

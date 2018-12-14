class Solution:

    def is_valid(self, s):
        st = []
        for char in s:
            if char == '(':
                st.append(char)
            elif char == ')':
                try:
                    st.pop()
                except IndexError:
                    return False
        return len(st) == 0

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        st = list(reversed(s))
        ans = {""}
        maxlen = 0
        while st:
            curr = st.pop()
            adder = set()
            for elem in ans:
                new = elem + curr
                is_alpha = curr not in (')', '(')
                is_closeable = new.count(')') <= new.count('(')
                if is_alpha or is_closeable:
                    adder.add(new)
                    if self.is_valid(new):
                        maxlen = max(maxlen, len(new))
            ans |= adder
        length = lambda x: len(x) == maxlen
        return list(filter(lambda x: length(x) and self.is_valid(x), ans))


if __name__ == '__main__':
    s = Solution()

    case1 = "()())()"
    print(s.removeInvalidParentheses(case1))

    case2 = "(a)())()"
    print(s.removeInvalidParentheses(case2))

    case3 = ")("
    print(s.removeInvalidParentheses(case3))

# Determine beforehand the number of parentheses that should be removed
# This will avoid spending compute on paths that will not yield the optimal result


class Solution:
    def removeInvalidParentheses(self, s):
        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == 0:
                    right += 1
                elif left > 0:
                    left -= 1

        self.ans = set()

        def dfs(depth, left, right, left_rem, right_rem, cur):
            if depth == len(s):
                if left_rem == 0 and right_rem == 0:
                    self.ans.add(cur)
            else:
                if s[depth] == "(" and left_rem > 0:
                    dfs(depth + 1, left, right, left_rem - 1, right_rem, cur)
                if s[depth] == ")" and right_rem > 0:
                    dfs(depth + 1, left, right, left_rem, right_rem - 1, cur)
                if s[depth] != "(" and s[depth] != ")":
                    dfs(depth + 1, left, right, left_rem, right_rem, cur + s[depth])
                elif s[depth] == "(":
                    dfs(depth + 1, left + 1, right, left_rem, right_rem, cur + "(")
                elif s[depth] == ")" and right < left:
                    dfs(depth + 1, left, right + 1, left_rem, right_rem, cur + ")")

        dfs(0, 0, 0, left, right, "")
        return list(self.ans)


if __name__ == '__main__':
    s = Solution()

    case1 = "()())()"
    print(s.removeInvalidParentheses(case1))

    case2 = "(a)())()"
    print(s.removeInvalidParentheses(case2))

    case3 = ")("
    print(s.removeInvalidParentheses(case3))

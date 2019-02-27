class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        self.res = []
        self.helper(n, n)
        return self.res

    def helper(self, o, c, combination=''):
        if o == 0 and c == 0:
            self.res.append(combination)
            return

        if o == c:
            self.helper(o - 1, c, combination + '(')
        
        if o < c and o > 0:
            self.helper(o - 1, c, combination + '(')
            self.helper(o, c - 1, combination + ')')

        if o < c and o == 0:
            self.helper(o, c - 1, combination + ')')

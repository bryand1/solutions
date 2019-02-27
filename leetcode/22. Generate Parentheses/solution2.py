class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, n, '', res)
        return res

    def helper(self, l, r, s, res):
        if l < 0 or r < 0 or l > r:
            return
        if l == 0 and r == 0:
            res.append(s)
            return
        self.helper(l - 1, r, s + '(', res)
        self.helper(l, r - 1, s + ')', res)

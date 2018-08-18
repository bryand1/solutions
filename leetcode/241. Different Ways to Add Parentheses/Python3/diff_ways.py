from operator import add, sub, mul
op = {'+': add, '-': sub, '*': mul}


class Solution:
    def diffWaysToCompute(self, expr):
        """
        :type input: str
        :rtype: List[int]
        """
        arr = self.parse(expr)
        return self.diffWaysToComputeRec(arr, 0, len(arr))

    def diffWaysToComputeRec(self, arr, lo, hi):
        if hi - lo == 1:
            return [arr[lo]]
        res = []
        for i in range(lo + 1, hi, 2):
            op = arr[i]
            lhs = self.diffWaysToComputeRec(arr, lo, i)
            rhs = self.diffWaysToComputeRec(arr, i + 1, hi)
            for a in lhs:
                for b in rhs:
                    res.append(op(a, b))
        return res

    def parse(self, expr):
        res = []
        n = 0
        for char in expr:
            if char.isdigit():
                n = 10 * n + int(char)
            else:
                res.append(n)
                n = 0
                res.append(op[char])
        res.append(n)
        return res


"""
LeetCode

241. Different Ways to Add Parentheses

Given a string of numbers and operators, return all possible results from computing all the
different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
"""
from operator import add, sub, mul
operator_map = {"+": add, "-": sub, "*": mul}


class Solution:
    def lexer(self, expr):
        self.pos = 0
        tokens = [self.integer(expr)]
        n = len(expr)
        while self.pos < n:
            if expr[self.pos].isdigit():
                tokens.append(self.integer(expr))
            else:
                tokens.append(operator_map[expr[self.pos]])
                self.pos += 1
        return tokens

    def integer(self, expr):
        result = ''
        while self.pos < len(expr) and expr[self.pos].isdigit():
            result += expr[self.pos]
            self.pos += 1
        return int(result)

    def diffWaysToComputeRec(self, tokens, lo, hi):
        if hi - lo == 1:
            return [tokens[lo]]
        ways = []
        for i in range(lo + 1, hi, 2):
            op = tokens[i]
            lhs = self.diffWaysToComputeRec(tokens, lo, i)
            rhs = self.diffWaysToComputeRec(tokens, i + 1, hi)
            for a in lhs:
                for b in rhs:
                    ways.append(op(a, b))
        return ways

    def diffWaysToCompute(self, expr):
        tokens = self.lexer(expr)
        return self.diffWaysToComputeRec(tokens, 0, len(tokens))

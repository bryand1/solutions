# 904. Fruit Into Baskets
# 
# Example 1:
# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].
#
# Example 2:
# Input: [0,1,2,2]
# Output: 3
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].
#
# Example 3:
# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
#
# Example 4:
# Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4 fruits.

class Solution:
    def totalFruit(self, tree: 'List[int]') -> 'int':
        if not tree:
            return 0
        res = i = j = 0
        d = {}
        while j < len(tree):
            if len(d) <= 2:
                d[tree[j]] = j
                j += 1
            if len(d) > 2:
                m = min(d.values())
                i = m + 1
                d.pop(tree[m])
            res = max(res, j - i)
        return res


if __name__ == '__main__':
    ex1 = [1, 2, 1]        # -> 3
    ex2 = [0, 1, 2, 2]     # -> 3
    ex3 = [1, 2, 3, 2, 2]  # -> 4
    ex4 = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]  # -> 5

    s = Solution()
    print(s.totalFruit(ex1))
    print(s.totalFruit(ex2))
    print(s.totalFruit(ex3))
    print(s.totalFruit(ex4))

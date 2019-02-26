# 315. Count of Smaller Numbers After Self
class BinaryIndexedTree:

    def __init__(self, n):
        self.tree = [0] * (n + 1)
    
    def update(self, i, v):
        while i < len(self.tree):
            self.tree[i] += v
            i += i & (-i)

    def getsum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s


class Solution:
    def countSmaller(self, nums):
        rank = {v: i for i, v in enumerate(sorted(set(nums)))}
        bit = BinaryIndexedTree(len(rank))
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(bit.getsum(rank[nums[i]]))
            bit.update(rank[nums[i]] + 1, 1)
        return res[::-1]


if __name__ == '__main__':
    solution = Solution()

    ex1 = [5, 2, 6, 1, 2, 7]
    print(solution.countSmaller(ex1))    

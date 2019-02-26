class BinaryIndexedTree:

    def __init__(self, n):
        self.sums = [0] * (n + 1)
    
    def update(self, i, v):
        while i < len(self.sums):
            self.sums[i] += v
            i += i & (-i)
    
    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & (-i)
        return r


class Solution:
    def countSmaller(self, nums):
        hash_table = {v: i for i, v in enumerate(sorted(set(nums)))}
        tree = BinaryIndexedTree(len(hash_table))
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(tree.sum(hash_table[nums[i]]))
            tree.update(hash_table[nums[i]] + 1, 1)
        return res[::-1]


if __name__ == '__main__':
    solution = Solution()

    ex1 = [5, 2, 6, 1, 2, 7]
    print(solution.countSmaller(ex1))    

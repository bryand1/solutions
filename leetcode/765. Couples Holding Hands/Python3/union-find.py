class UF:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.count = 0

    def find(self, i):
        if self.parents[i] == i:
            return i
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        a = self.find(i)
        b = self.find(j)
        if a != b:
            self.parents[a] = b
            self.count += 1


class Solution:

    def minSwapsCouples(self, row):
        N = len(row) // 2
        uf = UF(N)
        for i in range(N):
            a = row[2 * i]
            b = row[2 * i + 1]
            uf.union(a // 2, b // 2)
        return uf.count

# 421. Maximum XOR of Two Numbers in an Array
class Solution:

    def findMaximumXOR(self, nums: 'List[int]') -> 'int':
        accum = 0

        def exists(prefixes, cur):
            for p in prefixes:
                if (cur ^ 1 ^ p) in prefixes:
                    return True
            return False

        for i in reversed(range(8)):
            accum <<= 1
            pfx = {n >> i for n in nums}
            if exists(pfx, accum):
                accum += 1

        return accum

if __name__ == '__main__':
    ex = [3, 10, 5, 25, 2, 8]
    solution = Solution()
    print(solution.findMaximumXOR(ex))

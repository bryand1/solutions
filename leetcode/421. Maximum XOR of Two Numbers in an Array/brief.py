def findMaximumXOR(self, nums):
    answer = 0
    for i in reversed(range(8)):
        answer <<= 1
        prefixes = {num >> i for num in nums}
        answer += any(answer^1 ^ p in prefixes for p in prefixes)
    return answer

if __name__ == '__main__':
    ex = [3, 10, 5, 25, 2, 8]
    solution = Solution()
    print(solution.findMaximumXOR(ex))

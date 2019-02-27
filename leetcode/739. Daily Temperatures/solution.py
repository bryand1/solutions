class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * len(T)
        for index, temperature in enumerate(T):
            if stack:
                while stack and temperature > stack[-1][-1]:
                    j, _ = stack.pop()
                    result[j] = index - j
            stack.append((index, temperature))
        return result

if __name__ == '__main__':
    ex1 = [73,74,75,71,69,72,76,73]
    s = Solution()
    print(s.dailyTemperatures(ex1))

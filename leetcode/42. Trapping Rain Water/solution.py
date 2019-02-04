class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        L = [0] * n
        R = [0] * n
        for i in range(1, n):
            L[i] = max(L[i - 1], height[i - 1])
            R[-i - 1] = max(R[-i], height[-i])
        w = 0
        for i in range(n):
            w += max(0, min(L[i], R[i]) - height[i])
        return w

if __name__ == '__main__':
    # Example:

    # Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    # Output: 6
    solution = Solution()

    h = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(solution.trap(h))

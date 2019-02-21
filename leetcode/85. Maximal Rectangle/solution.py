# LeetCode 85. Maximal Rectangle
#
# Given a 2D binary matrix filled with 0's and 1's, find the
# largest rectangle containing only 1's and return its area.

class Solution:

    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix:
            return 0
        cols = len(matrix[0])
        hist = [0] * cols
        smax = 0
        for i in range(len(matrix)):
            for j in range(cols):
                hist[j] = 0 if matrix[i][j] == '0' else hist[j] + 1
            smax = max(smax, self.maxAreaHistogram(hist))
        return smax

    def maxAreaHistogram(self, heights: 'List[int]') -> 'int':
        heights.append(0)
        n = len(heights)
        st = []
        i = 0
        smax = 0
        while i < n:
            if (not st) or heights[i] >= heights[st[-1]]:
                st.append(i)
                i += 1
            else:
                top = st.pop()
                if st:
                    area = heights[top] * (i - st[-1] - 1)
                else:
                    area = heights[top] * i
                smax = max(smax, area)
        heights.pop()
        return smax

if __name__ == '__main__':
    # Example:
    # Input:
    # [
    # ["1","0","1","0","0"],
    # ["1","0","1","1","1"],
    # ["1","1","1","1","1"],
    # ["1","0","0","1","0"]
    # ]
    # Output: 6

    matrix =     [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]

    solution = Solution()
    print(solution.maximalRectangle(matrix))

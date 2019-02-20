# LeetCode 84. Largest Rectangle in Histogram
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the histogram.


class Solution:

    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        heights.append(0)
        n = len(heights)
        st = []
        smax = 0
        i = 0
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
        return smax

if __name__ == '__main__':
    # Example:

    # Input: [2,1,5,6,2,3]
    # Output: 10

    ex1 = [2, 1, 5, 6, 2, 3]  # 10

    solution = Solution()
    print(solution.largestRectangleArea(ex1))

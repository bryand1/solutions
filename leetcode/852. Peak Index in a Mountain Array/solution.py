class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if not A:
            return 0 
        return A.index(max(A))


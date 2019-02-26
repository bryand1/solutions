class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        invert = lambda x: 1 if x == 0 else 0
        return [list(map(invert, A[i][::-1])) for i in range(len(A))]

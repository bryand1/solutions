class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        d = {x: i for i, x in enumerate(B)}
        return [d[x] for x in A]


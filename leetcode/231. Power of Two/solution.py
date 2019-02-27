class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        b = bin(n)
        if b[2] == '1': 
            return b[3:].count('0') == len(b) - 3
        return False


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        i = len(digits) - 1
        while i >= 0 and carry:
            digits[i] += 1
            digits[i] %= 10
            carry = not digits[i]
            i -= 1
        if carry:
            digits.insert(0, 1)
        return digits


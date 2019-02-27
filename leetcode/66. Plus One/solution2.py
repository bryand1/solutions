class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            carry = not digits[i]
            if not carry:
                break
        else:
            digits.insert(0, 1)
        return digits


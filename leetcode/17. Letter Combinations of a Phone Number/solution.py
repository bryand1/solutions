class Solution:
    map = {
        '0': ' ',
        '1': '*',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        if not digits:
            return []
        res = []
        st = []
        for digit in digits:
            if digit not in self.map:
                continue
            if not res:
                res = list(self.map[digit])
                continue
            st = list(self.map[digit])
            new_res = []
            while st:
                letter = st.pop()
                for i in range(len(res)):
                    new_res.append(res[i] + letter)
            res = new_res
        return res

if __name__ == '__main__':
    solution = Solution()

    # Input: "23"
    # Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    ex = "23"

    print(solution.letterCombinations(ex))

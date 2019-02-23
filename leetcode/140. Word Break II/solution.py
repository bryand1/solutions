class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})
    
    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                rest = self.helper(s[len(word):], wordDict, memo)
                for item in rest:
                    res.append(word + ' ' + item)
        memo[s] = res
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input:
    # s = "catsanddog"
    # wordDict = ["cat", "cats", "and", "sand", "dog"]
    # Output:
    # [
    # "cats and dog",
    # "cat sand dog"
    # ]

    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(solution.wordBreak(s, wordDict))

    # Example 2:

    # Input:
    # s = "pineapplepenapple"
    # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    # Output:
    # [
    # "pine apple pen apple",
    # "pineapple pen apple",
    # "pine applepen apple"
    # ]
    # Explanation: Note that you are allowed to reuse a dictionary word.
    
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(solution.wordBreak(s, wordDict))

    # Example 3:

    # Input:
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # Output:
    # []
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(solution.wordBreak(s, wordDict))

    # Example 4: (Memory Limit Exceeded)

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(solution.wordBreak(s, wordDict))

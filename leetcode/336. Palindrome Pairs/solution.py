class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        is_palindrome = lambda x: x == x[::-1]
        res = []
        dic = {}
        n = len(words)
        for i in range(n):
            dic[words[i][::-1]] = i
        for i in range(n):
            for j in range(len(words[i])):
                left = words[i][:j]
                right = words[i][j:]
                if left in dic and dic[left] != i and is_palindrome(right):
                    res.append([i, dic[left]])
                    if not left:
                        res.append([dic[left], i])
                if right in dic and dic[right] != i and is_palindrome(left):
                    res.append([dic[right], i])
        return res

if __name__ == '__main__':
    s = Solution()

    # Example 1:

    # Input: ["abcd","dcba","lls","s","sssll"]
    # Output: [[0,1],[1,0],[3,2],[2,4]] 
    # Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
    
    # ex1 = ["abcd","dcba","lls","s","sssll"]
    # print(s.palindromePairs(ex1))

    # Example 2:

    # Input: ["bat","tab","cat"]
    # Output: [[0,1],[1,0]] 
    # Explanation: The palindromes are ["battab","tabbat"]
    # ex2 = ["bat", "tab", "cat"]
    # print(s.palindromePairs(ex2))

    # Example 3:

    ex3 = ["a",""]
    print(s.palindromePairs(ex3))

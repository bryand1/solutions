# LeetCode 269. Alien Dictionary
#
# There is a new alien language which uses the latin alphabet. However, the order among letters are 
# unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted 
# lexicographically by the rules of this new language. Derive the order of letters in this language.
from collections import deque

class Solution():

    def alienOrder(self, words):
        dag = {char: [] for char in set(''.join(words))}
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    dag[a].append(b)
                    break
        return self.topological_sort(dag)
    
    def topological_sort(self, dag):
        in_degree = {u: 0 for u in dag}
        for u in dag:
            for v in dag[u]:
                in_degree[v] += 1
        q = deque()
        for u in in_degree:
            if in_degree[u] == 0:
                q.appendleft(u)
        t = []
        while q:
            u = q.pop()
            t.append(u)
            for v in dag[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.appendleft(v)

        if len(t) == len(dag):
            return ''.join(t)
        else:
            return ''
        

if __name__ == '__main__':
    solution = Solution()

    # Example 1:

    # Input:
    # [
    #   "wrt",
    #   "wrf",
    #   "er",
    #   "ett",
    #   "rftt"
    # ]

    # Output: "wertf"

    ex1 = [
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]
    print(solution.alienOrder(ex1))  # wertf

    ex2 = [
        "z",
        "x"
    ]
    print(solution.alienOrder(ex2))  # zx

    ex3 = [
        "z",
        "x",
        "z",
    ]
    print(solution.alienOrder(ex3))  # ""  (empty string due to dag error)

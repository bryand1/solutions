class Solution:
    def reconstructQueue(self, people: 'List[List[int]]') -> 'List[List[int]]':
        people.sort(key=lambda p: (-p[0], p[1]))
        queue = []
        for person in people:
            queue.insert(person[1], person)
        return queue

if __name__ == '__main__':
    input = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    solution = Solution()
    print(solution.reconstructQueue(input))
    output = [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

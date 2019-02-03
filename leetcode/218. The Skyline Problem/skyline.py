from heapq import heappop, heappush


class Solution:

    def getSkyline(self, buildings):
        # add 'start' critical points
        # add 'end' critical points (0 height)
        # sort events in left to right order
        points = [(l, -h, r) for l, r, h in buildings]
        points += [(r, 0, 0) for _, r, _ in buildings]
        points.sort()

        res = [[0, 0]]  # result: [x, height]
        hp = [(0, float('inf'))]  # -height, ending position
        for l, neg_h, r in points:
            # 1: Pop buildings that are to the left of 'l'
            # 2: If the point is != 0, add it to the heap
            # 3: If previous height != current highest height, append to result
            while l >= hp[0][1]:
                heappop(hp)
            if negh:
                heappush(hp, (neg_h, r))
            max_h = -hp[0][0]
            if res[-1][1] != max_h:
                res.append([l, max_h])
        return res[1:]


if __name__ == '__main__':     
    buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
    solution = Solution()
    print(solution.getSkyline(buildings))

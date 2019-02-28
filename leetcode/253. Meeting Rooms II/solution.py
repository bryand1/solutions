# 253. Meeting Rooms II

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda interval: interval.start)
        it = iter(intervals)
        rooms = [[next(it)]]
        for interval in it:
            for room in rooms:
                if interval.start >= room[-1].end:
                    room.append(interval)
                    break
            else:
                rooms.append([interval])
        return len(rooms)


if __name__ == '__main__':

    s = Solution()

    # Input: [[0, 30],[5, 10],[15, 20]]  -> 2
    # ex1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    # print(s.minMeetingRooms(ex1))

    # [[13,15],[1,13]]  -> 1
    # ex2 = [Interval(13, 15), Interval(1, 13)]
    # print(s.minMeetingRooms(ex2))

    # [[1,5],[8,9],[8,9]]  -> 2
    # ex3 = [Interval(1, 5), Interval(8, 9), Interval(8, 9)]
    # print(s.minMeetingRooms(ex3))

    # [[2,15],[36,45],[9,29],[16,23],[4,9]] -> 2
    ex4 = [Interval(2, 15), Interval(36, 45), Interval(9, 29), Interval(16, 23), Interval(4, 9)]
    print(s.minMeetingRooms(ex4))

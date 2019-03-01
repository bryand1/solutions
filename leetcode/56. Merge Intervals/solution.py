# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if not intervals:
            return []
        intervals.sort(key=lambda i: i.start)
        it = iter(intervals)
        res = [next(it)]
        for interval in it:
            if interval.start <= res[-1].end:
                res[-1] = Interval(res[-1].start, max(res[-1].end, interval.end))
            else:
                res.append(interval)
        return res

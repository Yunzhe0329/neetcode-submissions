"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)

        for i in range(n):
            prev = intervals[i]
            for j in range(i + 1, n):
                later = intervals[j]
                if min(prev.end, later.end) > max(prev.start, later.start):
                    return False
        return True

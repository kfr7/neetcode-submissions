"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def printIntervals(self, intervals):
        for element in intervals:
            print(f'({element.start}, {element.end})', end=' ')
        print();
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        # should be sorting by end first
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        s, e = 0, 0
        # guaranteed that the first value of s will be lower than e
        most_collisions = 1
        while s < len(starts):
            if starts[s] < ends[e]:
                s += 1
                most_collisions = max(most_collisions, s - e)
                
            else:
                e += 1
        print(most_collisions)
        return most_collisions

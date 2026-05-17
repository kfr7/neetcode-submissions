"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: (x.start, x.end))
        h = []  # going to just store the end times
        rooms_needed = 0
        for i in range(len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            if len(h) != 0 and h[0] <= start:
                heapq.heappop(h) # we are reusing a room so no worries
            else:
                # need to add a room
                rooms_needed += 1
            
            heapq.heappush(h, end)
        return rooms_needed

                 

        
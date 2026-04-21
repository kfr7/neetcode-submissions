class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if (len(intervals) == 0):
            return [newInterval]
                
        res = []
        l, r = 0, 0 # initially try to be "valid"
        while r < len(intervals):
            if l == r:  # then we only need to see if the current interval overlaps with the newInterval
                if newInterval[1] < intervals[l][0]: # then we can insert the newInterval at this spot
                    res.append(newInterval)
                    # now loop through the rest of the le
                    res += intervals[l:]
                    return res
                elif newInterval[0] > intervals[l][1]: # they don't overlap but left comes first so append and go to next iteration
                    res.append(intervals[l])
                    l += 1
                    r += 1
                else:   # they are overlapping so we need to extend r
                    r += 1
            else:   # we need to continue extending right since we found overlapping stuff
                if newInterval[1] < intervals[r][0]:   # then this r does not overlap anymore so merge l and the max(intervals[r-1][1], newInterval[1])
                    min_start = min(intervals[l][0], newInterval[0])
                    max_end = max(intervals[r-1][1], newInterval[1])
                    res.append([min_start, max_end])
                    res += intervals[r:]
                    return res
                else:   # still overlapping
                    r += 1
        # if we reached this then the newInterval should be at the end
        if l == r:
            res.append(newInterval)
        else:
            min_start = min(intervals[l][0], newInterval[0])
            max_end = max(intervals[r-1][1], newInterval[1])
            res.append([min_start, max_end])

        return res

        


        
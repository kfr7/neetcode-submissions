class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if len(intervals) == 0:
            return res
        intervals.sort()

        l, r = 0, 0
        build_interval = []
        while r < len(intervals):
            if l == r:
                build_interval = [intervals[l][0], intervals[l][1]]
                r += 1
            elif intervals[r][0] > build_interval[1]:
                res.append(build_interval[::])
                l = r
            else:
                small = min(build_interval[0], intervals[r][0])
                big = max(build_interval[1], intervals[r][1])
                build_interval = [small, big]
                r += 1
        small = min(build_interval[0], intervals[r-1][0])
        big = max(build_interval[1], intervals[r-1][1])
        build_interval = [small, big]
        res.append(build_interval[::])
        return res



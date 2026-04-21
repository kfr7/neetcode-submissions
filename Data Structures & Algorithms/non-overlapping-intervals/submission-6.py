class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        l, r = 0, 1
        removed = 0
        while r < len(intervals):
            if l == r:  # should never get bigger than r
                r += 1
            elif intervals[l][0] == intervals[r][0]:  
                # always remove the right one since second value is greater
                removed += 1
                r += 1
            # at this point we know the right interval's first number is greater than the first number, but it still might be within the second number of the first interval
            elif intervals[l][1] > intervals[r][0]:
                # just remove the one that has a larger right value
                if intervals[l][1] > intervals[r][1]:
                    # then the left one should be removed
                    removed += 1
                    l = r
                else:
                    # then the right one should be removed
                    removed += 1
                    r += 1
            else:
                # they did not clash, so just move left all the way up to r
                l = r
        return removed
            

            


















        # intervals = sorted(intervals)
        
        # # now if there is a tie on the first number,
        # # we always remove the one(s) with greater "second" numbers
        # # but we have to remove all of them if
        # # all the second numbers are greater than the first number of the next one
        # print(intervals)
        # l, r, = 0, 1
        # removed = 0
        # advance = 0
        # while l < len(intervals) and r < len(intervals):
        #     print(l, r)
        #     if l == r:
        #         r += 1
        #     elif intervals[l][0] == intervals[r][0]:
        #         print('removing intervals[r]', intervals[r]);
        #         # since right has a larger second number
        #         removed += 1
        #         r += 1
        #         advance += 1
        #     elif intervals[l][1] <= intervals[r][0]:
        #         # then we are good s l can advance
        #         l += 1 + advance
        #         advance = 0
        #     else:   # 1 has to go but it is the one with the second number being greater
        #         removed += 1
        #         if intervals[l][1] > intervals[r][1]:   # we want to remove left
        #             print('removing intervals[l]', intervals[l]);
        #             l = r
        #         else:   # we need to remove the right
        #             print('removing intervals[r]', intervals[r]);
        #             advance += 1
        #         r += 1

                    
        
        # return removed
        
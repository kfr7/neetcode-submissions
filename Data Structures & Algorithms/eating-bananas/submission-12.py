import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            print('-1')
            return -1
        
        l, r = 1, max(piles)
        min_speed = max(piles)
        while l <= r:
            speed = (r+l) // 2
            print(l, r, speed)
            # at this speed, lets see how long it will take us
            total_hours_spent = 0
            for pile in piles:
                total_hours_spent += math.ceil(pile / speed)
            print('ths vs h', total_hours_spent, h)
            if total_hours_spent <= h:
                min_speed = min(min_speed, speed)
                r = speed - 1
            else:
                print('too slow so l is now +1')
                l = speed + 1
        print('on last one')
        return min_speed
        
        
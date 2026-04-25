import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_speed = max(piles)
        while l <= r:
            speed = (r+l) // 2
            # at this speed, lets see how long it will take us
            total_hours_spent = 0
            for pile in piles:
                total_hours_spent += math.ceil(pile / speed)
            if total_hours_spent <= h:
                min_speed = min(min_speed, speed)
                r = speed - 1
            else:
                l = speed + 1
        return min_speed
        
        
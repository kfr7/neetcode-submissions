import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # speeds = [i for i in range(1, max(piles)+1)]  # don't actually need the list
        # binary search the speeds and for each speed we will go through the banana piles O(n)
        # temp = ceil(bananas / piles[0]) + ... + ceil(bananas / piles[0]) 
        # to get the answer temp must be <= h
        # if temp is > h, then we must speed UP (go right) on the speed
        # else, we can try going slower (go left) on the speed
        l, r = 0, max(piles) - 1
        minimumSpeed = max(piles)
        # use math.ceil
        while l <= r:
            mid = (l + r) // 2
            tempSpeed = mid + 1
            currSum = 0
            # now go through each pile of bananas and compute
            # print("tempSpeed:", tempSpeed)
            # print("L:", l, "R:", r, "M:", mid)
            for element in piles:
                currSum += math.ceil(element / tempSpeed)

            # print("currSum", currSum)

            if currSum > h:
                l = mid + 1
            else:
                minimumSpeed = min(minimumSpeed, tempSpeed)
                r = mid - 1
        return minimumSpeed


        
        
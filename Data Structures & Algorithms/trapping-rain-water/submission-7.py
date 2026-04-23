class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0 or len(height) == 1:
            return 0
        water = 0
        left_wall, right_wall = height[0], height[-1]
        l, r = 1, len(height)-2
        while l <= r:
            if left_wall < right_wall:
                collected = left_wall - height[l]
                if collected > 0:
                    water += collected
                left_wall = max(left_wall, height[l])
                l += 1
            else:
                collected = right_wall - height[r]
                if collected > 0:
                    water += collected
                right_wall = max(right_wall, height[r])
                r -= 1

        return water







        # below is the o(n) memory space version (it is always o(n) runtime but this one is o(3n))
        # idea; keep track of the highest walls that are to the right or to the left
        max_to_left = []
        highest = 0
        for i in range(len(height)):
            max_to_left.append(highest)
            highest = max(highest, height[i])
        max_to_right = []
        highest = 0
        for j in range(len(height)-1,-1,-1):
            max_to_right.append(highest)
            highest = max(highest, height[j])
        
        water = 0
        max_to_right = max_to_right[::-1]

        for i in range(len(height)):
            smallest_wall = min(max_to_left[i], max_to_right[i])
            if smallest_wall > height[i]:
                water += smallest_wall - height[i]

        return water

        
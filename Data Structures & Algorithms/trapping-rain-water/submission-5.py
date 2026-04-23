class Solution:
    def trap(self, height: List[int]) -> int:
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
        print(max_to_left)
        max_to_right = max_to_right[::-1]
        print(max_to_right)

        for i in range(len(height)):
            smallest_wall = min(max_to_left[i], max_to_right[i])
            if smallest_wall > height[i]:
                water += smallest_wall - height[i]

        return water

        
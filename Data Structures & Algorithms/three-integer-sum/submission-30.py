class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        for i in range(len(nums)):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            # because at this there is nothing to the right (just one number but no triplet)
            if i == len(nums)-2:
                break
            target = -(nums[i])
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    final.append([nums[i], nums[l], nums[r]])
                    move_l = l+1
                    while move_l < len(nums)-1 and nums[move_l] == nums[l]:
                        move_l += 1
                    l = move_l
                    continue
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return final
                    

        
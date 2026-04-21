class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # case where the pivot is on the right side: checking if target > than last element
        # also checking if first element is smaller than the target, or something like that
        l, r, = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            print(l, mid, r)
            if nums[mid] == target:
                return mid
            # go RIGHT if:
            # 1) the target is smaller than the current, target is smaller/equal to than the far right, but the current is bigger than far right
            # or 2) target is bigger than current and target is smaller/equal to the far right
            elif (target < nums[mid] and target <= nums[r] and nums[mid] > nums[r]) or \
                (target > nums[mid] and target <= nums[r]):
                l = mid + 1
            else:
                r = mid - 1
        return -1
        
        
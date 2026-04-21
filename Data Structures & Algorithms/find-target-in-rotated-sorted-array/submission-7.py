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
            elif (target < nums[mid] and target <= nums[r] and nums[mid] > nums[r]) or \
                (target > nums[mid] and target <= nums[r]):
                l = mid + 1
            else:
                r = mid - 1

            # elif (target < nums[mid] and target <= nums[r] and nums[l] >= nums[r]) or \
            #     (target > nums[mid] and target <= nums[r]) or \

            #     l = mid + 1
            # else:
            #     r = mid - 1
        return -1
        
        
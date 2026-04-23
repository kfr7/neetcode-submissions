class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # don't worry about edge case since there will always be one valid solution
        # and we know the length will always be at least 2 numbers long
        l, r = 0, len(numbers) - 1
        while l < r:
            # we are guaranteed to find a solution within this loop
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]
        
        
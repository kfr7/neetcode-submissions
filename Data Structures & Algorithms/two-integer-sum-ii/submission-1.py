class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right: # guaranteed so we will return answer in this loop
            tempSum = numbers[left] + numbers[right]
            if tempSum > target:
                right -= 1
            elif tempSum < target:
                left += 1
            else:
                return [left+1, right+1]
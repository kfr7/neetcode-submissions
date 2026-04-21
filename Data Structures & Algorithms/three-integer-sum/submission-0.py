class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def sort_three_numbers(a, b, c):
            if a > b:
                a, b = b, a
            if b > c:
                b, c = c, b
            if a > b:
                a, b = b, a
            return tuple((a, b, c))
        neededNumbers = dict()   # {neededNumber: [{indices}]}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                neededNumber = -(nums[i] + nums[j])
                if neededNumber not in neededNumbers:
                    neededNumbers[neededNumber] = [{i, j}]
                else:
                    neededNumbers[neededNumber].append({i, j})
        # now we can loop through nums and start building result
        result = set()
        for i in range(len(nums)):
            if nums[i] not in neededNumbers:
                continue
            # now we know it is a neededNumber so loop through all the index combinations that caused this
            for s in neededNumbers[nums[i]]:
                if i in s:
                    continue    
                # now we know the number we are at wasn't one of the 2 numbers computed to get this neededNumber
                temp = [nums[element] for element in s]
                temp.append(nums[i])
                result.add(tuple(sorted(temp)))
        
        return [list(s) for s in result]

                    
        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3. neetcode solution
        res = []
        # must sort the array so we can do 2 sum!
        nums.sort()
        for i in range(len(nums)):
            # if the number before it was the same, skip and go to the next index
            if i > 0 and nums[i-1] == nums[i]:
                continue
            # otherwise, compute 2 sum and target is nums[i]
            li, ri = i + 1, len(nums) - 1   # TRICK IS HERE TOO: li doesn't need to start before i otherwise this would give duplicates in res
            while li < ri:
                if nums[li] + nums[ri] + nums[i] < 0:   # we need to increase the value
                    li += 1
                elif nums[li] + nums[ri] + nums[i] > 0:   # we need to decrease the value
                    ri -= 1
                else:   # it is equal so add it to the result but then move the left index past duplicates
                    res.append([nums[li], nums[ri], nums[i]])
                    li += 1
                    while li < ri and nums[li - 1] == nums[li]:
                        li += 1
        return res


        # 2. solution = sort, then just take out one number and do two sum for it
        # nums.sort()
        # res = set()
        # for i in range(len(nums)):
        #     # now do two sum of left + right = -nums[i]
        #     leftIndex, rightIndex = 0, len(nums) - 1
        #     while leftIndex < rightIndex:
        #         if leftIndex == i:
        #             leftIndex += 1
        #             continue
        #         elif rightIndex == i:
        #             rightIndex -= 1
        #             continue
        #         if nums[i] == 0:
        #             print(nums[leftIndex], nums[rightIndex])
        #         # now that we know we are not at the current "target", try to get it
        #         if (nums[leftIndex] + nums[rightIndex] + nums[i] == 0):
        #             res.add(tuple(sorted([nums[leftIndex], nums[rightIndex], nums[i]])))
        #             leftIndex += 1
        #             rightIndex -= 1
        #             # don't break because more than one pair might be able to equal 0 with nums[i]
        #         elif (nums[leftIndex] + nums[rightIndex] + nums[i] < 0):
        #             leftIndex += 1
        #         else:
        #             rightIndex -= 1
        
        # return [list(t) for t in res]
            
            


        # 1. solution before looking anything up (just knowing that I was able to do n^2 but more better solution above)
        # neededNumbers = dict()   # {neededNumber: [{indices}]}
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         neededNumber = -(nums[i] + nums[j])
        #         if neededNumber not in neededNumbers:
        #             neededNumbers[neededNumber] = [{i, j}]
        #         else:
        #             neededNumbers[neededNumber].append({i, j})
        # # now we can loop through nums and start building result
        # result = set()
        # for i in range(len(nums)):
        #     if nums[i] not in neededNumbers:
        #         continue
        #     # now we know it is a neededNumber so loop through all the index combinations that caused this
        #     for s in neededNumbers[nums[i]]:
        #         if i in s:
        #             continue    
        #         # now we know the number we are at wasn't one of the 2 numbers computed to get this neededNumber
        #         temp = [nums[element] for element in s]
        #         temp.append(nums[i])
        #         result.add(tuple(sorted(temp)))
        
        # return [list(s) for s in result]

                    
        
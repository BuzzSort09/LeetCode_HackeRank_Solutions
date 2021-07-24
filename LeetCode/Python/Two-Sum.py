class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #########################################################################
        # # Brute force: 0(n^2)        
        # for firstIndex in range(0, len(nums)):
        #     for secondIndex in range(0, len(nums)):
        #         if firstIndex != secondIndex:
        #             if target == nums[firstIndex] + nums[secondIndex]:
        #                 return [firstIndex, secondIndex]                    
        # return []
        #########################################################################
        
        #########################################################################
        # Hash O(n)
        hashDict = {}
        for index in range(0, len(nums)):
            seekNumber = target - nums[index]
            if seekNumber not in hashDict:
                hashDict[nums[index]] = index
            else:
                return [hashDict[seekNumber], index]
        #########################################################################
            
        #########################################################################
        # # Less than O(n)
        # # We can find if the target exsit in the list, but can't find two indeicdes less than O(n)
        # nums.sort()     # O(nlogn)
        # left, right = 0, len(nums)-1        
        # while left < right:
        #     if nums[left] + nums[right] > target:
        #         right -= 1
        #     elif nums[left] + nums[right] < target:
        #         result = nums[left] + nums[right]
        #         left += 1
        #     else:
        #         return [left, right]
        #########################################################################

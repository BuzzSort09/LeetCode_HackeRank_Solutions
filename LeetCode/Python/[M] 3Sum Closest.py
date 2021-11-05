class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        closet_value = 10 ** 4 + 1        
        
        # sort: O(nlog(n))
        nums.sort()
        
        output_value = nums[0] + nums[1] + nums[2]
        
        # O(n^2)
        for index in range(0, len(nums)-1):            
            left = index + 1
            right = len(nums) - 1   
            
            while left < right:
                three_sum = nums[index] + nums[left] + nums[right]
                check_sum = target - three_sum
                
                if abs(check_sum) < abs(closet_value):
                    output_value = three_sum
                    closet_value = check_sum
                
                if check_sum > 0:
                    left += 1
                elif check_sum == 0:
                    break
                else:
                    right -= 1
                    
        return output_value
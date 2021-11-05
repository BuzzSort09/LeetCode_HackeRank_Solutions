class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output_list = []
        
        # sort - O(nLog(n))
        nums.sort()
      
        # O(n^2)        
        # O(n)
        for index in range(0, len(nums)):
            first_number = nums[index]
            
            seek_nums = nums[index+1:]            
            
            if first_number > 0:
                break
                
            hash_dict = {}
            
            # O(n)
            for second_index in range(0, len(seek_nums)):                
                seek_number = (seek_nums[second_index] + first_number) * -1
            
                if seek_number not in hash_dict:
                    hash_dict[seek_nums[second_index]] = second_index
                else:
                    temp = [first_number, seek_nums[second_index], seek_number]
                    if temp not in output_list:
                        output_list.append(temp)
        
        return output_list       
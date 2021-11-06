class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
     
        # Time: O(2n) --> O(n)
        # Space: O(n)
    
        zero_index = []
        output_list = []
        products = 1
        
        # O(n)
        # calculate products and check how many zeros in the list
        for index, number in enumerate(nums):
            if number != 0:
                products *= number
            else:
                zero_index.append(index)
                
            # if there are two more zeros, the ouput is always '0'
            if (len(zero_index) >= 2):
                output_list = [0] * len(nums)
                return output_list         
        
        # O(n)
        for index in range(0, len(nums)):
            if nums[index] == 0:
                output_list.append(products)
            elif len(zero_index) == 1:
                output_list.append(0)
            else:
                output_list.append(int(products/nums[index]))
 
        return output_list
class Solution:
    def maxArea(self, height: List[int]) -> int:
            
        left = 0
        right = len(height) - 1
        MaximumWater = 0
        y = 0
        
        # O(N)
        while left < right:
            # Get y-axis (length)
            if height[left] > height[right]:
                y = height[right]
            else:
                y = height[left]
                            
            MaximumWater = max(MaximumWater, y * (right-left))
            
            if height[left] > height[right]:
                right = right - 1
            else:                
                left = left + 1
                
        return MaximumWater
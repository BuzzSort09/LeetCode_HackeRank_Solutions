class Solution:
    def trap(self, height: List[int]) -> int:
        
#         # O(3N) --> O(N)
#         leftToRight = []
#         rightToLeft = []
#         totalWater = 0        
#         highWall = 0
        
#         # O(N)
#         # left to right
#         for index in range(len(height)):            
#             highWall = max(highWall, height[index])            
#             leftToRight.append(max(0, highWall - height[index]))
            
#         # O(N)
#         # right to left
#         highWall = 0
#         for index in range(len(height)-1, -1, -1):
#             highWall = max(highWall, height[index])
#             rightToLeft.insert(0, max(0, highWall - height[index]))
      
#         # O(N)
#         for index in range(len(height)):
#             totalWater += min(leftToRight[index], rightToLeft[index])
            
#         return totalWater

        # O(2N) --> O(N)
        leftToRight = []
        rightToLeft = []
        totalWater = 0        
        leftHighWall = 0
        rightHighWall = 0
        
        # O(N)       
        for index in range(len(height)):
             # left to right
            leftHighWall = max(leftHighWall, height[index])            
            leftToRight.append(max(0, leftHighWall - height[index]))

            # right to left
            rightHighWall = max(rightHighWall, height[len(height)-index-1])
            rightToLeft.insert(0, max(0, rightHighWall - height[len(height)-index-1]))
      
        # O(N)
        for index in range(len(height)):
            totalWater += min(leftToRight[index], rightToLeft[index])
            
        return totalWater
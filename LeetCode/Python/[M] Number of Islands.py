class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # O(n^2)

        if not grid:
            return 0

        output_cnt = 0      
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1':
                    self.map_travel(grid, i, j)
                    output_cnt += 1                    
        return output_cnt

    def map_travel(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = '#'        
        self.map_travel(grid, i+1, j)
        self.map_travel(grid, i-1, j)
        self.map_travel(grid, i, j+1)
        self.map_travel(grid, i, j-1)     
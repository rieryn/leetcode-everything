class Solution:
    visited = []
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        self.visited = []


        for i, k in enumerate(grid):
            for j, v in enumerate(k):
                if v == '1':
                    if (i, j) in self.visited:
                        continue
                    islands = islands + 1
                    self.ssearch(i,j, grid)
        
        return islands
                    
    def ssearch(self, i, j, grid):
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'

        if (j > 0 and grid[i][j-1] =='1'):
            self.ssearch(i, j-1,grid)
        if (j < len(grid[0])-1 and grid[i][j+1] =='1'):
            self.ssearch(i, j+1,grid)
        if (i > 0 and grid[i-1][j] =='1'):
            self.ssearch(i-1, j,grid)
        if(i < len(grid)-1 and grid[i+1][j] =='1'):
            self.ssearch(i+1, j,grid)
        

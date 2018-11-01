'''
0 1 0 1 0
0 1 0 1 1
0 0 1 0 1
0 1 1 0 0
'''

# DFS 

class Solution:
    
    def __init__(self, grid):
        self.grid = grid
        self.row_cnt = len(grid)
        self.col_cnt = len(grid[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.visited = [[False for i in range(self.col_cnt)] for j in range(self.row_cnt)]
        
    def is_valid(self, x, y):
        return x >= 0 and y >= 0 and x < self.row_cnt and y < self.col_cnt and not self.visited[x][y] and self.grid[x][y] == 1
        
    def find_max(self):
        
        max_ = 0
        
        for x in range(self.row_cnt):
            for y in range(self.col_cnt):
                if self.is_valid(x, y):
                    cnt = self.dfs(x, y)
                    
                    if cnt > max_:
                        max_ = cnt
                        
        return max_
    
    def dfs(self, x, y):
        
        self.visited[x][y] = True
        max_ = 1
        
        for direction in self.directions:
            new_x = x + direction[0]
            new_y = y + direction[1]

            if self.is_valid(new_x, new_y):
                curr = self.dfs(new_x, new_y) + 1
                
                if curr > max_:
                    max_ = curr
            
        return max_

    
grid = [
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 1, 1, 0, 0]
        ]
        
    
print(Solution(grid).find_max())
        

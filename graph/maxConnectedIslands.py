# Flatiron Health Interview
# Find Longest connected spots

# https://www.geeksforgeeks.org/find-length-largest-region-boolean-matrix/

'''
0 1 0 1 0
0 1 0 1 1
0 0 1 0 1
0 1 1 0 0
'''

# DFS

import sys


class Solution:
    
    def __init__(self, grid):
        self.grid = grid
        self.row_cnt = len(grid)
        self.col_cnt = len(grid[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.visited = [[False for _ in range(self.col_cnt)] for _ in range(self.row_cnt)]
        
    def is_valid(self, x, y):
        return x in range(self.row_cnt) and y in range(self.col_cnt) \
               and not self.visited[x][y] \
               and self.grid[x][y] == 1
        
    def find_max(self):
        
        max_ = 0
        
        for x in range(self.row_cnt):
            for y in range(self.col_cnt):
                if self.is_valid(x, y):
                    cnt = [1]
                    self.dfs(x, y, cnt)

                    max_ = max(max_, cnt[0])
                        
        return max_
    
    def dfs(self, x, y, cnt):
        
        self.visited[x][y] = True

        for direction in self.directions:
            new_x = x + direction[0]
            new_y = y + direction[1]

            if self.is_valid(new_x, new_y):
                cnt[0] += 1
                self.dfs(new_x, new_y, cnt)

    
grid = [
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 1, 1, 0, 0]
        ]
        
    
print(Solution(grid).find_max())
        

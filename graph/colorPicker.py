# Segovia Interview
# 
# Your previous Plain Text content is preserved below:
# 
# R B Y Y Y
# Y Y G B B
# B G G B B
# 
# 
# 
# R B Y Y Y
# Y Y B B B
# B B B* B B
# 
# ||
# 
# R B Y Y Y
# Y Y B B B
# B B B B B
# 
# R B Y Y Y
# Y Y B* B* B*
# B* B* B* B* B*
# 


def place_color(grid, row, column, color):
    
    directions = [(-1,0), (1, 0), (0, 1), (0, -1)]
    r_cnt = len(grid)
    c_cnt = len(grid[0])
            
    orig_color = grid[row][column]
    
    stack = [(row, column)]
            
    while stack:
                
        element = stack.pop()
        x = element[0]
        y = element[1]
        grid[x][y] = color
        
        for direction in directions:
            tmp_x = x+direction[0]
            tmp_y = y+direction[1]
            
            if grid[tmp_x][tmp_y] == color:
                continue
            
            if tmp_x in range(r_cnt) and tmp_y in range(c_cnt) and grid[tmp_x][tmp_y] == orig_color:
                stack.append((tmp_x, tmp_y))
                        
    return grid
    

grid = [
        ['R', 'B', 'Y', 'Y', 'Y'],
        ['Y', 'Y', 'G', 'B', 'B'],
        ['B', 'G', 'G', 'B', 'B']
       ]

# grid = [
#         ['R','B','Y', 'Y', 'Y'],
#         ['Y','Y','Y', 'B', 'B'],
#         ['B','Y','Y', 'B', 'B']
#        ]

# R B Y Y Y
# Y Y W W W
# W W W W W

print(place_color(grid, 1, 2, 'G'))

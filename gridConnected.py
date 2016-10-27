# If grid is connected
# altschool interview
#
# grid = [[0, 0, 1],
#         [0, 0, 1],
#         [0, 1, 1]] -> True

# grid = [[1, 0, 1],
#         [0, 0, 1],
#         [0, 1, 1]] -> False

# grid = [[1, 0, 1],
#         [0, 1, 0],
#         [0, 0, 1]] -> False

# n is grid size

def ifConnected(grid):
    def neighbors(x, y):
        n = len(grid)
        # Returns a list of cells that are adjacent.
        candidates = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        return [c for c in candidates if c[0] in range(n) and c[1] in range(n) and grid[c[0]][c[1]]==1]

    # calculate total non-empty cells
    cnt = 0
    cells = []
    checked_cells = [] 

    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if grid[x][y]==1:
                cnt += 1

                if cnt==1:
                    cells = [(x,y)]
    
    while len(cells)>0:

        cell = cells.pop(0)
        checked_cells.append(cell)
        cells.extend([x for x in neighbors(cell[0],cell[1]) if x not in checked_cells])

    print cnt, len(checked_cells)
    return cnt==len(checked_cells)

# grid = [[1, 0, 1],
#         [0, 1, 0],
#         [0, 0, 1]]

grid = [[1, 0, 1],
        [0, 0, 1],
        [0, 1, 1]]

# grid = [[0, 0, 1],
#         [0, 0, 1],
#         [0, 1, 1]]

print ifConnected(grid)
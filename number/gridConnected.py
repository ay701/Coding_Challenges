# If grid is connected / altschool 
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


def if_connected(grid):
    def neighbors(x, y):
        n = len(grid)
        # Returns a list of cells that are adjacent.
        candidates = [(x-1, y), (x+1, y), (x, y-1),(x, y+1)]
        return [(x, y) for x, y in candidates if x in range(n) and y in range(n) and grid[x][y] == 1]
    
    cnt = 0 # Total non-empty cells
    cells = [] # DFS stack
    checked_cells = [] # Checked cells

    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if grid[x][y] == 1:
                cnt += 1

                if cnt == 1:
                    cells = [(x, y)]
    
    while len(cells) > 0:
        cell = cells.pop(0)
        checked_cells.append(cell)
        cells += [x for x in neighbors(cell[0], cell[1]) if x not in checked_cells]

    # print cnt, len(checked_cells)
    return cnt == len(checked_cells)

# grid = [[1, 0, 1],
#         [0, 1, 0],
#         [0, 0, 1]]

grid = [[1, 0, 1],
        [0, 0, 1],
        [0, 1, 1]]

grid = [[0, 0, 1],
        [0, 0, 1],
        [0, 1, 1]]

print if_connected(grid)

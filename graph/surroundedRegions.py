# LeetCode - Surrounded Regions (Python)
# https://shenjie1993.gitbooks.io/leetcode-python/130%20Surrounded%20Regions.html
#
# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
#
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X

# Use DFS -
# 1. Add bordered box with "O" to queue
# 2. Mark each element from the stack to "M" as visited
# 3. Add neighbour box with value "O" to the queue
# 4. Loop through the grid, flip those "M" to "O", all others to "X"


def surrounded_regions(regions):

    queue = []

    r_len = len(regions)
    c_len = len(regions[0])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for i in range(r_len):
        for j in range(c_len):
            if i in [0, r_len-1] or j in [0, c_len-1]:
                if regions[i][j] == 'O':
                    # Push coordinates as tuple
                    queue.append((i, j))

    while queue:
        r, c = queue.pop(0)
        regions[r][c] = 'M'

        for direction in directions:
            r += direction[0]
            c += direction[1]

            if r in [0, r_len-1] and c in [0, c_len-1] and regions[r][c] == 'O':
                queue.append((r, c))

    print(regions)

    # update box
    for i in range(r_len):
        for j in range(c_len):
            regions[i][j] = 'O' if regions[i][j] == 'M' else 'X'

    return regions

regions = [['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X']]

print(surrounded_regions(regions))


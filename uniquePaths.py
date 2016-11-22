# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below). 
# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below). 
# How many possible unique paths are there? Above is a 3 x 7 grid. 
# How many possible unique paths are there? Note: m and n will be at most 100.


# @return an integer
def uniquePaths(m, n):
    if m == 1 and n == 1:
        list = [[1]]
    elif m == 1 and n > 1:
        list = [[1 for i in range(n)]]
    elif m > 1 and n == 1:
        list = [[1] for i in range(m)]
    else:
        list = [[0 for i in range(n)] for i in range(m)]
        print list
        exit
        for i in range(0, n):
            list[0][i] = 1
        for i in range(0, m):
            list[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                list[i][j] = list[i-1][j] + list[i][j-1]

    return list[m-1][n-1]

# print uniquePaths(1,4)
print uniquePaths(3,3)
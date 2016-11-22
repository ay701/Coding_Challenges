def MinimumPathSum(matrix):

    m = len(matrix)
    n = len(matrix[0])

    # rst = [[0]*n]*m   
    rst = [[0 for i in range(n)] for j in range(m)]
    rst[0][0] = matrix[0][0]
    
    for i in range(1,m):
    	rst[i][0] += rst[i-1][0] + matrix[i][0]

    for j in range(1,n):
    	rst[0][j] += rst[0][j-1] + matrix[0][j]

    for i in range(1,m):
    	for j in range(1,n):
    		rst[i][j] = min(rst[i-1][j],rst[i][j-1]) + matrix[i][j]

    print rst
    return rst[m-1][n-1]

matrix = [ [1,2,3],
           [3,5,1],
           [4,1,7],
           [6,2,4] ]

print MinimumPathSum(matrix)
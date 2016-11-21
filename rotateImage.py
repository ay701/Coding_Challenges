# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Follow up:
# Could you do this in-place?
#
# Thoughts:
# In fact, for any point (x, y), the affected point is (y, n – x – 1), (n – x – 1, n – y – 1), (n – y – 1, x), in which 'n' is the size of the matrix. 
# In other words, we need to move point like (x, y) -> (y, n – x – 1) -> (n – x – 1, n – y – 1) -> (n – y – 1, x) -> (x, y).

# When we process (0, 0), the last element in the first line is moved. 
# In fact, for the first line, we only need to process (0, 0) to (0, n – 2). 
# The affected points are like the following.

# For the second line, we need to start from the second element. 
# And ends one element earlier comparing to the first line, which is from (1, 1) to (1, n – 3).
# In conclusion, for the ith line, we start from (i, i), and ends at (i, n – 2 – i).

def rotateImage( matrix, n ):

    for i in range(n):
    	print matrix[i]

    for i in range(n/2):
    	for j in range(i, n-i-1):
    		tmp = matrix[i][j]
    		matrix[i][j] = matrix[n-j-1][i]
    		matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
    		matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
    		matrix[j][n-i-1] = tmp

    print ""

    for i in range(n):
    	print matrix[i]

matrix_1 = [ 
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
        ]

matrix_2 = [ 
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]
        ]

# rotateImage(matrix_1, 4)
rotateImage(matrix_2, 5)


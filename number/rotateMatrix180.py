# Rotate a Matrix by 180 degree
# Given a square matrix the task is that we turn it by 180 degrees
# in anti-clockwise direction without using any extra space.
# https://www.geeksforgeeks.org/rotate-matrix-180-degree/
#
# Examples :
#
# Input :  1  2  3
#          4  5  6
#          7  8  9
# Output : 9 8 7
#          6 5 4
#          3 2 1
#
# Input :  1 2 3 4
#          5 6 7 8
#          9 0 1 2
#          3 4 5 6
# Output : 6 5 4 3
#          2 1 0 9
#          8 7 6 5


def rotate_matrix_180(arr):

    r_cnt = len(arr)
    c_cnt = len(arr[0])

    i = r_cnt-1

    while i >= 0:
        j = c_cnt-1

        while j >= 0:
            print str(arr[i][j]) + " "
            j -= 1

        i -= 1
        print "\n"


arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 0, 1, 2],
       [3, 4, 5, 6]]

rotate_matrix_180(arr)


#######################################
# Method : 2(In-place rotation)
# There are four steps :
# 1- Find transpose of matrix.
# 2- Reverse columns of the transpose.
# 3- Find transpose of matrix.
# 4- Reverse columns of the transpose


def transpose(arr):

    r_cnt = len(arr)
    c_cnt = len(arr[0])

    for i in range(r_cnt):
        for j in range(c_cnt):
            tmp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = tmp

    return arr


def reverse_columns(arr):

    r_cnt = len(arr)
    c_cnt = len(arr[0])

    for c in range(c_cnt):
        for i in range(r_cnt):
            tmp = arr[i][c]
            arr[i][c] = arr[r_cnt-i][c]
            arr[r_cnt - i][c] = tmp

    return arr


def rotate_matrix_180_2(arr):
    arr = transpose(arr)
    arr = reverse_columns(arr)
    arr = transpose(arr)
    arr = reverse_columns(arr)

    return arr

print(rotate_matrix_180_2)





# Search a Word in a 2D Grid of characters
# Given a 2D grid of characters and a word, find all occurrences of given word in grid.
# A word can be matched in all 8 directions at any point. Word is said be found in a direction
# if all characters match in this direction (not in zig-zag form).
#
# The 8 directions are, Horizontally Left, Horizontally Right, Vertically Up and 4 Diagonal directions.
#
# Example:
#
# Input:  grid[][] = {"GEEKSFORGEEKS",
#                     "GEEKSQUIZGEEK",
#                     "IDEQAPRACTICE"};
#         word = "GEEKS"
#
# Output: pattern found at 0, 0
#         pattern found at 0, 8
#         pattern found at 1, 0
#
# Input:  grid[][] = {"GEEKSFORGEEKS",
#                     "GEEKSQUIZGEEK",
#                     "IDEQAPRACTICE"};
#         word = "EEE"
#
# Output: pattern found at 0, 2
#         pattern found at 0, 10
#         pattern found at 2, 2
#         pattern found at 2, 12
# Below diagram shows a bigger grid and presence of different words in it.
# https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/


class Solution:

    def __init__(self, board):
        self.board = board
        self.row_size = len(board)
        self.col_size = len(board[0])
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        self.word = ""
        self.word_size = 0
        self.count = 0

    def search_word(self, word):
        self.word = word
        self.word_size = len(word)

        if self.word_size == 0:
            return

        for i in range(self.row_size):
            for j in range(self.col_size):
                self.search(i, j)

        print self.count

    def search(self, x, y):

        if self.board[x][y] != self.word[0]:
            return False

        for direction in self.directions:

            new_x = x + direction[0]
            new_y = y + direction[1]
            k = 1

            while k < self.word_size:

                if new_x < 0 or new_y < 0 \
                        or new_x >= self.row_size \
                        or new_y >= self.col_size \
                        or self.board[new_x][new_y] != self.word[k]:
                    break

                k += 1
                new_x += direction[0]
                new_y += direction[1]

            if k == self.word_size:
                self.count += 1


board = [ ['B', 'N', 'E', 'Y', 'S'],
          ['H', 'E', 'D', 'E', 'S'],
          ['S', 'G', 'N', 'D', 'E'] ]

word = "DE"

Solution(board).search_word(word)
# Count of number of given string in 2D character array
# Given a 2-Dimensional character array and a string, we need to find the given string in 2-dimensional character array
# such that individual characters can be present left to right, right to left, top to down or down to top.
#
# Examples:
#
# Input : a ={
#             {D,D,D,G,D,D},
#             {B,B,D,E,B,S},
#             {B,S,K,E,B,K},
#             {D,D,D,D,D,E},
#             {D,D,D,D,D,E},
#             {D,D,D,D,D,G}
#            }
#         str= "GEEKS"
# Output :2
#
# Input : a = {
#             {B,B,M,B,B,B},
#             {C,B,A,B,B,B},
#             {I,B,G,B,B,B},
#             {G,B,I,B,B,B},
#             {A,B,C,B,B,B},
#             {M,C,I,G,A,M}
#             }
#         str= "MAGIC"
#
# Output :3


class Solution:
    def __init__(self, board):
        self.board = board
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.word = ""
        self.word_cnt = 0
        self.row_cnt = 0
        self.col_cnt = 0
        self.count = 0

    def count_number(self, word):
        self.word = word
        self.word_cnt = len(word)
        self.row_cnt = len(word)
        self.col_cnt = len(word[0])

        for i in range(self.row_cnt):
            for j in range(self.col_cnt):
                print(i, j)
                self.search_word(i, j, -1, -1)

        print self.count

    def search_word(self, x, y):
        if self.board[x][y] != self.word[0]:
            return

        k = 1
        new_x = x
        new_y = y

        while True:

            # print(k, new_x, new_y)

            if k == self.word_cnt:
                self.count += 1
                break

            for direction in self.directions:
                print(direction[0], direction[1])
                new_x += direction[0]
                new_y += direction[1]

                # print "xx"
                if new_x >= 0 \
                        and new_y >= 0 \
                        and new_x < self.row_cnt \
                        and new_y < self.col_cnt \
                        and self.board[new_x][new_y] == self.word[k]:
                    k += 1
                    # print(new_x, new_y)


board = [ ["D", "D", "D", "G", "D", "D"],
          ["B", "B", "D", "E", "B", "S"],
          ["B", "S", "K", "E", "B", "K"],
          ["D", "D", "D", "D", "D", "E"],
          ["D", "D", "D", "D", "D", "E"],
          ["D", "D", "D", "D", "D", "G"] ]

word = "DE"

Solution(board).count_number(word)

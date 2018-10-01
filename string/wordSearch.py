# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

class WorldSearch:

    def __init__(self, board, word):
        self.word = word
        self.board = board
        self.row_len = len(self.board)
        self.col_len = len(self.board[0])

    def search_word(self):
        for i in range(self.row_len):
            for j in range(self.col_len):
                if self.dfs(i, j, 0):
                    print(i, j)
                    return True

        return False

    def dfs(self, i, j, depth):
        if i < 0 or j < 0 or i >= self.row_len or j >= self.col_len:
            return False

        if self.board[i][j] in self.word:
            if depth == len(self.word):
                return True

            tmp = self.board[i][j]
            self.board[i][j] = '#'

            if self.dfs(i-1, j, depth+1) or \
                    self.dfs(i+1, j, depth + 1) or \
                    self.dfs(i, j-1, depth + 1) or \
                    self.dfs(i, j+1, depth + 1):
                return True

            self.board[i][j] = tmp

        return False


L = [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]

word_1 = "ABCCED"
word_2 = "SEE"
word_3 = "ABCB"
ws = WorldSearch(L, word_1)
ws = WorldSearch(L, word_2)
ws = WorldSearch(L, word_3)

if ws.search_word():
    print("Found")
else:
    print("Not found!")

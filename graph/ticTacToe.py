# Example: "O" wins
#  
#  X | O | O
# --- --- ---
#  X | O | X
# --- --- ---
#  O  | X | X
#
# Time complexity: O(1)
#
# Reference:
# http://fernisoites.blogspot.com/2016/08/348-design-tic-tac-toe.html


class TicTacToe:
    def __init__(self, n):
        self.player_map = {"X": 1, "O": -1}
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag_1 = 0
        self.diag_2 = 0
        self.n = n

    def move(self, r, c, player):
        self.rows[r] += self.player_map[player]
        self.cols[c] += self.player_map[player]

        if r == c:
            self.diag_1 += self.player_map[player]

        if r+c == self.n-1:
            self.diag_2 += self.player_map[player]

        print(self.rows, self.cols, self.diag_1, self.diag_2)

        for val in [self.rows[r], self.cols[c], self.diag_1, self.diag_2]:
            if val == self.n:
                return "X"
            elif val == -1*self.n:
                return "O"

        return None

# t = ticTacToe(3)
# print t.move(0,0,"X")
# print t.move(0,1,"X")
# print t.move(0,2,"O")
# print t.move(1,1,"X")
# print t.move(1,2,"X")
# print t.move(2,2,"X")

# OUTPUT:
# [ [X, X, O],
#   [X, X, -]
#   [-, -, X]]


t = TicTacToe(3)
print t.move(0, 0, "X")
print t.move(0, 1, "X")
print t.move(0, 2, "O")
print t.move(1, 1, "X")
print t.move(1, 2, "X")
print t.move(2, 2, "X")


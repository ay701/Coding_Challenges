# Example: "O" wins
#  
#  X | O | O
# --- --- ---
#  X | O | X
# --- --- ---
#  O  | X | X
#
# Time complexity: O(1)

class ticTacToe:
    def __init__(self, leng):
        self.leng = leng
        self.player1 = "X"
        self.player2 = "O"
        self.rows = []
        self.cols = []
        self.diag1 = 0
        self.diag2 = 0

        for i in range(leng):
            self.rows.append(0)
            self.cols.append(0)

    def move(self, x, y, player):
    	value = 1 if player=="X" else -1

    	self.rows[x] += value
    	self.cols[y] += value

    	if x-y==0:
            self.diag1 += value

        if y+x==self.leng-1:
        	self.diag2 += value

        if self.leng in [abs(self.rows[x]),abs(self.cols[y]),abs(self.diag1),abs(self.diag2)]:
        	# print self.rows[x],self.rows[y]
        	return player

        return None

t = ticTacToe(3)
print t.move(0,0,"X")
print t.move(0,1,"X")
print t.move(0,2,"O")
print t.move(1,1,"X")
print t.move(1,2,"X")
print t.move(2,2,"X")

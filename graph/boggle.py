#
# (Find all possible words in a board of characters) | Set 1
# Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character.
# Find all possible words that can be formed by a sequence of adjacent characters.
# Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell.
# Example:
#
# Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
#       boggle[][]   = {{'G','I','Z'},
#                       {'U','E','K'},
#                       {'Q','S','E'}};
#      isWord(str): returns true if str is present in dictionary
#                   else false.
#
# Output:  Following words of dictionary are present
#         GEEKS
#         QUIZ
#
# https://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/
# http://www.martinbroadhurst.com/boggle-in-python.html
# 1. Use DFS
# 2. Use Trie
# Ref :
# https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1


class TrieNode:

    def __init__(self, char=""):
        self.char = char
        self.children = []
        self.word_finished = False  # is it last char of word
        self.counter = 1  # how many times this char appeared in addition process


def add_word(root, word):

    node = root

    for ch in word:
        # We only care if its found in children
        # update node with new node for loop
        found_in_child = False

        for child in node.children:
            if child.char == ch:
                child.counter += 1
                found_in_child = True
                node = child
                break

        if not found_in_child:
            new_node = TrieNode(ch)
            node.children.append(new_node)
            node = new_node

    node.word_finished = True


def boggle(root, word):

    node = root

    for ch in word:

        found_in_child = False

        for child in node.children:

            if child.char == ch:
                found_in_child = True
                node = child
                break

        # Not found
        if not found_in_child:
            return False, 0

    return True, node.counter


dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]

root = TrieNode()
for word in dictionary:
    add_word(root, word)


print(boggle(root, "FOR"))



####
#DFS
####


class Boggle:

    def __init__(self, board, words):
        self.board = board
        self.words = words
        self.r_cnt = len(board)
        self.c_cnt = len(board[0])
        self.visited = [[False for _ in range(self.r_cnt)] for _ in range(self.r_cnt)]
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    def is_word(self, word):
        if len(word) == 0:
            print("Input can't be empty!")
            return False

        if word not in self.words:
            print(word + " not found in dictionary!")
            return False

        for x in range(self.r_cnt):
            for y in range(self.c_cnt):
                if self.board[x][y] == word[0] and self.dfs(x, y, word, 1):
                    return True

        return False

    def dfs(self, x, y, word, index):

        if index == len(word):
            return True

        self.visited[x][y] = True

        for direction in self.directions:
            new_x = x + direction[0]
            new_y = x + direction[1]

            if new_x >= 0 and new_y >= 0 \
                    and new_x < self.r_cnt \
                    and new_y < self.c_cnt \
                    and not self.visited[new_x][new_y] \
                    and self.board[new_x][new_y] == word[index]:
                return self.dfs(new_x, new_y, word, index+1)


board = [['G', 'I', 'Z'],
         ['U', 'E', 'K'],
         ['Q', 'S', 'E']]
dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]

print(Boggle(board, dictionary).is_word("FOR"))



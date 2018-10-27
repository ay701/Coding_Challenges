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

class TrieNode:

    def __init__(self, char=""):
        self.char = char
        self.children = []
        self.word_finished = False # is it last char of word
        self.counter = 1 # how many times this char appeared in addition process


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

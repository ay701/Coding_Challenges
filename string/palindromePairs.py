# LeetCode - Palindrome Pairs (Java)
#
# Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list,
# so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
#
# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]

# https://fizzbuzzed.com/top-interview-questions-5/

from collections import defaultdict


class Trie:
    def __init__(self):
        # letter -> next trie node.
        self.paths = defaultdict(Trie)
        # If a word ends at this node, then this will be a positive value
        # that indicates the location of the word in the input list.
        self.wordEndIndex = -1
        # Stores all words that are palindromes from this node to end of word.
        # e.g. if we are on a path 'a','c' and word "babca" exists in this trie
        # (words are added in reverse), then "acbab"'s index will be in this
        # list since "bab" is a palindrome.
        self.palindromesBelow = []

    # Adds a word to the trie - the word will be added in 
    # reverse (e.g. adding abcd adds the path d,c,b,a,$index) to the trie.
    # word - string the word to be added
    # index - int index of the word in the list, used as word identifier.
    def addWord(self, word, index):
        trie = self
        for j, char in enumerate(reversed(word)): 
            if isPalindrome(word[0:len(word)-j]):
                trie.palindromesBelow.append(index)
            trie = trie.paths[char]
        trie.wordEndIndex = index


def isPalindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    return word[0] == word[-1] and isPalindrome(word[1:-1])


def makeTrie(words):
    trie = Trie()
    for i, word in enumerate(words):
        trie.addWord(word, i)
    return trie


# Takes the trie, a word, and its index in the word array 
# and returns the index of every word that could be appended
# to it to form a palindrome.
def getPalindromesForWord(trie, word, index):
    # Walk trie. Every time we find a word ending,
    # we need to check if we could make a palindrome.
    # Once we get to the end of the word, we must check
    # all endings below for palindromes (they are already
    # stored in 'palindromesBelow').
    output = []
    while word:
        if trie.wordEndIndex >= 0:
            if isPalindrome(word):
                output.append(trie.wordEndIndex)
        if not word[0] in trie.paths:
            return output
        trie = trie.paths[word[0]]
        word = word[1:]

    if trie.wordEndIndex >= 0:
        output.append(trie.wordEndIndex)
    output.extend(trie.palindromesBelow)
    return output


def palindromePairs(words):
    trie = makeTrie(words)
    output = []
    for i, word in enumerate(words):
        candidates = getPalindromesForWord(trie, word, i)
        output.extend([[i, c] for c in candidates if i != c])
    return output

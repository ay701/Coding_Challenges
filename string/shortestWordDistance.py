# LeetCode - Shortest Word Distance
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
#
# Given word1 = "coding", word2 = "practice", return 3.
# Given word1 = "makes", word2 = "coding", return 1.

import sys


def shortest_word_distance(words, word1, word2):

    m = -1
    n = -1

    min_ = sys.maxint

    for i, word in enumerate(words):

        if word == word1:
            m = i

            if n != -1:
                min_ = min(min_, m-n)

        if word == word2:
            n = i

            if m != -1:
                min_ = min(min_, n-m)

    return min_

words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"

print(shortest_word_distance(words, word1, word2))


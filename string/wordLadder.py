# Given two words (start and end), and a dictionary,
# find the length of shortest transformation sequence from start to end,
# such that only one letter can be changed at a time and each intermediate word must exist in the dictionary. 
# For example, given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", the program should return its length 5.

# Use BFS
# https://www.programcreek.com/2012/12/leetcode-word-ladder/


def word_ladder(start, end, word_list):

    if len(start) != len(end):
        return 0

    n = len(start)
    queue = [(start, 1)]  # add start to queue with level 1

    while len(queue) > 0:
        word_tuple = queue.pop(0)
        word = word_tuple[0]
        level = word_tuple[1]

        for i, c in enumerate(word):
            # Ascii code from "a" to "z"
            for code in range(ord('a'), ord('z')+1):
                if c == chr(code):
                    continue

                tmp_word = word[0:i] + chr(code) + word[i+1:n]
                if tmp_word == end:
                    return level+1

                if tmp_word in word_list:
                    queue.append((tmp_word, level+1))

    return 0


start = "hit"
end = "cog"
# end = "hot"
word_list = ["hot", "dot", "dog", "lot", "log"]

print word_ladder(start, end, word_list)
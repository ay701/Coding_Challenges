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
        word_tuple = queue.pop(0)  # BFS, pop the earliest word
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


# LeetCode - Word Ladder II
# Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end,
# such that: 1) Only one letter can be changed at a time, 2) Each intermediate word must exist in the dictionary.
#
# For example, given: start = "hit", end = "cog", and dict = ["hot","dot","dog","lot","log"], return:
#
# [
#     ["hit", "hot", "dot", "dog", "cog"],
#     ["hit", "hot", "lot", "log", "cog"]
# ]


def word_ladder_2(start, end, word_list):

    if len(start) != len(end):
        return 0

    n = len(start)
    queue = [[start, [start]]]  # add start to queue
    output = []

    while len(queue) > 0:

        if len(output) and len(output[0]) in range(1, len(queue[-1][1])):
            return output

        # if len(output) > 0:
        #     print(output)
        #     exit(0)

        word_tuple = queue.pop(0)  # BFS, pop the earliest word
        word = word_tuple[0]
        steps = word_tuple[1]

        for i, c in enumerate(word):
            # Ascii code from "a" to "z"
            for code in range(ord('a'), ord('z')+1):
                if c == chr(code):
                    continue

                tmp_word = word[0:i] + chr(code) + word[i+1:n]

                if tmp_word == end:
                    # steps.append(tmp_word)
                    output.append(steps)
                    continue

                if tmp_word in word_list and tmp_word not in steps:
                    steps.append(tmp_word)
                    queue.append((tmp_word, steps))

    return output


start = "hit"
end = "cog"
# end = "hot"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

print word_ladder_2(start, end, word_list)


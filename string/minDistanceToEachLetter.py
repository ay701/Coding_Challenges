# If you have a string BLOOMBERG, what is the minimum distance of each letter from the character 'B'.

import sys


def min_distance_to_each_letter(st, target):

    if st == "" or target == "":
        return 0

    dic = {}

    for i in range(len(st)):
        if dic.get(st[i]) is None:
            dic[st[i]] = [i]
        else:
            dic[st[i]].append(i)

    target_pos = dic[target]
    dic.pop(target, None)
    result = {}

    for letter, letter_pos in dic.items():

        min_ = sys.maxint

        for target_po in target_pos:
            for letter_po in letter_pos:
                cur_min = abs(letter_po - target_po)

                if cur_min < min_:
                    min_ = cur_min

        result[letter] = min_

    return result

print(min_distance_to_each_letter("BLOOMBERG", "B"))





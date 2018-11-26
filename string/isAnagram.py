# Given two strings s and t, write a function to determine if t is an anagram of s.

from collections import defaultdict


def is_anagram(st1, st2):

    map1 = {}
    map2 = {}

    if len(st1) != len(st2):
        return False

    for (s1, s2) in zip(st1, st2):
        if map1.get(s1) is None and map2.get(s2) is None:
            map1[s1], map2[s2] = s2, s1
            continue

        if map1.get(s1) != s2 or map2.get(s2) != s1:
            # print map1.get(s1), map2.get(s2)
            return False

    return True


print(is_anagram("hacaha", "dbhbdc"))


def is_anagram_(st1, st2):

    n = len(st1)
    m = len(st2)

    if n != m:
        return False

    dic = defaultdict(int)

    for i in range(n):
        dic[st1[i]] += 1
        dic[st2[i]] -= 1

    for v in dic.values():
        if v != 0:
            return False

    return True


print(is_anagram_("hacaha", "dbhbdc"))



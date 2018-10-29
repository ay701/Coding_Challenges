# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
#
# Example 1:
#
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
#
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true
# Note:
# You may assume both s and t have the same length.


def is_isomorphic(s, t):

    len_s = len(s)
    len_t = len(t)

    if len_s == 0 or len_s != len_t:
        return False

    hash_map = {}  # One map is enough

    for i in range(len_s):
        source = hash_map.get(s[i])
        target = hash_map.get(t[i])

        if source is None and target is None:
            hash_map[s[i]] = t[i]

            if s[i] != t[i]:
                hash_map[t[i]] = s[i]
        elif source != t[i] or target != s[i]:
            return False

    return True


s = 'abbaa'
t = 'cddcd'

print is_isomorphic(s, t)


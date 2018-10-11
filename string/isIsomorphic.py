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

    if len_s != len_t:
        return False

    s_map = {}
    t_map = {}

    for i in range(len_s):
        source = t_map.get(t[i])
        target = s_map.get(s[i])

        if source is None and target is None:
            s_map[s[i]] = t[i]
            t_map[t[i]] = s[i]
        elif source != s[i] or target != t[i]:
            return False

    return True


s = 'abbaa'
t = 'cddcd'

print is_isomorphic(s, t)


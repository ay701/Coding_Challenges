def is_isomorphic(s, t):

    if len(s) != len(t):
        return False

    s_map, t_map = {}, {}

    for i in range(len(s)):
        source, target = t_map.get(t[i]), s_map.get(s[i])

        if source is None and target is None:
            s_map[s[i]], t_map[t[i]] = t[i], s[i]
        elif source != s[i] or target != t[i]:
            return False

    return True


s = 'abbaa'
t = 'cddcd'
print is_isomorphic(s, t)


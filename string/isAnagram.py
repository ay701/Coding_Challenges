def isAnagram(st1, st2):

    map1 = {}
    map2 = {}

    if len(st1)!=len(st2):
	    return False

    for (s1,s2) in zip(st1,st2):
        if map1.get(s1) is None and map2.get(s2) is None:
            map1[s1], map2[s2] = s2, s1
            continue

        if map1.get(s1)!=s2 or map2.get(s2)!=s1:
            # print map1.get(s1), map2.get(s2)
            return False

    return True


print isAnagram("hacaha","dbhbdc")
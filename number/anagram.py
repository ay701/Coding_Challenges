# Enter your code here. Read input from STDIN. Print output to STDOUT

# {"cat", "act", "tac", "fat", "dog",  "aft" , "tca"} => 3

# n elements, m for each elem

# O(n*mlog(m))

# {"act", "act",  "aft", "aft", "dog"}

from collections import defaultdict


def find_num_of_anagram(l):
    
    dic = defaultdict(int)
    
    n = len(l)
    
    if n in [0, 1]:
        return n

    for i in range(n):
        
        e = ''.join(sorted(l[i]))
        dic[e] = 1
    
    return sum(dic.values())


l = ["act", "cat",  "aft", "aft", "dog"]
l2 = ["cat", "act", "tac", "fat", "dog",  "aft", "tca"]

print(find_num_of_anagram(l))
print(find_num_of_anagram(l2))

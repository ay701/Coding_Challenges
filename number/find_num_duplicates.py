## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.
## Bloomberg interview

"""

"aaaabbcddd"
"a4b2cd3"

"aaabaaa"
"a3ba3"

"""


def find_num_duplicates(s):
    
    output = ""

    if len(s) < 2:
        return s

    prev = s[0]
    cnt = 1

    for cur in s[1:]:
        if cur != prev:
            output += prev if cnt == 1 else prev + str(cnt)
            cnt = 1
        else:
            cnt += 1
        
        prev = cur

    output += cur if cnt == 1 else cur + str(cnt)

    return output
    
print find_num_duplicates("hi")
print find_num_duplicates("aaabaaa")
print find_num_duplicates("aaaabbcddd")
print find_num_duplicates("aaaabbcd")

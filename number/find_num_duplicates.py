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

    if len(s)<2:
        return s

    cur = s[0]
    cnt = 1

    for i, nex in enumerate(s[1:]):
        
        # print cur, nex, cnt
        
        if cur!=nex:
            output += cur if cnt==1 else cur + str(cnt)
            cnt = 1
        else:
            cnt += 1
        
        cur = nex

    output += nex if s[-2]!=nex else nex + str(cnt)

    return output       
    
print find_num_duplicates("hi")
print find_num_duplicates("aaabaaa")
print find_num_duplicates("aaaabbcddd")
print find_num_duplicates("aaaabbcd")

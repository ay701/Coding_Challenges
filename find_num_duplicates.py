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
    cnt = 0
    ln = len(s)

    if ln<=1:
        return s

    for i in range(ln-1):
        
        cur = s[i]
        nex = s[i+1]
        cnt += 1
        print cur, nex, cnt
        
        if cur!=nex:
            output += cur if cnt==1 else cur + str(cnt)
            cnt = 0

        if i==ln-2:
            cnt += 1

    output += nex if cnt==1 else nex + str(cnt)

    return output       
    
print find_num_duplicates("hi")
print find_num_duplicates("aaabaaa")
print find_num_duplicates("aaaabbcddd")

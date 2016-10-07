
def firstUniqueChar(data):

    order = {}
    occurrence = {}

    for i in range(len(data)):
        if data[i] in occurrence:
            occurrence[data[i]] += 1
        else:
            occurrence[data[i]] = 1
            order[data[i]] = i
            
    for k,v in occurrence.items():
        if v==1 :
            return order[k] 
        
        
print firstUniqueChar("xxyyz")

def firstNoneRepeat(s):

    if len(s)<=1:
        return s

    cnt = 1
    cur = s[0]

    for nex in s[1:]:
        
        if cur!=nex:
            if cnt==1:
                return cur
            else:
                cnt = 1
        else:
            cnt += 1
        
        cur = nex

    return None

print firstNoneRepeat("xxyyzzzzzzpuuiiiiiiioo")

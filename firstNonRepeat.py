
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

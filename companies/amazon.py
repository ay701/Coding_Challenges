import math

def ClosestXdestinations(numDestinations, allLocations, numDeliveries):
    dic = [False for i in range(numDestinations)]
    cur = [0,0]
    output = []
    
    while True:
        if len(output) == numDeliveries:
            break
        
        val = [0,0] 
    
        for i in range(numDestinations):
            if dic[i]:
                continue
            
            e = allLocations[i]
            x = e[0]-cur[0]
            y = e[1]-cur[1]
            tmp = math.sqrt(y*y+x*x)
            
            if tmp < val[1] or val[0] == 0:
                val = [i, tmp]
            
        dic[val[0]] = True
        cur = allLocations[val[0]]
        output.append(cur)
        print(cur)
        # print(dic)
        
    return output
        
    

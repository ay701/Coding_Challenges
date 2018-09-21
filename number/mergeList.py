# Canary.js
# Merge list (tuple as element)
# input a list of ranges represented by tuple 
# output a list of merged ranges 

# ex input [( 1,5), (7, 10), (3, 6), (-1, 0)]
# ex output [(1,6), (7, 10), (-1, 0)]

# ex input [( 1,5), (2, 10), (1, 7)]
# ex output [(1,10)]

def test_case1():
    data = [( 1,5), (7, 10), (3, 6), (-1, 0)]
    result = cal(data)
    print result
    # assert result == [(-1, 0), (1,6), (7, 10)]
    
def cal(data):
    
    output = []
    data = sorted(data, reverse=True)
    last = ()
    #[(-1, 0), ( 1,5),(3, 6) (7, 10)]
    
    while data :
            
        if last :
            cur = last
            nex = data.pop()
        else:
            cur = data.pop()
            
            if data:
                nex = data[-1]
            else:
                output.append(cur)
    
        if cur[1] < nex[0]:
            print output, cur, nex, data
            output.append(cur)
            last = ()
                
        elif cur[1] < nex[1]:
            last = (cur[0], nex[1])
        
        if not data and nex:
            output.append(nex)
        
    return output

test_case1()

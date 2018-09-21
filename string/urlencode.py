# urlencode()
# '&', ' ', '?', ',' 

# input : http://www.hi.com/hello?123
# output : http://www.hi.com/hello%3F123

# space -> %20
# space -> 32

# * -> %2A
# * -> 42 - 12 = 30 = 

def urlencode(st):

    output = ''
    
    for s in st:
    
        code_ = ord(s)
    
        if code_ in range(32,48) or code_ in range(58,65) or code_ in range(91,97) :
            output += "%" + str(hex(code_))[2:]
        else:
            output += s 
            
    return output
    
print urlencode('http://www.hi.com/hello?123')
##########################################
# Strings of symbols balanced:
# { { ( [ ] [ ] ) } ( ) }
# [ [ { { ( ( ) ) } } ] ]
# [ ] [ ] [ ] ( ) { }
# 
# Strings of symbols not balanced:
# ( [ ) ]
# ( ( ( ) ] ) )
# [ { ( ) ]
##########################################

def parChecker(data):
    stack = []
    balanced = True
    pars = {"{":"}","(":")","[":"]"}
 
    for ele in data:
        if ele in pars.keys() and balanced:
            stack.append(ele)
        else:
            if not stack:
                return False
            else :
                k = stack.pop()
                if pars[k]!=ele:
                    return False

    if stack :
        balanced = False 

    return balanced

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))

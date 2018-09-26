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

def parentheseChecker(data):
    stack = []
    balanced = True
    pars = {"{": "}", "(": ")", "[": "]"}
 
    for item in data:
        if item in pars.keys() and balanced:
            stack.append(item)
        else:
            if not stack:
                return False
            else:
                k = stack.pop()
                if pars[k] != item:
                    return False

    if stack:
        balanced = False 

    return balanced

print(parentheseChecker('{{([][])}()}'))
print(parentheseChecker('[{()]'))

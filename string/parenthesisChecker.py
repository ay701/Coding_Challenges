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


def parenthesis_checker(data):
    stack = []
    balanced = True
    pars = {"{": "}", "(": ")", "[": "]"}
 
    for item in data:
        if not balanced:
            return False

        if item in pars.keys():
            stack.append(item)
        else:
            if not stack:
                balanced = False
            else:
                k = stack.pop()
                if pars[k] != item:
                    balanced = False

    return len(stack) == 0 and balanced

print(parenthesis_checker('{{([][])}()}'))
print(parenthesis_checker('[{()]'))

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


def parenthesis_checker(items):
    stack = []
    pars = {"{": "}", "(": ")", "[": "]"}
    values = set(pars.values())
 
    for item in items:
        if pars.get(item):
            stack.append(item)
        elif values.get(item):
            # If stack is empty
            if not stack:
                return False
            else:
                k = stack.pop()

                if pars[k] != item:
                    return False

    return len(stack) == 0

print(parenthesis_checker('{{([][])}()}'))
print(parenthesis_checker('[{()]'))


# Write a function `is_balanced` that returns whether a given string contains
# balanced parentheses
#
# Examples
# is_balanced("(())") => True
# is_balanced("((())") => False
# is_balanced(")()()") => False
# is_balanced("(()())") => True
# is_balanced("(()))") => False


def is_balanced(input_str):
    stack = []
    pairs = {"(": ")", "{": "}", "[": "]"}
    values = set(pairs.values())

    for symb in input_str:
        if symb in pairs:
            stack.append(symb)
        elif symb in values:
            if not stack:
                return False

            top_symb = stack.pop()

            if symb != pairs[top_symb]:
                return False

    return len(stack) == 0


print(is_balanced("(())"))  # True
print(is_balanced("((())"))  # False
print(is_balanced(")()()"))  # False
print(is_balanced("(()())"))  # True
print(is_balanced("(()))"))  # False

print(is_balanced("Hello (hi)"))
print(is_balanced("))(("))

print(is_balanced("([{}])"))  # True
print(is_balanced("({[})]"))  # False










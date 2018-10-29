# LeetCode - Evaluate Reverse Polish Notation
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression. For example:
#
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


def evaluate_reverse(input):

    l = []
    operaters = ["+", "-", "*", "/"]

    for e in input:
        if e.isdigit():
            l.append(e)
        else:
            second = int(l.pop())
            first = int(l.pop())
            index = operaters.index(e)

            if index == 0:
                l.append(first+second)
            elif index == 1:
                l.append(first-second)
            elif index == 2:
                l.append(first*second)
            elif index == 3:
                l.append(first//second)

    return l.pop()


print(evaluate_reverse(["2", "1", "+", "3", "*"]))
print(evaluate_reverse(["4", "13", "5", "/", "+"]))

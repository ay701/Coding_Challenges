#Validate if a given string can be interpreted as a decimal number.
# https://shenjie1993.gitbooks.io/leetcode-python/065%20Valid%20Number.html
#
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false


def valid_number(s):

    s = s.strip()

    index = 0
    is_valid = False
    is_exp = True

    # Deal with symbol
    if s[0] in ['+', '-']:
        s = s[1:]

    n = len(s)

    # Deal with digit
    while index < n and s[index].isdigit():
        is_valid = True
        index += 1

    # Deal with dot
    if index < n and s[index] == '.':
        index += 1

        while index < n and s[index].isdigit():
            is_valid = True
            index += 1

    # Deal with exponent
    if is_valid and index < n and s[index] in ['e', 'E']:
        index += 1
        is_exp = False

        if s[index] in ['+', '-']:
            index += 1

        while index < n and s[index].isdigit():
            is_exp = True
            index += 1

    # Return true only deal with all the characters and the part in front of and behind 'e' are all ok
    return is_valid and is_exp and index == n and s[0].isdigit() and s[-1].isdigit()

print(valid_number("3.e-23"))
print(valid_number(".2e81"))
print(valid_number("2e10"))
print(valid_number(" 0.1"))
print(valid_number("1 b"))
print(valid_number("3-2"))
print(valid_number("abc"))
print(valid_number("3."))

# if __name__ == "__main__":
#     assert Solution().isNumber("3.e-23") == True
#     assert Solution().isNumber(".2e81") == True
#     assert Solution().isNumber("2e10") == True
#     assert Solution().isNumber(" 0.1") == True
#     assert Solution().isNumber("1 b") == False
#     assert Solution().isNumber("3-2") == False
#     assert Solution().isNumber("abc") == False

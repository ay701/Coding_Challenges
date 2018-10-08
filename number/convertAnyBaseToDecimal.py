#
# Convert a number from any base to base 10
#


def val(ch):
    ch = ord(ch)

    if ch in range(48, 58):
        ch -= 48

    if ch in range(65, 91):
        ch -= 55

    return ch


def to_decimal(number, base):
    result = 0

    for index, ch in enumerate(number[::-1]):
        ch = val(ch)

        if ch > base:
            return 'invalid number'

        result += ch * base ** index

    return result


def to_decimal_2(number, base):
    return sum([val(ch) * base ** index for index, ch in enumerate(number[::-1])])

print(to_decimal('1A', 36))
print(to_decimal_2('1A', 36))

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
    number = number[::-1]

    for k, v in enumerate(number):
        print v, ord(v), val(v)
        v = val(v)

        if v > base:
            return 'invalid number'

        result += v * base ** k

    return result


def to_decimal_2(number, base):
    return sum([val(v) * base ** k for k, v in enumerate(number[::-1])])

print(to_decimal('1A', 36))
print(to_decimal_2('1A', 36))

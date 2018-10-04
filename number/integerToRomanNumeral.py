# Write a Python program to convert an integer to a roman numeral.


class Solution:
    def __init__(self):
        self.val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]

        self.syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]

    def int_to_roman(self, num):

        roman_num = ''
        i = 0

        while num > 0:
            for _ in range(num // self.val[i]):
                roman_num += self.syb[i]
                num -= self.val[i]

            i += 1

        return roman_num


print(Solution().int_to_roman(1))
print(Solution().int_to_roman(3800))
print(Solution().int_to_roman(4000))

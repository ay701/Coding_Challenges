# LeetCode - Integer to English Words
#
# Convert a non-negative integer to its english words representation.
# Given input is guaranteed to be less than 231 - 1.
#
# For example,
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
#
# Reference:
# https://www.jianshu.com/p/a29a42152d70

class Solution:
    def __init__(self):
        self.less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                        "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def integers_to_english_words(self, num):

        if num == 0:
            return "Zero"

        result = ""
        i = 0  # use for count num of thousands

        while num > 0:
            if num % 1000 > 0:
                result = self.helper(num % 1000) + self.thousands[i] + " " + result

            num //= 1000
            i += 1

        return result

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.less_than_20[num] + " "
        elif num < 100:
            return self.tens[num//10] + " " + self.less_than_20[num%10] + " "
        else:
            return self.tens[num//100] + " Hundred " + self.helper(num%100)


print(Solution().integers_to_english_words(12345000000))

# LeetCode - Implement strStr() (Java)
#
# Problem:
# Implement strStr().
#
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# https://blog.csdn.net/coder_orz/article/details/51708389


def strStr(haystack, needle):

    n = len(haystack)
    m = len(needle)

    if m == 0 or n == 0:
        return -1

    for i in range(n):

        if i + m > n:
            return -1

        k = 0
        for j in range(m):
            if haystack[i+j] == needle[j]:
                if k == m-1:
                    return i

                k += 1
            else:
                break

    return -1

print(strStr("helloworld", "wor"))


def strStr2(haystack, needle):

    for i in range(len(haystack)-len(needle)):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1

print(strStr2("helloworld", "wor"))


# KMP resolve: (O(n+m))

def strStr3(haystack, needle)
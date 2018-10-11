# Single character and empty sth both are palindrome


def is_palindrome(st):
    return str(st) == str(st)[::-1]

# print is_palindrome("hello")
# print is_palindrome("helleh")


def is_palindrome_1(st):
    return st == ''.join(reversed(st))
#
# print is_palindrome_1("hello")
# print is_palindrome_1("helleh")


def is_palindrome_2(st):

    n = len(st)

    if n in [0, 1]:
        return True

    for i in range(n):
        if st[i] != st[n-i-1]:
            return False

    return True

print is_palindrome_2("hello")
print is_palindrome_2("helleh")


def is_palindrome_3(st):
    n = len(st)

    if n in [0, 1]:
        return True

    mid = n//2

    if n % 2 == 1:
        left = mid
        right = mid
    else:
        left = mid-1
        right = mid

    for i in range(mid):
        if st[left-i] != st[right+i]:
            return False

    return True

print is_palindrome_3("hello")
print is_palindrome_3("helleh")

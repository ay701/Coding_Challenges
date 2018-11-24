# Program to print all substrings of a given string
# Given a string as an input. We need to write a program that will print all non-empty substrings of that given string.
#
# Examples :
#
# Input :  abcd
# Output :  a
#           b
#           c
#           d
#           ab
#           bc
#           cd
#           abc
#           bcd
#           abcd


def sub_strings(st):

    n = len(st)

    for i in range(n):
        for j in range(i, n):
            print(st[i:j+1])


sub_strings("abcd")



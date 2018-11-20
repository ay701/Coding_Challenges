# Fizz Buzz Implementation
# Fizz Buzz is a very simple programming task, asked in software developer job interviews.
#
# A typical round of Fizz Buzz can be:
# Write a program that prints the numbers from 1 to 100 and for multiples of '3' print "Fizz"
# nstead of the number and for the multiples of '5' print "Buzz".
#
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14,
# Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26,
# Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ...


def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print "fizzbuzz"
        elif i % 3 == 0:
            print "fizz"
        elif i % 5 == 0:
            print "buzz"
        else:
            print i

fizz_buzz(100)

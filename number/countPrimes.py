# Leetcode - Count Primes
# Python Program for Sieve of Eratosthenes
# Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.
# For example, if n is 10, the output should be "2, 3, 5, 7".
# If n is 20, the output should be "2, 3, 5, 7, 11, 13, 17, 19".
# Reference:
# https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/


def count_primes(n):
    num = [True for _ in range(n+1)]
    i = 2

    while i * i < n:
        if num[i]:
            for j in range(i*2, n+1, i):
                num[j] = False

        i += 1

    return sum([1 for e in num[2:] if e])


print(count_primes(10))

# Use recursion
def fib(n):
    if n in [0, 1]:
        return n

    return fib(n-1)+fib(n-2)

# print fib(5)


# Use iterative
def fib_iterative(n):
    n1 = 0
    n2 = 1
    cnt = 0

    if n < 0:
        raise Exception('Error number')

    while cnt < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        cnt += 1

fib_iterative(6)


# use generator
def fib2():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a+b

for ind, res in enumerate(fib2()):
    if ind == 6:
        print ind, res
        break


# Large data
# use generator
def fib3(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a+b

for x in fib3(6):
    print(x)

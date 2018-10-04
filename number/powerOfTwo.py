# Use anonymous function


def power_of_two(n):
    return list(map(lambda x: x**2, range(n)))

print(power_of_two(5))


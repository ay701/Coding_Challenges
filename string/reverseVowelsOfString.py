# LeetCode - Reverse Vowels of a String
#
# Write a function that takes a string as input and reverse only the vowels of a string.

# Use two pointers, left to beginning by increasing, right to end of string by decreasing


def reverse_vowels_of_a_string(st):

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    l = list(st)  # Convert string to list
    i = 0
    j = len(st)-1

    while i < j:
        if st[i] not in vowels:
            i += 1
            continue

        if st[j] not in vowels:
            j -= 1
            continue

        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp
        i += 1
        j -= 1

    return "".join(l)


print(reverse_vowels_of_a_string('HELLO'))

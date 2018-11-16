# Given an array, make all its possible permutations. 
# For example, given [1,2,3] output

# [[1,2,3], [1,3,2], [3,2,1], [3,1,2], [2,3,1], [2,1,3]]


def permutations(numbers):
    n = len(numbers)

    if n == 0:
        return []
    elif n == 1:
        return [numbers]
    else:
        output = []

        for i in range(n):
            sub_numbers = permutations(numbers[0:i]+numbers[i+1:n])

            for cur_number in sub_numbers:
                tmp = cur_number + [numbers[i]]
                output += [tmp] if tmp not in output else []

        return output
        # return [element for index, element in output if element not in numbers[:index]]

# print(permutations([1,2,3]))
# print(permutations([1]))
# print(len(permutations([1,2,3,5,6])))
print(permutations([1, 2, 2]))
print(permutations([1, 2, 3]))


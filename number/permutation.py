# Given an array, make all its possible permutations. 
# For example, given [1,2,3] output

# [[1,2,3], [1,3,2], [3,2,1], [3,1,2], [2,3,1], [2,1,3]]


def permutations(nums):
    n = len(nums)

    if n == 0:
        return []
    elif n == 1:
        return [nums]
    else:
        output = []

        for i in range(n):
            sub_nums = permutations(nums[0:i]+nums[i+1:n])

            for sub_num in sub_nums:
                tmp = sub_num + [nums[i]]
                output += [tmp] if tmp not in output else []

        return output
        # return [element for index, element in output if element not in numbers[:index]]

# print(permutations([1,2,3]))
# print(permutations([1]))
# print(len(permutations([1,2,3,5,6])))
print(permutations([1, 2, 2]))
print(permutations([1, 2, 3]))

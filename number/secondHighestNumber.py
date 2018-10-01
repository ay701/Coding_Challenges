# Largest, Smallest, Second Largest, Second Smallest in a List
# Since, unlike other programming languages, Python does not have arrays, instead,
# it has list. Using lists is more easy and comfortable to work with in comparison to arrays.
# Moreover, the vast inbuilt functions of Python, make the task easier. So using these techniques,
# lets try to find the various ranges of the number in a given list.


def second_highest_number(L):

    first_max = L[0]
    second_max = L[0]
    first_min = L[0]
    second_min = L[0]

    for item in L:
        if item > first_max:
            first_max = item
        elif item != first_max and item > second_max:
            second_max = item
        elif item < first_min:
            first_min = item
        elif item != first_min and second_min > item:
            second_min = item

    print("Largest element is:", first_max)
    print("Smallest element is:", first_min)
    print("Second Largest element is:", second_max)
    print("Second Smallest element is:", second_min)

# Driver Code
list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
second_highest_number(list1)
def remove_duplicates(nums):
    final_list = []

    for num in nums:
        final_list += [num] if num not in final_list else []

    return final_list


# Driver Code 
duplicate = [2, 4, 10, 20, 5, 2, 20, 4] 
print(remove_duplicates(duplicate))

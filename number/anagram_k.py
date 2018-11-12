# Check if two strings are k-anagrams or not
# Given two strings of lowercase alphabets and a value k,
# the task is to find if two strings are K-anagrams of each other or not.
#
# Two strings are called k-anagrams if following two conditions are true.
#
# Both have same number of characters.
# Two strings can become anagram by changing at most k characters in a string.
#
# Examples :
#
# Input:  str1 = "anagram" , str2 = "grammar" , k = 3
# Output:  Yes
# Explanation: We can update maximum 3 values and
# it can be done in changing only 'r' to 'n'
# and 'm' to 'a' in str2.
#
# Input:  str1 = "geeks", str2 = "eggkf", k = 1
# Output:  No
# Explanation: We can update or modify only 1
# value but there is a need of modifying 2 characters.
# i.e. g and f in str 2.
#
# Here we use only one count array to store counts of characters in str1.
# We traverse str2 and decrement occurrence of every character in count array that is present in str2.
# If we find a character that is not there in str1, we increment count of different characters.
# If count of different character become more than k, we return false.


def anagram_k(st1, st2, k):

    dic = {}

    if len(st1) != len(st2):
        return False

    for ch in st1:
        dic[ch] = dic[ch]+1 if dic.get(ch) else 1

    cnt = 0

    for ch in st2:
        if dic.get(ch):
            dic[ch] -= 1

            if dic[ch] == 0:
                dic.pop(ch, None)
        else:
            print(ch)
            cnt += 1

    return k > cnt


# print(anagram_k("geeks", "eggkf", 2))
print(anagram_k("anagram", "grammar", 3))


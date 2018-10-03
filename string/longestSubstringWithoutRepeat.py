# Given a string, find the length of the longest substring without repeating characters.

def longest_substring_without_repeat(s):
    """
            :type s: str
            :rtype: int
            """

    subs = list()
    length = len(s)

    for i in range(length+1):
        for j in range(i+1, length+1):
            sub = s[i:j]
            no_dup = True

            for c in sub:
                if sub.count(c) > 1:
                    no_dup = False
                    break

            if no_dup and not subs.count(sub):
                subs.append(sub)

    return len(sorted(subs, key=lambda x: len(x), reverse=True)[0])

print(longest_substring_without_repeat("abcabcbbcdefg"))

# Using sliding window algorithm
# The final solution has O(N) time complexity and O(N) space complexity.
# http://blog.gainlo.co/index.php/2016/10/07/facebook-interview-longest-substring-without-repeating-characters/


def longest_substring_without_repeat_2(s):

    length = len(s)

    if length < 1:
        return s

    start = 0
    end = 0

    longest = ""
    my_set = set()

    while end < length:
        end += 1
        cur = s[end - 1]

        # If not in set, add to set, update values
        if cur not in my_set:
            my_set.add(cur)

            if end - start > len(longest):
               longest = s[start:end]

            continue

        # If not in set, move two pointers, update set
        while start < end - 1:
            if s[start] == cur:
                start += 1
                break
            else:
                my_set.remove(s[start])
                start += 1

    return longest

print longest_substring_without_repeat_2("abcadbef")







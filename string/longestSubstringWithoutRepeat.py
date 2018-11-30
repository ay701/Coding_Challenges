# Given a string, find the length of the longest substring without repeating characters.


def longest_substring_without_repeat(s):
    """
            :type s: str
            :rtype: int
            """

    n = len(s)
    longest = [""]

    if n < 1:
        return s

    for i in range(n):
        for j in range(i+1, n+1):
            sub = s[i:j]
            no_dup = True

            for c in sub:
                if sub.count(c) > 1:
                    no_dup = False
                    break

            if no_dup:
                if len(sub) > len(longest[0]):
                    longest = [sub]
                elif len(sub) == len(longest[0]):
                    longest.append(sub)

    return longest

    # print(sorted(subs, key=lambda x: len(x), reverse=True)[0])
    # return len(sorted(subs, key=lambda x: len(x), reverse=True)[0])

# print(longest_substring_without_repeat("abcabcbbcdefg"))


# Using sliding window algorithm
# The final solution has O(N) time complexity and O(N) space complexity.
# http://blog.gainlo.co/index.php/2016/10/07/facebook-interview-longest-substring-without-repeating-characters/


def longest_substring_without_repeat_2(s):

    n = len(s)

    if n <= 1:
        return s

    i = 0
    longest = s[0:1]
    result = s[0:1]

    for j in range(1, n):
        cur = s[j]

        # If not in result, update result
        if cur not in longest:
            print(longest)

            if j+1-i > len(longest):
                longest = s[i:j+1]
                result = s[i:j+1]
                print("result: " + result)
        else:
            # Move first pointer, clear set
            for index in range(i, j+1):
                if s[index] == cur:
                    i = index+1
                    j = i+1
                    longest = s[i:j]
                    break

    return result

print longest_substring_without_repeat_2("abcadbef")

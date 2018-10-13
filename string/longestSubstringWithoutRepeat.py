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

    if n < 1:
        return s

    start = 0
    end = 0

    longest = ""
    my_set = set()

    while end < n:
        end += 1
        cur = s[end-1]

        # If not in set, add to set, update values
        if cur not in my_set:
            my_set.add(cur)

            if end - start > len(longest):
               longest = s[start:end]

            continue
        else:
            # Move first pointer, clear set
            for i in range(start, end-1):
                if s[i] == cur:
                    start = i+1
                    end = start
            my_set.clear()

    return longest

print longest_substring_without_repeat_2("abcadbef")

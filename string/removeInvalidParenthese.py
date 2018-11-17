# LeetCode 301. Remove Invalid Parentheses
# https://zxi.mytechroad.com/blog/searching/leetcode-301-remove-invalid-parentheses/
# DFS -> Remove one char at a time
# Time Complexity: O(N^(l+r))

def remove_invalid_parentheses(st):

    l = 0
    r = 0
    result = []

    # Compute min number of left & right parentheses
    for ch in st:
        if ch == "(":
            l += 1

        if ch == ")":
            if l == 0:
                r += 1
            else:
                l -= 1

    print(l, r)

    dfs(st, 0, l, r, result)

    print(st)
    return result


def dfs(st, index, l, r, result):

    if l == 0 and r == 0 and is_valid(st):
        result.append(st)

    for i in range(index, len(st)):
        if i != index and st[i] == st[i-1]:
            continue

        if r > 0 and st[i] == ")":
            dfs(st[0:i]+st[i+1:], i, l, r-1, result)

        if l > 0 and st[i] == "(":
            dfs(st[0:i]+st[i+1:], i, l-1, r, result)


# Check if string is valid parentheses
def is_valid(st):

    cnt = 0

    for ch in st:
        if ch == "(":
            cnt += 1
        elif ch == ")":
            cnt -= 1

        if cnt < 0:
            return False

    return cnt == 0


# print(remove_invalid_parentheses("((((()())()"))
print(remove_invalid_parentheses("()())()"))
# print(remove_invalid_parentheses("(a)())()"))
print(remove_invalid_parentheses(")("))
# print(remove_invalid_parentheses(")())("))
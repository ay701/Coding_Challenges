# Max Binary Gap
# Problem: Get maximum binary Gap.
#
# For example, 9's binary form is 1001, the gap is 2.


def solution(N):
    max_gap = 0
    current_gap = 0

    # Skip the tailing zero(s)
    while N > 0 and N % 2 == 0:
        N //= 2
        print(N)

    while N > 0:
        remainder = N % 2

        if remainder == 0:
            # Inside a gap
            current_gap += 1
        else:
            # Gap ends
            if current_gap != 0:
                max_gap = max(current_gap, max_gap)
                current_gap = 0

        N //= 2

    return max_gap

print(solution(9))


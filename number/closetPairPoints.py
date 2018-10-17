def solution(x, y):
    a = list(zip(x, y))  # This produces list of tuples
    print a
    
    ax = sorted(a, key=lambda x: x[0])  # Presorting x-wise
    ay = sorted(a, key=lambda x: x[1])  # Presorting y-wise
    print ax
    print ay

    # p1, p2, mi = closest_pair(ax, ay)  # Recursive D&C function
    #return mi

solution([1, 2, 3], [4, 5, 6])

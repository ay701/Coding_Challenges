def isPanlindrome( st ):
    return str(st)==str(st)[::-1]    

print isPanlindrome( "hello" )
print isPanlindrome( "helleh" )

def isPanlindrome_1( st ):
    return st == ''.join(reversed(st))
print isPanlindrome_1( "hello" )
print isPanlindrome_1( "helleh" )

def isPanlindrome_2( st ):

    st = list(st)
    is_Pan = True

    if len(st)<=1:
       is_Pan = False

    while st and is_Pan:
        if st[0]!=st[-1]:
            is_Pan = False
        else:
            st.pop(0)
            st.pop()

    return is_Pan

print isPanlindrome_2( "hello" )
print isPanlindrome_2( "helleh" )

def isPanlindrome_3( st ):
    st = list(st) 
    length = len(st)

    if length<=1:
        return True

    half = length//2

    if length%2==1:
        left = half-1
        right = half+1
    else:
        left = half-1
        right = half

    for i in range(half):
        if st[left-i] != st[right+i]:
            return False

    return True
print isPanlindrome_3( "hello" )
print isPanlindrome_3( "helleh" )

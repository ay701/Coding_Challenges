# Leetcode 9
# Determine whether an integer is a palindrome. Do this without extra space.

def isPalindrome_int(num):

    if num<0:
    	num = num*-1

    if num<10:
        return True

    div = 1
    while num/div>10:
    	div *= 10

    print div

    while div>1:
    	left = num/div
    	right = num%10

        print left, right
    	if left!=right:
    		return False

        num = (num%div)/10
        div/=100 

    return True

print isPalindrome_int(12321)

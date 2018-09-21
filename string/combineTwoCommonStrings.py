# Write a function f(a, b) which takes two character string arguments and returns 
# a string containing only the characters found in both strings in the order of a. 
# Write a version which is order N-squared and one which is order N.

def combineTwoCommonStrings_n_square(str1,str2):
    output = []

    for i in str1:
        for j in str2:
            if i==j and i not in output:
            	output.append(i) 

    return ''.join(output)

print combineTwoCommonStrings_n_square("hello", "hallo")


def combineTwoCommonStrings_n(str1,str2):
    dic = {}
    output = []

    for i in str1:
    	dic[i] = True

    for j in str2:
    	if dic.get(j) is not None:
    	    output.append(j)
            del dic[j]
    	    
    return ''.join(output)

print combineTwoCommonStrings_n("hello", "hallo")
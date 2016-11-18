# Write a method that takes in a String and returns the length of most common length of words in the String. // Audible
# Test case : "the dog went to the big store" -> 3
# Test case : "the the the went town mark holt stop" -> 4
# Can we use built-in function, split, join?
# Consider the result could be a list of length
from collections import defaultdict

def mostCommonLengthWords(st):
    dic = defaultdict(int)
    leng = []
    cnt = 0

    l = st.split()

    for s in l:
        # s = s.strip(",.- ")

        # Use raw instead of strip
        s = s[:-1] if ord(s[-1]) not in range(65,91) and ord(s[-1]) not in range(97,123) else s
        s = s[1:] if ord(s[0]) not in range(65,91) and ord(s[0]) not in range(97,123) else s
        # print s 

        n = len(s)
        dic[n] += 1

        if dic[n]>cnt:
            cnt = dic[n]
            leng = [n]
        elif dic[n]==cnt:
            leng.append(n)

    return leng

print mostCommonLengthWords(s)


def mostCommonLengthWords(input):
   
    input = input.strip()
    leng = len(input)

    if leng<2:   
        return leng    
   
    start = 0
    max_occurence = 0
    max_leng = []
    dic = {}

    for i in range(leng-2):

        cur = input[i]
        nex = input[i+1]
   
        if cur!=" " and nex==" ":

            k = i-start+1
               
            dic[k] = dic.get(k,0)+1
            start = i+2

            if dic[k] > max_occurence:
                max_leng = [k]
                max_occurence = dic[k]
            elif dic[k] == max_occurence:
                max_leng.append(k)
           
        cur = nex
       
    k = leng-start
    dic[k] = dic.get(k,0)+1

    if dic[k] > max_occurence:
        max_leng = [k]
        max_occurence = dic[k]
    elif dic[k] == max_occurence:
        max_leng.append(k)

    return max_leng
   

s = "-the dog is a superb animals" # 3
# print countWords(s)



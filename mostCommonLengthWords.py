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

# Original way, use pointers, without split function
def mostCommonLengthWords(st):
   
    st = st.strip()
    n = len(st)

    if n<2:   
        return n    
   
    start = 0
    cnt = 0
    leng = []
    dic = defaultdict(int)

    for i in range(n):
   
        if st[i]==" ":

            k = i-start # get length
            dic[k] += 1
            start = i+1

            if dic[k] > cnt:
                leng = [k]
                cnt = dic[k]
            elif dic[k] == cnt:
                leng.append(k)
       
    k = leng-start
    dic[k] += 1

    if dic[k] > cnt:
        leng = [k]
        cnt = dic[k]
    elif dic[k] == cnt:
        leng.append(k)

    return leng
   
s = "-the dog is a superb animals" # 3
# print countWords(s)



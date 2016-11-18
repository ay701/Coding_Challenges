# Write a method that takes in a String and returns the length of most common length of words in the String.
# Audible
# "the dog went to the big store" -> 3
# "the the the went town mark holt stop" -> 4

# Can we use built-in function, split, join?

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
   

s = "the dog is a superb animal" # 3
print countWords(s)

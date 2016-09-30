# Write a method that takes in a String and returns the number of words in the String.
# input = "hello world"
# input = "it's me"

def countWords(input):
   
   if len(input)==0 or input==" ":   
       return 0    
       
   cur = input[0]   # cur = "h"
   start = 0
   dic = {}  # key -> length of word, val -> occurence
   
   for i, nex in enumerate(1,len(input)):
       # cur = "h"
       # nex =  "e" 
       # output = 0
   
       if nex==" ":  
           if cur!=" ": 
               # length of word
               k = len(input[i]-input[start])
               
               dic[k] = dic.get(k,0)+1
               # 5 -> 1
               # 5 -> 2
               
               # output += 1
               start = i
           
       cur = nex
       
    if input[-1]!=" ":
       k = len(len(input)-input[start]-1)
       dic[k] = dic.get(k,0)+1

    cnt = 0
    ret = -1

    for k, v in dic.items():
      if v>cnt:
          cnt = v 
          ret = k
       
   return None if ret == -1 else ret
   
test_input = "hello world"
test_input = "hello world "
print countWords(test_input)

# "the dog went to the big store" -> 3
# "the the the went town mark holt stop" -> 4















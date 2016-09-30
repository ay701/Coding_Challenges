# Write a method that takes in a String and returns the length of most common length of words in the String.
# Audible interview
# "the dog went to the big store" -> 3
# "the the the went town mark holt stop" -> 4

def countWords(input):
   
   if len(input)==0 or input==" ":   
       return 0    
       
   cur = input[0]   # cur = "h"
   start = 0
   dic = {}  # key -> length of word, val -> occurence
   
   for i, nex in enumerate(input[1:]):
       # cur = "t"
       # nex =  "h"
   
       if nex==" " and cur!=" ":
           # length of word
           k = len(input[i]-input[start])
               
           dic[k] = dic.get(k,0)+1
           # 3 -> 1
           # 3 -> 2
               
           start = i
           
       cur = nex
       
    if input[-1]!=" ":
       k = len(input)-start-1
       dic[k] = dic.get(k,0)+1

    cnt = 0
    ret = 0

    for k, v in dic.items():
      if v>cnt:
          cnt = v 
          ret = k
       
   return ret
   
test_input = "hello world"
test_input = "hello world "
print countWords(test_input)














# 
# Your previous Plain Text content is preserved below:
# 
# Given an unsorted array, print out any number which has a pair in that array.
#   Each pair should result in the number being printed exactly once.
#   A number may appear in multiple pairs 
#   Example: [2, 3, 1, 2, 3, 3, 3, 2, 4, 3] results in: 2 3 3
# 
#  Lifion / 2018-10-04


class Solution:
    
    def __init__(self, arr):
        self.arr = arr
        self.dic = {}

    def pairs(self):
        
        for element in self.arr:
            if self.dic.get(element) is None:
                self.dic[element] = True
            else:
                print(element)
                self.dic.pop(element)
                
arr = [2, 3, 1, 2, 3, 3, 3, 2, 4, 3]
Solution(arr).pairs()

# 
# The purpose of these functions is to perform run length encoding & decoding on a string,
# where a run  # of the same character are replaced by a single copy followed by the number of repetitions;
# e.g. aaabbcdda --> a3b2cd2a


def encoding(st):
    
    output = ""
    length = len(st)
    
    if length < 2:
        return st
    
    prev = st[0]
    cnt = 1
    
    for cur in st[1:length]:
        
        if prev == cur:
            cnt += 1
        else:
            if cnt > 1:
                output += prev + str(cnt)
            else:
                output += prev
            
            cnt = 1
            
        prev = cur
        
    if cnt > 1:
        output += prev + str(cnt)
    else:
        output += prev
    
    return output

st = "aaaaaaaaaaaaaaaaaaaaabbcdda"
print(encoding(st))


def decoding(st):

    # print(int("5"))
    # exit()

    output = ""
    length = len(st)
    prev = st[0]
    num = ""
    
    for cur in st[1:length]:
        if cur.isdigit():
            num += cur
        else:
            if num == "":
                output += prev
            else:
                cnt = int(num)

                for i in range(cnt):
                    output += prev

                num = ""

            # Only when cur is alphabet, it moves
            prev = cur

    if num == "":
        output += prev
    else:
        for i in range(int(num)):
            output += prev
        output += prev
        
    return output


st = "a13b2cd2a"
print(decoding(st))

Please use this Google doc to code during your interview. To free your hands for coding, we recommend that you use a headset or a phone with speaker option.


1. From a stream of bytes find the longest contiguous sequences of distinct bytes (no repeated byte). Return the length of the longest sequence seen and the number of times a sequence of that length has been seen.


Example:


    abcadba<<<  


    LONGEST  COUNT  SEQUENCE
    1        1      a
    2        1      ab
    3        1      abc
    3        2      bca
    4        1      bcad
    4        2      cadb
    3               dba


abcb


   1 a
   2 ab
   3 abc
   2 cb


Assume a language appropriate get_next_byte() function.


def parseString(st):


    seq = []
    unique_chars = []


    # char for key, index for value, dictionary
     
    dic = {}  # key for length, value for count
    longest = 0
    count = 0


    for s in st:
        if s in unique_chars:
            # find the index of s, cut the front part
            ind = seq.index(s)
            
            for i in range(ind):
                unique_chars.remove(seq[i]) 
  
            seq = seq[ind+1:]
        else:
            unique_chars.add(s)


        seq.append(s)
        leng = len(seq)
        dic[leng] = dic.get(leng,0) + 1
            
        if longest<leng:
             longest = leng
             count = dic[leng]
    
    return (longest, count)


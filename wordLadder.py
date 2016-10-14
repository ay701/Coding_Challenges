# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, 
# such that only one letter can be changed at a time and each intermediate word must exist in the dictionary. 
# For example, given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", the program should return its length 5.

def wordLadder(start,end,dic):

    if len(start)!=len(end):
    	return 0

    leng = len(start)
    queque = [(start,1)]  # add start to queque with level 1

    while len(queque)>0:
    	word_tuple = queque.pop(0)
        word = word_tuple[0]
        level = word_tuple[1]

        for i, c in enumerate(word):
        
            for c_ in range(97,123):
                if c==chr(c_):
            	    continue

                tmp_word = word[0:i] + chr(c_) + word[i+1:leng]
                if tmp_word==end:
                	return level+1

                if tmp_word in dic:
            	    queque.append((tmp_word,level+1))

    return 0


start = "hit"
end = "cog"
# end = "hot"
dic = ["hot","dot","dog","lot","log"]
print wordLadder(start,end,dic)
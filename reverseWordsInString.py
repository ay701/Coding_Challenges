################################
# 1. Reverse the whole string
# 2. Reverse each word
################################


def reverseWordsInString(data):
 
    output = []
    data = reverse(data)
    prev = -1

    for cur, item in enumerate(data):
        if item == " ":
            prev += 1
            output.append(reverse(data[prev:cur]))
            output.append(" ")
            prev = cur
            #print output

    output.append(reverse(data[prev+1:cur+1]))

    return "".join(output)


def reverse(data):

    data = list(data)
    leng = len(data)

    for i in range(leng):
        if i<=leng-i-1:
            tmp = data[leng-i-1]
            data[leng-i-1] = data[i]
            data[i] = tmp

    return ''.join(data)

print reverseWordsInString(" hi nihao esmayil")

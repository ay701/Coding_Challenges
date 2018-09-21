def bubbleSort(data):
    exchange = True

    for i in range(len(data)-1,-1,-1):

        if not exchange: 
            return data

        exchange = False

        for j in range(i):
            if data[j]>data[j+1]:
                exchange = True
                data[j], data[j+1] = data[j+1], data[j]

    return data

print bubbleSort([4,3,5,1,2,0])


def bubbleSort_(data):
    length = len(data)

    for i in range(length):
        for j in range(1,length-i):
            if data[j-1]>data[j]:
                data[j], data[j-1] = data[j-1], data[j]

    return data

print bubbleSort_([4,3,5,1,2,0])
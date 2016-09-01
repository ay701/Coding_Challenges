def bubbleSort(data):
    exchange = True

    for i in range(len(data)-1,-1,-1):

        if not exchange: 
            return data

        exchange = False

        for j in range(i):
            if data[j]>data[j+1]:
                exchange = True
                temp = data[j+1]
                data[j+1] = data[j]
                data[j] = temp

    return data

print bubbleSort([4,3,5,1,2,0])

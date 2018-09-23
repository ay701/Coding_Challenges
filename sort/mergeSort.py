# 
# Merge Sort is a Divide and Conquer algorithm. 
# Time Complexity : O(NlogN)
#

def mergeSort(data):
    output = []

    if len(data)<2:
        return data 

    mid = int(len(data)/2)
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])

    i = 0
    j = 0

    while i<len(left) and j<len(right):

        if left[i]<right[j]:
            output.append(left[i])
            i+=1
        else:
            output.append(right[j])
            j+=1

    output += left[i:]
    output += right[j:]
    return output


print mergeSort([3,4,1,2,6,7,8,0])

#!/usr/bin/env python

# Quick Sort
# Recursion

def qsort(alist):
    print(alist)
    if len(alist) <= 1:
        return alist
    else:
        pivot = alist[0]
        return qsort([x for x in alist[1:] if x < pivot]) + [pivot] + qsort([x for x in alist[1:] if x >= pivot])

unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]

# print(qsort(unsortedArray))

# iterative

def partition(array, begin, end):
    
    pivot = begin
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]

    # print array, pivot
    array[pivot], array[begin] = array[begin], array[pivot]
    print array, pivot, begin
    
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)

    return array

array = [97, 96, 95, 94, 93]
array_ = [90,91,92,97, 96, 95, 94, 93]
# array = [97, 200, 100, 101, 211, 107]
print quicksort(array_)
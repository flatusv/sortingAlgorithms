#!/usr/bin/env python3
#
# author:   Ablakim Giray Üstün
# date:     Sat 28 Dec 2019 10:53:07 PM CET
#
# descr:    Heapifies a list (bottom-up)

from random import randint

def heapify(arr):

        numElements = len(arr)-1

        # for all parent nodes: 3...2...1
        for i in range(numElements//2,0,-1):
            k = i       # current parent index
            v = arr[k]
            heap = False

            while not heap and 2*k <= numElements:
                j = 2*k
                if j < numElements:
                    if arr[j] < arr[j+1]:
                        j += 1
                if v >= arr[j]:
                    heap = True
                else:
                    arr[k], arr[j] = arr[j], arr[k]
                    print('swapped ', arr[j] , ' with ', arr[k])
                    k = j
            arr[k] = v


def main():
    # range(x,y): x is minimum number of nodes, y max number of nodes
    someList = [randint(0,100) for x in range(randint(3,10))]
    # insert a dummy value in index 0,
    # by doing this the parent nodes get adressed starting from index 1 (root).
    someList = [0] + someList

    # print list starting from index 1 -> don't show dummy at index 0
    print("Original list\t", someList[1:], " \twith n =",len(someList)-1)
    heapify(someList)
    # print final result
    print("Heapified list\t", someList[1:], "\n")


for i in range(10):
    main()
    print("--------------------------------------------------")

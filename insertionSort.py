def insertionSort(l):
    for i in range(len(l)):
        pos = i
        while pos>0 and l[pos]<l[pos-1]:
            l[pos],l[pos-1] = l[pos-1],l[pos]
            pos -= 1
    print(l)

l = [2,33,2,5,6,66,55,4,22,11,98,56,74,51,68]
insertionSort(l)
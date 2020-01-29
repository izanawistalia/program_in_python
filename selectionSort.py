def SSort(l):
    for i in range(len(l)):
        minpos = i
        for j in range(len(l)):
            if l[j]>l[minpos]:
                l[minpos],l[j] = l[j],l[minpos]

    print(l)

l=[55,4,56,22,35,12,00,2,556,2,8,35,32,6,5]
SSort(l)
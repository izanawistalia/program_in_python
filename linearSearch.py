def linearSearch(seq, value):
    for i in range(len(seq)):
        if seq[i]==value:
          return True
    else:
        return False

seq = [1,3,5,4,6,8,9,44,55,76,5,0,21,0]
value = 0
print (linearSearch(seq, value))
def binarySearch(seq, value, l, r):
    if len(seq)==0:
        return False
    mid=int((l+r)/2)
    if value==seq[mid]:
        return True
    elif value<seq[mid]:
        r=mid
        return binarySearch(seq, value, l, r)
    elif value>seq[mid]:
        l=mid
        return binarySearch(seq, value, l, r)
    
seq = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
value = 16
l=0
r=len(seq)
print(binarySearch(seq, value, l, r))
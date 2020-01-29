board = [["  ","  ","  ","  "],["  ","  ","  ","  "],["  ","  ","  ","  "],["  ","  ","  ","  "]]
found = False
Q = 0
insideExtended = 0
solution = []

def placeQueen(p,q,g=0,h=0):
      global insideExtended
      for j in range(g,p):
          
          if insideExtended:
              print("inside extended")
              if j>insideExtended:
                  print('inside extended checking for another row that\'s why we are quitting')
                  return False
          print("inside first for loop")
          for k in range(h,q):
            print("inside second for loop")
            if is_available(j,k):
                print("availability check") 
                update(j,k)
                print("updated")
                if j==len(board)-1:
                    global found
                    found = True
                    print("now rows are done.........")
                    solution.append(board)
                    return True
                else:
                    print(" checking for extended solution")
                    
                    insideExtended = insideExtended+1
                    print("current j : ",j)
                    print("j+1 : ",j+1)
                    extendSolution = placeQueen(p,q,j+1)
                    if extendSolution:
                        insideExtended = insideExtended-1
                        print("extend solution true")
                        return True
                    else:
                        insideExtended = insideExtended-1
                        print("extend solution false")
                        print(" j : ",j)
                        print(" k : ",k)
                        undo_and_update(j,k)
                        j=j
                        k=k+1
                        print(" j : ",j)
                        print(" k : ",k)
      
         

def update(j,k):
    global Q
    Q=Q+1
    print("inside update")
    board[j][k] = "Q"+str(Q)
    for z in board:
        print(z)
    print("placed queen ",Q)
    
    c=k-1
    while c>=0:
        if is_available(j,c):
            board[j][c] = "X"+str(Q)
        c=c-1
        for z in board:
          print(z)
    print("same row m peeche ka column bhar diya")
    c=k+1
    while c<=len(board[0])-1:
        if is_available(j,c):
            board[j][c] = "X"+str(Q)
        c=c+1
        for z in board:
          print(z)
    print("same row m aage ka column bhar diya")
    r=j-1
    while r>=0:
        if is_available(r,k):
            board[r][k] = "X"+str(Q)
        r=r-1
        for z in board:
          print(z)
    print("same column m peeche ka row bhar diya")
    r=j+1
    while r<=len(board)-1:
        if is_available(r,k):
            board[r][k] = "X"+str(Q)
        r=r+1
        for z in board:
          print(z)
    print("same column m aage ka row bhar diya")
    r=j-1
    c=k-1
    while r>=0 and c>=0 :
        if is_available(r,c):
            board[r][c] = "X"+str(Q)
        r=r-1
        c=c-1
        for z in board:
          print(z)
    print("NW diagonal bhar diya")
    r=j+1
    c=k+1
    while r<=len(board)-1 and c<=len(board[0])-1 :
        if is_available(r,c):
            board[r][c] = "X"+str(Q)
        r=r+1
        c=c+1
        for z in board:
          print(z)
    print("SE diagonal bhar diya")
    r=j+1
    c=k-1
    while r<=len(board)-1 and c>=0 :
        if is_available(r,c):
            board[r][c] = "X"+str(Q)
        r=r+1
        c=c-1
        for z in board:
          print(z)
    print("SW diagonal bhar diya")
    r=j-1
    c=k+1
    while r>=0 and c<=len(board[0])-1 :
        if is_available(r,c):
            board[r][c] = "X"+str(Q)
        r=r-1
        c=c+1
        for z in board:
          print(z)
    print("NE diagonal bhar diya")
    for z in board:
        print(z)

def is_available(j,k):
  if j>=0 and k>=0 and j<len(board) and k<len(board[0]):  
    print("inside available")
    print("j and k :",j,k)
    if board[j][k] == "  ":
        return True
    else:
        return False

def undo_and_update(j,k):
    global Q
    print("inside undo_and_update function")
    for r in range(len(board)):
        for c in range(len(board[0])):
            if str(Q) in board[r][c]:
                board[r][c] = "  "
    Q=Q-1
    for z in board:
        print(z)

#place = int(input("Enter the dimension of square board ... "))
#board[place][place]= ""
print("OUTPUT FOR A 4X4 SQUARE BOARD IN N QUEEN PROBLEM")
found = placeQueen(4,4)
print(" value of found : ", found)
for a in solution:
    print("------------------------------------------------------")
    for i in board:
        print(i)



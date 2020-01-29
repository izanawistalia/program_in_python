img = [
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 2, 0],
[1, 0, 0, 1, 0, 2, 1, 1],
[1, 2, 2, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 2, 2, 0],
[1, 1, 1, 1, 1, 2, 1, 1],
[2, 2, 1, 1, 1, 2, 2, 1],
]

lenr = len(img)
lenc = len(img[0])

def neighbour(r, c):
    return ((r-1,c-1),(r-1,c),(r-1,c+1),(r,c-1),(r,c+1),(r+1,c-1),(r,c+1),(r+1,c-1),(r+1,c),(r+1,c+1))

occupied = []

def fillColor(r,c, color, replace_color):
     if r<0 or r>=lenr :
         return
     if c<0 or c>=lenc :
         return
     if img[r][c] != color:
         return
     img[r][c] = replace_color

     moves = neighbour(r, c)
     for move in moves:
         fillColor(move[0], move[1], color, replace_color)



print("initial picture: ")
for i in img: print(i)
print("--"*25)
print("output: ")
fillColor(4, 4, 2, 5)
for i in img: print(i)
import turtle
myTurtle = turtle.Turtle()
#following code will make square
def square():
    myTurtle.forward(100)
    myTurtle.left(90)
    myTurtle.forward(100)
    myTurtle.left(90)
    myTurtle.forward(100)
    myTurtle.left(90)
    myTurtle.forward(100)






for i in range(10):
    myTurtle.forward(100)
    square()
    myTurtle.backward(50)
    square()
    if i>0:
        if i==1:
            myTurtle.forward(50)
        if i==2:
            myTurtle.backward(100)
        if i==3:
            myTurtle.forward(150)
        if i==4:
            myTurtle.backward(200)
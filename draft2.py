import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSth(t):
    t.forward(20)

def drawSpiral(myTurtle, lineLen):
    myTurtle.left(90)
    myTurtle.up()
    myTurtle.backward(100)
    myTurtle.color("green")
    drawSth(myTurtle)

drawSpiral(myTurtle,100)
myWin.exitonclick()
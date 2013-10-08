import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawCircle(myTurtle,radius):
    if radius > 0:
        myTurtle.forward(1)
        myTurtle.right(2)
        
        drawCircle(myTurtle,radius-1)
        
drawCircle(myTurtle, 200000)
myWin.exitonclick()
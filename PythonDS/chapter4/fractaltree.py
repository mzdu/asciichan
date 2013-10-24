import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.color("blue")
        t.forward(branchLen)
        t.right(20)
        t.color("red")
        tree(branchLen-15,t)
        t.left(40)
        t.color("green")
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    tree(125,t)
    myWin.exitonclick()

main()




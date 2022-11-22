import turtle
turtle.setup(600, 600)
turtle.penup()
turtle.speed(9)
turtle.goto(250, 250)
turtle.setheading(270)
turtle.pendown()
for x in range (500, 19, -10):
    turtle.forward(x)
    turtle.right(90)
turtle.done()
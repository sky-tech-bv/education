import turtle
turtle.setup(600, 600)
turtle.penup()
turtle.speed(9)
turtle.goto(250, -250)
turtle.setheading(90)
turtle.pendown()
for x in range (5, 501, 5):
    for y in range (1, 5):
        turtle.forward(x)
        turtle.left(90)
turtle.done()
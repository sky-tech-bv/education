import turtle
turtle.setup(600, 600)
turtle.penup()
turtle.speed(9)
turtle.goto(50, -200)
turtle.setheading(90)
turtle.pendown()
for x in range (1, 9):
    turtle.forward(400)
    turtle.left(135)
turtle.done()
import turtle
turtle.setup(600, 600)
turtle.penup()
turtle.speed(9)
turtle.goto(-75, 200)
turtle.pendown()
for x in range (1, 9):
    turtle.forward(150)
    turtle.right(45)
turtle.penup()
turtle.goto(-15, -10)
turtle.pendown()
turtle.write('STOP', font=(25))
turtle.done()
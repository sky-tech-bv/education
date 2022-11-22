import turtle
turtle_speed = 0
num = int(input('А давайте ка построим шахматную доску. Введите количество строк и столбцов на поле: '))
step = int(input('Введите размер ячейки доски. Число может быть от 10 до 100. Введите ваше значение: '))
if (step < 10 or step > 100):
    step = int(input('Вы ввели значение, выходящее за пределы диапазона от 10 до 100. Введите корректное значени: '))
screen_height = int(step * num)
screen_wide = screen_height
num_col = num
num_row = num
width = int(screen_height / num_row)
start_x = int(-screen_wide / 2)
start_y = int(screen_height / 2)
first_x = start_x
first_y = start_y
last_x = start_x + width * num_col
last_y = start_y - width * num_row            
def square(X, Y, width, color):
    turtle.fillcolor(color)
    turtle.goto(X, Y)
    turtle.setheading(0)
    turtle.begin_fill()
    turtle.pendown()
    for i in range (5):
        turtle.forward(width)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
def main():
    turtle.setup(screen_height + step // 2, screen_wide + step // 2)
    turtle.hideturtle()
    turtle.speed(turtle_speed)
    turtle.penup()
    color = 'black'
    for y in range (first_y, last_y, -width):
        for x in range (first_x, last_x, width):
            square(x, y, width, color)
            if color == 'black':
                color = 'white'
            else:
                color = 'black'
        if num % 2 == 0: 
            if color == 'black':
                color = 'white'
            else:
                color = 'black'
    turtle.done()
main()

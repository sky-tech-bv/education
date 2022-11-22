def main():
    number = int(input('Введите число строк в программе: '))
    while number <= 0:
        number = int(input('Введите верное число строк в программе: '))
    show_stars(number)
    
def show_stars(num):
    if num > 1:
        show_stars(num - 1)
    print(num * '*')

if __name__ == '__main__':
    main()
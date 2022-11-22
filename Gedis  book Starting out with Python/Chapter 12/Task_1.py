def main():
    number = int(input('Введите целое число, которое больше 1: '))
    while number <= 1:
        number = int(input('Введите верное число, которое больше 1: '))
    show_numbers(number)
    print('Готово!')
    
def show_numbers(num):
    if num > 1:
        show_numbers(num - 1)
    print(num)

if __name__ == '__main__':
    main()
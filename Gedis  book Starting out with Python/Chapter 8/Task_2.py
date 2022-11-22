def main():
    num = input('Введите ряд цифр без пробелов: ')
    summ = 0
    for ch in num:
        summ += int(ch)
    print(f'Сумма значений в списке составляет: {summ}')
if __name__ == '__main__':
    main()
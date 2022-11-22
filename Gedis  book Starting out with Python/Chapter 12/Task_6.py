def main():
    number = int(input('Введите цельночисленное число: '))
    summ = sum_value(number)
    print(f'Сумма всех чисел в списке равна - {summ}')
    
def sum_value(val):
    if val == 0:
        return 0
    else:
        return val + sum_value(val - 1)

if __name__ == '__main__':
    main()
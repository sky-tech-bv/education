def main():
    num1 = 0
    num2 = 0
    while num1 <= 0:
        num1 = int(input('Введите цельночисленное число степени: '))
    while num2 <= 0:
        num2 = int(input('Введите число для возведения в степень: '))
    result = multyply(num1, num2)
    print(f'Результат возведения в степень - {result}')
    
def multyply(val1, val2):
    if val1 == 0 or val2 == 0:
        return 1
    else:
        return val2 * multyply(val1 - 1, val2)
    
if __name__ == '__main__':
    main()
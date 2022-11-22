def main():
    total = 0
    count = 0
    result = 0
    num = open('numbers.txt', 'r')
    amount = num.readline()
    while amount != '':
        amount = int(amount)
        total += amount
        count += 1
        amount = num.readline()
    num.close()
    result = total / count
    print(f'Среднее арифметическое значений в файле numbers.txt равняется {result:,.2f}')
if __name__ == '__main__':
    main()
    
def main():
    total = 0
    count = 0
    result = 0
    try:
        num = open('middle_averege.txt', 'r')
        amount = num.readline()
        while amount != '':
            amount = int(amount)
            total += amount
            count += 1
            amount = num.readline()
        num.close()
        result = total / count
        print(f'Среднее арифметическое значений в файле numbers.txt равняется {result:,.2f}')
    except IOError:
        print('Ошибка! Файл не найден или не существует!')
    except ValueError:
        print('Ошибка! Введенное значение не является числовым!')
    except:
        print('Ошибка! Другая ошибка!')
if __name__ == '__main__':
    main()
    
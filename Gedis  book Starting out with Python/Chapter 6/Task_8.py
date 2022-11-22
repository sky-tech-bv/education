def main ():
    sum_num = 0
    count = 0
    number = 0
    mid_averege = open('middle_averege.txt', 'r')
    for line in mid_averege:
        number = int(line)
        sum_num += number
        count += 1
        print(f'Случайное число в {count} строке равняется {number}')
    mid_averege.close()
    print(f'Сумма всех случайный чисел равна {sum_num} \n' +
          f'Из файла прочитанно {count} случайных чисел.')
if __name__ == '__main__':
    main()
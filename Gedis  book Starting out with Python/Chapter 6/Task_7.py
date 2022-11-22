import random
def main ():
    num = 0
    count = int(input('Введите количество случайных чисел, помещаемых в файл: '))
    mid_averege = open('middle_averege.txt', 'w')
    for x in range (1, count + 1):
        num = random.randint(1, 500)
        mid_averege.write(str(num) + '\n')
    mid_averege.close()
    print(f'Выполнено заполнение {count} случайных чисел в файл middle_averege.txt')
if __name__ == '__main__':
    main()
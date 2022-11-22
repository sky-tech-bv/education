def main():
    num = int(input('Введите чисто от 1 до которого нужно выполнить запись в файл: '))
    count_num = open('count_num.txt', 'w')
    print('Выполним ка счет!')
    for count in range (1, num + 1):
        count_num.write(f'{count}\n')
        print(f'{count}')
    count_num.close()
    print('Последовательность сохранена в файл count_num.txt.')
if __name__ == '__main__':
    main()
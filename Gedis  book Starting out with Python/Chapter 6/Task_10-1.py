def main():
    name = ''
    averege = 0
    count_1 = 0
    answer = 'д'
    outfile = open('golf_club.txt', 'w')
    while answer == 'д' or answer == 'Д':
        name = input ('Введите имя игрока и нажмите Enter: ')
        averege = int(input(f'Введите счет игрока под именем {name} и нажмите Enter: '))
        count_1 += 1
        outfile.write(str(count_1) + ' ' + name + ' ' + str(averege) + '\n')
        #outfile.write(name + '\n')
        #outfile.write( str(averege) + '\n')
        answer = input('Хотите ввести еще одно значение? Нажмите д и далее Enter для подтверждения:')
    outfile.close()
if __name__ == '__main__':
    main()
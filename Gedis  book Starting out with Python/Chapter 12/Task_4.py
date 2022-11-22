def main():
    number = int(input('Введите длину списка: '))
    list = []
    for x in range (1, number + 1):
        number = int(input(f'Введите значение №{x} списка: '))
        list.append(number)
    max_val = max_value(list)
    print(f'Максимальное значение в списке это число - {max_val}')
    
def max_value(list):
    x = len(list)
    if x == 1:
        return list[x - 1]
    elif list[x - 2] > list[x - 1]:
        del list[x - 1]
        max_value(list)
    else:
        del list[x - 2]
        max_value(list)
    

if __name__ == '__main__':
    main()
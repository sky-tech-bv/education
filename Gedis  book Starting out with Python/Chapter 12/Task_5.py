def main():
    number = int(input('Введите длину списка: '))
    list = []
    for x in range (1, number + 1):
        number = int(input(f'Введите значение №{x} списка: '))
        list.append(number)
    summ = sum_value(list)
    print(f'Сумма всех чисел в списке равна - {summ}')
    
def sum_value(list):
    x = len(list)
    summ = 0
    if x == 1:
        return list[0]
    else:
        return list[x-1] + sum_value(list[0:x-1])
    

if __name__ == '__main__':
    main()
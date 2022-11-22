def main():
    month = 0
    name =''
    count_step = open('steps.txt', 'r')
    for x in range (1,13):
        month_num = 0
        if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
            month_num = 3
        elif x == 4 or x == 6 or x == 9 or x == 11:
            month_num = 30
        else:
            month_num = 28
        counter = 0
        equal = 0
        value = int(count_step.readline())    
        for num in range (month_num + 1):
            counter += 1
            equal += value
            value = int(count_step.readline())
        month = equal / counter
        name = month_validator(x)
        print(f'В {x} месяце под названием "{name}" среднее число шагов составило {month:,.0f}.')
    count_step.close()
    print('Готово.')
def month_validator(name):
    if name == 1:
        return 'январь'
    elif name == 2:
        return 'февраль'
    elif name == 3:
        return 'март'
    elif name == 4:
        return 'апрель'
    elif name == 5:
        return 'май'
    elif name == 6:
        return 'июнь'
    elif name == 7:
        return 'июль'
    elif name == 8:
        return 'август'
    elif name == 9:
        return 'сентябрь'
    elif name == 10:
        return 'октябрь'
    elif name == 11:
        return 'ноябрь'
    else:
        return 'декабрь'
if __name__ == '__main__':
    main()
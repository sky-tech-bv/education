import information

count_class = 3
def main():
    libr = []
    print(f'Программа собирает данные от {count_class} пользователях и после выводит их на экран.')
    for x in range(count_class):
        print(f'Введите данные пользователя №{x+1}:')
        name = input('Введите имя: ')
        adress = input('Введите адрес: ')
        age = input('Введите возраст: ')
        phone_num = input('Введите номер телефона: ')
        lib = information.Information(name, adress, age, phone_num)
        libr.append(lib)
    for item in libr:
        print('Вы ввели следующие данные:')
        print(f'Имя: {lib.get_name()}')
        print(f'Адрес: {lib.get_adress()}')
        print(f'Возраст: {lib.get_age()}')
        print(f'Телефонный номер: {lib.get_phone_num()}')
if __name__ == '__main__':
    main()
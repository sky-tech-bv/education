import pickle
dick = {}
def main():
    end_of_file = False
    in_file = open('dict.dat', 'rb')
    while not end_of_file:
        try:
            dic = pickle.load(in_file)
            for key, value in dic:
                dick[key] = value
        except:
            end_of_file = True     
        in_file.close()
    # Навигация пользователя по программе.
    answer = 0
    while answer != 4:
        display_interface()
        answer = int(input('Сделайте Ваш выбор, для подтверждения нажмите Enter: '))
        if answer == 1:
            show_base()
        elif answer == 2:
            add_note()
        elif answer == 3:
            del_note()
        elif answer == 4:
            end_program()
        else:
            display_interface()
            answer = int(input('Значение должно находится в пределах приведенного диапазона меню! Выберите верное значение' +
                               'в диапазоне от 1 до 4. Сделайте Ваш выбор, для подтверждения нажмите Enter: '))

# Функция расконсервации словаря из файла и демонстрации пользователю.
def show_base():
    try:
        display(dick)
    except:
        print('Словарь пока пуст, попробуйте ввести значение в словарь и после его отобразить.')
    answer = 0

# Функция добавления записи в словарь
def add_note():
    key = input('Введите имя человека, email которого Вы желаете добавить в словарь: ')
    value = input(f'Введите электронный адрес {key}: ')
    if key not in dick:
        dick[key] = value
    else:
        print('Пользователь с таким именем уже существует. Желаете изменить его электронный адрес? Попробуйте снова.')
    answer = 0

# Функция удаления записи из словаря
def del_note():
    del_key = input('Введите имя человека, email которого Вы желаете удалить из словаря: ')
    dick.pop(del_key, 'Такого имени не существует в словаре. Попробуйте снова')
    print(f'Запись с именем {del_key} удалена из словаря.')
    answer = 0

# Функция консервации словаря в файл
def end_program():
    out_file = open('dict.dat', 'wb')
    pickle.dump(dick, out_file)
    out_file.close()
    print('Программа завершила свою работу. Словарь законсервирован в файл dict.dat.')

# Функция отображения содержимого словаря
def display(data):
    if dick != {}:
        for key, value in data.items():
            print(f'{key} - {value}')
    else:
        print('Словарь пока пуст. По пробуйте его заполинить.')
    answer = 0

# Функция демонстрации интерфейса        
def display_interface():
    # Вводная часть программы, отображение меню
    print('')
    print('Настоящая программа является базой данных электронных адресов. Программа имеет следующие функции:')
    print('\t1 - Отобразить базу данных')
    print('\t2 - Внести новую запись в базу')
    print('\t3 - Удалить запить из базы')
    print('\t4 - Выйти из программы')
if __name__ == '__main__':
    main()
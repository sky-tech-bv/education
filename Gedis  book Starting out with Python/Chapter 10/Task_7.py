import employee
import pickle

LOOK_UP = 1
CHANGE = 2
ADD = 3
REMOVE = 4
QUIT = 5
filename = 'dictionary.dat'

def main():
    dictionary = load_dictionary()
    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(dictionary)
        elif choice == CHANGE:
            change(dictionary)
        elif choice == ADD:
            add(dictionary)
        elif choice == REMOVE:
            remove(dictionary)
    save_dictionary(dictionary)

def load_dictionary():
    try:
        input_file = open(filename, 'rb')
        dictionary_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        dictionary_dct = {}
        
    return dictionary_dct

def get_menu_choice():
    print('\n' +
          'Меню\n' +
          '--------------------\n' +
          '1. Найти сотрудника по имени.\n' +
          '2. Изменить данные сотрудника по его имени.\n' +
          '3. Добавить данные нового сотрудника.\n' +
          '4. Удалить сотрудника по его имени.\n' +
          '5. Выйти из программы.\n' +
          ' ')
    choice = int(input('Введите пункт меню и нажмите Enter для подтверждения: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = input('Введите верный пункт меню из предложенного списка и нажмите Enter для подтверждения: ')
    return choice

def look_up(dictionary):
    name = input('Введите имя сотрудника: ')
    print(dictionary.get(name, 'По такому имени запись не найдена. Попробуйте снова'))

def change(dictionary):
    name = input('Введите имя сотрудника: ')
    if name in dictionary:
        id_num = input(f'Введите новый индификационный номер сотрудника по имени {name}: ')
        department = input(f'Введите новое название отдела, где работает сотрудник по имени {name}: ')
        job_title = input(f'Введите новую должность сотрудника с именем {name}: ')
        stack = employee.Employee(name, id_num, department, job_title)
        dictionary[name] = stack
        print('Запись успешно изменена.')
    else:
        print('Запись с таким имени сотрудника отсутствует. Внести изменения невозможно.')
    

def add(dictionary):
    name = input('Введите имя сотрудника: ')
    id_num = input(f'Введите индификационный номер сотрудника по имени {name}: ')
    department = input(f'Введите название отдела, где работает сотрудник по имени {name}: ')
    job_title = input(f'Введите должность сотрудника с именем {name}: ')
    stack = employee.Employee(name, id_num, department, job_title)
    if name not in dictionary:
        dictionary[name] = stack
        print('Запись внесена.')
    else:
        print('Пользователь с таким именем уже существует!')

def remove(dictionary):
    name = input('Введите имя сотрудника: ')
    if name in dictionary:
        del dictionary[name]
        print('Запись успешно удалена.')
    else:
        print('Запись с таким имени сотрудника отсутствует, удалить ее невозможно.')
      
def save_dictionary(dictionary):
    out_file = open(filename, 'wb')
    pickle.dump(dictionary, out_file)
    out_file.close()
    print('Данные успешно сохранены и законсервированны.')
if __name__ == '__main__':
    main()
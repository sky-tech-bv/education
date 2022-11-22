import patient
import procedure

count_class = 3
def main():
    libr = []
    print('Введите данные медицинской карточки пациента:')
    name = input('Введите фамилию, имя и отчество пациента: ')
    adress = input('Введите полный адрес пациента, включая город, улицу и индекс: ')
    phone_num = input('Введите контактный телефонный номер пациента: ')
    contct_data = input('Введите полное имя и номер телефона контактного лица для экстренной связи: ')
    patiente = patient.Patient(name, adress, phone_num, contct_data)
    print()
    print(f'Программа собирает данные о пациенте {patiente.get_name()} и проведенных ним медицинских процедурах' +
          'и выводит их на экран.')
    for x in range(count_class):
        print(f'Введите данные о проведенной процедуре №{x+1}:')
        proced_name = input('\tВведите название процедуры: ')
        date = input('\tВведите дату проведения процедуры: ')
        doct_name = input('\tВведите имя врача, проводившего процедуру: ')
        price = input('\tВведите стоимость процедуры: ')
        print()
        proced = procedure.Procedure(proced_name, date, doct_name, price)
        libr.append(proced)
    print('Данные об пациенте:')
    print(f'\tПолное имя пациента: {patiente.get_name()};\n' +
          f'\tПолный адрес пациента: {patiente.get_adress()};\n' +
          f'\tКонтактный телефонный номер пациента: {patiente.get_phone_num()};\n' +
          f'\tИмя и контактный телефон лица для экстренной связи: {patiente.get_contct_data()}.' +
          ' ')
    print('Информация о проведенных процедурах:')
    counter = 1
    result_price = 0
    print()
    for item in libr:
        print(f'Данные о медицинской процедуре № {counter}:')
        print(f'\tНазвание процедуры: {item.get_proced_name()};\n' +
              f'\tДата выполнения процедуры: {item.get_date()};\n' +
              f'\tИмя врача, выполняющего процедуру: {item.get_doct_name()}\n' +
              f'\tСтоимость процедуры: ${item.get_price():,.2f}.\n' +
              ' ')
        counter += 1
        result_price += item.get_price()
    print(f'Общая стоимость процедур составила: ${result_price:,.2f}.')
if __name__ == '__main__':
    main()
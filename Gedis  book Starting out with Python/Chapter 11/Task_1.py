import employee

def main():
    p_w = employee.ProductionWorker('', '', 1, 0)
    p_w.set_empl_name(input('Введите имя работника: '))
    p_w.set_empl_numb(input('Введите идентификационный номер работника: '))
    p_w.set_work_id(int(input('Введите номер смены (1 - первая смена или 2 - вторя смена: ')))
    p_w.set_hour_rate(float(input('Введите часовую ставку оптаы труда работника: ')))
    print('Вы ввели следующую информацию:\n\t' +
          f'Имя работника: {p_w.get_empl_name()};\n\t' +
          f'Идентификационный номер работника: {p_w.get_empl_numb()};\n\t' +
          f'Рабочая смена работника: {p_w.get_work_id()};\n\t' +
          f'Часовая ставка оплаты труда работника: ${p_w.get_hour_rate():,.2f}.')
if __name__ == '__main__':
    main()
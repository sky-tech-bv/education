import employee

def main():
    s_s = employee.ShiftSupervisor('', '', 0, 0)
    s_s.set_empl_name(input('Введите имя начальника смены: '))
    s_s.set_empl_numb(input('Введите идентификационный номер начальника смены: '))
    s_s.set_year_salery(float(input('Введите размер годового оклада начальника смены: ')))
    s_s.set_year_benefit(float(input('Введите процентную ставку премиальных начальника смены: ')))
    print('Вы ввели следующую информацию:\n\t' +
          f'Имя начальника смены: {s_s.get_empl_name()};\n\t' +
          f'Идентификационный номер начальника смены: {s_s.get_empl_numb()};\n\t' +
          f'Годовой оклад начальника = ${s_s.get_year_salery():,.2f};\n\t' +
          f'Годовая сумма премиальных начальника смены = ${s_s.get_year_benefit():,.2f}.')
    
if __name__ == '__main__':
    main()
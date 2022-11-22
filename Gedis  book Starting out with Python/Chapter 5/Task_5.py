propety_tax = 0.72
def main():
    propety_value = 0
    extra_prise = 0
    propety_value = float(input('Введите стоимость имущества: '))
    extra_prise = propety_value - 4000
    result(extra_prise)
def result(extra):
    result = 0
    if extra > 0:
        result = (extra//100) * propety_tax
        print(f'Оценочная стоимость составляет ${extra:,.2f}')
        print(f'Налог на имещуетсво составляет ${result:,.2f}')
    else:
        print('Стоимость имущества ниже подлежащего налогообложению.')
main()
    
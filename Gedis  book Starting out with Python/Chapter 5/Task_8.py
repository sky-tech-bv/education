hour_rate = 2500.00
square = 10
hour_amount = 8
color_amount = 1
def main():
    paint_square = 0
    color_prise = 0
    color = 0
    hour = 0
    color_add = 0
    job_prise = 0
    color_prise = 0
    full_value = 0
    paint_square = float(input('Введите площадь окрашиваемой поверхности: '))
    color_prise = float(input('Введите стоимость банки краски: '))
    color = paint_square // square
    color_add = paint_square % square / 10
    hour = (color + color_add) * hour_amount
    job_prise = hour * hour_rate
    color_prise = (color + 1) * color_prise
    full_value = job_prise + color_prise
    show_result(color, hour, job_prise, color_prise, full_value, color_add)
def show_result(color, hour, job_prise, color_prise, full_value, color_add):
    if color_add == 0:
        print(f'Количество банок краски составит {color:.0f} шт.')
        print(f'Количество рабочих часов составит {hour:.2f}')
        print(f'Стоимость краски - ${color_prise:,.2f}')
        print(f'Соимость работы - ${job_prise:,.2f}')
        print(f'Общая стоимость - ${full_value:,.2f}')
    else:
        print(f'Количество банок краски составит {color:.0f} шт. и еще одна начатая банка')
        print(f'Количество рабочих часов составит {hour:.2f}')
        print(f'Стоимость краски - ${color_prise:,.2f}')
        print(f'Соимость работы - ${job_prise:,.2f}')
        print(f'Общая стоимость - ${full_value:,.2f}')
main()
    
    
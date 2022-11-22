def main():
    in_val = input('Введите дату в формате дд/мм/гггг:')
    sep_val = in_val.split('/')
    month = what_month(int(sep_val[1]))
    print(f'Дата: {sep_val[0]} {month} {sep_val[-1]} г.')
def what_month(name):
    month_list = ['января', 'февраля', 'марта', 'апреля',
                'мая', 'июня', 'июля', 'августа',
                'сентября', 'октября', 'ноября', 'декабря']
    return month_list[name - 1]
if __name__ == '__main__':
    main()
def main():
    year = 0
    month = 12
    av_year = 0
    min_av = 0
    max_av = 0
    min_month = ''
    max_month = ''
    year_list = []
    month_list = ['январе', 'феврале', 'марте', 'апреле', 'мае','июне',
                  'июле', 'августе', 'сентябре', 'октябре', 'ноябре', 'декабре',]
    for val in range (month):
        year_list.append(int(input('Введите количество осадков в ' + month_list[val] + ' и нажмите Enter: ')))
    for val in year_list:
        year += val
    av_year = year / month
    min_av = min(year_list)
    max_av = max(year_list)
    min_month = month_list[year_list.index(min_av)]
    max_month = month_list[year_list.index(max_av)]
    print(f'Общее количество осадков за год: {year} мм.\nСреднее количество осадков в месяц составило: {av_year:,.2f} мм.\n' +
          f'Минимальное количество осадков зафиксировано в {min_month} и составило {min_av:,.2f} мм.\n' +
          f'Максимальное количество осадков зафиксировано в {max_month} и составило {max_av:,.2f} мм.')
if __name__ == '__main__':
    main()
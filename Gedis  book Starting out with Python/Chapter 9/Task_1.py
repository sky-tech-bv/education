def main():
    courses = {'CS101':['3004', 'Хайис', '8:00'], 'CS102':['4501', 'Альвардо', '9:00'],
               'CS103':['6755', 'Рич', '10:00'], 'CS104':['1244', 'Берк', '11:00'],
               'CS105':['1411', 'Ли', '13:00']}
    answer = []
    question = input('Введите номер курса: ')
    if question == 'CS101':
        answer = courses['CS101']
    elif question == 'CS102':
        answer = courses['CS102']
    elif question == 'CS103':
        answer = courses['CS103']
    elif question == 'CS104':
        answer = courses['CS104']
    elif question == 'CS105':
        answer = courses['CS105']
    print(f'Занятие будет проводиться у {answer[1]} в аудитории {answer[0]} в {answer[2]}')
if __name__ == '__main__':
    main()
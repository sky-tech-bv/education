import question
import pickle

number = 10
filename = 'question_directory.dat'
win1 = 0
win2 = 0

def main():
    question_directory = load_question_directory()
    #for i in range (1, number + 1):
        #question_item = input(f'Введите вопрос №{i}: ')
        #answer1 = input(f'Введите ответ номер 1 на вопрос №{i}: ')
        #answer2 = input(f'Введите ответ номер 2 на вопрос №{i}: ')
        #answer3 = input(f'Введите ответ номер 3 на вопрос №{i}: ')
        #answer4 = input(f'Введите ответ номер 4 на вопрос №{i}: ')
        #right_answer = int(input('Введите номер верного ответа от 1 до 4: '))
        #while right_answer < 1 or right_answer > 4:
            #right_answer = int(input('Не верно! Введите верное значение ответа на вопрос числом от 1 до 4: '))
        #stack = question.Question(question_item, answer1, answer2, answer3, answer4, right_answer)
        #question_directory[question_item] = stack
    save_question_directory(question_directory)
    grade = game(question_directory)
    if win1 == 1:
        print(f'Поздравляем пользователя 1 с победой. Число верных ответов составило {grade} шт.')
    elif win2 == 1:
        print(f'Поздравляем пользователя 2 с победой. Число верных ответов составило {grade} шт.')
    else:
        print(f'Победила дружба! Пользователь 1 и 2 дали {grade} шт. верных ответов.')
        

def load_question_directory():
    try:
        input_file = open(filename, 'rb')
        question_directory_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        question_directory_dct = {}
        
    return question_directory_dct
            
def game(dic):
    counter = 1
    counter_player1 = 0
    counter_player2 = 0
    for key, value in dic.items():
        if counter % 2 == 0:
            print(f'Внимание вопрос для пользователя 2:')
            print(f'{key}\nВарианты ответа:\n1. {value.get_answer1()};\n' +
                  f'2. {value.get_answer2()};\n3. {value.get_answer3()};\n' +
                  f'4. {value.get_answer4()}.\n ')
            answer = int(input('Введите верный ответ числом от 1 до 4: '))
            if answer == value.get_right_answer:
                counter_player2 += 1
        else:
            print(f'Внимание вопрос для пользователя 1:')
            print(f'{key}\nВарианты ответа:\n1. {value.get_answer1()};\n' +
                  f'2. {value.get_answer2()};\n3. {value.get_answer3()};\n' +
                  f'4. {value.get_answer4()}.\n ')
            answer = int(input('Введите верный ответ числом от 1 до 4: '))
            if answer == value.get_right_answer():
                counter_player1 += 1
        counter += 1
    if counter_player1 > counter_player2:
        win1 = 1
        return counter_player1
    elif counter_player1 < counter_player2:
        win2 = 1
        return counter_player2
    else: 
        return counter_player1
      
def save_question_directory(question_directory):
    out_file = open(filename, 'wb')
    pickle.dump(question_directory, out_file)
    out_file.close()
    print('Данные успешно сохранены и законсервированны.')

if __name__ == '__main__':
    main()
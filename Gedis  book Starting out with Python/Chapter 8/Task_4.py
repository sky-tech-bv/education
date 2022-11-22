def main():
    input_message = input('Введите фразу для преобразования в азбуку Морзе: ')
    print('Преобразованное значение азбукой Морзе:')
    val = ''
    for ch in input_message:
        val = what_simbol(ch)
        print(val, sep = '', end = ' ')
def what_simbol(value):
    num = 0
    lang_list = [' ', ',', '.', '?', '0', '1', '2', '3', '4', '5', '6', '7',
                 '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                 'W', 'X', 'Y', 'Z', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ë', 'Ж',
                 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
                 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ' 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    morze_list = [' ', '--..--', '.-.-.-', '..--..', '-----', '.----', '..---', '...--',
                 '....-', '.....', '-....', '--...', '---..', '----.', '.-', '-...',
                 '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..',
                 '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-',
                 '.--', '-..-', '-.-', '--..', '.-', '-...', '.--', '--.', '-..', '.', '.',
                 '...-', '--..', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
                 '.-.', '...', '-', '..-', '..-.', '....', '-.-.', '---.', '----', '--.-',
                 '.==.=.' '-.--', '-..-', '..-..', '..--', '.-.-']
    for ch in lang_list:
        if value.upper() == ch:
            num = lang_list.index(ch)
            return morze_list[num]
if __name__ == '__main__':
    main()
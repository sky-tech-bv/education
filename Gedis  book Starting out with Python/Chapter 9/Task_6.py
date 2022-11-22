def main():
    # Open and read text from file number 1
    name_file1 = input('Введите название файла 1 для открытия: ')
    infile1 = open(name_file1 + '.txt', 'r')
    text1 = infile1.read()
    infile1.close()
    text_part1 = remain_text(text1)
    
    # Open and read text from file number 2
    name_file2 = input('Введите название файла 2 для открытия: ')
    infile2 = open(name_file2 + '.txt', 'r')
    text2 = infile2.read()
    infile2.close()
    text_part2 = remain_text(text2)
    
    # Create two sets and put text_parts to it
    myset1 = set()
    myset2 = set()
    for item in text_part1:
        myset1.add(item)
    for item in text_part2:
        myset2.add(item)
        
    # Compare sets and get new sets with words which needs for result
    myset3 = myset1 | myset2
    myset4 = myset1 - myset2
    myset5 = myset2 - myset1
    myset6 = myset1 ^ myset2
    
    # Show result
    print(f'Списки слов:\n\tсписок уникальных слов в 1 файле: {myset1}\n' +
          f'\tсписок уникальных слов в 2 файле: {myset2}\n' +
          f'\tсписок уникальных слов, входящий в 1 и 2 файлы: {myset3}\n' +
          f'\tсписок уникальных слов, входящий в 1 файл но не входящий во 2: {myset4}\n' +
          f'\tсписок уникальных слов, входящий в 2 файл но не входящих в 1: {myset5}\n' +
          '\tсписок уникальных слов, входящих исключительно в 1 и 2 файлы но не' +
          f'пересекающийся между собой: {myset6}')

# Function deleting unnecessary signs from list
def remain_text(value):
    new_text = ''
    # Make the list of unique words in text
    text_without_dot = value.replace('.', '')
    text_without_coma = text_without_dot.replace(',', '')
    text_without_exclamation_mark = text_without_coma.replace('!', '')
    text_without_question_mark = text_without_exclamation_mark.replace('?', '')
    new_text = text_without_question_mark
    new_text = new_text.lower()
    sep_text = new_text.split()
    return sep_text

if __name__ == '__main__':
    main()
def main():
    # Open and read text from file
    name_file = input('Введите название файла для открытия: ')
    infile = open(name_file + '.txt', 'r')
    text = infile.read()
    infile.close()
    new_text = ''
    # Make the list of unique words in text
    text_without_dot = text.replace('.', '')
    text_without_coma = text_without_dot.replace(',', '')
    text_without_exclamation_mark = text_without_coma.replace('!', '')
    text_without_question_mark = text_without_exclamation_mark.replace('?', '')
    new_text = text_without_question_mark
    
    new_text = new_text.lower()
    sep_text = new_text.split()
    myset = set()
    for item in sep_text:
        myset.add(item)
    # Swith on the counter of words
    count = 0
    count_list = {}
    for item in myset:
        count_list[item] = count
    # Count the quantity of each words
    for item in sep_text:
        for key, value in count_list.items():
            if item == key:
                count_list[key] = value + 1
            else:
                count_list[key] = value
    # Show result
    print(count_list)
if __name__ == '__main__':
    main()
def main():
    # Open and read text from file 
    name_file = input('Введите название файла для считывания: ')
    infile = open(name_file + '.txt', 'r')
    in_text = infile.read()
    in_line = in_text.split('\n')
    infile.close()
    sep_text = remain_text(in_text)
    
    # Create two sets and put text_parts to it
    myset = set()
    for item in sep_text:
        myset.add(item)
        
    # Create a dictionary with keys equal a unique words in in_text
    words = {}
    value = 0
    for item in myset:
        line_set = set()
        for x in range (len(in_line)):
            status = in_line[x].find(item)
            if status != -1:
                value = x + 1
                line_set.add(value)
        words[item] = line_set
    
    # Show result
    for key, value in sorted(words.items()):
        print(f'{key} : {value}')

# Function deleting unnecessary signs from list
def remain_text(value):
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
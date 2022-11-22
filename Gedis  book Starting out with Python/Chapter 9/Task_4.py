def main():
    name_file = input('Введите название файла для открытия: ')
    infile = open(name_file + '.txt', 'r')
    text = infile.read()
    infile.close()
    for ch in text:
        if ch != '.':
            text += ch
    print(text)
    text = text.lower()
    sep_text = text.split()
    myset = set()
    for item in sep_text:
        myset.add(item)
    print(myset)
if __name__ == '__main__':
    main()
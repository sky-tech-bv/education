def main():
    count_lower_leter = 0
    count_upper_leter = 0
    count_spaces = 0
    count_figure = 0
    infile = open('text.txt', 'r')
    infile_in = infile.readlines()
    infile.close()
    all_infile = []
    for un in infile_in:
        if un != '\n' or un != '':
            all_infile += un
    for ch in all_infile:
        if ch.isdigit():
            count_figure +=1
        if ch.isupper():
            count_upper_leter += 1
        if ch.islower():
            count_lower_leter += 1
        if ch.isspace():
            count_spaces += 1
    print(f'Количество символов:\nколичество букв в верхнем регистре - {count_upper_leter},\n' +
          f'количество букв в нижнем регистре - {count_lower_leter}\nколичество цифр - {count_figure}\n' +
          f'количество пробелов - {count_spaces}')
if __name__ == '__main__':
    main()
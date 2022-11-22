def main():
    result = ''
    c_word = ''
    add = 'КИ'
    info = input('Введите сообщение: ')
    words = info.split()
    for x in range (len(words)):
        item = words[x].upper()
        if len(item) == 1:
            c_word = item + add
        else:
            c_word = item[1:] + item[0] + add
        result = result + c_word
        if x < len(words) + 1:
            result = result + ' '
    print(result)
if __name__ == '__main__':
    main()
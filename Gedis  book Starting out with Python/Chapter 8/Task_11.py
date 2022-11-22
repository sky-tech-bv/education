def main():
    result = ''
    info = input('Введите первичное предложение: ')
    result += info[0]
    for x in range (1, len(info)):
        ch = info[x]
        if ch.isupper():
            ch = ch.lower()
            result += ' '
        result += ch
    print(result)
if __name__ == '__main__':
    main()
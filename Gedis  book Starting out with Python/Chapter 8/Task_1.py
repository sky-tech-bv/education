def main():
    s_line = input('Введите фамилию имя и отчество пользователя: ')
    sep_line = s_line.split()
    result = ''
    for str in sep_line:
        result += str[:1].upper() + '.'
    print(result)    
if __name__ == '__main__':
    main()
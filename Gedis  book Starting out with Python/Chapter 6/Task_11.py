def main():
    name = ''
    description = ''
    name = input('Введите Ваше имя и фамилию: ')
    description = input('Введите короткое описание о себе: ')
    about_user = open('user_description.html', 'w')
    about_user.write('<html>\n<head>\n</head>\n<body>\n\t\t' +
                     f'<center>\n\t<h1>{name}</h1>\n\t</center>\n\t' +
                     f'<hr />\n\t{description}\n\t<hr />\n</body>\n</html>')
    print('Готово.')
if __name__ == '__main__':
    main()
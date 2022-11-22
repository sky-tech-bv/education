def main():
    info = input('Введите предложение: ')
    result = convert(info)
    print(result)
def convert(value):
    isupper = True
    result = ''
    result_word = ''
    words = value.split()
    for item in words:
        if isupper:
            result_word = item[0].upper() + item[1:]
        else:
            result_word = item
        result = result + result_word + ' '
        if item[-1] == '.' or item[-1] == '!' or item[-1] == '?':
            isupper = True
        else:
            isupper = False
    return result
if __name__ == '__main__':
    main()
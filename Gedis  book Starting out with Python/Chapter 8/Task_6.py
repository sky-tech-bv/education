def main():
    info = ''
    in_info = open('text.txt', 'r')
    info = in_info.readlines()
    in_info.close()
    count = 0
    summ = 0
    result = 0
    for lines in info:
        for ch in lines:
            if ch == ' ':
                summ +=1
            if ch == '.':
                count +=1
                break
    result = summ / count
    print(result)
if __name__ == '__main__':
    main()
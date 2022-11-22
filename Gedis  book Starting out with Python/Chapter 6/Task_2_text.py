def main():
    amount = 0
    import_i = open('text_test.txt', 'r')
    line = import_i.readline()
    while line != '':
        amount = str(line)
        amount = amount.rstrip()
        print(f'{amount}')
        line = import_i.readline()
    import_i.close()
if __name__ == '__main__':
    main()
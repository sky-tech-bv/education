def main():
    amount = 0
    import_i = open('text_test.txt', 'r')
    for line in import_i:
        amount = line.rstrip('\n')
        print(f'{amount}')
    import_i.close()
if __name__ == '__main__':
    main()
find_av = 5658845
def main():
    num_account = []
    infile = open('charge_accounts.txt', 'r')
    num_account = infile.readlines()
    infile.close()
    val = 0
    while val < len(num_account):
        if find_av in num_account:
            print('Эврика! Нашлось!')
    print('Нет в этом файле!')
if __name__ == '__main__':
    main()
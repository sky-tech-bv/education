def main():
    num = ''
    get_user = input('Insert the phone number in format XXX-XXX-XXXX and press Enter: ')
    print('The phone number is', sep = '', end = ' ')
    for ch in get_user:
        if ch.isalpha():
            num = fix_simb(ch)
            print(num, sep = '', end = '')
        else:
            print(ch, sep = '', end = '')
def fix_simb(value):
    num = 0
    in_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    out_list = ['2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5',
                '5', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8',
                '9', '9', '9', '9']
    for ch in in_list:
        if value.upper() == ch:
            num = in_list.index(ch)
            return out_list[num]
if __name__ == '__main__':
    main()
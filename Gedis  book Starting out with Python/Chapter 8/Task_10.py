def main():
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    leters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЫЭЮЯ'
    index = 0
    condition = 0
    message = input('Введите сообщение: ') 
    for ch in message:
        ch = ch.upper()
        index = leters.find(ch)
        if index >= 0:
            count[index] = count[index] + 1
    for a in range (len(count)):
        if count[a] > count[condition]:
            condition = a
    print('В тексте чаще всего встречается символ ',\
          leters[condition], '.', sep = '')   
if __name__ == '__main__':
    main()
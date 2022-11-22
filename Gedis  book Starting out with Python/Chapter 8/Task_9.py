def main():
    info = input('Введите утверждение: ')
    avg_vowels = check_vowels(info)
    avg_consonants = check_consonants(info) - avg_vowels
    print(f'Количество гласных букв составляет {avg_vowels}')
    print(f'Количество согласных букв составляет {avg_consonants}')
def check_vowels(name):
    count = 0
    vowels = ['а', 'и', 'о', 'я', 'ю', 'е', 'э', 'ё']
    words = name.split()
    for item in words:
        for ch in item:
            for val in vowels:
                if ch == val:
                    count += 1
    return count
def check_consonants(name):
    count = 0
    words = name.split()
    for item in words:
        for ch in item:
            if ch.isalpha():
                count += 1
    return count
if __name__ == '__main__':
    main()
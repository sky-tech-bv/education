import Pet 

def main():
    name = input('Введите кличку Вашего питомца: ')
    animal_type = input('Введете тип питомца: ')
    age = input('Введите возраст питомца: ')
    pet = Pet.Pet(name, animal_type, age)
    print(pet)
if __name__ == '__main__':
    main()
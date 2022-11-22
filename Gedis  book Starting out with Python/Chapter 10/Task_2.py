import car

def main():
    year_model = input('Введите год выпуска автомобиля: ')
    make = input('Введите марку автомобиля: ')
    automobile = car.Car(year_model, make)
    print(f'Автомобиль {make} {year_model} года выпуска начал движение')
    for x in range(5):
        automobile.accelerating()
        print(f'{x+1}. Текущая скорость автомобиля {automobile.get_speed()} км/ч.')
    for i in range (5):
        automobile.breaking()
        print(f'{i+1}. Текущая скорость автомобиля {automobile.get_speed()} км/ч.')
if __name__ == '__main__':
    main()
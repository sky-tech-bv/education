def main():
    amount_fat = 0
    amount_carbohydrates = 0
    amount_fat = float(input('Введите количество потребленных жиров в граммах: '))
    amount_carbohydrates = float(input('Введите количество потребленных углеводов в граммах: '))
    calculate(amount_fat, amount_carbohydrates)
def calculate(amount_fat, amount_carbohydrates):
    calories_fat = 0
    calories_carbohydrates = 0
    calories_full = 0
    calories_fat = amount_fat * 9
    calories_carbohydrates = amount_carbohydrates * 4
    calories_full = calories_carbohydrates + calories_fat
    print(f'Итого потреблено {calories_fat:,.2f} каллорий от жиров')
    print(f'потреблено {calories_carbohydrates:,.2f} каллорий от углеводов')
    print(f'потреблено {calories_full:,.2f} каллорий в сумме.')
main()
    
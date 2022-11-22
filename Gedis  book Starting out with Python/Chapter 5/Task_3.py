k_insurence = 0.8
def main():
    price = 0
    price = float (input('Insert the prise of your property: '))
    insurence(price)
def insurence(price):
    value = 0
    value = k_insurence * price
    print(f'The minimal amout of insuranse = ${value:,.2f}')
main()

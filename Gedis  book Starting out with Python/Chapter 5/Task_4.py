def main():
    credit_payment = 0
    fuel = 0
    insurence = 0
    service = 0
    oil = 0
    wheels = 0
    cost_month = 0
    cost_year = 0
    credit_payment = float(input('Inserte the amount of month credit payment for your car: '))
    insurence = float(input('Inserte the amount of month insurance for your car: '))
    fuel = float(input('Inserte the amount of month fuel cost for your car: '))
    oil = float(input('Inserte the amount of month oil cost for your car: '))
    service = float(input('Inserte the amount of month service cost for your car: '))
    wheels = float(input('Inserte the amount of month wheel cost for your car: '))
    cost_month = credit_payment + insurence + fuel + oil + service + wheels
    cost_year = cost_month * 12
    show_result(cost_month, cost_year)
def show_result(cost_month, cost_year):    
    print(f'The full month cost of your car - ${cost_month:,.2f} and')
    print(f'year - ${cost_year:,.2f}.')
main()
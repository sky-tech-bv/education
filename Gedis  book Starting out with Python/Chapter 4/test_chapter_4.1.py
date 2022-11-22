month_sum = float(input('Insert your month budget end press Enter: '))
amount = int(input('Insert the amount of budget item end press Enter: '))
total = 0
for x in range (1, amount+1):
    print(f'Insert the amount of {x} budget')
    add = float(input('item: '))
    total +=add
if month_sum > total:
    dived_1 = month_sum - total
    print(f'Very nice! You saved the budget on {dived_1:,.2f} $')
elif month_sum < total:
    dived_2 = total - month_sum
    print(f'Oh no! You overspent the budget on {dived_2:,.2f} $')
else:
    print('Wow! Your expenses exactly match the budget')
years_amount = int(input('Insert the amount of years: '))
total_month = 0
for y in range (1, years_amount + 1):
    for x in range (1, 13):
        total = float(input(f'Insert the amount of {y} year {x} month and press Enter: '))
        total_month += total
resalt = total_month / x / years_amount
monthes = x * years_amount
print(f'The amount of monthes: {monthes}\nTotal value of\
precipitations: {total_month:,.2f} mm\nMean averege \
of precipitation: {resalt:,.2f} mm')
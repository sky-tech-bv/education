print('Welcome to the tip calculator!')
summ = float(input('What was the total bill? $'))
people_count = int(input('How many people to split the bill? '))
tax = int(input('What percentage tip would you like to give? 10, 12 or 15?'))
result = summ * (1+(tax/100))/people_count
print(f'Each person should pay: ${result:.2f}')
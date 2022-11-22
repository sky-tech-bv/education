speed = float(input('Insert the speed of moving machine: '))
hours = int (input('Insert the amount of hours for moving machine: '))
print ('Hours\tDistanse')
print('_____________')
for x in range (1, hours + 1):
    distanse = x * speed
    print(f'{x}\t{distanse}')
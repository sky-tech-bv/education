federal_tax = 0.05
region_tax = 0.025
def main():
    sum = 0
    sum = float(input('Insert the prise of purches: '))
    print('The sum of taxes:')
    federal(sum)
    regional(sum)
def federal(num):
    result = federal_tax * num
    print(f'Federal tax value - ${result:,.2f}')
def regional(num):
    result = region_tax * num
    print(f'Regional tax value - ${result:,.2f}')
main()
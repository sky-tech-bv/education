convert_value = 0.6214
def main():
    distance = float(input('Insert the distanse in km: '))
    convert(distance)
def convert(num):
    result = num * convert_value
    print(f'The distanse in mile value {result:.2f}')
main()
avg_figure = 69
max_figure = 10
def get_number():
    numbers = open('pbnumbers.txt', 'r')
    number = numbers.readlines()
    numbers.close()
    for i in range(len(number)):
        number[i] = number[i].rstrip('\n')
    num_out = []
    for i in range(len(number)):
        figures = number[i].split()
        for y in range(len(figures)):
            num_out.append(int(figures[y]))
    return num_out
def how_much_value(list, val_figure):
    count_list = [0] * (val_figure + 1)
def main():
    numbers = []
    numbers = get_number()
    print(numbers)
if __name__ == '__main__':
    main()
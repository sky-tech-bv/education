import random
def main():
    num_1 = 0
    num_2 = 0
    num_1 = random.randint(100, 250)
    num_2 = random.randint(100, 250)
    get_answer(num_1, num_2)
def get_answer(num1, num2):
    sum = 0
    sum = num1 + num2
    print(f'Insert the figure which equals \n  {num1}')
    result = int(input(f'+ {num2} and press Enter: '))
    if result == num1 + num2:
        print('Congratulate! You gave the right answer!')
    else:
        print(f'You made a mistake! The correct answer is {sum}')
main()
    